# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAssertdireccion():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_assertdireccion(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(974, 1040)
    self.driver.find_element(By.LINK_TEXT, "Your profile").click()
    self.driver.find_element(By.LINK_TEXT, "Edit Profile").click()
    self.driver.find_element(By.NAME, "address1").click()
    self.driver.find_element(By.NAME, "address1").send_keys("Pareja 300")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(11)").click()
  
  #ASSERT DE REGISTROS
assert self.driver.find_element(By.NAME, "address1").get_attribute(
            "value") == random_user["address1"]
assert "Sample" in address1

