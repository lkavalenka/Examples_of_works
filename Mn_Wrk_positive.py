import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.common.exceptions import TimeoutException
import HtmlTestRunner
import AllureReports
fake = Faker()


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

# As per unittest module, individual test should start with test_
    def test_MF_chrome(self):
        driver_chrome = self.driver
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



#Chrome Browser test for screen size 1450*850

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1450, 850)

# As per unittest module, individual test should start with test_
    def test_MF_chrome(self):
        driver_chrome = self.driver
        driver_chrome.get('https://markformelle.by/')
        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[@src='/local/templates/markformelle/images/logotype.png'])[1]")))
        assert "Интернет-магазин белорусского трикотажа и одежды: каталог с ценами в Минске, купить трикотаж с доставкой недорого" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)

        def delay():

         driver_chrome.find_element_by_xpath("//a[contains(.,'EXTRA SALE')]")

        try:
            wait.until((EC.presence_of_element_located((By.XPATH, "//a[contains(.,'EXTRA SALE')]")))).click()
            time.sleep(2)
            driver_chrome.find_element_by_xpath("//h1[@class='js-h1-section ']")
            print("You are on the correct page!")
            time.sleep(2)
        except TimeoutException:
            print("Something was wrong!")
            delay()
# Select your product and put into cart
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
            time.sleep(5)
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

        self.driver.quit()

class FireFoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

# As per unittest module, individual test should start with test_
    def test_MF_firefox(self):
        driver_firefox = self.driver
        driver_firefox.get('https://markformelle.by/')
        wait = WebDriverWait(driver_firefox, 3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[@src='/local/templates/markformelle/images/logotype.png'])[1]")))
        assert "Интернет-магазин белорусского трикотажа и одежды: каталог с ценами в Минске, купить трикотаж с доставкой недорого" in driver_firefox.title
        print("Page title in Chrome is:", driver_firefox.title)

        def delay():

         driver_firefox.find_element_by_xpath("//a[contains(.,'EXTRA SALE')]")

        try:
            wait.until((EC.presence_of_element_located((By.XPATH, "//a[contains(.,'EXTRA SALE')]")))).click()
            time.sleep(2)
            driver_firefox.find_element_by_xpath("//h1[@class='js-h1-section ']")
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


#Firefox Browser test for screen size 1450*850

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1450, 850)

# As per unittest module, individual test should start with test_
    def test_MF_firefox(self):
        driver_firefox = self.driver
        driver_firefox.get('https://markformelle.by/')
        wait = WebDriverWait(driver_firefox, 3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[@src='/local/templates/markformelle/images/logotype.png'])[1]")))
        assert "Интернет-магазин белорусского трикотажа и одежды: каталог с ценами в Минске, купить трикотаж с доставкой недорого" in driver_firefox.title
        print("Page title in Chrome is:", driver_firefox.title)

        def delay():

         driver_firefox.find_element_by_xpath("//a[contains(.,'EXTRA SALE')]")

        try:
            wait.until((EC.presence_of_element_located((By.XPATH, "//a[contains(.,'EXTRA SALE')]")))).click()
            time.sleep(2)
            driver_firefox.find_element_by_xpath("//h1[@class='js-h1-section ']")
            print("You are on the correct page!")
            time.sleep(2)
        except TimeoutException:
            print("Something was wrong!")
            delay()
# Select your product and put into cart
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
            time.sleep(5)
        except TimeoutException:
            print("Something was wrong!")
            delay()

# Select delivery date
        try:
            wait.until((EC.presence_of_element_located((By.XPATH, "//i[@class='bx-calendar']")))).click()
            time.sleep(3)
            wait.until((EC.presence_of_element_located((By.XPATH, "//span[contains(.,'Август')]")))).click()
            time.sleep(5)
            wait.until((EC.presence_of_element_located((By.XPATH, "//a[@data-date='1630281600000']")))).click()
            time.sleep(5)
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

        self.driver.quit()



#if __name__ == '__main__':
#    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

#if __name__ == '__main__':
#   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/PC/PycharmProjects/Tasks-05-21/LK/HtmlReports'))

#for run test from terminal or cmd python and file's name: python HW10html.py



if __name__ == "__main__":
    cross_test.main()