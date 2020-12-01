import os
import os.path
import time
import json

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException

FILE_NAME = 'your_choice.json'
LOGIN_URL = 'https://login.afreecatv.com/afreeca/login.php'
CHROME_PATH = os.getenv('CHROME_PATH', '/Users/chulkim/my_utils/chromedriver')
TARGET_URL = 'http://2020award.afreecatv.com/?page=vote'

driver = webdriver.Chrome(CHROME_PATH)

driver.get('https://afreecatv.com')

login_button = driver.find_element_by_css_selector('a.login')

login_button.click()

driver.implicitly_wait(10)

user_id = os.getenv('AFREECA_ID', '')
user_pw = os.getenv('AFREECA_PW', '')

if user_id == '' or user_pw == '':
    print('id 또는 pw 를 입력해주세요..')
    driver.close()
    exit()

driver.find_element_by_css_selector('input#uid').send_keys(user_id)
driver.find_element_by_css_selector('input#password').send_keys(user_pw)
driver.find_element_by_css_selector('input#password').send_keys(Keys.RETURN)

time.sleep(5)

driver.get(TARGET_URL)

driver.implicitly_wait(10)

category_list = driver.find_elements_by_class_name('bj_box')

bj_with_category = dict()

for category_box in category_list:
    bj_box = category_box.find_elements_by_css_selector('span.bjbox')
    category_name = category_box.find_element_by_class_name('title').text
    name_list = category_box.find_elements_by_css_selector('em.name')

    name_list = list(map(lambda x: x.text, name_list))

    bj_with_category[category_name] = name_list

chosen_bj_for_category = dict()

if not os.path.isfile(FILE_NAME):
    for key, items in bj_with_category.items():
        res = ''

        for idx, name in enumerate(items):
            res += '{}: {} '.format(idx + 1, name)
        print('========== ' + key + ' 부분 =============')
        chose_bj = input(res + ' 투표를 원하는 BJ를 선택해주세요. 없으면 그냥 엔터\n')

        if chose_bj == '':
            chosen_bj_for_category[key] = ''
            continue

        chose_bj = int(chose_bj) - 1

        chosen_bj_for_category[key] = items[chose_bj]

    try:
        with open(FILE_NAME, 'w') as choice_json:
            dump_choice_json = json.dumps(
                chosen_bj_for_category, indent=4, ensure_ascii=False)
            choice_json.write(dump_choice_json)
    except Exception as e:
        print(e)
        driver.close()
else:
    try:
        with open(FILE_NAME, 'r') as choice_json:
            chosen_bj_for_category = json.load(choice_json)
    except Exception as e:
        print(e)
        driver.close()

for category_box in category_list:
    category = category_box.find_element_by_css_selector('strong.title').text

    chose_bj_name = chosen_bj_for_category[category]

    if chose_bj_name == '':
        continue

    current_category_bj_list = category_box.find_elements_by_css_selector('li')

    chose_bj_box = [
        bj_box for bj_box in current_category_bj_list
        if bj_box.find_element_by_css_selector('em.name').text == chose_bj_name
    ][0]

    try:
        chose_bj_box.find_element_by_link_text('투표하기')
        chose_bj_box.find_element_by_link_text('투표하기').click()
    except NoSuchElementException as e:
        print(e)
        continue

    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except Exception as e:
        print(e)
        continue

    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.dismiss()
    except TimeoutException as e:
        print(e)
        continue


print('======= 끝 ^^ =========')

driver.close()
