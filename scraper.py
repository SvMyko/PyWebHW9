import requests
from bs4 import BeautifulSoup
import json


def get_author_info(author_link):
    author_page = requests.get(f"http://quotes.toscrape.com{author_link}")
    author_soup = BeautifulSoup(author_page.content, 'html.parser')
    fullname = author_soup.find('h3', class_='author-title').text.strip()
    born_date = author_soup.find('span', class_='author-born-date').text.strip()
    born_location = author_soup.find('span', class_='author-born-location').text.strip()
    description = author_soup.find('div', class_='author-description').text.strip()

    author_info = {
        "fullname": fullname,
        "born_date": born_date,
        "born_location": born_location,
        "description": description
    }
    return author_info


def parse_quotes(start_page, end_page):
    quotes = []
    authors = []
    
    for page_number in range(start_page, end_page + 1):
        page = requests.get(f"http://quotes.toscrape.com/page/{page_number}/")
        soup = BeautifulSoup(page.content, 'html.parser')
        quotes_container = soup.find_all('div', class_='quote')
        if not quotes_container:
            print(f"Page {page_number} is empty")
            continue
            
        print(f"Parsing web page {page_number}")
        for quote_container in quotes_container:
            quote_text = quote_container.find('span', class_='text').text.strip()
            author_name = quote_container.find('small', class_='author').text.strip()
            author_link = quote_container.find('a')['href']
            tags = [tag.text.strip() for tag in quote_container.find_all('a', class_='tag')]

            author_info = get_author_info(author_link)
            authors.append(author_info)
            quote_info = {
                "tags": tags,
                "author": author_name,
                "quote": quote_text
            }
            quotes.append(quote_info)
    return quotes, authors


def write_to_files(quotes, authors):
    print("Writing data to files")
    with open('quotes.json', 'w', encoding='utf-8') as quotes_file:
        json.dump(quotes, quotes_file, ensure_ascii=False, indent=2)
    with open('authors.json', 'w', encoding='utf-8') as authors_file:
        json.dump(authors, authors_file, ensure_ascii=False, indent=2)
    print("Job done")


def main():
    while True:
        try:
            start_page = int(input("Enter the starting page number (up to 10): "))
            if start_page < 1 or start_page > 10:
                raise ValueError("Page number should be between 1 and 10")
            end_page = int(input("Enter the ending page number (up to 10: "))
            if end_page < start_page or end_page > 10:
                raise ValueError("Page number should be between 1 and 10")
            quotes, authors = parse_quotes(start_page, end_page)
            write_to_files(quotes, authors)
            break
        except ValueError as verr:
            print(verr)


if __name__ == "__main__":
    main()
