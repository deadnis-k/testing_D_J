import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Initialize WebDriver
service = Service(executable_path="/path/to/chromedriver")  # Update with the path to your chromedriver
driver = webdriver.Chrome(service=service)

def check_image_change():
    # Step 1: Open localhost:5000
    driver.get("http://localhost:5000")
    
    # Wait for the page to load
    time.sleep(2)
    
    # Step 2: Find the image or GIF
    img_element = driver.find_element(By.TAG_NAME, "img")  # Assumes only one image or gif on the page
    original_image_url = img_element.get_attribute("src")
    
    # Step 3: Reload the page up to 5 times
    for _ in range(5):
        driver.refresh()
        time.sleep(2)
        
        # Get the current image URL after refresh
        img_element = driver.find_element(By.TAG_NAME, "img")
        new_image_url = img_element.get_attribute("src")
        
        # Step 4: Check if the image URL has changed
        if new_image_url != original_image_url:
            driver.quit()
            return True  # Image URL changed, return True
    
    driver.quit()
    return False  # Image URL did not change after 5 refreshes

# Call the function to check image change
result = check_image_change()

# Exit with status code for Jenkins (0 for True, 1 for False)
if result:
    print("Image changed successfully.")
    sys.exit(0)  # Exit with 0 (success)
else:
    print("Image did not change.")
    sys.exit(1)  # Exit with 1 (failure)
