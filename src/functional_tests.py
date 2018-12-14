from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)

	# def tearDown(self):
	# 	self.browser.quit()
	# 	pass

	def test_can_start_the_webpage(self):
		self.browser.get('https://www.google.co.in/')
		searchbox = self.browser.find_element_by_css_selector('.gLFyf')
		searchbox.send_keys('dingu sagar')
		self.assertIn('Coding', self.browser.title)

if __name__ == '__main__':
	unittest.main(warnings='ignore')