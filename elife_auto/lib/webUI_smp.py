import sys
sys.path.append(r'C:\Users\root\Desktop\elife_auto')
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from cfg import *
from selenium.webdriver.support.ui import Select



class SMP_UI:
  def __init__(self):
    # 创建一个ChromeOptions对象，用于设置Chrome的参数
    option = webdriver.ChromeOptions()
    # 添加一个参数，排除日志记录
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    # 创建一个Chrome浏览器实例，并设置参数
    self.driver = webdriver.Chrome(options=option)
    # 设置隐式等待时间
    self.driver.implicitly_wait(10)
  def login(self,username,password):
    # 最大化窗口
    self.driver.maximize_window()
    # 打开登录页面
    self.driver.get(SMP_URL_LOGIN) 
    # 设置隐式等待时间
    self.driver.implicitly_wait(10)
    if  username != None:
      self.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(username)
    # 找到密码的输入框，并输入密码
    if  password != None:
      self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    time.sleep(1)
    self.driver.find_element(By.XPATH,'//*[@id="loginBtn"]').click()
    self.driver.implicitly_wait(10)
  def get_first_page_device_modes(self):
    values=self.driver.find_elements(By.CSS_SELECTOR,'.field-value')
    self.driver.implicitly_wait(10)
    deviceModels=[]
    for index,value in enumerate(values):
      if (index + 1) % 3 == 0:
     
        # deviceModels.append([values[index-2].text,values[index-1].text,values[index].text])
        deviceModels.append([values[index-2].text,values[index-1].text,values[index].text])
    return deviceModels
  def del_first_item(self) -> bool:
    self.driver.implicitly_wait(3)
    delBtn = self.driver.find_elements(By.CSS_SELECTOR, '.result-list-item:nth-child(1) .result-list-item-btn-bar span:nth-child(1)')
    self.driver.implicitly_wait(3)
    if not delBtn:
      return False
    delBtn[0].click()
    self.driver.implicitly_wait(3)
    self.driver.switch_to.alert.accept()
    return True
  
  def add_device_mode(self,dev_type,a,b):
   # 创建Select对象
   select = Select(smpUI.driver.find_element(By.XPATH,'//*[@id="device-type"]'))
   # 通过 Select 对象选中 '存储柜' 类型
   select.select_by_visible_text(dev_type)
   ele=smpUI.driver.find_element(By.XPATH,'//*[@id="device-model"]')
   ele.clear()
   ele.send_keys(a)
   ele=smpUI.driver.find_element(By.XPATH,'//*[@id="device-model-desc"]')
   ele.clear()
   ele.send_keys(b)
   smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[4]/span').click()
   smpUI.driver.implicitly_wait(3)
smpUI = SMP_UI()