# Y Combinator Co-founder Matching Profile Search

This script automates the process of searching for profiles on the [Y Combinator Co-founder Matching](https://www.ycombinator.com/cofounder-matching) platform that contain specific keywords in their bio sections. It helps streamline the process of finding potential co-founders whose interests align with yours.

## Features

*   Automates the login process to the Y Combinator Co-founder Matching platform.
*   Searches through profiles for specified keywords.
*   Prints matching profiles to the console and saves them to a `matches.txt` file.
*   Leaves the browser open on a matching profile for you to review. You can then close the browser to terminate the script or skip to other profiles if you want it to continue searching.

## Prerequisites

Before using this script, you'll need the following:

*   **Python 3.7 or higher**
*   **Selenium:** A Python library for web browser automation.
*   **ChromeDriver:** A WebDriver for Chrome. The version should be compatible with your Chrome browser.

## Installation

1. **Install Python Packages:**

    ```bash
    pip install selenium
    ```

2. **Download ChromeDriver:**

    *   Go to the [ChromeDriver downloads page](https://sites.google.com/chromium.org/driver/downloads?authuser=0).
    *   Download the version that matches your Chrome browser version. You can find your Chrome version by going to "Help" -> "About Google Chrome."
    *   Extract the `chromedriver.exe` (or `chromedriver` on macOS/Linux) file to a suitable location. For example:
        *   Windows: `C:\Users\[YourUserName]\chromedriver.exe`
        *   macOS/Linux: `/usr/local/bin/chromedriver` (or any directory in your system's `PATH`)

## Configuration

1. **Open `yc_cofounder_matching_github.py`:**

2. **Update Placeholders:**

    *   **`chrome_driver_path`:** Replace `r"your chrome driver path"` with the actual path to your downloaded `chromedriver.exe` file. Remember to use a raw string (prefix with `r`) for Windows paths.

    *   **`yc_username`:** Replace `"your email or username"` with your Y Combinator username or email.

    *   **`yc_password`:** Replace `"your password"` with your Y Combinator Co-founder Matching password.

    *   **`keywords`:** Modify the list of keywords to search for:

        ```python
        keywords = ["keyword", "keyword", "keyword", "keyword"]
        ```

## Usage

1. **Run the Script:**

    Open your terminal or command prompt and navigate to the directory where you saved the script. Then, run the script using:

    ```bash
    python yc_cofounder_matching_github.py
    ```

2. **What the Script Does:**

    *   The script will open a new Chrome browser window.
    *   It will automatically log in to the Y Combinator Co-founder Matching platform using your provided credentials.
    *   It will navigate to the "View Profiles" section.
    *   It will start searching through profiles, checking the "About Me" and other sections for the specified keywords.
    *   **If a match is found:**
        *   The profile information (with the matching keywords) will be printed to the console.
        *   The profile information will also be appended to a file named `matches.txt` in the same directory as the script.
        *   The browser will **remain open** on the matching profile, allowing you to review it.
        *   **To stop the script:** Close the browser window.
        *   **To continue searching (if you want to find more matches):** You can manually skip profiles in the open browser window, and the script will resume the search from the next profile.

## Troubleshooting

*   **`UnicodeError: 'unicodeescape' codec can't decode bytes...`:**
    *   This usually happens on Windows if you don't use a raw string for the `chrome_driver_path`. Make sure to prefix the path with an `r`:
        ```python
        chrome_driver_path = r"C:\path\to\your\chromedriver.exe"
        ```

*   **`TimeoutException: Timed out waiting for page elements...`:**
    *   This means the script couldn't find the necessary elements on the page within the specified timeout. This could be due to:
        *   **Incorrect XPaths:** The website structure might have changed. You'll need to update the XPaths in the script. Use your browser's developer tools (usually by pressing F12) to inspect the elements and find the correct XPaths.
        *   **Slow Internet Connection:** Try increasing the timeout values in the `WebDriverWait` instances (e.g., from 10 to 15 or 20 seconds).
        *   **Dynamic Content:** The page might load content dynamically. You might need to add waits for specific elements to become visible or clickable.

*   **`NoSuchElementException: Unable to locate element...`:**
    *   Similar to `TimeoutException`, this indicates that the script couldn't find an element with the specified XPath. Double-check your XPaths and make sure they are still valid.

*   **Script Clicks "Sign In" but Doesn't Enter Credentials:**
    *   This usually means the XPaths for the username or password fields are incorrect or that the fields are not immediately interactable after clicking "Sign In". Verify the XPaths and consider adding waits for visibility or a small delay if necessary (see the comments in the code).

## Disclaimer

*   This script is provided for educational and informational purposes only.
*   Use this script responsibly and ethically.
*   Always respect the Y Combinator website's [terms of service](https://www.ycombinator.com/legal/terms) and [privacy policy](https://www.ycombinator.com/legal/privacy).
*   The author of this script is not responsible for any consequences that may arise from the use of this script.

## Contributing

Contributions are welcome! If you find any bugs or want to suggest improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
