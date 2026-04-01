#!/usr/bin/env python3
"""
Script to remove redundant "References" section from SKILL.md files.
Preserves "Using the Reference Files" section.
"""

import os
import re
from pathlib import Path

def remove_references_section(content):
    """
    Remove the redundant "## References" section.
    This section has unqualified links like [Text](references/file.md)
    We preserve "## Using the Reference Files" which has qualified links like [Text](./references/file.md)
    """
    # Pattern to match "## References" section until the next section or end of file
    # We look for "## References" followed by content until we hit another ## header or EOF
    pattern = r'\n## References\n(?:.*?\n)*?(?=\n##|\Z)'
    
    # Check if the pattern exists
    if re.search(pattern, content, re.DOTALL):
        # Remove the section
        new_content = re.sub(pattern, '', content, flags=re.DOTALL)
        return new_content, True
    
    return content, False

def process_skill_files():
    """Process all SKILL.md files in the repository."""
    files_processed = 0
    files_modified = 0
    sections_removed = 0
    
    # Find all SKILL.md files
    for skill_file in Path('.').rglob('SKILL.md'):
        files_processed += 1
        
        try:
            # Read the file
            with open(skill_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # Remove the redundant References section
            new_content, was_modified = remove_references_section(original_content)
            
            if was_modified:
                # Write back the modified content
                with open(skill_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                files_modified += 1
                sections_removed += 1
                print(f"✓ Modified: {skill_file}")
            else:
                print(f"  Skipped (no References section): {skill_file}")
                
        except Exception as e:
            print(f"✗ Error processing {skill_file}: {e}")
    
    return files_processed, files_modified, sections_removed

if __name__ == "__main__":
    print("Starting cleanup of redundant References sections...")
    print("=" * 70)
    
    files_processed, files_modified, sections_removed = process_skill_files()
    
    print("=" * 70)
    print(f"\nSummary:")
    print(f"  Total SKILL.md files found: {files_processed}")
    print(f"  Files modified: {files_modified}")
    print(f"  References sections removed: {sections_removed}")
    print(f"\nCleanup complete!")
