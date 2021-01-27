# -*- coding: utf-8 -*-

# 采集蛋壳太原的房源信息
# 周期 天
from selenium import webdriver
import json
from selenium.common.exceptions import NoSuchElementException
import sys
import re
# url_yj = 'https://ty.ke.com/ershoufang/pg100'
url_all='https://{}.ke.com/ershoufang/pg{}'
citys=['ty']
class bk (object):
    '''
    功能:爬取贝壳的二手房
    传入参数:爬取地址
    '''

    def __init__(self,city,page):
        '''
        参数:网页第几页
        '''
        self.url=url_all.format(city,page)

    def get_info(self):
        self.browser = webdriver.PhantomJS()
        self.browser.get(self.url)
        self.li_list = self.browser.find_elements_by_xpath('//*[@class="sellListContent"]/li')
        infos=[]
        for li in self.li_list:
            try:
                div_1=li.find_element_by_xpath('./div/div[1]')
                div_2=li.find_element_by_xpath('./div/div[2]')

                infos=[
                # 网址
                div_1.find_element_by_xpath('./a').get_attribute('href'),
                # 标题
                div_1.find_element_by_xpath('./a').get_attribute('innerText'),
                # 小区名
                div_2.find_element_by_xpath('./div[1]/div/a').get_attribute('innerText'),
                # 房屋描述
                div_2.find_element_by_xpath('./div[2]').get_attribute('innerText').replace(' ',''),
                # 价格
                re.sub('\s',' ',div_2.find_element_by_xpath('./div[5]').get_attribute('innerText'))
                # 关注
                #div_2.find_element_by_xpath('./div[3]').get_attribute('innerText').replace(' ','')

                ]
                line='\t'.join(infos)
                print(line)
            except IndexError as mag:
                print(mag,file=sys.stderr)
            except NoSuchElementException as mag:
                print(mag,file=sys.stderr)
if __name__ == '__main__':

    for city in citys:
        for page in range(100):
            b=bk(city,page)
            b.get_info()


