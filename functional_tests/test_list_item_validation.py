import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import unittest
from unittest import skip

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    
    
    def test_cannot_add_empty_list_items(self):


        self.fail('write me!')