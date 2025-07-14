# 🇰🇪 Kenya Government Tenders Web Scraper

This project is a **Python-based web scraper** that extracts all public tenders listed on [https://tenders.go.ke/tenders](https://tenders.go.ke/tenders).  
It uses **Selenium** and **BeautifulSoup** to:
- Navigate the site
- Scrape tender data across multiple pages
- Save everything into a well-formatted CSV file

---

## 📦 Features

- ✅ Scrapes all tenders (not just the first page)
- ✅ Extracts clean headers and rows
- ✅ Handles pagination automatically
- ✅ Saves data to `tenders_data.csv`
- ✅ Clean and readable code for learning or extension

---

## 🛠️ Technologies Used

- Python 3
- Selenium
- BeautifulSoup (bs4)
- Webdriver Manager (for Chrome)
- CSV module

---

## 📁 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/tenders-scraper.git
cd tenders-scraper
