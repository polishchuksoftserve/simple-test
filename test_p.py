import time

import variables, methods
import string, random
from selenium import webdriver
import subprocess



def test_get_status():
    r = methods.request_get(variables.url + variables.status)
    assert r.status_code == variables.OK_status_code


def test_post_system_monitoring():
    r = methods.request_post_(variables.url + variables.system_monitoring, variables.data, variables.headers)
    assert r.status_code == variables.OK_status_code


def test_get_system_monitoring():
    r = methods.request_get(variables.url + variables.system_monitoring)
    assert r.status_code == 200
    print variables.st
    assert r.json()['timestamp'] == variables.st


def test_open_google():
    new = webdriver.Firefox()
    new.maximize_window()
    time.sleep(3)
    new.get('http://google.com')
    new.save_screenshot('new.png') # save a screenshot to disk
    assert 5 == 4+ 1

# def test_sheep_dog():
#     print subprocess.call("ls")
#     assert 2+2 == 3
