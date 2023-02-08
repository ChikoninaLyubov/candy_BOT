from aiogram import types
from loader import dp
total = 100
new_game = False

@dp.message_handler(commands=['start','старт'])
async def mes_start(massage: types.Message):
    print('Вам пришло сообщение')

@dp.message_handler(commands=['help'])
async def mes_help(massage: types.Message):
    await massage.answer('Бог поможет')
    
@dp.message_handler(commands=['new_game'])
async def mes_new(massage: types.Message):
    global new_game
    new_game = True
    await massage.answer('Игра началась')  


@dp.message_handler(commands=['set'])
async def mes_set(massage:types.Message):
    global total
    global new_game
    count = massage.text.split()[1]
    if  not new_game:
        if count.isdigit():
            total = int(count)
            await massage.answer(f'Конфет теперь будет {count}')
        else:
            await massage.answer(f'{massage.from_user.first_name} напишите цифрами')
    else:
        await massage.answer(f'{massage.from_user.first_name} нельзя менять праила во время игры')



@dp.message_handler()
async def mes_all(massage: types.Message):
    global total
    global new_game
    if new_game:
       
        if massage.text.isdigit():
            total -= int(massage.text)
            await massage.answer(f'{massage.from_user.first_name} взял(а) {massage.text} конфет.'
                                 f'на столе осталось {total}')
           
        if total <=0:
           await massage.answer(f'Урааа!{massage.from_user.first_name} ты победил(а)')
           new_game = False
    else:
        await massage.answer(f'{massage.from_user.first_name} взял(а) {massage.text} конфет.'
                                 f'на столе осталось {total}')
           
        


     