import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.common.exceptions import TimeoutException

fake = Faker()
from Helpers import my_key


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': '10',
            'resolution': '1920x1080',
            'browser': 'Chrome',
            'browser_version': 'latest',
            'os': 'Windows',
            'name': 'BStack-[Python] Sample Test',  # test name
            'build': 'BStack Build Number 1'  # CI/CD job or build name
        }
        url = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)



# As per unittest module, individual test should start with test_
    def test_MF_chrome(self):

        driver_chrome = self.driver
        self.driver.maximize_window()
        driver_chrome.get('https://markformelle.by/')
        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[@src='/local/templates/markformelle/images/logotype.png'])[1]")))
        assert "Интернет-магазин белорусского трикотажа и одежды: каталог с ценами в Минске, купить трикотаж с доставкой недорого" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)

        def delay():

         driver_chrome.find_element_by_xpath("//a[contains(.,'EXTRA SALE')]")

        try:
            wait.until((EC.presence_of_element_located((By.XPATH, "//a[contains(.,'EXTRA SALE')]")))).click()
            time.sleep(3)
            driver_chrome.find_element_by_xpath("//h1[@class='js-h1-section ']")
            print("You are on the correct page!")
            time.sleep(2)
        except TimeoutException:
            print("Something was wrong!")
            delay()
#Select your product and put into cart
        try:
            wait.until((EC.presence_of_element_located((By.XPATH, "(//div[contains(.,'-27%')])[5]")))).click()
            time.sleep(5)
            wait.until((EC.presence_of_element_located((By.XPATH, "//div[@class='size-arrow']")))).click()
            time.sleep(5)
            wait.until((EC.presence_of_element_located((By.XPATH, "(//div[contains(@class,'w25per growth')])[3]")))).click()
            time.sleep(5)
            wait.until((EC.presence_of_element_located((By.ID, "bx_117848907_254961_add_basket_link")))).click()
            time.sleep(5)
            print("You selected product, size M and put it into cart!")
            time.sleep(2)
        except TimeoutException:
            print("Something was wrong!")
            delay()

# Go to cart
        try:
            wait.until((EC.presence_of_element_located((By.ID, "addedToCart")))).click()
            time.sleep(5)
            print("You are in the cart!")
            time.sleep(5)
        except TimeoutException:
            print("Something was wrong!")
            delay()

# Fill in address
        try:
            wait.until((EC.presence_of_element_located((By.ID, "soa-property-22")))).send_keys(fake.address())
            time.sleep(5)
            wait.until((EC.presence_of_element_located((By.ID, "soa-property-23")))).send_keys("10")
            time.sleep(5)
            print("Your address entered!")
            time.sleep(3)
        except TimeoutException:
            print("Something was wrong!")
            delay()

# Select delivery date
        try:
            wait.until((EC.presence_of_element_located((By.XPATH, "//i[@class='bx-calendar']")))).click()
            time.sleep(3)
            wait.until((EC.presence_of_element_located((By.XPATH, "//span[contains(.,'Август')]")))).click()
            time.sleep(3)
            wait.until((EC.presence_of_element_located((By.XPATH, "//a[@data-date='1630281600000']")))).click()
            time.sleep(3)
            print("You selected delivery date!")
            time.sleep(3)
        except TimeoutException:
            print("Something was wrong!")
            delay()


# Fill in contact information
        try:
            wait.until((EC.presence_of_element_located((By.ID, "soa-property-20")))).send_keys(fake.name())
            time.sleep(10)
            wait.until((EC.presence_of_element_located((By.ID, "soa-property-1")))).send_keys(fake.name())
            time.sleep(10)
            wait.until((EC.presence_of_element_located((By.ID, "soa-property-2")))).send_keys(fake.email())
            time.sleep(10)
            wait.until((EC.presence_of_element_located((By.ID, "soa-property-3")))).send_keys(fake.phone_number())
            time.sleep(10)
            print("You entered contact information!")
            time.sleep(3)
        except TimeoutException:
            print("Something was wrong!")
            delay()

# Select payment method
        try:
            wait.until((EC.presence_of_element_located((By.ID, "ID_PAY_SYSTEM_ID_13-styler")))).click()
            time.sleep(3)
            time.sleep(10)
            print("Payment method selected!")
            time.sleep(10)
        except TimeoutException:
            print("Something was wrong!")
            delay()
# Create order
        try:
            wait.until((EC.presence_of_element_located((By.XPATH, "//a[contains(@class,'b btn-order-save')]")))).click()
            time.sleep(5)
            print("Order created!")
            time.sleep(5)
        except TimeoutException:
            print("Something was wrong!")
            delay()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    cross_test.main()