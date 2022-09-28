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
        self.browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        # self.context = self.browser.new_context()
        # self.context = self.browser.new_context(viewport={"width": 1920, "height": 1080}
        #                                         )
        self.context = self.browser.new_context(no_viewport=True)

        # Open new page
        self.page = self.context.new_page()

    def test_delivery_record(self):
        login(self)
        print('投递记录测试开始：')
        # 进入招聘系统
        locator = self.page.locator("div:nth-child(12) > .iconWrapper___14jI8")
        locator.hover()
        locator.click()
        # 鼠标悬停应用首页
        self.page.locator("text=应用首页").hover()
        time.sleep(30)
        # 测试投递记录列表

        # 新增投递记录
        self.page.locator("button:has-text(\"新增\")").nth(1).click()
        time.sleep(3)
        # 输入姓名
        self.page.locator("[placeholder=\"请输入姓名\"]").fill('雷粒')
        time.sleep(3)
        # 输入手机号
        self.page.locator("#phone_number").fill("1901111")
        # 输入学校
        self.page.locator("#school_name").fill('浙江万里学院')
        # 选择性别

        # 选择简历来源，搜索：前程无忧
        self.page.locator("text=简历来源请选择一条数据 >> input[role=\"combobox\"]").click()
        time.sleep(3)
        self.page.locator("text=简历来源请选择一条数据 >> input[role=\"combobox\"]").fill("前程无忧")
        self.page.locator(".ant-select-item-option-content").locator('text=前程无忧').click()

        time.sleep(2)
        # 选择实际沟通职位
        self.page.locator("text=实际沟通职位第一面试官人才备注已读是否创建时间将由系统自动生成计入月度统计否计入年度统计否 >> button").click()
        # Check text=1助理工程师QQ-助理工程师-IT类是马梦笛- >> input[type="checkbox"]
        self.page.locator("text=1助理工程师QQ-助理工程师-IT类是马梦笛- >> input[type=\"checkbox\"]").check()
        # Click button:has-text("确认")
        self.page.locator("button:has-text(\"确认\")").click()
        time.sleep(2)
        # 点击提交
        self.page.locator("button:has-text(\"提交\")").click()
        # # Click text=搜索人不能为空！
        # locator = self.page.locator("text=搜索人不能为空！")
        # assert locator
        # print(self.page.locator("text=搜索人不能为空！"))
        locator = self.page.locator("text=雷粒")
        assert locator

    def teardown(self):
        time.sleep(10)
        self.page.close()
