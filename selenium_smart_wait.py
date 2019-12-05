

import time
from selenium import webdriver     #导入浏览器驱动
def smart_wait(self, element_id):  # 智能等待时间，60秒超时
    for i in range(60):            # 循环60次，从0至59
        if i >= 59 :               # 当i大于等于59时，打印提示时间超时
            print("timeout")    
            break
        try:                       # try代码块中出现找不到特定元素的异常会执行except中的代码
            if browser.find_element_by_id(element_id): # 如果能查找到特定的元素id就提前退出循环
                break
        except:                    # 上面try代码块中出现异常，except中的代码会执行打印提示会继续尝试查找特定的元素id
            print("wait for find element")
        time.sleep(1)