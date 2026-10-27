# Folder Organizer

A lightweight, automated Python utility designed to clean up cluttered directories by sorting files based on their extensions and isolating duplicate files. 

## Features

* **Extension-Based Sorting:** Automatically groups files into clean, categorized directories (e.g., `.pdf` to `/Documents`, `.png` to `/Images`).
* **Deduplication:** Scans files to identify and isolate duplicate files to save disk space.
* **Custom Mapping:** Easily configurable file-to-folder mapping rules.
* **Safe Operations:** Minimizes data loss risks by isolating duplicates rather than deleting them outright.

## Built With

* **Python 3.x**
* `os` & `shutil` (Standard libraries for file manipulation)
* `hashlib` (For cryptographic file hashing to accurately spot duplicates)

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd Folder-Organizer
   ```

2. **(Optional) Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

## Usage

Run the script from your terminal by providing the path to the directory you want to clean up:

```bash
python organizer.py --path "/path/to/your/cluttered/folder"
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
├── Documents/
│   └── invoice.pdf
├── Images/
│   └── photo.png
├── TextFiles/
│   └── notes.txt
└── Duplicates/
    └── invoice_copy.pdf
```

## Roadmap & Future Enhancements

- [ ] Add a visual Graphical User Interface (GUI) using Tkinter.
- [ ] Add logging functionality (`logging` module) to keep track of moved files.
- [ ] Implement a dry-run feature (`--dry-run`) to preview sorting actions without moving files.

## License

Distributed under the MIT License. See `LICENSE` for more information.
