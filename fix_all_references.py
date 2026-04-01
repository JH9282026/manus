#!/usr/bin/env python3
"""
Automated script to fix missing references in all SKILL.md files.
Adds proper markdown links to unreferenced .md files in references/ folders.
"""

import os
import re
from pathlib import Path
from typing import List, Set, Tuple

def get_existing_links(content: str) -> Set[str]:
    """Extract all markdown link targets from content."""
    # Match [text](path) style links
    link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    matches = re.findall(link_pattern, content)
    links = set()
    for _, path in matches:
        # Normalize path - remove leading ./ and references/
        normalized = path.replace('./', '').replace('references/', '')
        if normalized.endswith('.md'):
            links.add(normalized)
    return links

def get_reference_files(skill_path: Path) -> List[str]:
    """Get all .md files in the references/ folder."""
    refs_dir = skill_path / 'references'
    if not refs_dir.exists():
        return []
    
    md_files = []
    for file in sorted(refs_dir.glob('*.md')):
        md_files.append(file.name)
    return md_files

def create_reference_section(missing_files: List[str]) -> str:
    """Create a References section with links to missing files."""
    if not missing_files:
        return ""
    
    section = "\n\n## References\n\n"
    for filename in sorted(missing_files):
        # Create a readable title from filename
        title = filename.replace('.md', '').replace('_', ' ').replace('-', ' ').title()
        section += f"- [{title}](references/{filename})\n"
    
    return section

def fix_skill_references(skill_path: Path) -> Tuple[bool, int]:
    """
    Fix references in a single SKILL.md file.
    Returns (was_modified, num_links_added)
    """
    skill_file = skill_path / 'SKILL.md'
    if not skill_file.exists():
        return False, 0
    
    # Read current content
    with open(skill_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get existing links and available reference files
    existing_links = get_existing_links(content)
    reference_files = get_reference_files(skill_path)
    
    if not reference_files:
        return False, 0
    
    # Find missing references
    missing_files = [f for f in reference_files if f not in existing_links]
    
    if not missing_files:
        return False, 0
    
    # Check if there's already a References section
    has_references_section = bool(re.search(r'^##\s+References\s*$', content, re.MULTILINE))
    
    if has_references_section:
        # Find the References section and append to it
        ref_match = re.search(r'(^##\s+References\s*$)', content, re.MULTILINE)
        if ref_match:
            # Find the position after the header
            insert_pos = ref_match.end()
            # Add new links right after the header
            new_links = "\n" + "\n".join([
                f"- [{f.replace('.md', '').replace('_', ' ').replace('-', ' ').title()}](references/{f})"
                for f in sorted(missing_files)
            ])
            content = content[:insert_pos] + new_links + content[insert_pos:]
    else:
        # Add new References section at the end
        ref_section = create_reference_section(missing_files)
        content = content.rstrip() + ref_section
    
    # Write back
    with open(skill_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True, len(missing_files)

def main():
    """Main execution function."""
    repo_root = Path('/home/ubuntu/github_repos/manus')
    
    total_modified = 0
    total_links_added = 0
    modified_skills = []
    
    # Find all directories that contain SKILL.md files
    skill_dirs = []
    for item in repo_root.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            skill_file = item / 'SKILL.md'
            if skill_file.exists():
                skill_dirs.append(item)
    
    print(f"Found {len(skill_dirs)} skill directories with SKILL.md files")
    print("Processing...\n")
    
    for skill_dir in sorted(skill_dirs):
        was_modified, links_added = fix_skill_references(skill_dir)
        if was_modified:
            total_modified += 1
            total_links_added += links_added
            modified_skills.append(skill_dir.name)
            print(f"✓ {skill_dir.name}: Added {links_added} reference link(s)")
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total SKILL.md files updated: {total_modified}")
    print(f"Total reference links added: {total_links_added}")
    print("="*60)
    
    # Save summary to file
    summary_file = repo_root / 'fix_references_summary.txt'
    with open(summary_file, 'w') as f:
        f.write("Reference Fix Summary\n")
        f.write("="*60 + "\n\n")
        f.write(f"Total SKILL.md files updated: {total_modified}\n")
        f.write(f"Total reference links added: {total_links_added}\n\n")
        f.write("Modified Skills:\n")
        for skill in modified_skills:
            f.write(f"  - {skill}\n")
    
    print(f"\nSummary saved to: {summary_file}")

if __name__ == '__main__':
    main()
