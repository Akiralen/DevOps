import logging
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

default_html = "http://localhost:8080"
path = "c:\selenium\chromedriver.exe"


def main():
    if test_scores_service(default_html):
        logging("Test Passed")
        sys.exit(0)
    else:
        sys.exit(-1)


def test_scores_service(landing_page):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    try:
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=path)
        driver.get(landing_page)
        elem = driver.find_element(By.ID, "score")
        return len(elem.text) > 0
    except:
        return False


if __name__ == "__main__":
    main()
else:
    logging.info("Module " + __name__ + "loaded")
