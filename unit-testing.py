import unittest
from selenium import webdriver

class WebsiteTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Use appropriate web driver for your browser
        self.driver.maximize_window()

    def test_website_loads(self):
        self.driver.get("https://atg.world")  # Replace with the URL of atg.world
        self.assertEqual(self.driver.title, "atg.world")  # Assert that the website loads properly

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
