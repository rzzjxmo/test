import sys
sys.path.append(r'C:\Users\root\Desktop\elife_auto')
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from lib.webUI_smp import smpUI
from cfg import *
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope="module")  
def inDeviceModeLMgr():
   smpUI.login('byhy','sdfsdf') 
   smpUI.driver.get(SMP_URL_DEVICE_MODEL)
   return 
@pytest.fixture()
def delAddedDeviceModel():
   print('函数级别初始化')
   yield
   print('函数级别清除')
   smpUI.del_first_item()
def test_device_mode_001(inDeviceModeLMgr,delAddedDeviceModel):
   if smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/span').text == '添加':
      smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/span').click()
   smpUI.add_device_mode( "存储柜",'elife-canbinlocker-g22-10-20-40', '南京e生活存储柜-10大20中40小')
   dms=smpUI.get_first_page_device_modes()
   assert dms == [
      [
         "存储柜",
         'elife-canbinlocker-g22-10-20-40',
         '南京e生活存储柜-10大20中40小'
      ]
   ]
def test_device_mode_002(inDeviceModeLMgr,delAddedDeviceModel):
   if smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/span').text == '添加':
      smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/span').click()
   smpUI.add_device_mode( "存储柜", '难'*100, '南京e生活存储柜-10大20中40小')
   dms=smpUI.get_first_page_device_modes()
   assert dms == [
      [
         "存储柜",
         '难'*100,
         '南京e生活存储柜-10大20中40小'
      ]
   ]
def test_device_mode_003(inDeviceModeLMgr,delAddedDeviceModel):
   if smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/span').text == '添加':
      smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/span').click()
   smpUI.add_device_mode( "电瓶车充电站", 'bokpower-charger-g22-220v450w', '杭州bok 2022款450瓦 电瓶车充电站')
   dms=smpUI.get_first_page_device_modes()
   assert dms == [
      [
         "电瓶车充电站",
         'bokpower-charger-g22-220v450w',
         '杭州bok 2022款450瓦 电瓶车充电站'
      ]
   ]
def test_device_mode_004(inDeviceModeLMgr,delAddedDeviceModel):
   if smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/span').text == '添加':
      smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/span').click()
   smpUI.add_device_mode( "汽车充电站", 'yixun-charger-g22-220v7kw', '南京易迅能源2022款7千瓦汽车充电站')
   dms=smpUI.get_first_page_device_modes()
   assert dms == [
      [
         "汽车充电站",
         'yixun-charger-g22-220v7kw',
         '南京易迅能源2022款7千瓦汽车充电站'
      ]
   ]
def test_device_mode_005(inDeviceModeLMgr,delAddedDeviceModel):
   if smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/span').text == '添加':
      smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/span').click()
   smpUI.add_device_mode( "洗车站", 'njcw-carwasher-g22-2s', '南京e生活2022款洗车机 2个洗车位')
   dms=smpUI.get_first_page_device_modes()
   assert dms == [
      [
         "洗车站",
         'njcw-carwasher-g22-2s',
         '南京e生活2022款洗车机 2个洗车位'
      ]
   ]
def test_device_mode_006(inDeviceModeLMgr,delAddedDeviceModel):
   if smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/span').text == '添加':
      smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/span').click()
   smpUI.add_device_mode( "电瓶车充电站", 'bokpower-charger-g22-220v450w', '杭州bok 2022款450瓦 电瓶车充电站')
   smpUI.d.driver.get(SMP_URL_LOGIN) 
   try:
      # /html/body/main/div[3]/div[1]/div[1]/div[3]/input
      smpUI.driver.find_element(By.XPATH,'/html/body/main/div[1]/span').click()
      smpUI.get_first_page_device_modes()
   except:
      pass
   else:
   dms=smpUI.get_first_page_device_modes()
   assert dms == [
      [
         "电瓶车充电站",
         'bokpower-charger-g22-220v450w',
         '杭州bok 2022款450瓦 电瓶车充电站'
      ]
   ]