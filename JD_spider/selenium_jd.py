from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import time

from save_db import save_good

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=chrome_options)

# 设置浏览器窗口大小
browser.set_window_size(1400, 700)
wait = WebDriverWait(browser, 5)
KEYWORD = '跑步鞋'


def get_page(page):
    # 第一页，输入商品名
    if page == 1:
        url = 'https://www.jd.com/'
        browser.get(url)
        # print(browser.page_source)

        # 输入框输入信息
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#key')))
        input.clear()
        input.send_keys('鞋')

        # 提交输入框内容
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#search button.button')))
        submit.click()

        time.sleep(5)

        # print(browser.current_url)

    if page > 1:
        # 页码输入框
        input = wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="J_bottomPage"]//input[@class="input-txt"]')))
        input.clear()
        input.send_keys(page)

        # 提交页码
        submit = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="J_bottomPage"]//a[@class="btn btn-default"]')))
        submit.click()

    # 让窗口分十次滚动，尽量让商品信息加载完全，避免取到空信息
    for i in range(10):
        str_js = 'var step = document.body.scrollHeight / 8; window.scrollTo(0, step * %d)' % (i + 1)
        browser.execute_script(str_js)
        # 3秒滚一次
        time.sleep(3)

    return browser.page_source


def parse_page(page_source):
    html_etree = etree.HTML(page_source)
    goods_list = html_etree.xpath('//li[@class="gl-item"]')
    all_lists = []
    for good in goods_list:
        all_dict = {}
        title = ''.join(good.xpath('.//div[@class="p-name p-name-type-2"]//em//text()'))
        img_1 = good.xpath('.//div[@class="p-img"]//img/@src')
        # 判断是否抓取到图片信息
        if not img_1:
            img = ''
        else:
            img = img_1[0]
        price = good.xpath('.//div[@class="p-price"]//i/text()')[0]
        commits = good.xpath('.//div[@class="p-commit"]//a/text()')[0]
        shop = good.xpath('.//div[@class="p-shop"]//a/text()')[0]
        # 商品名
        all_dict['title'] = title
        all_dict['img'] = img
        all_dict['price'] = price
        # 商品评论数量
        all_dict['commits'] = commits
        all_dict['shop'] = shop
        all_lists.append(all_dict)
    return all_lists


def main():
    for page in range(2):
        page_source = get_page(page + 1)
        result_list = parse_page(page_source)
        save_good(result_list)
        parse_page(page_source)


if __name__ == '__main__':
    main()
