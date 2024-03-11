import ebooklib
from ebooklib import epub
import os
import glob
from bs4 import BeautifulSoup

# Function to create a table of contents page
def create_toc_page(toc):
    toc_page = epub.EpubHtml(title='Table of Contents', file_name='toc.xhtml')
    toc_page.content = '<h1>Table of Contents</h1><ul>'
    for link in toc:
        if link.href != 'credits.xhtml':
            toc_page.content += f'<li><a href="{link.href}">{link.title}</a></li>'
    toc_page.content += '</ul>'
    return toc_page

# Function to sanitize a filename by replacing invalid characters
def sanitize_filename(filename):
    invalid_chars = '<>:"/\\|?*'  # Characters not allowed in filenames
    for char in invalid_chars:
        filename = filename.replace(char, '_')  # Replace invalid characters with underscores
    return filename

try:
    # Create a new EPUB book
    book = epub.EpubBook()

    # Set the book's metadata
    book.set_title('Rupegia')
    book.set_language('en')
    book.add_metadata('DC', 'publisher', 'https://www.scribblehub.com/series/52931/rupegia/')
    book.add_author('Manasong')

    # Set the cover image
    try:
        book.set_cover("image.jpg", open('cover.jpg', 'rb').read())
    except FileNotFoundError:
        print('Cover image not found')
        exit(1)

    # Add a credits page
    credits = epub.EpubHtml(title='Credits', file_name='credits.xhtml')
    credits.content = '<h1>Credits</h1><p>Original website: <a href="https://www.scribblehub.com/series/52931/rupegia/">Scribble Hub</a></p><p>Author: Manasong</p>'
    book.add_item(credits)

    # Create the table of contents
    toc = [epub.Link('credits.xhtml', 'Credits', 'credits')]

    # Set the folder containing chapter HTML files
    chapters_folder = 'D:\\Files\\PyScrap\\Rupegia'
    chapter_files = sorted(glob.glob(os.path.join(chapters_folder, '*.html')), key=os.path.getmtime)
    print(f"Found {len(chapter_files)} chapter files")
    
    chapters = []
    
    # Iterate through chapter HTML files
    for i, chapter_file in enumerate(chapter_files):
        with open(chapter_file, 'r', encoding='utf-8') as f:
            chapter_content = f.read()

        # Extract the chapter title
        soup = BeautifulSoup(chapter_content, 'html.parser')
        h1_tag = soup.find('h1')
        if h1_tag is not None:
            chapter_title = h1_tag.text.strip()
        else:
            print(f"Can't find title for file {i+1}")
            exit(1)

        # Sanitize the title for use as a filename
        sanitized_title = sanitize_filename(chapter_title)
        chapter_filename = f'{sanitized_title}.xhtml'
        
        # Create an EPUB HTML item for the chapter
        chapter = epub.EpubHtml(title=chapter_title, file_name=chapter_filename, content=chapter_content)
        book.add_item(chapter)
        toc.append(epub.Link(chapter_filename, chapter_title, sanitized_title))
        
        chapters.append(chapter)

    # Add a table of contents page
    toc_page = create_toc_page(toc)
    book.add_item(toc_page)

    # Add the table of contents to the book
    book.toc = toc

    # Set the order of the chapters in the book
    book.spine = ['nav', credits, toc_page] + chapters

    # Save the EPUB file
    epub_path = 'D:\\Files\\PyScrap\\Rupegia\\rupegia.epub'
    epub.write_epub(epub_path, book, {})
except Exception as e:
    print(f"An error occurred: {e}")
