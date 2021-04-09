import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

import notify
from datetime import datetime

TEST = "https://www.bestbuy.com/site/apple-watch-series-6-gps-44mm-space-gray-aluminum-case-with-black-sport-band-space-gray/6215931.p?skuId=6215931"

RTX3080LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"


def createDriver():
    """Creating driver."""
    options = Options()
    options.headless = False  # Change To False if you want to see Firefox Browser Again.
    profile = webdriver.FirefoxProfile(
        r'C:\Users\igamb\AppData\Roaming\Mozilla\Firefox\Profiles\ecdn3awe.default-release')
    driver = webdriver.Firefox(profile, options=options, executable_path=GeckoDriverManager().install())
    return driver


def checkStock(driver):
    driver.get(RTX3080LINK)

    isComplete = False

    while not isComplete:
        # find add to cart button
        try:
            atcBtn = WebDriverWait(driver, 1.5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
            )

        except:
            print('Add to cart button not found')
            print('Refreshing')
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)
            print('...................................')
            print('\n')
            driver.refresh()
            continue

        print("Add to cart button found")
        atcBtn.click()
        notify.sendMessage()
        isComplete = True
        print("Add to cart button has been clicked. Wait to click the button again")


if __name__ == '__main__':
    i = 0
    l = 20
    while i < 20:
        try:
            driver = createDriver()
            checkStock(driver)
        except:
            i = i + 1
            time.sleep(1)
            print('Script ran into a problem. Restarting now.')
