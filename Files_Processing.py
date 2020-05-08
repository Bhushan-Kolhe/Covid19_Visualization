import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import glob


def getScreenshots():
    files = [f for f in glob.glob(os.getcwd() + "\Maps\*.html", recursive=True)]
    delay=5
    options = Options()
    options.headless = True
    for f in files:
        tmpurl='file://{}'.format(f)
        browser = webdriver.Firefox(options=options)
        browser.get(tmpurl)
        #Give the map tiles some time to load
        time.sleep(delay)
        browser.save_screenshot('./images/{}.png'.format(f.split('\\')[-1].split('.')[0]))
        browser.quit()

def moveDatasets():
    files = [f for f in glob.glob(os.getcwd() + "\*.csv", recursive=True)]
    for f in files:
        os.rename(f, '{}\\Datasets\\{}'.format(os.getcwd(), f.split('\\')[-1]))

moveDatasets()
getScreenshots()
