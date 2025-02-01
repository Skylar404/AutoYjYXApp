from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy


desired_caps={
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'Redmi_6',
            'appPackage': 'com.yjyxapp',
            'appActivity': '.MainActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True,
            'newCommandTimeout': 6000,
            'automationName': 'UiAutomator2'
}

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',options=UiAutomator2Options().load_capabilities(desired_caps))

driver.implicitly_wait(10)

sleep(3)


code='new UiSelector().text("请填写服务器地址")'
add=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code)
add.click()
add.send_keys("http://192.168.38.11")

code='new UiSelector().text("请输入vcode")'

inputvs=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code)
inputvs.click()
inputvs.send_keys("00000004074389951477")

sleep(5)
code='new UiSelector().text("登录")'
LGbutton=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code).click()


sleep(10)
quit()