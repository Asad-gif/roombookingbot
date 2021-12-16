from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove


from config import TOKEN










bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

















# start command
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hi! This is TTPURoomBookingBot! \n/Register to get the room!")






main_menu = types.ReplyKeyboardMarkup(
    keyboard=[
       [
           types.KeyboardButton(text="/Register 🗒")
       ],
       [
           types.KeyboardButton(text="/chooseday"),
           types.KeyboardButton(text="/Contact ☎")
       ],
       [
           types.KeyboardButton(text="/Back ↩️")
       ]
    ],
    resize_keyboard=True)



@dp.message_handler(commands= "Contact")
async def date(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    await bot.send_message(message.from_user.id, "Phone☎📞: +998912345678\nWrite✏:@aaa_aaa_888\nAlso,\nif you want to be anonymous,\n you can write to @ttpunobodyknowsadminbot",reply_markup=ReplyKeyboardRemove())


# back
@dp.message_handler(commands="Back")
async def date(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    await bot.send_message(message.from_user.id, "Ok, just /register and /chooseday for booking the room", reply_markup=ReplyKeyboardRemove())




# registration command
@dp.message_handler(commands="Register")
async def cmd_inline_url(message: types.Message):
        buttons = [
            types.InlineKeyboardButton(text="Name", callback_data="get_Name"),
            types.InlineKeyboardButton(text="Surname", callback_data="get_Surname"),
            types.InlineKeyboardButton(text="Student ID", callback_data="get_ID"),
            types.InlineKeyboardButton(text="Which course you are", callback_data="get_level"),
            types.InlineKeyboardButton(text="Faculty", callback_data="get_Faculty"),
            types.InlineKeyboardButton(text="Contact", callback_data="get_Contact")
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        await message.answer("Write👇\nName:\nSurname:\nStudent ID:\nWhich course you are:\nFaculty:\nYour number:\n\nTab: /Contact", reply_markup=keyboard)

@dp.callback_query_handler(Text(startswith="get_"))
async def callbacks(call: types.CallbackQuery):
    action = call.data.split("_")[1]
    if action == "Name":
        await call.message.answer("Please, enter your name")
    elif action == "Surname":
        await call.message.answer("Please, enter your surname")
    elif action == "ID":
        await call.message.answer("Please, enter your student ID")
    elif action == "level":
        await call.message.answer("Please, enter your level")
    elif action == "Faculty":
        await call.message.answer("Please, enter your faculty")
    elif action == "Contact":
        await call.message.answer("Please, share your contact")



@dp.message_handler(commands="Info")
async def send_message(message: types.Message):
    await message.answer("Choose👇", reply_markup=main_menu)

@dp.message_handler(commands="chooseday")
async def cmd_choose_day(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    keyboard.add(*buttons)
    await message.answer("In which day you want to sit?", reply_markup=keyboard)

#Monday
@dp.message_handler(lambda message: message.text == "Monday")
async def date(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1st pair", "5th pair", "6th pair"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the time:", reply_markup=keyboard)







#Tuesday
@dp.message_handler(lambda message: message.text == "Tuesday")
async def date(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1st pair", "5th pair", "6th pair"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the time:", reply_markup=keyboard)



#Wednesday
@dp.message_handler(lambda message: message.text == "Wednesday")
async def date(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1st pair", "5th pair", "6th pair"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the time:", reply_markup=keyboard)







#Thursday
@dp.message_handler(lambda message: message.text == "Thursday")
async def date(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1st pair", "5th pair", "6th pair"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the time:", reply_markup=keyboard)



#Friday
@dp.message_handler(lambda message: message.text == "Friday")
async def date(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1st pair", "5th pair", "6th pair"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the time:", reply_markup=keyboard)







#Saturday
@dp.message_handler(lambda message: message.text == "Saturday")
async def date(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1st pair", "2nd pair", "3rd pair", "4th pair", "5th pair", "6th pair"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the time:", reply_markup=keyboard)





























# 1st pair

@dp.message_handler(lambda message: message.text == "1st pair")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1st floor", "2nd floor", "3rd floor", "4th floor"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the floor:", reply_markup=keyboard)



# 2nd pair

@dp.message_handler(lambda message: message.text == "2nd pair")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1st floor", "2nd floor", "3rd floor", "4th floor"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the floor:", reply_markup=keyboard)

# 3rd pair

@dp.message_handler(lambda message: message.text == "3rd pair")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1st floor", "2nd floor", "3rd floor", "4th floor"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the floor:", reply_markup=keyboard)

# 4th pair

@dp.message_handler(lambda message: message.text == "4th pair")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1st floor", "2nd floor", "3rd floor", "4th floor"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the floor:", reply_markup=keyboard)

