from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://www.google.com/maps/place/Meghana+Foods+-+Marathahalli/@12.9496268,77.6971488,17z/data=!4m18!1m9!3m8!1s0x3bae12335ccf1b9d:0xa3365bee1a2d62ed!2sMeghana+Foods+-+Marathahalli!8m2!3d12.9496216!4d77.6997237!9m1!1b1!16s%2Fg%2F11b5pjcvm4!3m7!1s0x3bae12335ccf1b9d:0xa3365bee1a2d62ed!8m2!3d12.9496216!4d77.6997237!9m1!1b1!16s%2Fg%2F11b5pjcvm4?entry=ttu&g_ep=EgoyMDI1MDkwNy4wIKXMDSoASAFQAw%3D%3D"
driver.get(url)
time.sleep(5)  # let page load

try:
    # Find the Reviews button by visible text
    reviews_button = driver.find_element(By.XPATH, '//div[contains(text(),"Reviews")]')
    reviews_button.click()
    print("✅ Clicked on Reviews button")
except Exception as e:
    print("⚠️ Could not click Reviews button:", e)

time.sleep(5)
driver.quit()
