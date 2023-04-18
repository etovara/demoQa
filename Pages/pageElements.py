from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locatorsElements import *

class pageElementsTextBox():
  
  def __init__(self, driver):
    self.driver = driver
    
    self.click_textbox_xpath          = locatorsElements.click_textbox_xpath
    self.userName_textbox_id          = locatorsElements.userName_textbox_id
    self.email_textbox_id             = locatorsElements.email_textbox_id
    self.currentAddress_textbox_id    = locatorsElements.currentAddress_textbox_id
    self.permanentAddress_textbox_id  = locatorsElements.permanentAddress_textbox_id
    self.submit_button_id             = locatorsElements.submit_button_id
      
  def click_textbox(self):
    self.driver.find_element(By.XPATH, self.click_textbox_xpath).click()
  
  def enter_username(self, userName):
    self.driver.find_element(By.ID, self.userName_textbox_id).clear()
    self.driver.find_element(By.ID, self.userName_textbox_id).send_keys(userName)
  
  def enter_email(self, email):
    self.driver.find_element(By.ID, self.email_textbox_id).clear()
    self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)
  
  def enter_currentAddress(self, currentAddress):
    self.driver.find_element(By.ID, self.currentAddress_textbox_id).clear()
    self.driver.find_element(By.ID, self.currentAddress_textbox_id).send_keys(currentAddress)
    
  def enter_permanentAddress(self, permanentAddress):
      self.driver.find_element(By.ID, self.permanentAddress_textbox_id).clear()
      self.driver.find_element(By.ID, self.permanentAddress_textbox_id).send_keys(permanentAddress)
      

      
  def enter_submit(self, submit):
      self.driver.find_element(By.ID, self.submit_button_id).clear()
      self.driver.find_element(By.ID, self.submit_button_id).send_keys(submit)
      ActionChains(self).scroll_to_element(self.enter_submit)

class pageElementsCheckBox():
      
  def __init__(self, driver):
    self.driver = driver
    
    self.checkbox_button_xpath          = locatorsElementsCheckBox.checkbox_button_xpath
    self.expand_button_css              = locatorsElementsCheckBox.expand_button_css
    self.home_button_xpath              = locatorsElementsCheckBox.home_button_xpath
    self.collapse_button_css            = locatorsElementsCheckBox.collapse_button_css

      
  def checkbox_button(self):
    self.driver.find_element(By.XPATH, self.checkbox_button_xpath).click()
  
  def expand_button(self):
    self.driver.find_element(By.CSS_SELECTOR, self.expand_button_css).click()
  
  def home_button(self):
    self.driver.find_element(By.XPATH, self.home_button_xpath).click()

  def collapse_button(self):
    self.driver.find_element(By.CSS_SELECTOR, self.collapse_button_css).click()


class pageElementsRadioButton():
      
  def __init__(self, driver):
    self.driver = driver
    
    self.radio_button_xpath          = locatorsElementsRadioButton.radio_button_xpath
    self.yes_radio_xpath                = locatorsElementsRadioButton.yes_radio_xpath
    self.impressive_radio_xpath      = locatorsElementsRadioButton.impressive_radio_xpath
  
  def radio_button(self):
    self.driver.find_element(By.XPATH, self.radio_button_xpath)
    ActionChains(self.driver).click()

  def yes_radio(self):
    self.driver.find_element(By.XPATH, self.yes_radio_xpath)
    ActionChains(self.driver).click()

  def impressive_radio(self):
    self.driver.find_element(By.ID, self.impressive_radio_xpath)
    ActionChains(self.driver).click().click()


class pageElementwebTables():
  
  def __init__(self, driver):
    self.driver = driver
    
    self.webTables_button_xpath       = locatorsElementsWebTables.webTables_button_xpath
    self.searchBox_input_id           = locatorsElementsWebTables.searchBox_input_id
    self.delete_button_xpath          = locatorsElementsWebTables.delete_button_xpath
    self.edit_button_xpath            = locatorsElementsWebTables.edit_button_xpath
    
  def webTables(self):
    self.driver.find_element(By.CSS_SELECTOR, self.webTables_button_xpath)
    ActionChains(self.webTables_button_xpath).click()
  
  def searchBox(self, searchbox):
    self.driver.find_element(By.ID, self.searchBox_input_id).send_keys(searchbox)
  
  def delete(self):
    self.driver.find_element(By.XPATH, self.delete_button_xpath).click()