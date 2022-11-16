import logging
import sys,getopt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 

logging.basicConfig(
    format='%(asctime)s<%(name)s>%(levelname)s:%(message)s',
    datefmt='[%d.%m.%Y|%I:%M.%S]',
    level=logging.INFO,
    filename='event.log'
    )

win_path = "c:\selenium\chromedriver.exe"


def main(argv):
    app_ip = "localhost"
    app_port = "8777" 
    #check arguments for ip/port override
    try:
        opts, args = getopt.getopt(argv, "hi:p:", ["ip=", "port="])
    except getopt.GetoptError:
        print("Usage: e2e.py -i <ip/adress> -p <port>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("Usage: e2e.py -i <ip/adress> -p <port>")
            sys.exit()
        elif opt in ("-i", "--ip"):
            app_ip = arg
        elif opt in ("-p", "--port"):
            app_port = arg
    app_address = "http://" + app_ip + ":" + app_port
    if test_scores_service(app_address):
        logging.info("Test Passed on: " + app_address)
        sys.exit(0)
    else:
        logging.error("Test Failed on: " + app_address)
        sys.exit(-1)


def test_scores_service(landing_page):
    driver_location = '/usr/bin/chromedriver'
    binary_location = '/usr/bin/google-chrome'

    options = webdriver.ChromeOptions()
    options.binary_location = binary_location

    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")

    try:
        driver = webdriver.Chrome(executable_path=driver_location,options=options)
        # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=win_path)
        driver.get(landing_page)
        elem = driver.find_element(By.ID, "score")
        return len(elem.text) > 0
    except:
        return False


if __name__ == "__main__":
    main(sys.argv[1:])
else:
    logging.info("Module " + __name__ + "loaded")
