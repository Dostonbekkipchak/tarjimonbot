from aiogram import Bot,Dispatcher,types
from aiogram.utils import executor
from translator import tarjimon,tarjimon1
from config import TOKEN
b=Bot(token=TOKEN,parse_mode="HTML")
dp=Dispatcher(bot=b)
@dp.message_handler(commands='start')
async def start_bosganda(xabar:types.Message):
   
     x=xabar.from_user.username
     await xabar.answer(f"Assalamu alaykum {x}")
#help 
@dp.message_handler(commands='help')
async def help(xabar:types.Message):
    await xabar.answer("Ag'alli menam senga yardam beralmiyman")
#inglischa
@dp.message_handler(commands='/en')
async def til():
    til=False
    return til==True
#uzbekcha
@dp.message_handler(commands='/uz')
async def til():
   
    return til==False
#yuborilgan matn
@dp.message_handler(content_types='text')
async def xabar_kelganda(message:types.Message):
    t=message.text
    
    if til:
        tarjima=tarjimon1(text=t)
    else:
        tarjima=tarjimon(text=t)
    await message.answer(tarjima)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)