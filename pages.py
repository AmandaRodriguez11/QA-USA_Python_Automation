from selenium.webdriver.common.by import By


class UrbanRoutesPage:
	# Addresses
	from_field = (By.ID, 'From')
	to_field = (By.ID, 'To')
	# Tariff and call button
	call_taxi_button = (By.XPATH, "Call Taxi")

	def __init__(self, urbanroutes_driver):
		self.driver = driver = urbanroutes_driver
	def test_fill_address_to(self, to_address):
		self.driver.find_element(*self.to_field).send_keys(By.ID, to_address)
	def test_fill_address_from_(self):
		self.driver.find_element(*self.from_field).send_keys(By.ID)
	def test_submit_button(self, test_submit_button, to_submit=None):
		self.driver.find_element(*self.test_submit_button()).click(By.XPATH, to_submit)
	def test_submit_phone_number(self):
		self.driver.find_element(*self.test_submit_phone_number()).send_keys(By.ID)
	def test_fill_card_number(self):
		 self.driver.find_element(*self.test_fill_card_number()).send_keys(By.ID)
	def test_fill_card_code(self):
		self.driver.find_element(*self.test_fill_card_code())
	def test_fill_message_for_driver(self):
		self.driver.find_element(*self.test_fill_message_for_driver())

