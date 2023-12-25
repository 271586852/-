import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import ctypes
import pytz 
from datetime import datetime
from tqdm import tqdm


# Get the current time in Beijing
beijing_timezone = pytz.timezone('Asia/Shanghai')

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=options)

# # -----------------------------------------------------------------

# str2 = driver.capabilities['browserVersion']
# str3 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
# print(str2)
# print(str3)

# # -----------------------------------------------------------------



now1 = datetime.now(beijing_timezone)

print("页面已打开,等待时间到达执行，当前时间为：", now1.hour, ":", now1.minute, ":", now1.second)

time.sleep(1)

user_name = input("请输入你的姓名：")
user_id = input("请输入你的学号：")
inpuTime = input("输入开始时间：格式为21:30:00\n")
# 检测用户输入，如为中文的：号则替换为英文的:号
if inpuTime.find('：') != -1:
    inpuTime = inpuTime.replace('：', ':')



openUrl = input("请输入问卷链接：")

openHour = int(inpuTime.split(':')[0])
openMinute = int(inpuTime.split(':')[1])
openSecond = int(inpuTime.split(':')[2])

# 当用户输入完成后，提示
now = datetime.now(beijing_timezone)

print("姓名为：",user_name)
print("学号为：",user_id)
print("链接为:",openUrl)

print("等待时间到达执行，当前时间为：", now.hour, ":", now.minute, ":", now.second, "预计时间为：", openHour, ":", openMinute, ":", openSecond)
print("请勿关闭窗口，程序将在预定时间自动运行")

# Calculate the time difference
current_time = now.hour * 3600 + now.minute * 60 + now.second
target_time = openHour * 3600 + openMinute * 60 + openSecond
countdown = target_time - current_time

# Create a progress bar
progress_bar = tqdm(total=countdown, desc="Progress", unit="sec")

while countdown > 0:
    # Update the progress bar
    progress_bar.update(1)
    time.sleep(1)
    countdown -= 1

# Close the progress bar
progress_bar.close()


while True:
    now = datetime.now(beijing_timezone)
    if now.hour == openHour and now.minute == openMinute and now.second >= openSecond:
        driver.get(openUrl)
        print("页面已打开")
        break

#找到id为q1的input框，type为text，输入姓名jzh
driver.find_element(By.ID, 'q1').send_keys(user_name)

#找到id为q2的input框，type为text，输入学号123456789
driver.find_element(By.ID, 'q2').send_keys(user_id)

#找到for为q3_1的单选框，div内文字为2023，勾选
driver.find_element(By.CSS_SELECTOR, 'div[for="q3_1"]').click()

#点击id为ctlNext的提交按钮
driver.find_element(By.ID, 'ctlNext').click()
print("代码成功运行")

time.sleep(3)




# -----------------------------------------------------------------

# # 若当前时间到达23:04:00，则执行后续代码
# while True:
#     now = datetime.now(beijing_timezone)
#     if now.hour == 23 and now.minute == 4 and now.second == 0:
#         break

#     # 打开页面
# driver.get('https://www.wjx.top/vm/rZuMpCH.aspx#')



# #找到id为q1的input框，type为text，输入姓名jzh
# driver.find_element(By.XPATH, '//*[@id="q1"]').send_keys('蒋子豪')

# #找到id为q2的input框，type为text，输入学号123456789
# driver.find_element(By.XPATH, '//*[@id="q2"]').send_keys('20232014007')

# # #找到for为q3_1的单选框，div内文字为2023，勾选
# # driver.find_element(By.CSS_SELECTOR, 'div[for="q3_1"]').click()

# driver.find_element(By.XPATH, '//*[@id="div3"]/div[2]/div[1]/div').click()


# #     #找到id为q1的input框，type为text，输入姓名jzh
# # driver.find_element(By.ID, 'q1').send_keys('蒋子豪')

# #     #找到id为q2的input框，type为text，输入学号123456789
# # driver.find_element(By.ID, 'q2').send_keys('20232014007')

# #     #找到for为q3_1的单选框，div内文字为2023，勾选
# # driver.find_element(By.CSS_SELECTOR, 'div[for="q3_1"]').click()

#     #点击id为ctlNext的提交按钮
# driver.find_element(By.ID, 'ctlNext').click()
# print("代码成功运行")
# time.sleep(3)

# -----------------------------------------------------------------