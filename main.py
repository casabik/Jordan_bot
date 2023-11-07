import html
import webbrowser

import telebot
from telebot import types
from telebot.apihelper import ApiTelegramException

bot = telebot.TeleBot('6192847761:AAEQMdItXVJVWijsSy4K5mZfyHsjmkSmYTI')

lines = open("konkurs.txt", "r", encoding="utf-8", errors='ignore')
print(lines)
c = 0
for line in lines:
    c += 1
    photo = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg"]
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Хочу на Сайт ⚡️", url='https://jordanm.mobz.click/promo')
    markup.add(button)
    temp = line.strip().split()
    id = temp[0]
    print(c)
    try:
        bot.send_message(id,
                         text="Мы запустили свой <a href='https://jordanm.mobz.click/promo'>сайт</a> и <b>эксклюзивно</b> "
                              "для участников наших конкурсов <b>дарим флеш скидку в 🔥17%</b>🔥по промокоду <b>flesh</b> "
                              "на все купальники бикини! Скидка <b>действует всего 3 дня</b> до 16 Августа. Количество "
                              "использований не ограниченно, так что не забудь порадовать подружек. Have fun💖💖💖\n \n(Дублируем"
                              " рассылку тк в промокоде была опечатка) 🥹 извините🥹", reply_markup=markup,
                         parse_mode='html')
        bot.send_media_group(id,
                             [telebot.types.InputMediaPhoto(open(p, 'rb')) for p in photo])
    except ApiTelegramException as e:
        if e.description == "Forbidden: bot was blocked by the user":
            print("Attention please! The user {} has blocked the bot. I can't send anything to them")

'''
@bot.message_handler(commands=['start'])
def hello(message):
    markup = types.InlineKeyboardMarkup()
    kon = types.InlineKeyboardButton('КОНКУРС', callback_data='konkurs')
    markup.row(kon)
    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}!\nЯ Степан, робот помощник 😇',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def button1(callback):
    if callback.data == 'konkurs':
        mark = types.InlineKeyboardMarkup()
        bot.send_chat_action(callback.message.chat.id, 'typing')
        kon = types.InlineKeyboardButton('Участвую', callback_data='check')
        mark.row(kon)
        bot.send_message(callback.message.chat.id, f'Для участия в конкурсе нажми, пожалуйста, на кнопку',
                         reply_markup=mark)
    elif callback.data == 'check2':
        res = bot.get_chat_member(chat_id='@LLL_Olya', user_id=callback.message.chat.id)
        if res.status == 'left':
            bot.answer_callback_query(callback.id, text="Нужно подписаться на канал")
        else:
            ch = True
            lines = open('konkurs.txt', 'r')
            for line in lines:
                temp = line.strip().split()
                if int(temp[0]) == callback.message.chat.id:
                    ch = not ch
                    break
            lines.close()
            if not ch:
                bot.send_message(callback.message.chat.id, 'Спасибо, конечно, но ты и так участвуешь в конкурсе.')
            else:
                lines = open('konkurs.txt', 'a')
                if callback.message.chat.username is not None:
                    lines.write(f'{callback.message.chat.id} {callback.message.chat.username} \n')
                else:
                    lines.write(
                        f'{callback.message.chat.id} {callback.message.chat.first_name} {callback.message.chat.last_name} \n')
                lines.close()
                bot.send_message(callback.message.chat.id, f'Спасибо, ты бесподобна 💘')
                bot.send_message(callback.message.chat.id,
                                 f'Результат конкурса будет опубликованы на странице группы 30 Июня. С победителем свяжется админ.')

    elif callback.data == 'check':
        res = bot.get_chat_member(chat_id='@LLL_Olya', user_id=callback.message.chat.id)
        if res.status == 'left':
            mark = types.InlineKeyboardMarkup()
            kon1 = types.InlineKeyboardButton('Канал', url='https://t.me/LLL_Olya')
            kon2 = types.InlineKeyboardButton('Подписался✅', callback_data='check2')
            mark.row(kon1)
            mark.row(kon2)
            bot.send_message(callback.message.chat.id, f'Ой ой ой, для участия в конкурсе надо сначала на нас подписаться!',
                             reply_markup=mark)
        else:
            ch = True
            lines = open('konkurs.txt', 'r')
            for line in lines:
                temp = line.strip().split()
                if int(temp[0]) == callback.message.chat.id:
                    ch = not ch
                    break
            lines.close()
            if not ch:
                bot.send_message(callback.message.chat.id, 'Спасибо, конечно, но ты и так участвуешь в конкурсе.')
            else:
                lines = open('konkurs.txt', 'a')
                if callback.message.chat.username is not None:
                    lines.write(f'{callback.message.chat.id} {callback.message.chat.username} \n')
                else:
                    lines.write(f'{callback.message.chat.id} {callback.message.chat.first_name} {callback.message.chat.last_name} \n')
                lines.close()
                bot.send_message(callback.message.chat.id, f'Спасибо, ты бесподобна 💘')
                bot.send_message(callback.message.chat.id,
                                 f'Результат конкурса будет опубликованы на странице группы 30 Июня. С победителем свяжется админ.')


bot.infinity_polling(none_stop=True)'''
