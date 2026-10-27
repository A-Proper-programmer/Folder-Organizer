# Folder Organizer

A lightweight, automated Python utility designed to clean up cluttered directories by sorting files based on their extensions and isolating duplicate files. 

## Features

* **Extension-Based Sorting:** Automatically groups files into clean, categorized directories (e.g., `.pdf` to `/.pdf files`, `.png` to `.png files`).
* **Logging:** Add logging functionality to keep track of moved files.
* **Deduplication:** Scans files to identify and isolate duplicate files to save disk space.
* **Safe Operations:** Minimizes data loss risks by isolating duplicates rather than deleting them outright.

## Built With

* **Python 3.11.3**
* `os` & `shutil` (Standard libraries for file manipulation)
* `hashlib` (For cryptographic file hashing to accurately spot duplicates)

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com <URL>
   cd Folder-Organizer
   
## Usage

Run the script from your terminal by providing the path to the directory you want to clean up:

```bash
FolderOrganizer.py --folder "/path/to/your/cluttered/folder"
```

### Example Before & After

**Before running the script:**
```text
Downloads/
├── invoice.pdf
├── photo.png
├── notes.txt
└── invoice_copy.pdf  (Duplicate)
```

**After running the script:**
```text
Downloads/
├── .pdf files/
│   └── invoice.pdf
├── .png files/
│   └── photo.png
├── .txt files/
│   └── notes.txt
└── Duplicate files/
    └── invoice_copy.pdf
```

## Roadmap & Future Enhancements

- [ ] Manage situations with password-protected files
- [ ] Try to group file based on type of file (image, video) instead of raw extensions.
- [ ] Handle situations where file-to-be-organized has the same name as an already organized file.
