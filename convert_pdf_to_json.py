#!/usr/bin/env python3
"""
Convert PDF files to JSON format
Handles:
- Dictionary of Church Terms - Father Tadros Yacoub Malaty.pdf
- Bible Atlas - Zaine Ridling.pdf
"""
import json
import sys
import os

import PyPDF2


def convert_pdf_to_json(pdf_path, output_path):
    """
    Convert a PDF file to JSON format.
    Extracts text content from each page.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' not found.")
        return None
    
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            pages = []
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                
                pages.append({
                    'page_number': page_num + 1,
                    'content': text.strip()
                })
            
            # Create JSON structure
            result = {
                'source': os.path.basename(pdf_path),
                'type': 'PDF Document',
                'total_pages': len(pdf_reader.pages),
                'pages': pages
            }
            
            # Write to output file
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            
            print(f"Converted {len(pages)} pages from {pdf_path} to {output_path}")
            return result
    
    except Exception as e:
        print(f"Error converting PDF: {e}")
        return None


if __name__ == '__main__':
    # Convert Dictionary of Church Terms
    dict_pdf = 'Dictionary of Church Terms - Father Tadros Yacoub Malaty.pdf'
    if os.path.exists(dict_pdf):
        convert_pdf_to_json(
            dict_pdf,
            'Dictionary_of_Church_Terms.json'
        )
    else:
        print(f"Note: '{dict_pdf}' not found. Skipping.")
    
    # Convert Bible Atlas
    atlas_pdf = 'Bible Atlas - Zaine Ridling.pdf'
    if os.path.exists(atlas_pdf):
        convert_pdf_to_json(
            atlas_pdf,
            'Bible_Atlas.json'
        )
    else:
        print(f"Note: '{atlas_pdf}' not found. Skipping.")
