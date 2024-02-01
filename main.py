from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup


storage=MemoryStorage()
bot = Bot("6328972664:AAGuH9KjCkspDTthHDkGcg5fs5-YWrvhPC4")
dp = Dispatcher(bot,storage=storage)


kb2=ReplyKeyboardMarkup(resize_keyboard=True)
kb2.add(KeyboardButton('/start'))

class Support(StatesGroup):
    idea = State()



@dp.message_handler(commands=['start'],commands_prefix='/')
async def commandasd(message: types.Message):
    await message.answer(text="Это придложка для swydk. Напиши свою идею одним сообщением")

    await Support.idea.set()
  


@dp.message_handler(state=Support.idea)
async def prob(message: types.Message,state=FSMContext):
    
    await message.answer(text="Спасибо за вашу идею",reply_markup=kb2)
    await bot.send_message(5128389615,str("Новая идея  "+message.text))
    await state.finish()


# start_polling
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)




