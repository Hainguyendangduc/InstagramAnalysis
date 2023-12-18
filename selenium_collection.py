from selenium import webdriver
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

driver = webdriver.Chrome()
driver.get('https://twitter.com/login')

driver.maximize_window()

sleep(3)
username = driver.find_element_by_xpath('//input[@autocapitalize="sentences"]')
username.send_keys('20010952@st.phenikaa-uni.edu.vn')
username.send_keys(Keys.RETURN)


sleep(3)
username = driver.find_element_by_xpath('//input[@autocapitalize="none"]')
username.send_keys('HaiNguyenD50400')
username.send_keys(Keys.RETURN)

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

sleep(3)
my_password = getpass()
password = driver.find_element_by_xpath('//input[@autocomplete="current-password"]')
password.send_keys(my_password)
password.send_keys(Keys.RETURN)

sleep(3)
search_input = driver.find_element_by_xpath('//input[@aria-label="Search query"]')
search_input.send_keys('#covid')
search_input.send_keys(Keys.RETURN)



cards = driver.find_element_by_xpath('//div[@aria-label="Timeline: Search timeline"]')
card = cards[0]

def get_data(card):
	username = card.find_element_by_xpath('.//span').text
	handle = card.find_element_by_xpath('.//span[contains(text(), "@")}').text
	
	try:
		postdate = card.find_element_by_xpath('.//time').get_attribute('datetime')
	except NoSuchElementException:
		return
	comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
	responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
	text = comment + responding 
	reply = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
	retweet = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
	like = card.find_element_by_xpath('.//div[@data-testid="like"]').text
	
	tweet = (username, handle, postdate, text, reply, retweet, like)
	return tweet
	
get_data(card)



cards = driver.find_element_by_xpath('//div[@data-testid="cellInnerDiv"]')
cards.find_element_by_xpath('.//div[@data-testid="tweetText"]//span').text


