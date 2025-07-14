from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://tenders.go.ke/tenders"
driver.get(url)
time.sleep(5)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

headers = []
headers_row = soup.find_all("tr", class_="text-caption")

for row in headers_row:
    th_elements = row.find_all("th", class_="font-weight-bold")
    for th in th_elements:
        span = th.find("span", class_="me-2")
        if span:
            headers.append(span.get_text(strip=True))

print("\nHeaders:")
print(" | ".join(headers))


all_tenders = []

while True:
  
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")


    rows = soup.select("tbody tr")
    for row in rows:
        cols = row.find_all("td")
        data = [col.get_text(strip=True) for col in cols]
        all_tenders.append(data)

    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "li.v-pagination__next button")
        if "disabled" in next_button.get_attribute("class"):
            print("🚫 'Next' button is disabled. No more pages.")
            break
        next_button.click()
        print("➡️  Clicked 'Next' to go to next page...")
        time.sleep(3)
    except Exception as e:
        print("🚫 No more pages or error:", e)
        break


driver.quit()

print(f"\nTotal Tenders Scraped: {len(all_tenders)}")
print("Sample Rows:\n")
for tender in all_tenders[:10]: 
    print(" | ".join(tender))

filename = "tenders_data.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)       
    writer.writerows(all_tenders)  

print(f"\n✅ Saved all tenders to '{filename}'")