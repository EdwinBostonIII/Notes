#!/usr/bin/env python3
"""
Master conversion script for all files to JSON format
Converts:
1. HebrewOT.txt
2. Dictionary of Church Terms - Father Tadros Yacoub Malaty.pdf
3. Bible Atlas - Zaine Ridling.pdf
"""
import os
import sys
import json

# Import the individual converters
try:
    from convert_text_to_json import parse_hebrew_ot
    from convert_pdf_to_json import convert_pdf_to_json
except ImportError as e:
    print(f"Error importing conversion modules: {e}")
    print("Please ensure all conversion scripts are in the same directory.")
    sys.exit(1)


def main():
    """
    Run all conversions
    """
    print("=" * 60)
    print("Converting files to JSON format")
    print("=" * 60)
    
    conversions = []
    
    # 1. Convert HebrewOT.txt
    print("\n1. Converting HebrewOT.txt...")
    if os.path.exists('HebrewOT.txt'):
        try:
            parse_hebrew_ot('HebrewOT.txt', 'HebrewOT.json')
            conversions.append(('HebrewOT.txt', 'HebrewOT.json', 'SUCCESS'))
        except Exception as e:
            print(f"   Error: {e}")
            conversions.append(('HebrewOT.txt', 'HebrewOT.json', f'FAILED: {e}'))
    else:
        print("   File not found. Skipping.")
        conversions.append(('HebrewOT.txt', 'HebrewOT.json', 'SKIPPED: File not found'))
    
    # 2. Convert Dictionary of Church Terms PDF
    print("\n2. Converting Dictionary of Church Terms - Father Tadros Yacoub Malaty.pdf...")
    dict_pdf = 'Dictionary of Church Terms - Father Tadros Yacoub Malaty.pdf'
    if os.path.exists(dict_pdf):
        try:
            convert_pdf_to_json(dict_pdf, 'Dictionary_of_Church_Terms.json')
            conversions.append((dict_pdf, 'Dictionary_of_Church_Terms.json', 'SUCCESS'))
        except Exception as e:
            print(f"   Error: {e}")
            conversions.append((dict_pdf, 'Dictionary_of_Church_Terms.json', f'FAILED: {e}'))
    else:
        print("   File not found. Skipping.")
        conversions.append((dict_pdf, 'Dictionary_of_Church_Terms.json', 'SKIPPED: File not found'))
    
    # 3. Convert Bible Atlas PDF
    print("\n3. Converting Bible Atlas - Zaine Ridling.pdf...")
    atlas_pdf = 'Bible Atlas - Zaine Ridling.pdf'
    if os.path.exists(atlas_pdf):
        try:
            convert_pdf_to_json(atlas_pdf, 'Bible_Atlas.json')
            conversions.append((atlas_pdf, 'Bible_Atlas.json', 'SUCCESS'))
        except Exception as e:
            print(f"   Error: {e}")
            conversions.append((atlas_pdf, 'Bible_Atlas.json', f'FAILED: {e}'))
    else:
        print("   File not found. Skipping.")
        conversions.append((atlas_pdf, 'Bible_Atlas.json', 'SKIPPED: File not found'))
    
    # Print summary
    print("\n" + "=" * 60)
    print("CONVERSION SUMMARY")
    print("=" * 60)
    for source, output, status in conversions:
        print(f"Source: {source}")
        print(f"Output: {output}")
        print(f"Status: {status}")
        print("-" * 60)
    
    # Check if all successful
    successful = [c for c in conversions if 'SUCCESS' in c[2]]
    skipped = [c for c in conversions if 'SKIPPED' in c[2]]
    failed = [c for c in conversions if 'FAILED' in c[2]]
    
    print(f"\nTotal: {len(conversions)} files")
    print(f"Successful: {len(successful)}")
    print(f"Skipped: {len(skipped)}")
    print(f"Failed: {len(failed)}")
    
    if skipped:
        print("\nNote: Some files were skipped because they don't exist yet.")
        print("Please add the missing PDF files to the repository and run this script again.")


if __name__ == '__main__':
    main()
