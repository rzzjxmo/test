import sys
import pytest
from selenium import webdriver
sys.path.append(r'C:\Users\root\Desktop\elife_auto')
from lib.webUI_smp import smpUI
from selenium.webdriver.common.by import By
def setup_module():
    print('\n *** 初始化-模块 ***')


def teardown_module():
    print('\n ***   清除-模块 ***')


# 定义一个fixture，用于创建vhangsaj（作用初始化清除使用。）
@pytest.fixture
def createvhangsaj():
    # 执行fixture，并接受返回值
    yield
    try:
        # 尝试接受弹窗，如果出现异常则打印异常信息
        smpUI.driver.switch_to.alert.accept()
    except Exception as e:
        print(e)
# 定义一个测试SMP登录的函数
def test_SMP_login_001():
    # 调用smpUI.login函数，传入用户名和密码
    smpUI.login("byhy","sdfsdf")
    # 断言登录成功后，页面标题是否为"1号超级管理员"
    assert smpUI.driver.find_element(By.XPATH,'//*[@id="top-right"]/a').text == "1号超级管理员"




# 测试用户名，密码，期望的提示（定义一个数据驱动修饰器）
@pytest.mark.parametrize('username,password,expectedalert',[
    (None,"sdfsdf","请输入用户名"),
    ("byhy",None,"请输入密码"),
    ("byhy","sdfsdff","登录失败： 用户名或者密码错误" ),
    ("byhy","sdfsd","登录失败： 用户名或者密码错误" ),
    ("byh","sdfsdf","登录失败： 用户名不存在"),
    ("byhyy","sdfsdf","登录失败： 用户名不存在"),]       
)


def test_SMP_login_002(username,password,expectedalert,createvhangsaj):
    smpUI.login(username,password)
    alert=smpUI.driver.switch_to.alert
    assert alert.text == expectedalert
  