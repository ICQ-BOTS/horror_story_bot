from random import choice
from tarantool_utils import *
import json

async def start(bot, event):
	if event.type.value == 'newMessage':
		await bot.send_text(
			chat_id=event.from_chat,
			text="""BOO! 👻
Я знаю все самые страшные истории, которые напугают тебя до чертиков. Если не боишься – жми на кнопку.""",
			inline_keyboard_markup="[{}]".format(json.dumps([
            	{"text": "☠️☠️☠️", "callbackData": "horro_story"}
        	]))
		)


async def story(bot, event):
	await bot.answer_callback_query(query_id=event.data['queryId'])
	story = space_story.select()
	user = User(user_id=event.data['from']['userId'])
	rend_list = choice(story)
	c = 0
	# Выдаём историю, которую пользователь не видел
	while rend_list[0] in user.user[0][3]:
		rend_list = choice(story)
		if c == len(story):
			user.user[0][3].clear()
			user.save()
			rend_list = choice(story)
			break
		else:
			c += 1
	await bot.send_text(
		chat_id=event.data['message']['chat']['chatId'],
		text=rend_list[1]
	)	
	await bot.send_text(
		chat_id=event.data['message']['chat']['chatId'],
		text="Еще одну?",
		inline_keyboard_markup="[{}]".format(json.dumps([
            {"text": "Boo! 👻", "callbackData": "horro_story"}
        ]))
	)
	user.user[0][3].append(rend_list[0])
	user.save()

   