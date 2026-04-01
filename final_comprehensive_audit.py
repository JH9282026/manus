#!/usr/bin/env python3
"""
Final Comprehensive Audit - All 9 Requirements
Verifies 100% compliance across all skills
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

# All 9 requirements
REQUIREMENTS = [
    "1. Has SKILL.md file",
    "2. Has references folder with .md files",
    "3. SKILL.md has valid YAML frontmatter",
    "4. YAML has meaningful description (20+ chars)",
    "5. SKILL.md is under 500 lines (< 500)",
    "6. Has 'Using the Reference Files' section",
    "7. All reference links use qualified paths (./references/)",
    "8. All links have meaningful descriptions (10+ chars)",
    "9. No redundant/duplicate 'Reference Files' sections"
]

def extract_yaml_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except:
            return None
    return None

def count_reference_sections(content):
    """Count occurrences of 'Using the Reference Files' sections."""
    pattern = r'#+\s*Using\s+the\s+Reference\s+Files'
    matches = re.findall(pattern, content, re.IGNORECASE)
    return len(matches)

def check_reference_links(content):
    """Check all reference links for qualified paths and meaningful descriptions."""
    # Find markdown links: [text](url)
    link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    links = re.findall(link_pattern, content)
    
    issues = []
    for text, url in links:
        # Check if it's a reference link (contains 'reference' in path)
        if 'reference' in url.lower():
            # Check qualified path
            if not url.startswith('./references/'):
                issues.append(f"Link '{url}' doesn't use qualified path ./references/")
            
            # Check meaningful description (10+ chars)
            if len(text.strip()) < 10:
                issues.append(f"Link text '{text}' is too short (< 10 chars)")
    
    return issues

def audit_skill(skill_path):
    """Audit a single skill against all 9 requirements."""
    results = {
        'path': skill_path,
        'compliant': True,
        'issues': [],
        'checks': {}
    }
    
    skill_md_path = skill_path / 'SKILL.md'
    references_path = skill_path / 'references'
    
    # Check 1: Has SKILL.md file
    has_skill_md = skill_md_path.exists()
    results['checks']['has_skill_md'] = has_skill_md
    if not has_skill_md:
        results['compliant'] = False
        results['issues'].append("Missing SKILL.md file")
        return results
    
    # Read SKILL.md content
    with open(skill_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check 2: Has references folder with .md files
    has_references = references_path.exists() and references_path.is_dir()
    results['checks']['has_references_folder'] = has_references
    if has_references:
        md_files = list(references_path.glob('*.md'))
        results['checks']['reference_md_count'] = len(md_files)
        if len(md_files) == 0:
            results['compliant'] = False
            results['issues'].append("References folder exists but has no .md files")
    else:
        results['compliant'] = False
        results['issues'].append("Missing references folder")
        results['checks']['reference_md_count'] = 0
    
    # Check 3: SKILL.md has valid YAML frontmatter
    yaml_data = extract_yaml_frontmatter(content)
    has_valid_yaml = yaml_data is not None
    results['checks']['has_valid_yaml'] = has_valid_yaml
    if not has_valid_yaml:
        results['compliant'] = False
        results['issues'].append("Missing or invalid YAML frontmatter")
    
    # Check 4: YAML has meaningful description (20+ chars)
    if has_valid_yaml and 'description' in yaml_data:
        desc = yaml_data['description']
        desc_length = len(desc) if desc else 0
        results['checks']['description_length'] = desc_length
        if desc_length < 20:
            results['compliant'] = False
            results['issues'].append(f"Description too short ({desc_length} chars, need 20+)")
    elif has_valid_yaml:
        results['compliant'] = False
        results['issues'].append("YAML missing 'description' field")
        results['checks']['description_length'] = 0
    
    # Check 5: SKILL.md is under 500 lines (< 500)
    lines = content.split('\n')
    line_count = len(lines)
    results['checks']['line_count'] = line_count
    if line_count >= 500:
        results['compliant'] = False
        results['issues'].append(f"SKILL.md has {line_count} lines (must be < 500)")
    
    # Check 6: Has "Using the Reference Files" section
    ref_section_count = count_reference_sections(content)
    results['checks']['reference_section_count'] = ref_section_count
    if ref_section_count == 0:
        results['compliant'] = False
        results['issues'].append("Missing 'Using the Reference Files' section")
    
    # Check 7 & 8: All reference links use qualified paths and meaningful descriptions
    link_issues = check_reference_links(content)
    results['checks']['link_issues'] = link_issues
    if link_issues:
        results['compliant'] = False
        results['issues'].extend(link_issues)
    
    # Check 9: No redundant/duplicate "Reference Files" sections
    if ref_section_count > 1:
        results['compliant'] = False
        results['issues'].append(f"Found {ref_section_count} 'Using the Reference Files' sections (should be 1)")
    
    return results

def main():
    """Run comprehensive audit on all skills."""
    repo_root = Path('/home/ubuntu/github_repos/manus')
    
    # Find all skill directories (directories with SKILL.md)
    skill_dirs = []
    for item in repo_root.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            skill_md = item / 'SKILL.md'
            if skill_md.exists():
                skill_dirs.append(item)
    
    skill_dirs.sort()
    
    print(f"Found {len(skill_dirs)} skill directories")
    print("Running comprehensive audit...\n")
    
    all_results = []
    compliant_count = 0
    
    for skill_dir in skill_dirs:
        result = audit_skill(skill_dir)
        all_results.append(result)
        if result['compliant']:
            compliant_count += 1
    
    # Generate comprehensive report
    report_lines = [
        "# Final Comprehensive Audit Report",
        "",
        "## Executive Summary",
        "",
        f"**Total Skills Checked:** {len(skill_dirs)}",
        f"**Fully Compliant Skills:** {compliant_count}",
        f"**Non-Compliant Skills:** {len(skill_dirs) - compliant_count}",
        f"**Compliance Rate:** {(compliant_count / len(skill_dirs) * 100):.1f}%",
        "",
        f"**100% COMPLIANCE STATUS:** {'✅ YES - ALL SKILLS COMPLIANT' if compliant_count == len(skill_dirs) else '❌ NO - ISSUES REMAIN'}",
        "",
        "## Requirements Checked",
        ""
    ]
    
    for i, req in enumerate(REQUIREMENTS, 1):
        report_lines.append(f"{i}. {req}")
    
    report_lines.extend([
        "",
        "## Detailed Results by Skill",
        ""
    ])
    
    # Group by compliance status
    compliant_skills = [r for r in all_results if r['compliant']]
    non_compliant_skills = [r for r in all_results if not r['compliant']]
    
    if compliant_skills:
        report_lines.extend([
            f"### ✅ Fully Compliant Skills ({len(compliant_skills)})",
            ""
        ])
        for result in compliant_skills:
            skill_name = result['path'].name
            report_lines.append(f"- **{skill_name}**")
            report_lines.append(f"  - Lines: {result['checks'].get('line_count', 'N/A')}")
            report_lines.append(f"  - Description length: {result['checks'].get('description_length', 'N/A')} chars")
            report_lines.append(f"  - Reference files: {result['checks'].get('reference_md_count', 0)}")
            report_lines.append(f"  - Reference sections: {result['checks'].get('reference_section_count', 0)}")
            report_lines.append("")
    
    if non_compliant_skills:
        report_lines.extend([
            f"### ❌ Non-Compliant Skills ({len(non_compliant_skills)})",
            ""
        ])
        for result in non_compliant_skills:
            skill_name = result['path'].name
            report_lines.append(f"- **{skill_name}**")
            report_lines.append(f"  - **Issues Found:** {len(result['issues'])}")
            for issue in result['issues']:
                report_lines.append(f"    - {issue}")
            report_lines.append("")
    
    # Statistics section
    report_lines.extend([
        "## Comprehensive Statistics",
        "",
        "### Line Count Distribution",
        ""
    ])
    
    line_counts = [r['checks'].get('line_count', 0) for r in all_results if 'line_count' in r['checks']]
    if line_counts:
        report_lines.append(f"- **Average:** {sum(line_counts) / len(line_counts):.1f} lines")
        report_lines.append(f"- **Maximum:** {max(line_counts)} lines")
        report_lines.append(f"- **Minimum:** {min(line_counts)} lines")
        report_lines.append(f"- **Skills under 500 lines:** {sum(1 for lc in line_counts if lc < 500)}/{len(line_counts)}")
        report_lines.append("")
    
    report_lines.extend([
        "### Description Length Distribution",
        ""
    ])
    
    desc_lengths = [r['checks'].get('description_length', 0) for r in all_results if 'description_length' in r['checks']]
    if desc_lengths:
        report_lines.append(f"- **Average:** {sum(desc_lengths) / len(desc_lengths):.1f} chars")
        report_lines.append(f"- **Maximum:** {max(desc_lengths)} chars")
        report_lines.append(f"- **Minimum:** {min(desc_lengths)} chars")
        report_lines.append(f"- **Skills with 20+ char descriptions:** {sum(1 for dl in desc_lengths if dl >= 20)}/{len(desc_lengths)}")
        report_lines.append("")
    
    report_lines.extend([
        "### Reference Files",
        ""
    ])
    
    ref_counts = [r['checks'].get('reference_md_count', 0) for r in all_results]
    report_lines.append(f"- **Total reference files:** {sum(ref_counts)}")
    report_lines.append(f"- **Average per skill:** {sum(ref_counts) / len(ref_counts):.1f}")
    report_lines.append(f"- **Skills with reference files:** {sum(1 for rc in ref_counts if rc > 0)}/{len(ref_counts)}")
    report_lines.append("")
    
    report_lines.extend([
        "### Reference Sections",
        ""
    ])
    
    ref_section_counts = [r['checks'].get('reference_section_count', 0) for r in all_results]
    report_lines.append(f"- **Skills with exactly 1 section:** {sum(1 for rsc in ref_section_counts if rsc == 1)}/{len(ref_section_counts)}")
    report_lines.append(f"- **Skills with 0 sections:** {sum(1 for rsc in ref_section_counts if rsc == 0)}")
    report_lines.append(f"- **Skills with duplicate sections:** {sum(1 for rsc in ref_section_counts if rsc > 1)}")
    report_lines.append("")
    
    report_lines.extend([
        "## Final Verdict",
        "",
        f"**All 9 requirements met across all {len(skill_dirs)} skills:** {'✅ YES' if compliant_count == len(skill_dirs) else '❌ NO'}",
        "",
        f"**Ready for agentic AI:** {'✅ YES - 100% COMPLIANT' if compliant_count == len(skill_dirs) else '❌ NO - FIXES REQUIRED'}",
        ""
    ])
    
    # Write report
    report_path = repo_root / 'final_audit_report.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"✅ Audit complete!")
    print(f"📊 Report written to: {report_path}")
    print(f"\n{'='*60}")
    print(f"FINAL RESULT: {compliant_count}/{len(skill_dirs)} skills fully compliant")
    print(f"100% COMPLIANCE: {'✅ YES' if compliant_count == len(skill_dirs) else '❌ NO'}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
