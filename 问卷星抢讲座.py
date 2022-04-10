# -- 只适用于谷歌浏览器的问卷星抢讲座、抢座位等 --

# 导入包
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

if __name__ == '__main__':
    # 启动浏览器、屏蔽自动检测等
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(options=option)
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    })

    # 上述过程成功后，确认网址和讲座开始时间
    while True:
        url='https://www.wjx.cn/vj/rlbhz46.aspx'
        time_now=time.strftime("%H:%M:%S", time.localtime())
        if time_now=="23:15:01":    # 自行修改时间
          browser.get(url)

          # 填写问卷相关问题（根据问卷内容进行调整）
          # 1.姓名（填空题）
          text1 = '到此一游'
          browser.find_element_by_id("q1").send_keys(text1)     # 以
          # 2.学号（填空题）
          text2 = 'thanks'
          browser.find_element_by_id("q2").send_keys(text2)

          #点击“下一页”(在网页右键“检查”下一页的id)
          browser.find_element_by_id('btnNext').click()

          #3.班级（选择题）
          js ='document.getElementById("q3_3").click()'
          browser.execute_script(js)
          
          # 模拟点击提交按钮
          browser.find_element_by_xpath("//input[@value='提交']").click()
          time.sleep(0.5)

          # 模拟点击智能验证按钮
          # 先点确认
          browser.find_element_by_xpath("//button[text()='确认']").click()
          # 再点智能验证提示框，进行智能验证
          browser.find_element_by_xpath("//div[@id='captcha']").click()

          print('抢讲座成功！')
