```markdown
# WebNovel Scraper

## Introduction
WebNovel Scraper is a Python script for scraping and saving web novel content from Scribble Hub. It uses Selenium for web automation and BeautifulSoup for HTML parsing.

## Prerequisites
- Python 3.x
- Selenium (`pip install selenium`)
- Microsoft Edge WebDriver (Download and install from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Usage
1. Navigate to the directory containing the script:
   ```bash
   cd path/to/webnovel-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python scrapeweb.py
   ```

## Configuration
- Set the URL of the first page you want to scrape by modifying the `url` variable inside `scrapeweb.py`.
  ```python
  # Set the URL of the first page
  url = 'https://www.scribblehub.com/read/52931-rupegia/chapter/64649/'
  ```

- Set the number of pages you want to save by modifying the `page_count` variable inside `scrapeweb.py`.
  ```python
  # Set the number of pages you want to save
  page_count = 5
  ```

## Features
- Scrapes content from Scribble Hub.
- Handles pagination to scrape multiple pages.
- Cleans HTML content by removing author notes.

## Example
```python
# Set the URL of the first page
url = 'https://www.scribblehub.com/read/52931-rupegia/chapter/64649/'

# Set the number of pages you want to save
page_count = 5

# Run the web novel scraping script
python scrapeweb.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Selenium](https://www.selenium.dev/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

## Author
John Randel Carpio
Contact: carpio.johnrandel@gmail.com
