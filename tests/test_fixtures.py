# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from selenium.webdriver.remote.webdriver import WebDriver


def test_selenium_fixture(driver):
    assert isinstance(driver, WebDriver)
