<img src="https://github.com/ICQ-BOTS/horror_story_bot/blob/main/horror_story.png" width="100" height="100">


# Страшилки

[Страшилки](https://icq.im/boo_bot)

Старт:
1. Установка всех зависимостей 
```bash
pip3 install -r requirements.txt
```

2. Запуск space tarantool.
```bash
tarantoolctl start horror_story.lua
```
> Файл из папки scheme нужно перекинуть в /etc/tarantool/instances.available

3. Запуск скрипта push_tarantool.py
```bash
python3 push_tarantool.py
```

4. Вставляем токен в horror_story_bot.py

5. Запуск бота!
```bash
python3 horror_story_bot.py
```
