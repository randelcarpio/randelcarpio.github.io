```markdown
# Rupegia EPUB Creator

## Introduction
Rupegia EPUB Creator is a Python script that generates an EPUB file from a series of HTML chapters, creating a cohesive eBook. It utilizes the ebooklib, BeautifulSoup, and other libraries.

## Prerequisites
- Python 3.x
- ebooklib (`pip install EbookLib`)
- BeautifulSoup (`pip install beautifulsoup4`)

## Usage
1. Navigate to the directory containing the script:
   ```bash
   cd path/to/rupegia-epub-creator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python createbook.py
   ```

## Configuration
- Set the folder containing chapter HTML files in the `chapters_folder` variable inside `createbook.py`.
  ```python
  # Set the folder containing chapter HTML files
  chapters_folder = 'D:\\Files\\PyScrap\\Rupegia'
  ```

- Set the path where the EPUB file will be saved by modifying the `epub_path` variable inside `createbook.py`.
  ```python
  # Set the path for saving the EPUB file
  epub_path = 'D:\\Files\\PyScrap\\Rupegia\\rupegia.epub'
  ```

- Ensure a valid cover image named `cover.jpg` is present in the script directory.

## Features
- Creates an EPUB eBook from a series of HTML chapters.
- Sets book metadata, cover image, credits, and table of contents.

## Example
```python
# Set the folder containing chapter HTML files
chapters_folder = 'D:\\Files\\PyScrap\\Rupegia'

# Run the EPUB creation script
python createbook.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [ebooklib](https://github.com/aerkalov/ebooklib)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

## Author
John Randel Carpio
Contact: carpio.johnrandel@gmail.com
