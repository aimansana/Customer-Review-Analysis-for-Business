from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Launch browser
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.google.com/maps/place/Domino's+Pizza/@12.9716,77.5946,17z"
driver.get(url)
time.sleep(5)

# Open All Reviews
all_reviews_button = driver.find_element(By.XPATH, '//button[contains(text(),"reviews")]')
all_reviews_button.click()
time.sleep(5)

# Sort reviews by "Newest"
sort_button = driver.find_element(By.XPATH, '//button[@aria-label="Sort reviews"]')
sort_button.click()
time.sleep(2)
newest_button = driver.find_element(By.XPATH, '//div[@role="menuitem" and contains(text(),"Newest")]')
newest_button.click()
time.sleep(3)

# Scroll to load reviews
for _ in range(10):
    scrollable_div = driver.find_element(By.XPATH, '//div[@class="m6QErb DxyBCb kA9KIf dS8AEf"]')
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
    time.sleep(2)

# Extract fields
reviews = driver.find_elements(By.CLASS_NAME, "wiI7pd")   # review text
ratings = driver.find_elements(By.CLASS_NAME, "kvMYJc")   # star ratings
dates = driver.find_elements(By.CLASS_NAME, "rsqaWe")     # review date (e.g., "2 weeks ago")
likes = driver.find_elements(By.CLASS_NAME, "GBkF3d")     # number of likes (can be blank)

data = []
for r, s, d, l in zip(reviews, ratings, dates, likes):
    likes_count = l.text if l.text != "" else "0"  # blank means 0 likes
    data.append({
        "review": r.text,
        "rating": int(s.get_attribute("aria-label")[0]),  # "5 stars" → 5
        "date": d.text,
        "likes": int(likes_count)
    })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("google_latest_reviews.csv", index=False, encoding="utf-8-sig")

driver.quit()
