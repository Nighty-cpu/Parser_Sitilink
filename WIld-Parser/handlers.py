from aiogram import F,Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,FSInputFile,CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
from keyboard import Inline_keyboard
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder

import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

router = Router()
index = 0
flag = True

value_description = []  # Список описаний
value_price = []        # Список цен
value_img = []          # Список изображений
value_url = []          # Список ссылок для покупки

class Register(StatesGroup):
    answer = State()

async def keyboard_for_buy(url,index1,index2):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Купить',url=url))
    if index2 != index1-1:
        keyboard.add(InlineKeyboardButton(text='Вперёд', callback_data='next'))
    if int(index2) != 0:
        keyboard.add(InlineKeyboardButton(text='Назад', callback_data='previous'))
    keyboard.add(InlineKeyboardButton(text='Ввести другой запрос', callback_data='callback'))
    return keyboard.adjust(2).as_markup()

@router.callback_query(F.data == 'next')
async def callback_message(callback: CallbackQuery):
    global index
    index += 1
    await callback.answer()
    await callback.message.answer_photo(photo=f'{value_img[index]}',
                               caption=f'<code>{value_description[index]}</code>' + '\n' +
                                       f'<code>Цена - {value_price[index]}</code>',
                               reply_markup=await keyboard_for_buy((r'https://www.citilink.ru/'+value_url[index]), len(value_price),
                                                             index),parse_mode='HTML')



@router.callback_query(F.data == 'previous')
async def callback_message(callback: CallbackQuery):
    global index
    index -= 1
    await callback.answer()
    await callback.message.answer_photo(photo=f'{(value_img[index])}',
                                caption=f'<code>{value_description[index]}</code>' + '\n' +
                                        f'<code>Цена - {value_price[index]}</code>',
                                reply_markup=await keyboard_for_buy((r'https://www.citilink.ru/'+value_url[index]), len(value_price),
                                                              index),parse_mode='HTML')

@router.callback_query(F.data == 'callback')
async def callback_message(callback: CallbackQuery,state: FSMContext):
    await callback.answer()
    await callback.message.answer('<code>Введите запрос, что вы хотите найти?</code>',parse_mode='HTML')
    global flag
    flag = True
    await state.set_state(Register.answer)
    value_description.clear()
    value_price.clear()
    value_img.clear()
    value_url.clear()

@router.message(CommandStart())
async def start_message(message: Message):
    path = 'image_for_message/citilink.jpg'
    await message.answer_photo(photo=FSInputFile(path=path),caption=f'<code>Приветствую вас,пользователь {message.from_user.username}</code>'+'\n'+'-'*60+'\n'+
                         f'<code>Я бот, созданный для показа карточек товаров из магазина Citilink по запросу.</code>'+'\n'+'-'*60+'\n'+
                         f'<code>Прошу вас,нажмите на кнопку ниже и введите свой запрос.</code>',parse_mode='HTML',reply_markup=Inline_keyboard)

@router.message(Register.answer)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(answer=message.text)
    data = await state.get_data()
    answer_from_user = data['answer']
    await state.clear()
    await message.answer('<code>Ожидайте...?</code>', parse_mode='HTML')
    global flag
    if flag:
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

        service = Service(executable_path='chromedriver.exe',)
        driver = webdriver.Chrome(service=service,options=options)
        driver.get("https://www.citilink.ru")
        path = '/html/body/div[2]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/form/div/div/label/input'
        path2= '/html/body/div[2]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/form/div/div/label/div/div/button'

        driver.find_element(By.XPATH,path).send_keys(str(answer_from_user))
        driver.find_element(By.XPATH, path2).click()
        driver.find_element(By.XPATH, path2).click()
        time.sleep(10)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        description = soup.find_all(class_="app-catalog-1g0fl7h-Anchor--Anchor-Anchor--StyledAnchor ejir1360")
        price = soup.find_all(class_='e4ahr150 e1a7a4n70 app-catalog-e46fw7-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent-MainPriceNumber--StyledMainPriceNumber ez8h4tf0')
        img = soup.find_all(class_='eikooao0 app-catalog-1uk1s5v-Img--StyledImg-Img--StyledImg-StyledImage ed4p12j0 is-selected')
        for item1 in description:
            value_description.append(item1.get('title'))
            value_url.append(item1.get('href'))
        for item2 in price:
            value_price.append(str(item2).split('>')[1].split('<')[0])
        for item3 in img:
            value_img.append(item3.get('src'))
        global index
        index = 0
        try:
            await message.delete()
            await message.answer_photo(photo=f'{value_img[index]}',
                                       caption=f'<code>{value_description[index]}</code>' + '\n' +
                                               f'<code>Цена - {value_price[index]}</code>',
                                       reply_markup=await keyboard_for_buy(
                                           (r'https://www.citilink.ru/' + value_url[index]), len(value_price), index),
                                       parse_mode='HTML')
        except Exception as e:
            await message.answer("<code>По вашему запросу ничего не найдено</code>",parse_mode='HTML')
        flag = False
        driver.quit()

