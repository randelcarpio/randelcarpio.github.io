# WebNovel Scraper

# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re

# Function to scrape the content of a webpage
def scrape_webpage(url):
    # Set up the Selenium WebDriver for Microsoft Edge
    driver = webdriver.Edge()
    driver.get(url)

    # Wait for the chp_raw div element to be loaded
    try:
        chp_raw_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "chp_raw"))
        )
    except TimeoutException:
        raise ValueError("The 'chp_raw' div element was not found.")

    # Extract the content of the chp_raw div element
    content = chp_raw_div.get_attribute('innerHTML')

    # Remove all author notes from the content
    soup = BeautifulSoup(content, 'html.parser')
    for author_notes in soup.find_all('div', class_='wi_authornotes'):
        author_notes.decompose()
    content = str(soup)

    # Extract the title from the webpage, remove the "| Scribble Hub" and "Rupegia - " parts, and replace ":" with " - "
    title = driver.title.strip().replace(' | Scribble Hub', '').replace('Rupegia - ', '').replace(':', ' - ')

    # Find the next page link
    next_page_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn-next'))
    )
    
    if next_page_link:
        next_page_url = next_page_link.get_attribute('href')
    else:
        next_page_url = None

    # Close the WebDriver
    driver.quit()

    return title, content, next_page_url

# Function to save HTML content to a file
def save_html(title, content):
    # Remove invalid characters from the file name
    file_name = re.sub(r'[\\/*?:"<>|]', '', title) + '.html'

    # Write the HTML content to a file
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write('<html>\n<head>\n<meta charset="UTF-8">\n</head>\n<body>\n')
        file.write(f'<h1>{title}</h1>\n')
        file.write(content)
        file.write('\n</body>\n</html>\n')

    print(f'HTML file "{file_name}" created successfully.')

# Main function
def main():
    # Replace with the URL of the first page
    url = 'https://www.scribblehub.com/read/52931-rupegia/chapter/64649/'

    # Set the number of pages you want to save
    page_count = 5

    # Loop through pages and scrape content
    for page_number in range(1, page_count + 1):
        title, content, url = scrape_webpage(url)
        save_html(title, content)

        # Break the loop if there is no next page
        if not url:
            break

# Entry point of the script
if __name__ == '__main__':
    main()
