# import asyncio
# from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
# from aiogram import Bot,Dispatcher,F
# from aiogram.filters import CommandStart,Command
# from aiogram.types import Message
# from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
#
#
# card = ['123','1236','12345']
#
# class Reg(StatesGroup):
#     name = State()
#     number = State()
#
# async def inline_cars():
#     keyboard = InlineKeyboardBuilder()
#     for car in card:
#         keyboard.add(InlineKeyboardButton(text=car,callback_data=car))
#     return keyboard.adjust(2).as_markup()
#
# bot = Bot(token='8485015218:AAHaStZDEZHLMqJwjdiykLHKPcyGJPSVzuo')
# dp = Dispatcher()
#
# main2 = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Каталог')],
#     [KeyboardButton(text='<UNK>'),KeyboardButton(text='<2>')]
# ],
#                                 resize_keyboard=True,
#                                 input_field_placeholder='Абаюдна',
#                                                             )
# settings = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='<UNK> <UNK> <UNK>', callback_data='catalog')]
#     ])
#
# @dp.callback_query(F.data == 'catalog')
# async def catalog2(callback: CallbackQuery):
#     await callback.answer('123',show_alert=True)
#     await callback.message.edit_text('Привет',reply_markup= await inline_cars())
#
# @dp.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer('Hello world and BBC!',reply_markup=settings)
#
# @dp.message(Command('help'))
# async def help_call(message: Message):
#     await message.answer('No,suck my little dick')
#
# @dp.message(Command('reg'))
# async def reg_call(message: Message,state: FSMContext):
#     await state.set_state(Reg.name)
#     await message.answer('<UNK>')
# @dp.message(Reg.name)
# async def reg_call1(message: Message,state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(Reg.number)
#     await message.answer('<UNK>2')
# @dp.message(Reg.number)
# async def reg_call2(message: Message,state: FSMContext):
#     await state.update_data(number=message.text)
#     data = await state.get_data()
#     await message.answer(f'{data["name"]} + {data["number"]}')
#     await state.clear()
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == '__main__':
#     try:
#         asyncio.run(main())
#     except:
#         print('No no no,mister fish')
#
#
# #message.text('основа',reply_markup=kb.main)
#
# # from aiogram import Bot, Dispatcher
# # from aiogram.filters import CommandStart,Command
# # from aiogram.types import Message
# # import asyncio
# # bot = Bot(token='8485015218:AAHaStZDEZHLMqJwjdiykLHKPcyGJPSVzuo')
# # dp = Dispatcher()
# # @dp.message(CommandStart())
# # async def echo(message: Message):
# #     await message.reply('Hello')
# # @dp.message()
# # async def echo(message: Message):
# #     await message.answer(message.text)
# # async def main():
# #     await dp.start_polling(bot)
# #
# # if __name__ == '__main__':
# #     try:
# #         asyncio.run(main())
# #     except:
# #         print('No no no,mister fish')
# def out_red(text):
#     print("\033[34m{}".format(text))
# out_red("ПРИВЕТ")3