"""
Author:     Yashwanth G
LinkedIn:   https://www.linkedin.com/in/yash-g-2412241bb

Copyright (C) 2024 Yashwanth G

"""

from modules.helpers import make_directories
from yaml import safe_load
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from modules.helpers import find_default_profile_directory, critical_error_log, print_lg
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

config = safe_load(open("setup/config.yaml", "r"))   
chromeProfilePath = os.path.join(os.getcwd(), "chrome_profile", "linkedin_profile")

def ensure_chrome_profile():
    profile_dir = os.path.dirname(chromeProfilePath)
    print_lg(f"Ensuring Chrome profile exists at path: {chromeProfilePath}")
    if not os.path.exists(profile_dir):
        print_lg(f"Creating Chrome profile directory at path: {profile_dir}")
        os.makedirs(profile_dir)
    if not os.path.exists(chromeProfilePath):
        print_lg(f"Creating Chrome profile at path: {chromeProfilePath}")
        os.makedirs(chromeProfilePath)
    return chromeProfilePath

def chrome_browser_options():
    ensure_chrome_profile()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("window-size=1200x800")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-autofill")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-animations")
    options.add_argument("--disable-cache")
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    if config["run_in_background"]:   options.add_argument("--headless")

    prefs = {
        "profile.default_content_setting_values.images": 2,
        "profile.managed_default_content_settings.stylesheets": 2,
    }
    options.add_experimental_option("prefs", prefs)

    if len(chromeProfilePath) > 0:
        initial_path = os.path.dirname(chromeProfilePath)
        profile_dir = os.path.basename(chromeProfilePath)
        options.add_argument('--user-data-dir=' + initial_path)
        options.add_argument("--profile-directory=" + profile_dir)
    else:
        options.add_argument("--incognito")

    return options


try:
    make_directories([config["logs_folder_path"]])

    options = chrome_browser_options()
    driver = webdriver.Chrome(options=options, service = Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)
    
except Exception as e:
    msg = 'Error in opening Chrome. Check logs for more details. Close instances of Chrome profile of the bot and try again.'
    if isinstance(e,TimeoutError): msg = "Chrome took too long to open. Check logs for more details and try again."
    print_lg(msg)
    critical_error_log("In Opening Chrome", e)
    from pyautogui import alert
    alert(msg, "Error in opening chrome")
    try: driver.quit()
    except NameError: exit()
    