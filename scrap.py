from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# --- Setup Chrome Driver ---
options = Options()
options.add_argument("--start-maximized")  # open full screen
options.add_argument("--disable-blink-features=AutomationControlled")  # avoid bot detection

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# --- Replace this with your restaurant Google Maps link ---
url = "https://www.google.com/maps/place/Domino's+Pizza/@12.9716,77.5946,17z"
driver.get(url)
time.sleep(5)

# --- Click "All Reviews" button ---
try:
    all_reviews_button = driver.find_element(By.XPATH, '//button[contains(@aria-label,"reviews")]')
    all_reviews_button.click()
    time.sleep(5)
except:
    print("⚠️ Could not find the All Reviews button")
    driver.quit()

# --- Scroll to load more reviews ---
scrollable_div = driver.find_element(By.XPATH, '//div[@class="m6QErb DxyBCb kA9KIf dS8AEf"]')

for _ in range(15):  # adjust for more/less reviews
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
    time.sleep(2)

# --- Extract Reviews ---
reviews = driver.find_elements(By.CLASS_NAME, "wiI7pd")   # review texts
ratings = driver.find_elements(By.CLASS_NAME, "kvMYJc")   # star ratings

data = []
for r, s in zip(reviews, ratings):
    review_text = r.text.strip()
    rating_value = int(s.get_attribute("aria-label")[0])  # e.g. "5 stars" → 5
    data.append({"rating": rating_value, "review": review_text})

# --- Save to CSV ---
df = pd.DataFrame(data)
df.to_csv("google_reviews.csv", index=False, encoding="utf-8-sig")

print(f"✅ Scraped {len(df)} reviews and saved to google_reviews.csv")

driver.quit()
