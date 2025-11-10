import lxml
from selenium.common.exceptions import ElementClickInterceptedException
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
service = Service(executable_path='WIld-Parser/chromedriver.exe', )

driver = webdriver.Chrome(service=service,options=options)
driver.get("https://www.citilink.ru")
path = '/html/body/div[2]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/form/div/div/label/input'
path2= '/html/body/div[2]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/form/div/div/label/div/div/button'
path3 = '<a data-meta-name="PageLink__page-9" href="https://www.citilink.ru/search/?ref=undefined&amp;p=9&amp;text=%D0%BA%D0%BE%D0%B2%D0%BA%D1%80%D0%B8%D0%BA" class="app-catalog-b37od0-Anchor--Anchor e1136wl80"><div data-meta-name="PaginationElement__page9" data-meta-page-number="9" class="app-catalog-10181fg-ElementWrapper--ElementWrapper evbl9mj0">9</div></a>'

23
driver.find_element(By.XPATH,path).send_keys("клавиатура")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(driver.find_element(By.XPATH, path2))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(driver.find_element(By.XPATH, path2))).click()
#
soup = BeautifulSoup(driver.page_source, 'html.parser')
pagination_elements = soup.find_all('div', class_='app-catalog-10181fg-ElementWrapper--ElementWrapper')
description = soup.find_all(class_='app-catalog-1g0fl7h-Anchor--Anchor-Anchor--StyledAnchor ejir1360')
price = soup.find_all(class_='e4ahr150 e1a7a4n70 app-catalog-e46fw7-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent-MainPriceNumber--StyledMainPriceNumber ez8h4tf0')
img = soup.find_all(class_='app-catalog-14s4sql-Anchor--Anchor e1136wl80')
print(description, price, img, pagination_elements,sep='\n'+ '------')

# ass = []
# ass_price = []
# ass_img = []
#
last_element = pagination_elements[-1]  # Берем последний элемент
last_page_number = last_element.text.strip()
print(last_page_number)
#
# for _ in range(3):
#   try:
#     driver.find_element(By.LINK_TEXT, 'Следующая').click()
#     break # Successful click, exit the loop
#
#   except:
#     time.sleep(2) # Wait for a while before retrying
#
#
# description = soup.find_all(class_='app-catalog-51bw0j-Anchor--Anchor-Anchor--StyledAnchor e1rznl640')
# price = soup.find_all(class_='e4ahr150 e1a7a4n70 app-catalog-e46fw7-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent-MainPriceNumber--StyledMainPriceNumber ez8h4tf0')
# img = soup.find_all(class_="eikooao0 app-catalog-1uk1s5v-Img--StyledImg-Img--StyledImg-StyledImage ed4p12j0 is-selected")
#
# for i in description:
#    if i not in ass:
#       ass.append(i)
# for i in price:
#    if i not in ass_price:
#       ass_price.append(i)
# for i in img:
#    if i not in ass_img:
#       ass_img.append(i)
# print(len(ass),len(ass_price),len(ass_img))
# # soup = BeautifulSoup(driver.page_source, 'html.parser')
# # description = soup.find_all(class_='app-catalog-51bw0j-Anchor--Anchor-Anchor--StyledAnchor e1rznl640')
# # price = soup.find_all(class_='e4ahr150 e1a7a4n70 app-catalog-e46fw7-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent-MainPriceNumber--StyledMainPriceNumber ez8h4tf0')
# # img = soup.find_all(class_="eikooao0 app-catalog-1uk1s5v-Img--StyledImg-Img--StyledImg-StyledImage ed4p12j0 is-selected")
# # counter = 0
# # for j in price:
# #    counter += 1
# # print(counter)
# # counter = 0
# # num = soup.find_all(class_="app-catalog-10181fg-ElementWrapper--ElementWrapper evbl9mj0")
# # exctract_num = len(num)
# # # driver.get(f'{'https://www.citilink.ru/catalog/myshi/'+'?ref=undefined&p='+str(num_of_pages)}')
# # price = soup.find_all(class_='e4ahr150 e1a7a4n70 app-catalog-e46fw7-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent-MainPriceNumber--StyledMainPriceNumber ez8h4tf0')
# # for j in price:
# #    counter += 1
# # print(counter,num,exctract_num,sep='\n'+'- - -')
# #
# # element = '/html/body/div[2]/div[1]/main/section/div[3]/div/div[3]/section/div[2]/div[3]/div/div[2]/a[6]'
# # page_number = element.get('data-meta-page-number')
# # print(page_number)
#    # link = j.get('href')
#    # title = j.get('title')
#
#    # price1 = str(j).split('>')[1].split('<')[0]
#    # print(price1)
#
#    # img = j.get('src')
#    # print(img)
#
#
# #a_tag = soup.find('a')
# # Получаем ссылку и название
# #link = a_tag.get('href')
# #title = a_tag.get('title')
# #print("Ссылка:", link)
# #print("Название:", title)
#
# #soup = BeautifulSoup(html_string, 'html.parser')
# # Находим img тег
# #img_tag = soup.find('img')
# # Получаем ссылку из атрибута src
# #image_url = img_tag.get('src')
# #print(image_url)
#
# #price = soup.get_text()
# #
#
# # driver.back
# # driver.forward()
# # driver.refresh()
# # driver.current_url
# #assert - для условий,a == a,'BugaWuga'
# #page_cource - html код страницы
# # driver.find_element(By.XPATH,path).send_keys("клавиатура")
# # driver.find_element(By.XPATH,path2).click()
#
# # st_accept = "text/html" # говорим веб-серверу,
# #                         # что хотим получить html
# # # имитируем подключение через браузер Mozilla на macOS
# # st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
# # # формируем хеш заголовков
# # headers = {
# #    "Accept": st_accept,
# #    "User-Agent": st_useragent
# # }
# #
# # # отправляем запрос с заголовками по нужному адресу
# # req = requests.get("https://selectel.ru/blog/courses/", headers)
# # # считываем текст HTML-документа
# # src = req.text
# # soup = BeautifulSoup(src, "lxml")
# # title = soup.title.string
# #
# #
# # open_search = browser.find_element("header_search")
# # open_search.click()
# # # регистрируем текстовое поле и имитируем ввод строки "Git"
# # search = browser.find_element("search-modal_input")
# # search.send_keys("Git")