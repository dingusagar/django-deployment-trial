from selenium import webdriver

browser = webdriver.Chrome()
# browser.get('https://www.google.com/imghp?sbi=1')
# browser.implicitly_wait(3)
# img_url = "https://cdn.waterstones.com/bookjackets/large/9781/7853/9781785301544.jpg"
# searchbox = browser.find_element_by_xpath("""//*[@id="qbui"]""")
# searchbox.send_keys(img_url)
# search_button = browser.find_element_by_xpath("""//*[@id="qbbtc"]/input""")
# search_button.click()

# topic_title  = browser.find_element_by_xpath("""//*[@id="topstuff"]/div/div[2]/a""").text
# print(topic_title)



topic_title = 'Deception Point'
def google_it(browser,search_text):
	browser.get('https://www.google.com/')
	searchbox = browser.find_element_by_xpath("""//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input""")
	searchbox.send_keys(search_text)

	search_button = browser.find_element_by_xpath("""//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]""")
	search_button.click()

google_it(browser, 'site:https://www.goodreads.com/book/show/  ' + topic_title  )
first_link = browser.find_elements_by_class_name('iUh30')[0].text

browser.get(first_link)
reviews = browser.find_elements_by_class_name('reviewText')

for review in reviews:
	subelements = review.find_elements_by_tag_name('span')
	if not subelements:
		continue
	n = len(subelements)
	subelement = subelements[n-1]
	print(subelement.get_attribute('textContent'))
	print('\n\n')