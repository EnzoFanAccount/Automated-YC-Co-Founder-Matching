from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
import time
import random
import re  # Import the regular expression module

# Replace with the path to your ChromeDriver executable
chrome_driver_path = r"your chrome driver path"  # Use a raw string

# Configure Chrome options (optional)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Enable after testing
# options.add_argument("--disable-gpu")  # Might be needed in headless mode
options.add_argument("--window-size=1920,1080")

# Create a new Chrome driver instance
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

# Keywords to search for
keywords = ["keyword", "keyword", "keyword", "keyword"] # You can add as many keywords as you want

# Login credentials
yc_username = "your email or username"
yc_password = "your password"

def login_to_yc(driver, username, password):
    driver.get("https://www.ycombinator.com/cofounder-matching")
    try:
        # Click "Sign In"
        sign_in_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'ycdc-btn') and contains(@class, 'ycdc-btn-outline') and contains(@class, 'ycdc-btn-lg') and contains(@href, '/users/sign_in')]"))
        )
        sign_in_button.click()

        # Wait for the username field to be visible and enter the username
        username_field = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='ycid-input']"))
        )
        username_field.send_keys(username)

        # Wait for the password field to be visible and enter the password
        password_field = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='password-input']"))
        )
        password_field.send_keys(password)

        # Click "Log In"
        login_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'MuiButton-contained') and contains(@class, 'MuiButton-containedPrimary')]"))
        )
        login_button.click()

        # Click "View Profiles"
        view_profiles_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'MuiButton-label') and text()='View Profiles']"))
        )
        view_profiles_button.click()

        # Wait for the first profile to load (adjust this as needed)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'css-1tp1ukf')]"))
        )
        print("Successfully logged in and navigated to profiles!")

    except TimeoutException:
        print("Login failed: Timed out waiting for login page elements or successful login.")
        driver.quit()
        exit()

def search_profiles(driver, keywords):
    profile_count = 0
    while True:
        try:
            profile_count += 1
            print(f"Checking profile {profile_count}...")

            # Find all sections with the specified class
            sections = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'css-1tp1ukf')]"))
            )

            # Concatenate text from all sections
            bio_text = " ".join([section.text.lower() for section in sections])

            # Check for keywords using regular expressions (whole word matching)
            if any(re.search(r"\b" + keyword.lower() + r"\b", bio_text) for keyword in keywords):
                print(f"Match found! Bio: {bio_text}")
                with open("matches.txt", "a") as file:
                    file.write(f"Profile {profile_count}: {bio_text}\n\n")
                # Don't break the loop or close the driver
                print("Browser left open on the matching profile. Close the browser to run the script again or skip profiles to continue.")

                # Wait indefinitely until the user closes the browser or an exception occurs
                while True:
                    try:
                        # Check if the browser is still open
                        driver.current_url
                        # Wait for a short time before checking again
                        time.sleep(1)
                    except Exception:
                        # Browser is closed, exit the loop
                        break

            # Skip to next profile
            skip_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'eaxdrh') and contains(@class, 'e1qryfvo1') and text()='Skip for now']"))
            )
            skip_button.click()
            time.sleep(random.uniform(2, 5))  # Random delay

        except TimeoutException:
            print("Timed out waiting for an element. Ending process.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    login_to_yc(driver, yc_username, yc_password)
    search_profiles(driver, keywords)