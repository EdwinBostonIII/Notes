#!/usr/bin/env python3
"""
Convert HebrewOT.txt to JSON format
"""
import json
import re


def parse_hebrew_ot(input_file, output_file):
    """
    Parse HebrewOT.txt and convert to JSON format.
    Expected format: Book Chapter:Verse followed by text
    """
    verses = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_verse = None
    current_text = []
    
    for line in lines:
        line = line.strip()
        if not line:
            # Empty line - save current verse if exists
            if current_verse:
                verses.append({
                    'reference': current_verse,
                    'text': ' '.join(current_text).strip()
                })
                current_verse = None
                current_text = []
            continue
        
        # Check if line matches verse reference pattern (e.g., "Genesis 1:1" or "1 Chronicles 1:1")
        match = re.match(r'^(.+?)\s+(\d+):(\d+)$', line)
        if match:
            # Save previous verse if exists
            if current_verse:
                verses.append({
                    'reference': current_verse,
                    'text': ' '.join(current_text).strip()
                })
            # Start new verse
            book, chapter, verse = match.groups()
            current_verse = f"{book} {chapter}:{verse}"
            current_text = []
        else:
            # This is text content
            current_text.append(line)
    
    # Don't forget the last verse
    if current_verse:
        verses.append({
            'reference': current_verse,
            'text': ' '.join(current_text).strip()
        })
    
    # Create JSON structure
    result = {
        'source': 'HebrewOT.txt',
        'type': 'Biblical Text',
        'verses': verses
    }
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"Converted {len(verses)} verses to {output_file}")
    return result


if __name__ == '__main__':
    parse_hebrew_ot('HebrewOT.txt', 'HebrewOT.json')
