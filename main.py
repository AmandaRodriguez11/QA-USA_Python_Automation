from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:
  @classmethod
  def setup_class(cls):
      # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
      from selenium.webdriver import DesiredCapabilities
      capabilities = DesiredCapabilities.CHROME
      capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
      cls.driver = webdriver.Chrome()
      cls.driver.implicitly_wait(5)
if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
    print("Connected to URBAN ROUTES server")
else:
 print("Cannot connect to URBAN ROUTES server. Check the server is on and still running.")



 def test_set_route(self):
     self.driver.get('https://cnt-c0d9a00c-9d24-4c13-bfb8-c31d2d0a6faa.containerhub.tripleten-services.com/')
     routes_page = UrbanRoutesPage(self.driver)
     routes_page.set_route('East 2nd Street, 601', '1300 1st St')
     assert routes_page.get_from('East 2nd Street, 601') == data.ADDRESS_FROM
     assert routes_page.get_to('1300 1st St') == data.ADDRESS_TO

def test_select_plan(self):
        self.driver.get('https://cnt-c0d9a00c-9d24-4c13-bfb8-c31d2d0a6faa.containerhub.tripleten-services.com/')
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route('East 2nd Street, 601','1300 1st St')
        assert routes_page.get_from('East 2nd Street, 601') == data.ADDRESS_FROM
        assert routes_page.get_to('1300 1st St') == data.ADDRESS_TO


def test_fill_phone_number(self):
    self.driver.get('https://cnt-c0d9a00c-9d24-4c13-bfb8-c31d2d0a6faa.containerhub.tripleten-services.com/')
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route('East 2nd Street, 601','1300 1st St' )
    routes_page_select_test_fill_phone_number = UrbanRoutesPage(self.driver)
    assert routes_page.get_test_fill_phone_number == '+1 123 123 12 12'

def test_fill_card(self):
    self.driver.get('https://cnt-c0d9a00c-9d24-4c13-bfb8-c31d2d0a6faa.containerhub.tripleten-services.com/')
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route('East 2nd Street','1300 1st St' )
    routes_page_select_test_fill_card = UrbanRoutesPage(self.driver)
    assert routes_page.get_test_fill_card == '1234 5678 9100', '111'

def test_comment_for_driver(self):
    self.driver.get('https://cnt-c0d9a00c-9d24-4c13-bfb8-c31d2d0a6faa.containerhub.tripleten-services.com/')
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route('East 2nd Street','1300 1st St' )
    routes_page_select_test_comment_for_driver = UrbanRoutesPage(self.driver)
    assert routes_page.get_test_comment_for_driver  ('Stop at the juice bar, please')

def test_order_blanket_and_handkerchiefs(self):
    self.driver.get('https://cnt-c0d9a00c-9d24-4c13-bfb8-c31d2d0a6faa.containerhub.tripleten-services.com/')
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route('East 2nd Street','1300 1st St')
    routes_page_select_test_order_blanket_and_handkerchiefs = UrbanRoutesPage(self.driver)
    assert routes_page.get_test_order_blanket_and_handkerchiefs

def test_order_2_ice_creams(self):
    self.driver.get('https://cnt-c0d9a00c-9d24-4c13-bfb8-c31d2d0a6faa.containerhub.tripleten-services.com/')
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route('East 2nd Street','1300 1st St' )
    routes_page_select_test_order_2_ice_creams = UrbanRoutesPage(self.driver)
    assert routes_page.get_test_order_2_ice_creams

def test_car_search_model_appears(self):
    self.driver.get('https://cnt-c0d9a00c-9d24-4c13-bfb8-c31d2d0a6faa.containerhub.tripleten-services.com/')
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route('East 2nd Street', '1300 1st St')
    routes_page_select_test_model_appears = UrbanRoutesPage(self.driver)
    assert routes_page.get_test_car_search_model_appears


@classmethod

def teardown_class(cls):
        cls.driver.quit()