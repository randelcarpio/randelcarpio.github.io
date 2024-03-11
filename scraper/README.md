```markdown
# WebNovel Scraper

## Introduction
WebNovel Scraper is a Python script for scraping and saving web novel content from Scribble Hub. It utilizes Selenium for web automation and BeautifulSoup for HTML parsing.

## Prerequisites
- Python 3.x
- Selenium library (`pip install selenium`)
- Microsoft Edge WebDriver (Download and install from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/webnovel-scraper.git
   cd webnovel-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python saveweb.py
   ```

## Configuration
- Ensure that the Microsoft Edge WebDriver executable is in your system's PATH.
- Update the `url` variable in `saveweb.py` with the URL of the first page you want to scrape.

## Features
- Scrapes content from Scribble Hub.
- Handles pagination to scrape multiple pages.
- Cleans HTML content by removing author notes.

## Example
```python
# Update the URL with the starting page
url = 'https://www.scribblehub.com/read/52931-rupegia/chapter/64649/'

# Set the number of pages you want to save
page_count = 5

for page_number in range(1, page_count + 1):
    title, content, url = scrape_webpage(url)
    save_html(title, content)

    if not url:
        break
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Selenium](https://www.selenium.dev/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

## Author
John Randel Carpio
Contact: carpio.johnrandel@gmail.com
