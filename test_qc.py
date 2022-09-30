# Python版本：3.7
# -*- coding:utf-8 -*-
import time

import playwright
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
        iphone = playwright.devices["iPhone 12"]
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(**iphone)
        page = context.new_page()
        page.goto("http://m.test.powertradepro.com")
        print(page.context)
        # other actions...
        time.sleep(5)
        browser.close()

    def test_QC(self):
        print('123')


    def teardown(self):
        time.sleep(10)
        self.page.close()

from playwright.sync_api import sync_playwright
import time


