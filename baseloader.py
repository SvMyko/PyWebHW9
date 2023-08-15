import json
from connection import mongo_connect
from models import Author, Quote


def mongo_loader():

    with open('authors.json', 'r', encoding='utf-8') as authors_file:
        authors_data = json.load(authors_file)

    with open('quotes.json', 'r', encoding='utf-8') as quotes_file:
        quotes_data = json.load(quotes_file)

    for author_data in authors_data:
        author = Author(**author_data)
        author.save()

    for quote_data in quotes_data:
        author_fullname = quote_data.pop('author')
        authors = Author.objects.filter(fullname=author_fullname)

        for author in authors:
            quote = Quote(author=author, **quote_data)
            quote.save()
    print("Data loaded")

if __name__ == "__main__":
    mongo_connect()
    mongo_loader()
