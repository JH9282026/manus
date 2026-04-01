#!/usr/bin/env python3
"""
Comprehensive Skill Audit Script
Verifies all skills are production-ready for agentic AI use
"""

import os
import json
import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple

def count_lines(file_path: str) -> int:
    """Count lines in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except Exception as e:
        return -1

def extract_frontmatter(content: str) -> Tuple[bool, dict, str]:
    """
    Extract YAML frontmatter from markdown content
    Returns: (has_frontmatter, frontmatter_dict, error_message)
    """
    if not content.startswith('---'):
        return False, {}, "No frontmatter delimiter found"
    
    # Find the closing ---
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False, {}, "Incomplete frontmatter (missing closing ---)"
    
    frontmatter_text = parts[1].strip()
    
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, {}, "Frontmatter is not a valid YAML dictionary"
        return True, frontmatter, ""
    except yaml.YAMLError as e:
        return False, {}, f"YAML parsing error: {str(e)}"

def check_reference_links(content: str) -> Tuple[List[str], List[str]]:
    """
    Check reference links in content
    Returns: (valid_links, invalid_links)
    """
    # Pattern for markdown links: [text](path)
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(link_pattern, content)
    
    valid_links = []
    invalid_links = []
    
    for text, path in matches:
        # Check if it's a reference link
        if 'references/' in path or path.startswith('./references/'):
            if path.startswith('./references/'):
                valid_links.append((text, path))
            else:
                invalid_links.append((text, path))
    
    return valid_links, invalid_links

def has_using_reference_section(content: str) -> bool:
    """Check if content has 'Using the Reference Files' section"""
    patterns = [
        r'##\s+Using\s+the\s+Reference\s+Files',
        r'##\s+Using\s+Reference\s+Files',
        r'###\s+Using\s+the\s+Reference\s+Files',
    ]
    
    for pattern in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    return False

def has_redundant_references_section(content: str) -> bool:
    """Check for redundant 'References' section (not 'Reference Files')"""
    # Split content by frontmatter
    parts = content.split('---', 2)
    if len(parts) >= 3:
        main_content = parts[2]
    else:
        main_content = content
    
    # Look for standalone "References" section (not "Reference Files")
    pattern = r'##\s+References\s*$'
    matches = re.findall(pattern, main_content, re.MULTILINE)
    
    # Filter out "Using the Reference Files" type headers
    for match in matches:
        if 'file' not in match.lower():
            return True
    
    return False

def check_skill(skill_path: Path) -> Dict:
    """
    Comprehensive check of a single skill
    Returns dict with all check results
    """
    result = {
        'skill_name': skill_path.name,
        'skill_path': str(skill_path),
        'has_skill_md': False,
        'has_references_folder': False,
        'reference_files_count': 0,
        'skill_md_line_count': 0,
        'has_valid_frontmatter': False,
        'frontmatter_error': '',
        'has_description': False,
        'description_text': '',
        'description_meaningful': False,
        'has_using_reference_section': False,
        'valid_reference_links': [],
        'invalid_reference_links': [],
        'has_redundant_references': False,
        'all_checks_passed': False,
        'issues': []
    }
    
    skill_md_path = skill_path / 'SKILL.md'
    references_path = skill_path / 'references'
    
    # Check 1: Has SKILL.md
    if skill_md_path.exists():
        result['has_skill_md'] = True
    else:
        result['issues'].append('Missing SKILL.md file')
        return result
    
    # Check 2: Has references folder
    if references_path.exists() and references_path.is_dir():
        result['has_references_folder'] = True
        # Count .md files in references
        md_files = list(references_path.glob('*.md'))
        result['reference_files_count'] = len(md_files)
        if len(md_files) == 0:
            result['issues'].append('References folder exists but has no .md files')
    else:
        result['issues'].append('Missing references folder')
    
    # Read SKILL.md content
    try:
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        result['issues'].append(f'Cannot read SKILL.md: {str(e)}')
        return result
    
    # Check 3: Line count
    line_count = count_lines(skill_md_path)
    result['skill_md_line_count'] = line_count
    if line_count > 500:
        result['issues'].append(f'SKILL.md has {line_count} lines (exceeds 500 line limit)')
    
    # Check 4: Valid YAML frontmatter
    has_fm, frontmatter, fm_error = extract_frontmatter(content)
    result['has_valid_frontmatter'] = has_fm
    result['frontmatter_error'] = fm_error
    
    if not has_fm:
        result['issues'].append(f'Invalid or missing YAML frontmatter: {fm_error}')
    else:
        # Check 5: Has description field
        if 'description' in frontmatter:
            result['has_description'] = True
            desc = frontmatter['description']
            result['description_text'] = desc
            
            # Check if description is meaningful (not empty, not too short)
            if desc and len(desc.strip()) > 20:
                result['description_meaningful'] = True
            else:
                result['issues'].append('Description is too short or empty (needs >20 chars)')
        else:
            result['issues'].append('Missing description field in frontmatter')
    
    # Check 6: Has "Using the Reference Files" section
    if has_using_reference_section(content):
        result['has_using_reference_section'] = True
    else:
        result['issues'].append('Missing "Using the Reference Files" section')
    
    # Check 7: Reference links use qualified paths
    valid_links, invalid_links = check_reference_links(content)
    result['valid_reference_links'] = [{'text': t, 'path': p} for t, p in valid_links]
    result['invalid_reference_links'] = [{'text': t, 'path': p} for t, p in invalid_links]
    
    if invalid_links:
        result['issues'].append(f'Found {len(invalid_links)} reference links without qualified paths (./references/)')
    
    # Check 8: No redundant "References" sections
    if has_redundant_references_section(content):
        result['has_redundant_references'] = True
        result['issues'].append('Has redundant "References" section')
    
    # Final verdict
    result['all_checks_passed'] = len(result['issues']) == 0
    
    return result

def find_all_skills(base_path: Path) -> List[Path]:
    """Find all directories containing SKILL.md files"""
    skills = []
    
    for item in base_path.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            skill_md = item / 'SKILL.md'
            if skill_md.exists():
                skills.append(item)
    
    return sorted(skills, key=lambda x: x.name)

def generate_audit_report(results: List[Dict]) -> Dict:
    """Generate comprehensive audit report"""
    total_skills = len(results)
    fully_compliant = sum(1 for r in results if r['all_checks_passed'])
    skills_with_issues = total_skills - fully_compliant
    
    # Categorize issues
    issue_breakdown = {}
    for result in results:
        for issue in result['issues']:
            if issue not in issue_breakdown:
                issue_breakdown[issue] = []
            issue_breakdown[issue].append(result['skill_name'])
    
    # Statistics
    stats = {
        'total_skills': total_skills,
        'fully_compliant': fully_compliant,
        'skills_with_issues': skills_with_issues,
        'compliance_rate': f"{(fully_compliant/total_skills*100):.1f}%" if total_skills > 0 else "0%",
        'avg_line_count': sum(r['skill_md_line_count'] for r in results) / total_skills if total_skills > 0 else 0,
        'skills_over_500_lines': sum(1 for r in results if r['skill_md_line_count'] > 500),
        'skills_with_valid_frontmatter': sum(1 for r in results if r['has_valid_frontmatter']),
        'skills_with_description': sum(1 for r in results if r['has_description']),
        'skills_with_meaningful_description': sum(1 for r in results if r['description_meaningful']),
        'skills_with_using_section': sum(1 for r in results if r['has_using_reference_section']),
        'total_invalid_links': sum(len(r['invalid_reference_links']) for r in results),
        'skills_with_redundant_sections': sum(1 for r in results if r['has_redundant_references']),
    }
    
    report = {
        'audit_timestamp': '2026-04-01',
        'summary': stats,
        'issue_breakdown': {issue: len(skills) for issue, skills in issue_breakdown.items()},
        'issue_details': issue_breakdown,
        'all_skills_ready': skills_with_issues == 0,
        'detailed_results': results
    }
    
    return report

def main():
    """Main audit function"""
    base_path = Path('/home/ubuntu/github_repos/manus')
    
    print("=" * 80)
    print("COMPREHENSIVE SKILL AUDIT - FINAL VERIFICATION")
    print("=" * 80)
    print(f"\nScanning repository: {base_path}")
    
    # Find all skills
    skills = find_all_skills(base_path)
    print(f"Found {len(skills)} skills to audit\n")
    
    # Audit each skill
    results = []
    for i, skill_path in enumerate(skills, 1):
        print(f"[{i}/{len(skills)}] Auditing: {skill_path.name}...", end=' ')
        result = check_skill(skill_path)
        results.append(result)
        
        if result['all_checks_passed']:
            print("✓ PASS")
        else:
            print(f"✗ FAIL ({len(result['issues'])} issues)")
    
    # Generate report
    print("\n" + "=" * 80)
    print("GENERATING FINAL REPORT")
    print("=" * 80)
    
    report = generate_audit_report(results)
    
    # Save to JSON
    output_path = base_path / 'audit_result.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\nAudit complete! Results saved to: {output_path}")
    
    # Print summary
    print("\n" + "=" * 80)
    print("AUDIT SUMMARY")
    print("=" * 80)
    print(f"Total Skills Checked:        {report['summary']['total_skills']}")
    print(f"Fully Compliant:             {report['summary']['fully_compliant']}")
    print(f"Skills with Issues:          {report['summary']['skills_with_issues']}")
    print(f"Compliance Rate:             {report['summary']['compliance_rate']}")
    print(f"\nALL SKILLS READY:            {'YES ✓' if report['all_skills_ready'] else 'NO ✗'}")
    print("=" * 80)
    
    if not report['all_skills_ready']:
        print("\nISSUE BREAKDOWN:")
        for issue, count in sorted(report['issue_breakdown'].items(), key=lambda x: -x[1]):
            print(f"  • {issue}: {count} skill(s)")
    
    return 0 if report['all_skills_ready'] else 1

if __name__ == '__main__':
    exit(main())
