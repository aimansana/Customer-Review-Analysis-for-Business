import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://www.google.com/maps/place/Meghana+Foods+-+Marathahalli/@12.9496268,77.6971488,17z/data=!4m18!1m9!3m8!1s0x3bae12335ccf1b9d:0xa3365bee1a2d62ed!2sMeghana+Foods+-+Marathahalli!8m2!3d12.9496216!4d77.6997237!9m1!1b1!16s%2Fg%2F11b5pjcvm4!3m7!1s0x3bae12335ccf1b9d:0xa3365bee1a2d62ed!8m2!3d12.9496216!4d77.6997237!9m1!1b1!16s%2Fg%2F11b5pjcvm4?entry=ttu&g_ep=EgoyMDI1MDkwNy4wIKXMDSoASAFQAw%3D%3D"
driver.get(url)
time.sleep(5)

# Click Reviews button
reviews_button = driver.find_element(By.XPATH, '//button[contains(@aria-label,"reviews")]')
reviews_button.click()
time.sleep(5)

# Instead of hardcoding class, grab the first scrollable panel
scrollable_div = driver.find_element(By.XPATH, '//div[contains(@class, "m6QErb WNBkOb XiKgde")]')

# Scroll multiple times
for i in range(10):  # Increase for more reviews
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
    time.sleep(2)

# Extract reviews
reviews = driver.find_elements(By.XPATH, '//span[@class="wiI7pd"]')

data = []
for idx, review in enumerate(reviews, 1):
    try:
        text = review.find_element(By.CLASS_NAME, "wiI7pd").text
        rating = review.find_element(By.CLASS_NAME, "kvMYJc").get_attribute("aria-label")
        date = review.find_element(By.CLASS_NAME, "rsqaWe").text
        data.append([idx, rating, date, text])
    except:
        pass

# Save to CSV
with open("reviews.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Rating", "Date", "Review"])
    writer.writerows(data)

print(f"✅ Saved {len(data)} reviews into google_reviews.csv")

driver.quit()
