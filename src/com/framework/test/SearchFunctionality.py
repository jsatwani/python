from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from com.framework.repository import ObjectRepo
from com.framework.test.BaseTest import BaseTest

class SearchFunctionality(unittest.TestCase):
   
         
    def setUp(self):
        self.driver=webdriver.Chrome()
    def tearDown(self):
        print "teardown"
        self.driver.quit()
        
    def test_a(self):
        print "Test"
        BaseTest.driver.get("http://www.google.com")
        #self.driver.implicitly_wait(10)
        BaseTest.driver.find_element_by_id(ObjectRepo.frontpage['searchboxId']).send_keys("Wikipedia")
        sleep(3)
        BaseTest.driver.find_element_by_class_name(ObjectRepo.frontpage['searchIconClass']).click()
        BaseTest.driver.implicitly_wait(10)
        element = WebDriverWait(BaseTest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Wikipedia")))
        element.click()
        sleep(10)
    
    

        