#!/usr/bin/env python3
"""
Final Comprehensive Audit Script for Manus Skills Repository
Verifies 100% compliance across all requirements.
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

# Configuration
REPO_ROOT = Path("/home/ubuntu/github_repos/manus")
MAX_LINES = 500

# Results tracking
results = {
    "total_skills": 0,
    "fully_compliant": 0,
    "issues": [],
    "stats": {
        "has_skill_md": 0,
        "has_references_folder": 0,
        "valid_yaml": 0,
        "meaningful_description": 0,
        "under_500_lines": 0,
        "has_using_references_section": 0,
        "qualified_paths": 0,
        "meaningful_link_text": 0,
        "no_redundant_references": 0
    },
    "line_counts": [],
    "skills_details": []
}

def check_yaml_frontmatter(content):
    """Extract and validate YAML frontmatter."""
    if not content.startswith("---"):
        return None, "Missing YAML frontmatter delimiter"
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, "Incomplete YAML frontmatter"
    
    try:
        yaml_content = yaml.safe_load(parts[1])
        return yaml_content, None
    except yaml.YAMLError as e:
        return None, f"Invalid YAML: {str(e)}"

def check_meaningful_description(yaml_data):
    """Check if description is meaningful (not just skill name)."""
    if not yaml_data or "description" not in yaml_data:
        return False, "No description field"
    
    desc = yaml_data["description"].strip()
    if len(desc) < 20:
        return False, f"Description too short ({len(desc)} chars)"
    
    # Check if it's just the skill name or very generic
    if desc.lower() in ["skill", "a skill", "this skill"]:
        return False, "Description not meaningful"
    
    return True, None

def check_using_references_section(content):
    """Check for 'Using the Reference Files' section."""
    pattern = r"##\s+Using\s+the\s+Reference\s+Files"
    if re.search(pattern, content, re.IGNORECASE):
        return True, None
    return False, "Missing 'Using the Reference Files' section"

def check_reference_links(content):
    """Check that reference links use qualified paths and meaningful text."""
    # Find all markdown links
    link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    links = re.findall(link_pattern, content)
    
    issues = []
    reference_links = []
    
    for link_text, link_url in links:
        # Check if it's a reference link (pointing to references folder)
        if "./references/" in link_url:
            reference_links.append((link_text, link_url))
            
            # Check meaningful link text
            # Should not be just filename or very short
            if len(link_text) < 10 or link_text.endswith(".md"):
                issues.append(f"Non-meaningful link text: [{link_text}]({link_url})")
        elif "reference" in link_url.lower() and link_url.endswith(".md"):
            # Found a reference link without qualified path
            issues.append(f"Non-qualified path: [{link_text}]({link_url})")
    
    if issues:
        return False, "; ".join(issues)
    return True, None

def check_redundant_references(content):
    """Check for redundant 'References' sections."""
    # Look for standalone "References" or "Reference Files" headers
    pattern = r"##\s+(References?|Reference\s+Files)\s*$"
    matches = re.findall(pattern, content, re.MULTILINE | re.IGNORECASE)
    
    # Filter out "Using the Reference Files"
    redundant = [m for m in matches if "using" not in m.lower()]
    
    if redundant:
        return False, f"Found redundant section(s): {', '.join(redundant)}"
    return True, None

def audit_skill(skill_path):
    """Audit a single skill directory."""
    skill_name = skill_path.name
    skill_issues = []
    skill_stats = defaultdict(bool)
    
    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        skill_issues.append("Missing SKILL.md file")
        return skill_issues, skill_stats, 0
    
    skill_stats["has_skill_md"] = True
    
    # Read SKILL.md
    try:
        with open(skill_md, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            line_count = len(lines)
    except Exception as e:
        skill_issues.append(f"Error reading SKILL.md: {str(e)}")
        return skill_issues, skill_stats, 0
    
    # Check line count
    if line_count >= MAX_LINES:
        skill_issues.append(f"SKILL.md has {line_count} lines (must be < {MAX_LINES})")
    else:
        skill_stats["under_500_lines"] = True
    
    # Check YAML frontmatter
    yaml_data, yaml_error = check_yaml_frontmatter(content)
    if yaml_error:
        skill_issues.append(f"YAML issue: {yaml_error}")
    else:
        skill_stats["valid_yaml"] = True
        
        # Check meaningful description
        is_meaningful, desc_error = check_meaningful_description(yaml_data)
        if not is_meaningful:
            skill_issues.append(f"Description issue: {desc_error}")
        else:
            skill_stats["meaningful_description"] = True
    
    # Check "Using the Reference Files" section
    has_section, section_error = check_using_references_section(content)
    if not has_section:
        skill_issues.append(section_error)
    else:
        skill_stats["has_using_references_section"] = True
    
    # Check reference links
    links_ok, links_error = check_reference_links(content)
    if not links_ok:
        skill_issues.append(f"Link issues: {links_error}")
    else:
        skill_stats["qualified_paths"] = True
        skill_stats["meaningful_link_text"] = True
    
    # Check redundant references sections
    no_redundant, redundant_error = check_redundant_references(content)
    if not no_redundant:
        skill_issues.append(redundant_error)
    else:
        skill_stats["no_redundant_references"] = True
    
    # Check references folder
    references_dir = skill_path / "references"
    if not references_dir.exists() or not references_dir.is_dir():
        skill_issues.append("Missing references folder")
    else:
        # Check for .md files
        md_files = list(references_dir.glob("*.md"))
        if not md_files:
            skill_issues.append("No .md files in references folder")
        else:
            skill_stats["has_references_folder"] = True
    
    return skill_issues, skill_stats, line_count

def main():
    """Main audit function."""
    print("=" * 80)
    print("FINAL COMPREHENSIVE AUDIT - MANUS SKILLS REPOSITORY")
    print("=" * 80)
    print()
    
    # Find all skill directories (directories with SKILL.md)
    skill_dirs = []
    for item in REPO_ROOT.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            skill_md = item / "SKILL.md"
            if skill_md.exists():
                skill_dirs.append(item)
    
    skill_dirs.sort()
    
    results["total_skills"] = len(skill_dirs)
    
    print(f"Found {len(skill_dirs)} skill directories")
    print()
    
    # Audit each skill
    for skill_dir in skill_dirs:
        skill_name = skill_dir.name
        print(f"Auditing: {skill_name}...", end=" ")
        
        skill_issues, skill_stats, line_count = audit_skill(skill_dir)
        
        # Track line count
        if line_count > 0:
            results["line_counts"].append(line_count)
        
        # Update global stats
        for stat_key, stat_value in skill_stats.items():
            if stat_value:
                results["stats"][stat_key] += 1
        
        # Track issues
        if skill_issues:
            print(f"❌ {len(skill_issues)} issue(s)")
            for issue in skill_issues:
                results["issues"].append(f"{skill_name}: {issue}")
        else:
            print("✅ COMPLIANT")
            results["fully_compliant"] += 1
        
        # Store details
        results["skills_details"].append({
            "name": skill_name,
            "compliant": len(skill_issues) == 0,
            "issues": skill_issues,
            "line_count": line_count
        })
    
    # Generate report
    print()
    print("=" * 80)
    print("AUDIT RESULTS")
    print("=" * 80)
    print()
    
    # Summary
    print(f"Total Skills Checked: {results['total_skills']}")
    print(f"Fully Compliant Skills: {results['fully_compliant']}")
    print(f"Skills with Issues: {results['total_skills'] - results['fully_compliant']}")
    print()
    
    # Compliance percentage
    if results['total_skills'] > 0:
        compliance_pct = (results['fully_compliant'] / results['total_skills']) * 100
        print(f"Compliance Rate: {compliance_pct:.1f}%")
        print()
    
    # Statistics
    print("REQUIREMENT COMPLIANCE:")
    print(f"  ✓ Has SKILL.md: {results['stats']['has_skill_md']}/{results['total_skills']}")
    print(f"  ✓ Has references folder: {results['stats']['has_references_folder']}/{results['total_skills']}")
    print(f"  ✓ Valid YAML frontmatter: {results['stats']['valid_yaml']}/{results['total_skills']}")
    print(f"  ✓ Meaningful description: {results['stats']['meaningful_description']}/{results['total_skills']}")
    print(f"  ✓ Under 500 lines: {results['stats']['under_500_lines']}/{results['total_skills']}")
    print(f"  ✓ Has 'Using the Reference Files' section: {results['stats']['has_using_references_section']}/{results['total_skills']}")
    print(f"  ✓ Qualified reference paths: {results['stats']['qualified_paths']}/{results['total_skills']}")
    print(f"  ✓ Meaningful link text: {results['stats']['meaningful_link_text']}/{results['total_skills']}")
    print(f"  ✓ No redundant References sections: {results['stats']['no_redundant_references']}/{results['total_skills']}")
    print()
    
    # Line count statistics
    if results['line_counts']:
        print("LINE COUNT STATISTICS:")
        print(f"  Maximum: {max(results['line_counts'])} lines")
        print(f"  Average: {sum(results['line_counts']) / len(results['line_counts']):.1f} lines")
        print(f"  Minimum: {min(results['line_counts'])} lines")
        print()
    
    # Issues
    if results['issues']:
        print("REMAINING ISSUES:")
        for issue in results['issues']:
            print(f"  ❌ {issue}")
        print()
    else:
        print("✅ NO ISSUES FOUND - 100% COMPLIANCE ACHIEVED!")
        print()
    
    # Final verdict
    print("=" * 80)
    if results['fully_compliant'] == results['total_skills']:
        print("🎉 FINAL VERDICT: ALL SKILLS ARE 100% COMPLIANT AND READY FOR AGENTIC AI!")
    else:
        print(f"⚠️  FINAL VERDICT: {results['total_skills'] - results['fully_compliant']} skill(s) need attention")
    print("=" * 80)
    
    # Write report to file
    report_path = REPO_ROOT / "audit_report_final.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Final Comprehensive Audit Report - Manus Skills Repository\n\n")
        f.write(f"**Audit Date:** {os.popen('date').read().strip()}\n\n")
        f.write("## Executive Summary\n\n")
        f.write(f"- **Total Skills Checked:** {results['total_skills']}\n")
        f.write(f"- **Fully Compliant Skills:** {results['fully_compliant']}\n")
        f.write(f"- **Skills with Issues:** {results['total_skills'] - results['fully_compliant']}\n")
        
        if results['total_skills'] > 0:
            compliance_pct = (results['fully_compliant'] / results['total_skills']) * 100
            f.write(f"- **Compliance Rate:** {compliance_pct:.1f}%\n\n")
        
        if results['fully_compliant'] == results['total_skills']:
            f.write("### ✅ 100% COMPLIANCE ACHIEVED!\n\n")
            f.write("All skills meet every requirement and are ready for agentic AI deployment.\n\n")
        else:
            f.write("### ⚠️ Issues Detected\n\n")
            f.write(f"{results['total_skills'] - results['fully_compliant']} skill(s) require attention.\n\n")
        
        f.write("## Requirement Compliance Statistics\n\n")
        f.write("| Requirement | Compliant | Total | Percentage |\n")
        f.write("|-------------|-----------|-------|------------|\n")
        
        for req_name, req_key in [
            ("Has SKILL.md", "has_skill_md"),
            ("Has references folder", "has_references_folder"),
            ("Valid YAML frontmatter", "valid_yaml"),
            ("Meaningful description", "meaningful_description"),
            ("Under 500 lines", "under_500_lines"),
            ("Has 'Using the Reference Files' section", "has_using_references_section"),
            ("Qualified reference paths", "qualified_paths"),
            ("Meaningful link text", "meaningful_link_text"),
            ("No redundant References sections", "no_redundant_references")
        ]:
            count = results['stats'][req_key]
            total = results['total_skills']
            pct = (count / total * 100) if total > 0 else 0
            f.write(f"| {req_name} | {count} | {total} | {pct:.1f}% |\n")
        
        f.write("\n## Line Count Statistics\n\n")
        if results['line_counts']:
            f.write(f"- **Maximum:** {max(results['line_counts'])} lines\n")
            f.write(f"- **Average:** {sum(results['line_counts']) / len(results['line_counts']):.1f} lines\n")
            f.write(f"- **Minimum:** {min(results['line_counts'])} lines\n")
            f.write(f"- **Limit:** < {MAX_LINES} lines\n\n")
        
        if results['issues']:
            f.write("## All Issues Summary\n\n")
            for issue in results['issues']:
                f.write(f"- ❌ {issue}\n")
            f.write("\n")
        
        f.write("## Final Verdict\n\n")
        if results['fully_compliant'] == results['total_skills']:
            f.write("### 🎉 ALL SKILLS ARE 100% COMPLIANT AND READY FOR AGENTIC AI!\n\n")
            f.write("Every skill in the repository meets all requirements:\n")
            f.write("- ✅ Has SKILL.md file\n")
            f.write("- ✅ Has references folder with .md files\n")
            f.write("- ✅ Valid YAML frontmatter\n")
            f.write("- ✅ Meaningful description for AI skill selection\n")
            f.write("- ✅ Under 500 lines\n")
            f.write("- ✅ Has 'Using the Reference Files' section\n")
            f.write("- ✅ All reference links use qualified paths (./references/)\n")
            f.write("- ✅ All links have meaningful descriptions\n")
            f.write("- ✅ No redundant 'References' sections\n")
        else:
            f.write(f"### ⚠️ {results['total_skills'] - results['fully_compliant']} skill(s) need attention\n\n")
            f.write("Please review the issues listed above.\n")
    
    print(f"\nReport written to: {report_path}")

if __name__ == "__main__":
    main()
