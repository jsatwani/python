import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    
    def __init__(self):
        print "init"
        
    @classmethod
    def setUpClass(cls):
        print "setupClass"

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass"
        
    def setUp(self):
        self.driver=webdriver.Chrome()
    def tearDown(self):
        print "teardown"
        self.driver.quit()
        