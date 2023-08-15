# Homework 9  

##  Quotes Scraper

## This package includes the following scripts: 
**Scraper**  
	This script allows you to scrape quotes and author information from the website http://quotes.toscrape.com and store the data in JSON files. The extracted data includes the quote text, author name, tags, and author details. 
 
**Baseloader**  
	This script from the previous homework assignment is used to upload data to the MongoDB Atlas database.

## Requirements

- Python 3.x
- `beautifulsoup4` library
- `mongoengine`  library 

You can install the required libraries using the following command:

	pip install beautifulsoup4 requests
	pip install mongoengine

## Usage

1. Clone this repository or download the ZIP file and extract it to your desired location.
2. Open a terminal or command prompt and navigate to the project directory.

**Scraper**

1. Run the script by entering the following command:

		python scraper.py

or run this script for multiprocessing version of scrapper:

		python scraper_multiprocess.py

**ATTENTION. The order of the parsing results will differ from the order in the source.**

3. You will be prompted to enter the starting page number for scraping (up to 10). Follow the instructions on the terminal.
4. The script will start scraping quotes and author information from the specified page onwards. The extracted data will be stored in two JSON files: `quotes.json` and `authors.json`.

**Baseloader**  
	Run the `baseloader.py` script to load the data from `quotes.json` and `authors.json` into the MongoDB Atlas database:

		python baseloader.py


You can verify the availability of the data in MongoDB database using this connection string:

		"mongodb+srv://deuterrium:QdW9KTJr3ssa8gMy@cluster0.7r0vvpw.mongodb.net/test?retryWrites=true&w=majority"

## License

This project is licensed under the MIT License.
