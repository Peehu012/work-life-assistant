from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

def auto_fill_reservation(name, date, time_str, people_count, url):
    print("🔗 Opening reservation site...")

    # Path to your ChromeDriver
    chrome_path = r"C:/Users/user/PycharmProjects/nebula9.ai/chromedriver-win64/chromedriver.exe"
    service = Service(chrome_path)
    driver = webdriver.Chrome(service=service)

    driver.get(url)
    time.sleep(3)  # Wait for the page to load

    try:
        # Adapt the below selectors to match the form fields on the restaurant's site
        driver.find_element(By.NAME, "name").send_keys(name)
        driver.find_element(By.NAME, "date").send_keys(date)
        driver.find_element(By.NAME, "time").send_keys(time_str)
        driver.find_element(By.NAME, "people").send_keys(str(people_count))

        driver.find_element(By.NAME, "submit").click()
        print("✅ Reservation submitted successfully!")

    except Exception as e:
        print("❌ Failed to auto-submit form:", e)

    finally:
        time.sleep(5)
        driver.quit()
