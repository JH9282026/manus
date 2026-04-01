#!/usr/bin/env python3
"""
Audit script to verify SKILL.md files properly reference their supporting .md files
in the references/ folder.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def find_skill_folders(root_dir):
    """Find all folders containing SKILL.md files."""
    skill_folders = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'SKILL.md' in filenames:
            skill_folders.append(dirpath)
    return sorted(skill_folders)

def get_reference_files(skill_folder):
    """Get all .md files in the references/ subfolder."""
    refs_dir = os.path.join(skill_folder, 'references')
    if not os.path.exists(refs_dir):
        return []
    
    ref_files = []
    for filename in os.listdir(refs_dir):
        if filename.endswith('.md'):
            ref_files.append(filename)
    return sorted(ref_files)

def extract_references_from_skill(skill_md_path):
    """Extract all references to files in references/ folder from SKILL.md."""
    try:
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [], [], str(e)
    
    # Pattern 1: Markdown links [text](references/filename.md)
    pattern1 = r'\[([^\]]*)\]\(references/([^)]+\.md)\)'
    
    # Pattern 2: Direct references like references/filename.md
    pattern2 = r'references/([a-zA-Z0-9_\-]+\.md)'
    
    # Pattern 3: [[references/filename.md]] wiki-style
    pattern3 = r'\[\[references/([^\]]+\.md)\]\]'
    
    referenced_files = set()
    all_references = []
    
    # Find all matches
    for match in re.finditer(pattern1, content):
        filename = match.group(2)
        referenced_files.add(filename)
        all_references.append({
            'type': 'markdown_link',
            'text': match.group(1),
            'file': filename,
            'full_match': match.group(0)
        })
    
    for match in re.finditer(pattern2, content):
        filename = match.group(1)
        referenced_files.add(filename)
        all_references.append({
            'type': 'direct_reference',
            'file': filename,
            'full_match': match.group(0)
        })
    
    for match in re.finditer(pattern3, content):
        filename = match.group(1)
        referenced_files.add(filename)
        all_references.append({
            'type': 'wiki_link',
            'file': filename,
            'full_match': match.group(0)
        })
    
    return list(referenced_files), all_references, None

def audit_skill(skill_folder):
    """Audit a single skill folder."""
    skill_md_path = os.path.join(skill_folder, 'SKILL.md')
    skill_name = os.path.basename(skill_folder)
    
    result = {
        'skill_name': skill_name,
        'skill_path': skill_folder,
        'has_references_folder': False,
        'reference_files': [],
        'referenced_in_skill': [],
        'missing_references': [],
        'all_references_found': [],
        'error': None,
        'status': 'unknown'
    }
    
    # Check if references folder exists
    refs_dir = os.path.join(skill_folder, 'references')
    result['has_references_folder'] = os.path.exists(refs_dir)
    
    # Get all reference files
    ref_files = get_reference_files(skill_folder)
    result['reference_files'] = ref_files
    
    # Extract references from SKILL.md
    referenced_files, all_refs, error = extract_references_from_skill(skill_md_path)
    result['referenced_in_skill'] = referenced_files
    result['all_references_found'] = all_refs
    result['error'] = error
    
    if error:
        result['status'] = 'error'
        return result
    
    # Find missing references
    missing = []
    for ref_file in ref_files:
        if ref_file not in referenced_files:
            missing.append(ref_file)
    result['missing_references'] = missing
    
    # Determine status
    if not result['has_references_folder']:
        result['status'] = 'no_references_folder'
    elif len(ref_files) == 0:
        result['status'] = 'empty_references_folder'
    elif len(missing) == 0:
        result['status'] = 'all_referenced'
    else:
        result['status'] = 'missing_some'
    
    return result

def generate_report(audit_results, output_path):
    """Generate a comprehensive markdown report."""
    
    total_skills = len(audit_results)
    all_referenced = sum(1 for r in audit_results if r['status'] == 'all_referenced')
    missing_some = sum(1 for r in audit_results if r['status'] == 'missing_some')
    no_refs_folder = sum(1 for r in audit_results if r['status'] == 'no_references_folder')
    empty_refs = sum(1 for r in audit_results if r['status'] == 'empty_references_folder')
    errors = sum(1 for r in audit_results if r['status'] == 'error')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# SKILL.md Reference Audit Report\n\n")
        f.write("## Executive Summary\n\n")
        f.write(f"**Total Skills Checked:** {total_skills}\n\n")
        f.write(f"- ✅ **Skills with ALL references properly linked:** {all_referenced}\n")
        f.write(f"- ⚠️  **Skills with MISSING references:** {missing_some}\n")
        f.write(f"- 📁 **Skills with no references/ folder:** {no_refs_folder}\n")
        f.write(f"- 📂 **Skills with empty references/ folder:** {empty_refs}\n")
        f.write(f"- ❌ **Skills with errors:** {errors}\n\n")
        
        # Answer the key question
        f.write("## Key Question: Are ALL SKILL.md files properly referencing their reference files?\n\n")
        if missing_some == 0 and errors == 0:
            f.write("**✅ YES** - All SKILL.md files that have reference files are properly referencing them!\n\n")
        else:
            f.write(f"**❌ NO** - {missing_some} skill(s) have reference files that are NOT mentioned in their SKILL.md\n\n")
        
        f.write("---\n\n")
        
        # Detailed breakdown by status
        f.write("## Detailed Breakdown\n\n")
        
        # Skills with missing references
        if missing_some > 0:
            f.write(f"### ⚠️  Skills with Missing References ({missing_some})\n\n")
            for result in audit_results:
                if result['status'] == 'missing_some':
                    f.write(f"#### {result['skill_name']}\n")
                    f.write(f"**Path:** `{result['skill_path']}`\n\n")
                    f.write(f"**Total reference files:** {len(result['reference_files'])}\n")
                    f.write(f"**Referenced in SKILL.md:** {len(result['referenced_in_skill'])}\n")
                    f.write(f"**Missing:** {len(result['missing_references'])}\n\n")
                    
                    f.write("**Missing reference files:**\n")
                    for missing in result['missing_references']:
                        f.write(f"- `{missing}`\n")
                    f.write("\n")
                    
                    if result['referenced_in_skill']:
                        f.write("**Files that ARE referenced:**\n")
                        for ref in result['referenced_in_skill']:
                            f.write(f"- `{ref}`\n")
                        f.write("\n")
                    
                    f.write("---\n\n")
        
        # Skills with all references
        if all_referenced > 0:
            f.write(f"### ✅ Skills with ALL References Properly Linked ({all_referenced})\n\n")
            for result in audit_results:
                if result['status'] == 'all_referenced':
                    f.write(f"- **{result['skill_name']}** ({len(result['reference_files'])} reference files)\n")
            f.write("\n---\n\n")
        
        # Skills with no references folder
        if no_refs_folder > 0:
            f.write(f"### 📁 Skills with No references/ Folder ({no_refs_folder})\n\n")
            for result in audit_results:
                if result['status'] == 'no_references_folder':
                    f.write(f"- **{result['skill_name']}** - `{result['skill_path']}`\n")
            f.write("\n---\n\n")
        
        # Skills with empty references folder
        if empty_refs > 0:
            f.write(f"### 📂 Skills with Empty references/ Folder ({empty_refs})\n\n")
            for result in audit_results:
                if result['status'] == 'empty_references_folder':
                    f.write(f"- **{result['skill_name']}** - `{result['skill_path']}`\n")
            f.write("\n---\n\n")
        
        # Errors
        if errors > 0:
            f.write(f"### ❌ Skills with Errors ({errors})\n\n")
            for result in audit_results:
                if result['status'] == 'error':
                    f.write(f"- **{result['skill_name']}**: {result['error']}\n")
            f.write("\n---\n\n")
        
        # Examples of proper vs improper referencing
        f.write("## Examples of Reference Patterns Found\n\n")
        
        # Find examples
        proper_examples = []
        for result in audit_results:
            if result['status'] == 'all_referenced' and result['all_references_found']:
                proper_examples.append(result)
                if len(proper_examples) >= 2:
                    break
        
        if proper_examples:
            f.write("### ✅ Proper Referencing Examples\n\n")
            for example in proper_examples:
                f.write(f"**{example['skill_name']}:**\n")
                for ref in example['all_references_found'][:3]:  # Show first 3
                    f.write(f"- Type: `{ref['type']}` - `{ref['full_match']}`\n")
                f.write("\n")
        
        improper_examples = []
        for result in audit_results:
            if result['status'] == 'missing_some':
                improper_examples.append(result)
                if len(improper_examples) >= 2:
                    break
        
        if improper_examples:
            f.write("### ⚠️  Improper Referencing Examples\n\n")
            for example in improper_examples:
                f.write(f"**{example['skill_name']}:**\n")
                f.write(f"- Has {len(example['reference_files'])} reference files\n")
                f.write(f"- Only references {len(example['referenced_in_skill'])} of them\n")
                f.write(f"- Missing: {', '.join(example['missing_references'][:5])}\n\n")
        
        f.write("---\n\n")
        f.write("## Complete Audit Data\n\n")
        
        for result in sorted(audit_results, key=lambda x: x['skill_name']):
            f.write(f"### {result['skill_name']}\n")
            f.write(f"- **Status:** {result['status']}\n")
            f.write(f"- **Path:** `{result['skill_path']}`\n")
            f.write(f"- **Has references/ folder:** {result['has_references_folder']}\n")
            f.write(f"- **Reference files count:** {len(result['reference_files'])}\n")
            f.write(f"- **Referenced in SKILL.md:** {len(result['referenced_in_skill'])}\n")
            
            if result['reference_files']:
                f.write(f"\n**All reference files:**\n")
                for rf in result['reference_files']:
                    status = "✅" if rf in result['referenced_in_skill'] else "❌"
                    f.write(f"  {status} `{rf}`\n")
            
            f.write("\n")

def main():
    """Main execution function."""
    repo_root = os.path.dirname(os.path.abspath(__file__))
    
    print("🔍 Starting SKILL.md Reference Audit...")
    print(f"📁 Repository root: {repo_root}\n")
    
    # Find all skill folders
    skill_folders = find_skill_folders(repo_root)
    print(f"Found {len(skill_folders)} skill folders with SKILL.md files\n")
    
    # Audit each skill
    audit_results = []
    for i, folder in enumerate(skill_folders, 1):
        skill_name = os.path.basename(folder)
        print(f"[{i}/{len(skill_folders)}] Auditing: {skill_name}...", end=" ")
        result = audit_skill(folder)
        audit_results.append(result)
        
        status_emoji = {
            'all_referenced': '✅',
            'missing_some': '⚠️ ',
            'no_references_folder': '📁',
            'empty_references_folder': '📂',
            'error': '❌'
        }
        print(f"{status_emoji.get(result['status'], '?')} {result['status']}")
    
    # Generate report
    report_path = os.path.join(repo_root, 'REPORT_REFERENCE_AUDIT.md')
    print(f"\n📝 Generating report: {report_path}")
    generate_report(audit_results, report_path)
    
    print("\n✅ Audit complete!")
    print(f"📄 Report saved to: {report_path}")
    
    # Print summary
    all_referenced = sum(1 for r in audit_results if r['status'] == 'all_referenced')
    missing_some = sum(1 for r in audit_results if r['status'] == 'missing_some')
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total skills checked: {len(audit_results)}")
    print(f"✅ All references linked: {all_referenced}")
    print(f"⚠️  Missing some references: {missing_some}")
    
    if missing_some == 0:
        print("\n🎉 ALL SKILL.md files properly reference their supporting files!")
    else:
        print(f"\n⚠️  {missing_some} skill(s) have unreferenced files. See report for details.")

if __name__ == '__main__':
    main()
