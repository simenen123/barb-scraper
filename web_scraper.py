import requests
from bs4 import BeautifulSoup
from bs4 import Comment
from helium import *
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def scrape_chapter_text(url):
    # session = requests.Session()
    # headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'}
    # response = session.get(url, headers=headers)
    browser = start_chrome(url, headless=False)
    wait_until(Text("Consent").exists, timeout_secs=10)
    click("Consent")
    try:
        # wait_until(lambda text: isinstance(text, Comment), timeout_secs=10)
        wait_until(lambda: find_all(S("//p")), timeout_secs=10)


    except TimeoutException:
        print("Innholdet ble ikke funnet i tide.")
        return ""

    soup = BeautifulSoup(browser.page_source, 'html.parser')

    paragraphs = soup.find_all('p')
    text = "\n\n".join(p.get_text().strip() for p in paragraphs)
    kill_browser()
    return text

# Eksempelbruk:
# url = "https://novelbin.com/b/bjorn-yandel-the-barbarian/chapter-529"

# chapter_text = scrape_chapter_text(url)

# print(chapter_text) 







