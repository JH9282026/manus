#!/usr/bin/env python3
"""
Fix links in 'Using the Reference Files' sections of SKILL.md files.
- Add ./ prefix to relative paths
- Generate meaningful descriptions from filenames
"""

import re
import glob
from pathlib import Path

def filename_to_description(filename):
    """Convert kebab-case filename to Title Case description."""
    # Remove .md extension
    name = filename.replace('.md', '')
    # Replace hyphens and underscores with spaces
    name = name.replace('-', ' ').replace('_', ' ')
    # Title case
    return name.title()

def fix_links_in_section(content):
    """Fix links in the 'Using the Reference Files' section."""
    # Find the "Using the Reference Files" section
    section_pattern = r'(## Using the Reference Files\s*\n)(.*?)(?=\n##|\Z)'
    
    match = re.search(section_pattern, content, re.DOTALL)
    if not match:
        return content, 0, 0
    
    section_start = match.start(2)
    section_end = match.end(2)
    section_content = match.group(2)
    original_section = section_content
    
    links_fixed = 0
    descriptions_improved = 0
    
    # Pattern to match markdown links: [text](url)
    link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    
    def fix_link(match):
        nonlocal links_fixed, descriptions_improved
        
        link_text = match.group(1)
        link_url = match.group(2)
        
        # Fix 1: Add ./ prefix if missing
        new_url = link_url
        if link_url.startswith('references/') and not link_url.startswith('./'):
            new_url = './' + link_url
            links_fixed += 1
        
        # Fix 2: Improve description if it's just the path
        new_text = link_text
        # Check if link text is essentially the same as the URL (with or without ./)
        if link_text == link_url or link_text == new_url or link_text.replace('./', '') == new_url.replace('./', ''):
            # Extract filename from path
            filename = Path(new_url).name
            new_text = filename_to_description(filename)
            descriptions_improved += 1
        
        return f'[{new_text}]({new_url})'
    
    # Apply fixes to all links in the section
    new_section_content = re.sub(link_pattern, fix_link, section_content)
    
    # Only return modified content if changes were made
    if new_section_content != original_section:
        new_content = content[:section_start] + new_section_content + content[section_end:]
        return new_content, links_fixed, descriptions_improved
    
    return content, 0, 0

def main():
    # Find all SKILL.md files
    skill_files = glob.glob('**/*SKILL.md', recursive=True)
    
    total_files_updated = 0
    total_links_fixed = 0
    total_descriptions_improved = 0
    
    for filepath in skill_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content, links_fixed, descriptions_improved = fix_links_in_section(content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                total_files_updated += 1
                total_links_fixed += links_fixed
                total_descriptions_improved += descriptions_improved
                
                print(f"✓ {filepath}: {links_fixed} links fixed, {descriptions_improved} descriptions improved")
        
        except Exception as e:
            print(f"✗ Error processing {filepath}: {e}")
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Files updated: {total_files_updated}")
    print(f"Links fixed (added ./ prefix): {total_links_fixed}")
    print(f"Descriptions improved: {total_descriptions_improved}")
    print("="*60)

if __name__ == '__main__':
    main()
