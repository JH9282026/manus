#!/usr/bin/env python3
"""
Automated script to fix 210 incomplete skills by:
1. Adding missing "## Using the Reference Files" sections
2. Ensuring all reference files are linked with qualified relative links
3. Adding meaningful descriptions based on filenames
"""

import os
import re
import json
from pathlib import Path
from typing import List, Dict, Tuple

def kebab_to_title(kebab_str: str) -> str:
    """Convert kebab-case filename to readable title case description."""
    # Remove .md extension
    name = kebab_str.replace('.md', '')
    # Split on hyphens and underscores
    words = re.split(r'[-_]', name)
    # Capitalize each word
    title = ' '.join(word.capitalize() for word in words if word)
    return title

def find_reference_files(skill_dir: Path) -> List[Tuple[str, str]]:
    """Find all reference files in the references subdirectory."""
    refs_dir = skill_dir / 'references'
    if not refs_dir.exists() or not refs_dir.is_dir():
        return []
    
    ref_files = []
    for ref_file in sorted(refs_dir.glob('*.md')):
        filename = ref_file.name
        description = kebab_to_title(filename)
        ref_files.append((filename, description))
    
    return ref_files

def has_using_reference_section(content: str) -> bool:
    """Check if the content already has a 'Using the Reference Files' section."""
    pattern = r'^##\s+Using\s+the\s+Reference\s+Files\s*$'
    return bool(re.search(pattern, content, re.MULTILINE | re.IGNORECASE))

def create_using_reference_section(ref_files: List[Tuple[str, str]]) -> str:
    """Create the 'Using the Reference Files' section with proper links."""
    if not ref_files:
        return ""
    
    section = "## Using the Reference Files\n\n"
    for filename, description in ref_files:
        section += f"- [./references/{filename}](./references/{filename}): {description}\n"
    section += "\n"
    
    return section

def insert_using_reference_section(content: str, section: str) -> str:
    """Insert the 'Using the Reference Files' section before 'References' if it exists."""
    # Look for a References section (## References or similar)
    references_pattern = r'^(##\s+References?\s*)$'
    match = re.search(references_pattern, content, re.MULTILINE | re.IGNORECASE)
    
    if match:
        # Insert before the References section
        insert_pos = match.start()
        new_content = content[:insert_pos] + section + content[insert_pos:]
    else:
        # Append at the end
        new_content = content.rstrip() + "\n\n" + section
    
    return new_content

def count_links_in_section(content: str) -> int:
    """Count the number of reference links in the Using Reference Files section."""
    # Extract the section
    pattern = r'##\s+Using\s+the\s+Reference\s+Files\s*\n(.*?)(?=\n##|\Z)'
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    
    if not match:
        return 0
    
    section_content = match.group(1)
    # Count markdown links
    links = re.findall(r'\[.*?\]\(.*?\)', section_content)
    return len(links)

def process_skill_file(skill_path: Path, base_path: Path) -> Dict:
    """Process a single SKILL.md file."""
    result = {
        'path': str(skill_path.relative_to(base_path)),
        'updated': False,
        'section_added': False,
        'links_added': 0,
        'error': None
    }
    
    try:
        # Read the file
        with open(skill_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Find reference files
        skill_dir = skill_path.parent
        ref_files = find_reference_files(skill_dir)
        
        if not ref_files:
            # No reference files, skip
            return result
        
        # Check if section exists
        has_section = has_using_reference_section(original_content)
        
        if has_section:
            # Section exists, count existing links
            existing_links = count_links_in_section(original_content)
            result['links_added'] = 0  # Not adding new section
        else:
            # Create and insert the section
            section = create_using_reference_section(ref_files)
            new_content = insert_using_reference_section(original_content, section)
            
            # Write back
            with open(skill_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            result['updated'] = True
            result['section_added'] = True
            result['links_added'] = len(ref_files)
    
    except Exception as e:
        result['error'] = str(e)
    
    return result

def main():
    """Main execution function."""
    base_path = Path.cwd()
    
    # Find all SKILL.md files
    skill_files = list(base_path.rglob('**/SKILL.md'))
    
    print(f"Found {len(skill_files)} SKILL.md files")
    
    # Process each file
    results = []
    for skill_file in skill_files:
        result = process_skill_file(skill_file, base_path)
        results.append(result)
    
    # Calculate summary statistics
    files_updated = sum(1 for r in results if r['updated'])
    sections_added = sum(1 for r in results if r['section_added'])
    total_links_added = sum(r['links_added'] for r in results)
    errors = [r for r in results if r['error']]
    
    summary = {
        'total_skill_files': len(skill_files),
        'files_updated': files_updated,
        'sections_added': sections_added,
        'total_links_added': total_links_added,
        'errors': len(errors),
        'error_details': errors if errors else []
    }
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total SKILL.md files found: {summary['total_skill_files']}")
    print(f"Files updated: {summary['files_updated']}")
    print(f"'Using the Reference Files' sections added: {summary['sections_added']}")
    print(f"Total reference links added: {summary['total_links_added']}")
    print(f"Errors encountered: {summary['errors']}")
    
    if errors:
        print("\nErrors:")
        for err in errors:
            print(f"  - {err['path']}: {err['error']}")
    
    # Save summary to file
    with open('/tmp/skill_fix_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nDetailed summary saved to: /tmp/skill_fix_summary.json")
    
    return 0 if not errors else 1

if __name__ == '__main__':
    exit(main())
