
# Automated Book Data Collector

## Webora Tec – Advanced Python Programming Internship

**Task:** 3 – Automated Web Data Collector  
**Developer:** Mohamed Raahiq  
**Status:** Completed

## Project Overview

This Python project automatically collects book information
from Books to Scrape, a website designed for web scraping practice.

The application extracts book titles, prices, ratings,
availability, and product URLs.

Collected data is cleaned and exported to CSV and JSON formats.

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- Pandas
- CSV
- JSON

## Key Features

- Automated website data collection
- Multi-page web scraping
- Configurable keyword filtering
- Extract five book information fields
- Handle HTTP and connection errors
- Remove duplicate records
- Extract and validate book prices
- Export data to CSV and JSON
- Display summary statistics

## Project Results

| Metric | Result |
|--------|--------|
| Pages Scraped | 3 |
| Total Books | 60 |
| Average Price | GBP 35.00 |
| Highest Price | GBP 57.31 |
| Average Rating | 3.00/5 |

## Sample Data

| Book Title | Price (GBP) | Rating |
|------------|-------------|--------|
| A Light in the Attic | 51.77 | 3 |
| Tipping the Velvet | 53.74 | 1 |
| Soumission | 50.10 | 1 |
| Sharp Objects | 47.82 | 4 |
| Sapiens: A Brief History of Humankind | 54.23 | 5 |

## Project Structure

    Webora-Book-Data-Collector/
    |
    |-- main.py
    |-- books_data.csv
    |-- books_data.json
    |-- README.md

## Installation

Install the required libraries:

    py -m pip install requests beautifulsoup4 pandas

## How to Run

Run the application:

    py main.py

## Configuration

You can change the following settings in main.py:

    SEARCH_KEYWORD = ""
    MAX_PAGES = 3

Set SEARCH_KEYWORD to filter books by title.

Change MAX_PAGES to control the number of pages collected.

## Data Source

Website: https://books.toscrape.com/

This website is intended for educational web scraping practice.

## Learning Outcomes

- Web scraping with Python
- HTML parsing using BeautifulSoup
- HTTP requests and error handling
- Data cleaning using Pandas
- CSV and JSON file handling
- Duplicate removal
- Automated data collection

## Internship Details

**Organization:** Webora Tec  
**Program:** Advanced Python Programming Internship  
**Task:** 3 – Automated Web Data Collector

## Conclusion

This project demonstrates how Python can automate
web data collection, process structured information,
and generate reusable datasets for analysis.
