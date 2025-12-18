# Notes Repository - File Conversion to JSON

This repository contains biblical texts and reference materials, with conversion scripts to transform them into JSON format for easier programmatic access.

## Files Converted to JSON

### 1. HebrewOT.txt → HebrewOT.json
**Status**: ✅ Converted

A text file containing verses from the Hebrew Old Testament. The conversion script parses the verse references and text content into a structured JSON format.

**JSON Structure**:
```json
{
  "source": "HebrewOT.txt",
  "type": "Biblical Text",
  "verses": [
    {
      "reference": "Genesis 1:1",
      "text": "In the beginning God created the heaven and the earth."
    }
  ]
}
```

### 2. Dictionary of Church Terms - Father Tadros Yacoub Malaty.pdf
**Status**: ⏳ Pending - PDF file needs to be added to repository

This PDF will be converted to extract text content from each page into JSON format.

**Expected JSON Structure**:
```json
{
  "source": "Dictionary of Church Terms - Father Tadros Yacoub Malaty.pdf",
  "type": "PDF Document",
  "total_pages": N,
  "pages": [
    {
      "page_number": 1,
      "content": "..."
    }
  ]
}
```

### 3. Bible Atlas - Zaine Ridling.pdf
**Status**: ⏳ Pending - PDF file needs to be added to repository

This PDF will be converted to extract text content from each page into JSON format.

**Expected JSON Structure**:
```json
{
  "source": "Bible Atlas - Zaine Ridling.pdf",
  "type": "PDF Document",
  "total_pages": N,
  "pages": [
    {
      "page_number": 1,
      "content": "..."
    }
  ]
}
```

## Conversion Scripts

### convert_text_to_json.py
Converts HebrewOT.txt to JSON format.

**Usage**:
```bash
python3 convert_text_to_json.py
```

**Input Format**: Text file with verse references followed by verse text:
```
Book Chapter:Verse
Text content here...

Book Chapter:Verse
More text content...
```

### convert_pdf_to_json.py
Converts PDF files to JSON format by extracting text from each page.

**Usage**:
```bash
python3 convert_pdf_to_json.py
```

**Dependencies**: PyPDF2 (automatically installed if missing)

**Note**: The PDF files need to be added to the repository before running this script.

## Adding PDF Files

To complete the conversion of the PDF files:

1. Add the following files to the repository root:
   - `Dictionary of Church Terms - Father Tadros Yacoub Malaty.pdf`
   - `Bible Atlas - Zaine Ridling.pdf`

2. Run the conversion script:
   ```bash
   python3 convert_pdf_to_json.py
   ```

3. The JSON files will be created:
   - `Dictionary_of_Church_Terms.json`
   - `Bible_Atlas.json`

## Output Files

- `HebrewOT.json` - Converted biblical text
- `Dictionary_of_Church_Terms.json` - (Will be created when PDF is added)
- `Bible_Atlas.json` - (Will be created when PDF is added)
