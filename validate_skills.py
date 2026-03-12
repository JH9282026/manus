#!/usr/bin/env python3
import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    # Match content between first two '---' markers
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def validate_yaml_frontmatter(frontmatter_text):
    """Validate YAML frontmatter and check description formatting."""
    try:
        data = yaml.safe_load(frontmatter_text)
        if not isinstance(data, dict):
            return False, "YAML is not a dictionary"
        
        # Check if description exists and is properly quoted
        if 'description' not in data:
            return False, "Missing 'description' field"
        
        # Check if description in raw text has quotes
        desc_line_match = re.search(r'description:\s*(.+)', frontmatter_text)
        if not desc_line_match:
            return False, "Description field malformed"
        
        desc_value = desc_line_match.group(1).strip()
        # Valid if it starts with quote (single or double)
        if not (desc_value.startswith('"') or desc_value.startswith("'")):
            return False, f"Description not quoted: {desc_value[:50]}"
        
        return True, "Valid"
    except yaml.YAMLError as e:
        return False, f"YAML parse error: {str(e)[:100]}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)[:100]}"

def count_lines(filepath):
    """Count lines in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except Exception as e:
        return -1

def validate_all_skills():
    """Validate all SKILL.md files in the repository."""
    results = {
        'total': 0,
        'yaml_pass': 0,
        'yaml_fail': 0,
        'lines_pass': 0,
        'lines_fail': 0,
        'details': []
    }
    
    # Find all SKILL.md files
    skill_files = list(Path('.').rglob('SKILL.md'))
    results['total'] = len(skill_files)
    
    print(f"Found {len(skill_files)} SKILL.md files")
    print("=" * 80)
    
    for skill_file in sorted(skill_files):
        skill_path = str(skill_file)
        skill_name = skill_file.parent.name
        
        # Read file content
        try:
            with open(skill_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            results['details'].append({
                'skill': skill_name,
                'path': skill_path,
                'yaml_valid': False,
                'yaml_error': f"File read error: {str(e)}",
                'line_count': -1,
                'lines_valid': False
            })
            results['yaml_fail'] += 1
            results['lines_fail'] += 1
            continue
        
        # Validate YAML frontmatter
        frontmatter = extract_frontmatter(content)
        if frontmatter is None:
            yaml_valid = False
            yaml_error = "No frontmatter found"
        else:
            yaml_valid, yaml_error = validate_yaml_frontmatter(frontmatter)
        
        if yaml_valid:
            results['yaml_pass'] += 1
        else:
            results['yaml_fail'] += 1
        
        # Count lines
        line_count = count_lines(skill_file)
        lines_valid = line_count > 0 and line_count < 500
        
        if lines_valid:
            results['lines_pass'] += 1
        else:
            results['lines_fail'] += 1
        
        # Store details
        results['details'].append({
            'skill': skill_name,
            'path': skill_path,
            'yaml_valid': yaml_valid,
            'yaml_error': yaml_error if not yaml_valid else 'Valid',
            'line_count': line_count,
            'lines_valid': lines_valid
        })
    
    return results

# Run validation
results = validate_all_skills()

# Print summary
print("\n" + "=" * 80)
print("VALIDATION SUMMARY")
print("=" * 80)
print(f"Total skills checked: {results['total']}")
print()
print("YAML Frontmatter Validation:")
print(f"  ✓ Passing: {results['yaml_pass']}")
print(f"  ✗ Failing: {results['yaml_fail']}")
print()
print("Line Count Validation (< 500 lines):")
print(f"  ✓ Passing: {results['lines_pass']}")
print(f"  ✗ Failing: {results['lines_fail']}")
print()

# Calculate compliance
if results['total'] > 0:
    yaml_compliance = (results['yaml_pass'] / results['total']) * 100
    lines_compliance = (results['lines_pass'] / results['total']) * 100
    overall_compliance = ((results['yaml_pass'] + results['lines_pass']) / (results['total'] * 2)) * 100
    
    print(f"YAML Compliance: {yaml_compliance:.1f}%")
    print(f"Lines Compliance: {lines_compliance:.1f}%")
    print(f"Overall Compliance: {overall_compliance:.1f}%")
    print()
    
    if yaml_compliance == 100 and lines_compliance == 100:
        print("🎉 REPOSITORY IS 100% COMPLIANT! 🎉")
    else:
        print("⚠️  ISSUES FOUND - See detailed report below")

print("=" * 80)

# Generate detailed report
report_lines = []
report_lines.append("# SKILL.md Validation Report")
report_lines.append(f"\nGenerated: {os.popen('date').read().strip()}")
report_lines.append(f"\n## Summary\n")
report_lines.append(f"- **Total Skills Checked:** {results['total']}")
report_lines.append(f"- **YAML Valid:** {results['yaml_pass']} ({yaml_compliance:.1f}%)")
report_lines.append(f"- **YAML Invalid:** {results['yaml_fail']}")
report_lines.append(f"- **Lines < 500:** {results['lines_pass']} ({lines_compliance:.1f}%)")
report_lines.append(f"- **Lines ≥ 500:** {results['lines_fail']}")
report_lines.append(f"- **Overall Compliance:** {overall_compliance:.1f}%\n")

# YAML failures
if results['yaml_fail'] > 0:
    report_lines.append("\n## ❌ YAML Validation Failures\n")
    report_lines.append("| Skill | Path | Error |")
    report_lines.append("|-------|------|-------|")
    for detail in results['details']:
        if not detail['yaml_valid']:
            report_lines.append(f"| {detail['skill']} | `{detail['path']}` | {detail['yaml_error']} |")

# Line count failures
if results['lines_fail'] > 0:
    report_lines.append("\n## ❌ Line Count Failures (≥ 500 lines)\n")
    report_lines.append("| Skill | Path | Line Count |")
    report_lines.append("|-------|------|------------|")
    for detail in results['details']:
        if not detail['lines_valid']:
            report_lines.append(f"| {detail['skill']} | `{detail['path']}` | {detail['line_count']} |")

# All passing skills
passing_skills = [d for d in results['details'] if d['yaml_valid'] and d['lines_valid']]
if passing_skills:
    report_lines.append(f"\n## ✅ Compliant Skills ({len(passing_skills)})\n")
    report_lines.append("| Skill | Path | Lines |")
    report_lines.append("|-------|------|-------|")
    for detail in passing_skills[:20]:  # Show first 20
        report_lines.append(f"| {detail['skill']} | `{detail['path']}` | {detail['line_count']} |")
    if len(passing_skills) > 20:
        report_lines.append(f"\n*...and {len(passing_skills) - 20} more compliant skills*\n")

# Write report
report_content = '\n'.join(report_lines)
with open('skill_validation_report.md', 'w') as f:
    f.write(report_content)

print("\n📄 Detailed report saved to: skill_validation_report.md")

# Print failures for immediate visibility
if results['yaml_fail'] > 0:
    print("\n" + "=" * 80)
    print("YAML VALIDATION FAILURES:")
    print("=" * 80)
    for detail in results['details']:
        if not detail['yaml_valid']:
            print(f"❌ {detail['skill']}: {detail['yaml_error']}")

if results['lines_fail'] > 0:
    print("\n" + "=" * 80)
    print("LINE COUNT FAILURES:")
    print("=" * 80)
    for detail in results['details']:
        if not detail['lines_valid']:
            print(f"❌ {detail['skill']}: {detail['line_count']} lines")

