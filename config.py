# Currently only English and Russian languages are avelible
# English = EN
# Russian = RU
LANGUAGE = 'EN'

# Debug mode loads local dotenv file
# Turn off debug mode before deploying
DEBUG = True

PREFIX = '.'
MODMAIL_CHANNEL_NAME = '🔒┃почта'
EMBED_COLOUR = '0x9F85FF'
DICE_URL = 'https://i.imgur.com/HbLQ9CQ.png'
COIN_URL = 'https://i.imgur.com/y3sZ7Ll.png'
PYTZ_TIMEZONE = 'Europe/Moscow' # You can get yours here: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

if LANGUAGE == 'EN':
    # Evo.py
    DEBUG_IS_ON = 'DEBUG MODE IS ON'
    LOADED = 'Loaded'
    UNLOADED = 'Unloaded'
    RELOADED = 'Reloaded'
    LOGING_IN = 'Logging in'

    # Basic.py
    LOGGED_AS = 'Logged in as'
    LATENCY_IS = 'Latency is'

    # Mix.py
    SUM = 'Sum is'
    DICE = 'dice'
    REQUESTED_BY = 'Requested by'
    RESULT = 'Result'
    HEADS = 'Heads'
    TAILS = 'Tails'
    FIRST_NUMER = 'First number'
    SECOND = 'Second'
    BETWEEN = 'Between'
    AND = 'and'
    POLL = 'Poll'

    # Mod.py
    MESSEGES_WERE_DELETED = 'messeges were deleted'
    USER = 'User'
    WAS_BANNED_REASON = 'was baned with the reason'
    WAS_UNBANNED = 'was unbanned'
    WAS_KICKED_REASON = 'was kicked with the reason'
    INFO_ABOUT = 'Info about'
    NAME_ON_SERVER = 'Name on the server'
    ID = 'ID'
    MENTION = 'Mention'
    JOINED = 'Joined'
    ACC_CREATED = 'Account was created'
    BEEN_ON_SERVER = 'Have been on the server'
    HOURS = 'hours'
    MSG_WAS_SENT = 'Messege was sent'
    MSG = 'Messege'
    NOT_FOUND = 'not found'
    INCORRECT_COMMAND_USAGE = 'Incorrect command usage'
    USAGE = 'Usage'

if LANGUAGE == 'RU':
    # Evo.py
    DEBUG_IS_ON = 'РЕЖИМ ДЕБАГА ВКЛЮЧЕН'
    LOADED = 'Загружено'
    UNLOADED = 'Выгружено'
    RELOADED = 'Перезагружено'
    LOGING_IN = 'Загрузка'

    # Basic.py
    LOGGED_AS = 'Вход как'
    LATENCY_IS = 'Время отклика'

    # Mix.py
    SUM = 'Сумма'
    DICE = 'кубик'
    REQUESTED_BY = 'Запрошено'
    RESULT = 'Результат'
    HEADS = 'Орел'
    TAILS = 'Решка'
    FIRST_NUMER = 'Первое число'
    SECOND = 'Второе'
    BETWEEN = 'Межды'
    AND = 'и'
    POLL = 'Голосование'

    # Mod.py
    MESSEGES_WERE_DELETED = 'сообщений было удалено'
    USER = 'Пользователь'
    WAS_BANNED_REASON = 'был забанен по причине'
    WAS_UNBANNED = 'был разбанен'
    WAS_KICKED_REASON = 'был кикнут по причине'
    INFO_ABOUT = 'Информация о'
    NAME_ON_SERVER = 'Имя на сервере'
    ID = 'ID'
    MENTION = 'Упоминание'
    JOINED = 'Присоединился'
    ACC_CREATED = 'Аккаунт создан'
    BEEN_ON_SERVER = 'Пробыл на сервере'
    HOURS = 'часов'
    MSG_WAS_SENT = 'Сообщение было отправлено'
    MSG = 'Сообщение'
    NOT_FOUND = 'не найден'
    COMMAND_INCORRECT_USAGE = 'Неверное использование команды'
    USAGE = 'Использование'

