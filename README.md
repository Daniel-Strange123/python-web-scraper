# Books to Scrape – Python Web Scraper

## Project Overview

This project is a Python web scraper built with **Requests** and **BeautifulSoup**. It extracts book information from [Books to Scrape](https://books.toscrape.com/), a website designed for practicing web scraping.

The scraper automatically navigates through all 50 pages of the website, collects information about the books, and saves the results in a CSV file.

## Features

- Scrapes all 50 pages automatically.
- Extracts information about 1,000 books.
- Collects book titles.
- Extracts book prices.
- Retrieves book ratings.
- Checks book availability.
- Handles pagination using a `while` loop.
- Saves the collected information into a CSV file.

## Technologies Used

- **Python** – Programming language.
- **Requests** – Sends HTTP requests to the website.
- **BeautifulSoup** – Parses HTML and extracts information.
- **CSV** – Stores scraped information in a spreadsheet-compatible format.
- **URL Join** – Combines relative links with the website's base URL.

## Project Structure

```text
web_scraper_project/
│
├── main.py
├── books.csv
├── README.md
└── venv/
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone /Daniel-Strange123/python-web-scraper/
```

### 2. Navigate into the project folder

```bash
cd web_scraper_project
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install requests beautifulsoup4
```

## How to Run the Project

Run the following command in your terminal:

```bash
python main.py
```

The scraper will automatically visit the website, collect book information from all available pages, and save the results in `books.csv`.

## Data Collected

The scraper extracts four fields:

| Field | Description |
|---|---|
| Title | Name of the book |
| Price | Listed price of the book |
| Rating | Book rating (One to Five) |
| Availability | Whether the book is in stock |

## Output

The scraped information is saved in:

```text
books.csv
```

The expected result is 1,000 book records, plus one header row.

The CSV file can be opened using Microsoft Excel, Google Sheets, or any spreadsheet application that supports CSV files.

## Concepts Practised

Through this project, I practised:

- Python imports and libraries.
- HTTP requests.
- HTML structure and elements.
- HTML attributes and CSS classes.
- BeautifulSoup's `find()` and `find_all()` methods.
- Python lists and loops.
- Conditional statements.
- URL handling and pagination.
- CSV file creation and writing.
- Data extraction and storage.

## Learning Outcome

This project helped me understand how web scraping works, how to extract structured information from HTML pages, how to automate pagination, and how to save collected data for further use.

## Disclaimer

This project is for educational purposes. Books to Scrape is a practice website intended for learning web scraping.
