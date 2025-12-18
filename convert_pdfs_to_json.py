#!/usr/bin/env python3
"""
Script to convert PDF files to JSON format.
Extracts text from each page and creates a structured JSON output.
"""

import json
import os
import pdfplumber
import sys
from pathlib import Path


def convert_pdf_to_json(pdf_path, output_path=None):
    """
    Convert a PDF file to JSON format.
    
    Args:
        pdf_path: Path to the input PDF file
        output_path: Path to the output JSON file (optional)
    
    Returns:
        Dictionary containing the PDF data
    """
    if output_path is None:
        output_path = str(Path(pdf_path).with_suffix('.json'))
    
    print(f"Processing: {pdf_path}")
    
    pdf_data = {
        "filename": os.path.basename(pdf_path),
        "total_pages": 0,
        "pages": []
    }
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            pdf_data["total_pages"] = len(pdf.pages)
            
            for i, page in enumerate(pdf.pages, start=1):
                # Extract text from the page
                text = page.extract_text()
                
                page_data = {
                    "page_number": i,
                    "text": text if text else ""
                }
                
                pdf_data["pages"].append(page_data)
                
                # Print progress
                if i % 10 == 0:
                    print(f"  Processed {i}/{pdf_data['total_pages']} pages...")
        
        # Write to JSON file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(pdf_data, f, ensure_ascii=False, indent=2)
        
        print(f"  Successfully converted to: {output_path}")
        print(f"  Total pages: {pdf_data['total_pages']}")
        
        return pdf_data
        
    except Exception as e:
        print(f"  Error processing {pdf_path}: {str(e)}", file=sys.stderr)
        raise


def main():
    """Main function to convert all PDF files in the repository."""
    # Get the directory where the script is located
    script_dir = Path(__file__).parent.absolute()
    
    # Find all PDF files in the directory
    pdf_files = list(script_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in the directory.")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s) to convert:\n")
    
    for pdf_file in sorted(pdf_files):
        try:
            convert_pdf_to_json(str(pdf_file))
            print()
        except Exception as e:
            print(f"Failed to convert {pdf_file}: {e}\n", file=sys.stderr)
            continue
    
    print("Conversion complete!")


if __name__ == "__main__":
    main()
