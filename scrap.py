from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time, pandas as pd

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

url = "https://www.google.com/maps/place/Domino's+Pizza/@12.9716,77.5946,17z"
driver.get(url)

# wait for "All reviews" button
wait = WebDriverWait(driver, 10)
all_reviews_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(@jsaction,"pane.reviewChart.moreReviews")]'))
)
all_reviews_button.click()
time.sleep(3)

# scroll container
scrollable_div = driver.find_element(By.XPATH, '//div[@class="m6QErb DxyBCb kA9KIf dS8AEf"]')

for _ in range(10):
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
    time.sleep(2)

reviews = driver.find_elements(By.CLASS_NAME, "wiI7pd")
ratings = driver.find_elements(By.CLASS_NAME, "kvMYJc")

data = []
for r, s in zip(reviews, ratings):
    data.append({
        "rating": int(s.get_attribute("aria-label")[0]),
        "review": r.text.strip()
    })

df = pd.DataFrame(data)
df.to_csv("google_reviews.csv", index=False, encoding="utf-8-sig")
print(f"✅ Scraped {len(df)} reviews")
driver.quit()
