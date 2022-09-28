import time

from playwright.sync_api import sync_playwright
import pytest


def login(self):
    # Go to https://account.dangquyun.com/useridentity/Account/Login
    self.page.goto("https://account.dangquyun.com/useridentity/Account/Login")
    time.sleep(3)
    # Click input[name="Account"]
    self.page.locator("input[name=\"Account\"]").click()
    # Fill input[name="Account"]
    self.page.locator("input[name=\"Account\"]").fill("13777207532")
    # Press Tab
    self.page.locator("input[name=\"Account\"]").press("Tab")
    # Fill input[name="Password"]
    self.page.locator("input[name=\"Password\"]").fill("123456abcde")
    # Click button:has-text("登录")
    with self.page.expect_navigation():
        self.page.locator("button:has-text(\"登录\")").click()
    time.sleep(5)


class TestHR():
    def setup(self):
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
        # self.context = self.browser.new_context()
        # self.context = self.browser.new_context(viewport={"width": 1920, "height": 1080}
        #                                         )
        self.context = self.browser.new_context(no_viewport = True)

        # Open new page
        self.page = self.context.new_page()

    def test_delivery_record(self):
        login(self)
        print('投递记录测试开始：')
        # # Click text=HR招聘系统  进入招聘系统
        locator=self.page.locator("div:nth-child(12) > .iconWrapper___14jI8")
        locator.hover()
        locator.click()
        # time.sleep()

        # Click .ant-select-selection-overflow >> nth=0

        self.page.locator("text=应用首页").hover()



        # Click button:has-text("新增") >> nth=1  新增投递记录
        self.page.locator("button:has-text(\"新增\")").nth(1).click()
        time.sleep(3)
        # Click [placeholder="请输入姓名"]
        self.page.locator("[placeholder=\"请输入姓名\"]").fill('雷粒')
        time.sleep(3)
        # # Fill #phone_number
        self.page.locator("#phone_number").fill("1901111")
        # Click #school_name
        # self.page.locator("#school_name").fill('浙江万里学院')
        # time.sleep(3)

        # Click text=简历来源请选择一条数据 >> input[role="combobox"]
        self.page.locator("text=简历来源请选择一条数据 >> input[role=\"combobox\"]").click()
        time.sleep(3)
        self.page.locator("text=简历来源请选择一条数据 >> input[role=\"combobox\"]").fill("自己搜索(BOSS)")
        self.page.locator(".ant-select-item-option-content").locator('text=自己搜索(BOSS)').click()

        time.sleep(2)
        # 选择实际沟通职位
        self.page.locator("text=实际沟通职位第一面试官人才备注已读是否创建时间将由系统自动生成计入月度统计否计入年度统计否 >> button").click()
        # Check text=1助理工程师QQ-助理工程师-IT类是马梦笛- >> input[type="checkbox"]
        self.page.locator("text=1助理工程师QQ-助理工程师-IT类是马梦笛- >> input[type=\"checkbox\"]").check()
        # Click button:has-text("确认")
        self.page.locator("button:has-text(\"确认\")").click()
        time.sleep(2)

        # self.page.select_option('ant-select-selector', label='前程无忧')
        # # self.page.locator("div:nth-child(46) > .ant-select-item-option-content").click()

        # Click div:nth-child(6) > .ant-select-item-option-content
        # self.page.locator("div:nth-child(6) > .ant-select-item-option-content").click()
        # Click button:has-text("提交")
        self.page.locator("button:has-text(\"提交\")").click()
        # Click text=搜索人不能为空！
        locator= self.page.locator("text=搜索人不能为空！")
        assert locator
        print(self.page.locator("text=搜索人不能为空！"))

        # self.page.locator("text=HR招聘系统").click()
        # expect(page).to_have_url("https://app.dangquyun.com/tabs/3a01f867-29ce-a184-ed7b-957802f9b2ae/dynamicApp/3a03ddf4-6bdb-0cfe-c168-37fd57af0a3d/pagedetail/3a022ddc-19e0-9d3d-a0e6-10e251f5560e/host")
        # Click text=RR20220900002  点击投递记录
        # self.page.locator("text=RR20220900005").click()
        # time.sleep(5)
        # self.page.click('[type="checkbox"][value="Click me"]')  # 点击checkbox
        # # assert self.page.is_checked('[type="checkbox"][value="Click me"]') is True
        # assert self.page.is_checked("[type = 'checkbox'][value='是']") is True
        # # Click button:has-text("提交")
        # self.page.locator("button:has-text(\"提交\")").click()
        # time.sleep(5)
        # 点击左边显示菜单列表
        # self.page.click('//*[@id="root-master"]/section/aside/div/div/div/div/div[2]/div/div/div[2]/div[3]')



    def teardown(self):
        time.sleep(10)
        self.page.close()