# 5th pair

@dp.message_handler(lambda message: message.text == "5th pair")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1st floor", "2nd floor", "3rd floor", "4th floor"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the floor:", reply_markup=keyboard)

# 6th pair

@dp.message_handler(lambda message: message.text == "6th pair")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1st floor", "2nd floor", "3rd floor", "4th floor"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the floor:", reply_markup=keyboard)



@dp.message_handler(commands="1st pair")
async def cmd_chooseroom(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1st floor", "2nd floor", "3rd floor", "4th floor"]
    keyboard.add(*buttons)
    await message.answer("In which floor you want to sit?", reply_markup=keyboard)

#1st floor
@dp.message_handler(lambda message: message.text == "1st floor")
async def without_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1️⃣0️⃣5️⃣", "1️⃣0️⃣7️⃣"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the room:", reply_markup=keyboard)

    # 105 - 107
@dp.message_handler(lambda message: message.text in ["1️⃣0️⃣5️⃣", "1️⃣0️⃣7️⃣"])
async def firstfloor(message: types.Message):
    await bot.send_message(message.from_user.id, "Your place in ordering: ", reply_markup=ReplyKeyboardRemove())







#2nd floor
@dp.message_handler(lambda message: message.text == "2nd floor")
async def secfloor(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["2️⃣0️⃣3️⃣", "2️⃣0️⃣5️⃣", "2️⃣0️⃣6️⃣", "2️⃣0️⃣7️⃣"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the room:", reply_markup=keyboard)


    # 203 - 207
@dp.message_handler(lambda message: message.text in ["2️⃣0️⃣3️⃣", "2️⃣0️⃣5️⃣", "2️⃣0️⃣6️⃣", "2️⃣0️⃣7️⃣"])
async def secfloor(message: types.Message):
    await bot.send_message(message.from_user.id, "Great✅! We have received your messages! you are: ", reply_markup=ReplyKeyboardRemove())



#3rd floor
@dp.message_handler(lambda message: message.text == "3rd floor")
async def thirfloor(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["3️⃣0️⃣3️⃣", "3️⃣0️⃣5️⃣", "3️⃣0️⃣6️⃣", "3️⃣0️⃣7️⃣"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the room:", reply_markup=keyboard)


 # 303 - 307
@dp.message_handler(lambda message: message.text in ["3️⃣0️⃣3️⃣", "3️⃣0️⃣5️⃣", "3️⃣0️⃣6️⃣", "3️⃣0️⃣7️⃣"])
async def secfloor(message: types.Message):
    await bot.send_message(message.from_user.id, "Great✅! We have received your messages! you are: ", reply_markup=ReplyKeyboardRemove())





#4th floor
@dp.message_handler(lambda message: message.text == "4th floor")
async def foufloor(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["4️⃣0️⃣3️⃣", "4️⃣0️⃣4️⃣", "4️⃣0️⃣5️⃣", "4️⃣0️⃣6️⃣", "4️⃣0️⃣2️⃣🆎", "4️⃣0️⃣4️⃣🆎"]
    keyboard.add(*buttons)
    await message.answer("Great! Choose the room:", reply_markup=keyboard)



# 403 - 404AB

@dp.message_handler(lambda message: message.text in ["4️⃣0️⃣3️⃣","4️⃣0️⃣4️⃣", "4️⃣0️⃣5️⃣", "4️⃣0️⃣6️⃣", "4️⃣0️⃣2️⃣🆎", "4️⃣0️⃣4️⃣🆎"])
async def secfloor(message: types.Message):
        await bot.send_message(message.from_user.id, "Great✅! You are:", reply_markup=ReplyKeyboardRemove())












@dp.message_handler()
async def process_start_command(message: types.Message):
    global dictionary_users  # empty dictionary of users
    print("# User Name", message.from_user.first_name)
    print("# Last Name", message.from_user.last_name)
    print("id", message.from_user.id)
    print("Username: ", message.from_user.username)

    print("Text:", message.text)















if __name__ == '__main__':
    executor.start_polling(dp)
