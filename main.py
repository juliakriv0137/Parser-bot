import telebot
import random
import re
from telebot import types
import sqlite3
import time
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(
    '5747827912:AAFNIzZKpT2GwXvbDYKy3O-VyNckB2Fjw-Y', parse_mode='html')
# my: 5786049786:AAGuWgUmyTh9hDgOm5d9P7_nFQemvxK2kT4
# mot-my: 5747827912:AAFNIzZKpT2GwXvbDYKy3O-VyNckB2Fjw-Y



def if_table():
    try:
        # scriptDir = os.path.dirname(os.path.realpath(__file__))
        db_connection = sqlite3.connect("database.db")
        db = db_connection.cursor()
        # print("1 Подключен к SQLite")
        sqlite_select_query = """SELECT * from company"""
        db.execute(sqlite_select_query)
        db_connection.commit()
        records = db.fetchall()
        print("Всего строк:  ", len(records))
        
        db.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite 1", error)

    finally:
        if (db_connection):
            db_connection.close()
            # print("Соединение с SQLite закрыто 1")
    return records

def insert_table_comp(a,b,c):
    try:
        # scriptDir = os.path.dirname(os.path.realpath(__file__))
        db_connection = sqlite3.connect("database.db")
        db = db_connection.cursor()
        # print("Подключен к SQLite 2")
        sqlite_insert_query = """INSERT OR IGNORE INTO company
                          (name, group_id, status)
                          VALUES
                          (?, ?, ?);"""
        data_tuple = (a,b,c)
        db.execute(sqlite_insert_query, data_tuple)
        db_connection.commit()
        db.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite 2", error)

    finally:
        if (db_connection):
            db_connection.close()
            # print("Соединение с SQLite закрыто 2")

def insert_table_words(a,b):
    if(b==''):b='---'
    
    try:
        # scriptDir = os.path.dirname(os.path.realpath(__file__))
        db_connection = sqlite3.connect("database.db")
        db = db_connection.cursor()
        # print("Подключен к SQLite 2")
        sqlite_insert_query = """INSERT OR IGNORE INTO words
                          (cmp_id, word)
                          VALUES
                          (?, ?);"""
        data_tuple = (a,b)
        db.execute(sqlite_insert_query, data_tuple)
        db_connection.commit()
        db.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite 2", error)

    finally:
        if (db_connection):
            db_connection.close()
            # print("Соединение с SQLite закрыто 2")

def get_status(nm):
    try:
        # scriptDir = os.path.dirname(os.path.realpath(__file__))
        db_connection = sqlite3.connect("database.db")
        db = db_connection.cursor()
        # print("1 Подключен к SQLite")
        sqlite_select_query = f"""SELECT status from company WHERE name='{nm}'"""
        print(sqlite_select_query)
        db.execute(sqlite_select_query)
        db_connection.commit()
        records = db.fetchall()
        print("Всего строк:  ", len(records))
        if(records[0][0]==1):
            stat=1
        if(records[0][0]==0):
            stat=0

        db.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite 1", error)

    finally:
        if (db_connection):
            db_connection.close()
            # print("Соединение с SQLite закрыто 1")
    return stat

def insert_table_stops(a,b):
    if(b==''):b='---'
    
    try:
        # scriptDir = os.path.dirname(os.path.realpath(__file__))
        db_connection = sqlite3.connect("database.db")
        db = db_connection.cursor()
        # print("Подключен к SQLite 2")
        sqlite_insert_query = """INSERT OR IGNORE INTO stops
                          (cmp_id, word)
                          VALUES
                          (?, ?);"""
        data_tuple = (a,b)
        db.execute(sqlite_insert_query, data_tuple)
        db_connection.commit()
        db.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite 2", error)

    finally:
        if (db_connection):
            db_connection.close()
            # print("Соединение с SQLite закрыто 2")

def insert_table_wgr(a,b):
    if(b==''):b='---'
    
    try:
        # scriptDir = os.path.dirname(os.path.realpath(__file__))
        db_connection = sqlite3.connect("database.db")
        db = db_connection.cursor()
        # print("Подключен к SQLite 2")
        sqlite_insert_query = """INSERT OR IGNORE INTO groups
                          (company_id, group_id)
                          VALUES
                          (?, ?);"""
        data_tuple = (a,b)
        db.execute(sqlite_insert_query, data_tuple)
        db_connection.commit()
        db.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite 2", error)

    finally:
        if (db_connection):
            db_connection.close()
            # print("Соединение с SQLite закрыто 2")

def insert_table_sgr(a,b):
    if(b==''):b='---'
    
    try:
        # scriptDir = os.path.dirname(os.path.realpath(__file__))
        db_connection = sqlite3.connect("database.db")
        db = db_connection.cursor()
        # print("Подключен к SQLite 2")
        sqlite_insert_query = f"""UPDATE company SET group_id='{b}' WHERE name='{a}';"""
        print(sqlite_insert_query)
        db.execute(sqlite_insert_query)
        db_connection.commit()
        db.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite 2", error)

    finally:
        if (db_connection):
            db_connection.close()
            # print("Соединение с SQLite закрыто 2")

def get_comp_nm(idd):
    try:
        # scriptDir = os.path.dirname(os.path.realpath(__file__))
        db_connection = sqlite3.connect("database.db")
        db = db_connection.cursor()
        # print("1 Подключен к SQLite")
        sqlite_select_query = f"""SELECT name from company WHERE id={idd} ORDER BY id DESC LIMIT 1"""
        print(sqlite_select_query)
        db.execute(sqlite_select_query)
        db_connection.commit()
        records = db.fetchall()
        print("Всего строк:  ", len(records))
        
        db.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite 1", error)

    finally:
        if (db_connection):
            db_connection.close()
            # print("Соединение с SQLite закрыто 1")
    if records[0][0]:return records[0][0]

class Filter:
    def __init__(self, name):
        self.name = name
        self.id = None
        self.camp_name = None
        self.group_id = None
        self.status = None
        self.words = None
        self.stops = None
        self.filter_table = None
        
filt=Filter('one')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Добрый день! <b>{message.from_user.first_name} {message.from_user.last_name}</b>. Я бот :). Ваш user.id:{message.from_user.id}\nВведите /filter - для начала работы'
    bot.send_message(message.chat.id, mess)
    

@bot.message_handler(commands=['filter'])
def filter(message):
    markup = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text=f'Создать', callback_data=f'createCmp')
    btn2 = InlineKeyboardButton(text=f'Список', callback_data=f'listCmp')
    markup.add(btn1,btn2)
    bot.send_message(message.chat.id, text="Создать ID или посмотреть список существующих ID?".format(message.from_user), reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def func(message):
#     pass
    

#############################################################################################################
def naming(message):
    filt.camp_name=message.text
    if (filt.camp_name=='/start' or filt.camp_name==''): 
        back(message.chat.id)
        return
    else:
        insert_table_comp(filt.camp_name, 0,1)
        # markup = InlineKeyboardMarkup()
        # bnt_back = InlineKeyboardButton(text=f'Главное меню', callback_data=f'back')
        # btn1 = InlineKeyboardButton(text=f'Добавить ключи', callback_data=f'createKey')
        # btn12 = InlineKeyboardButton(text=f'Просмотреть ключи', callback_data=f'viewKey')
        # btn2 = InlineKeyboardButton(text=f'Удалить ключи', callback_data=f'delKey')
        # btn3 = InlineKeyboardButton(text=f'Добавить стоп-ключ', callback_data=f'createStop')
        # btn13 = InlineKeyboardButton(text=f'Просмотреть стоп-слова', callback_data=f'viewStop')
        # btn4 = InlineKeyboardButton(text=f'Удалить стоп-ключ', callback_data=f'delStop')
        # btn5 = InlineKeyboardButton(text=f'Группы отслеживания', callback_data=f'listWatchGroup')
        # btn6 = InlineKeyboardButton(text=f'Группы рассылки', callback_data=f'listSndGroup')
        # markup.add(btn1,btn3)
        # markup.add(btn12,btn13)
        # markup.add(btn2,btn4)
        # markup.add(btn5, btn6)
        # markup.add(bnt_back)
        markup = InlineKeyboardMarkup(row_width=2)
        btn1 = InlineKeyboardButton(text=f'Создать', callback_data=f'createCmp')
        btn2 = InlineKeyboardButton(text=f'Список', callback_data=f'listCmp')
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id, text=f"Название сохранено.\nID_Name: {filt.camp_name}", reply_markup=markup)

def listing(message):
    print('listing')
    filt.camp_name=message.text
    markup = InlineKeyboardMarkup()
    bnt_back = InlineKeyboardButton(text=f'Главное меню', callback_data=f'back')
    btn1 = InlineKeyboardButton(text=f'Добавить ключи', callback_data=f'createKey')
    btn12 = InlineKeyboardButton(text=f'Просмотреть ключи', callback_data=f'viewKey')
    btn2 = InlineKeyboardButton(text=f'Удалить ключи', callback_data=f'delKey')
    btn3 = InlineKeyboardButton(text=f'Добавить стоп-ключ', callback_data=f'createStop')
    btn13 = InlineKeyboardButton(text=f'Просмотреть стоп-слова', callback_data=f'viewStop')
    btn4 = InlineKeyboardButton(text=f'Удалить стоп-ключ', callback_data=f'delStop')
    btn5 = InlineKeyboardButton(text=f'Группы отслеживания', callback_data=f'listWatchGroup')
    btn6 = InlineKeyboardButton(text=f'Группы рассылки', callback_data=f'listSndGroup')
    markup.add(btn1,btn3)
    markup.add(btn12,btn13)
    markup.add(btn2,btn4)
    markup.add(btn5, btn6)
    markup.add(bnt_back)
    bot.send_message(message.chat.id, text=f"ID_Name: {filt.camp_name}", reply_markup=markup)

def creatingKey(message):
    filt.camp_name=get_comp_nm(filt.id)
    words_dim=[]
    words_dim=str(message.text).split(',')
    for x in words_dim:
        insert_table_words(filt.id,x)
    
    markup = InlineKeyboardMarkup()
    bnt_back = InlineKeyboardButton(text=f'Главное меню', callback_data=f'back')
    markup.add(bnt_back)
    bot.send_message(message.chat.id, text="Ключи сохранены", reply_markup=markup)
        # back(message.chat.id)

def creatingStop(message):
    filt.camp_name=get_comp_nm(filt.id)
    words_dim=[]
    words_dim=str(message.text).split(',')
    for x in words_dim:
        insert_table_stops(filt.id,x)
    markup = InlineKeyboardMarkup()
    bnt_back = InlineKeyboardButton(text=f'Главное меню', callback_data=f'back')
    markup.add(bnt_back)
    bot.send_message(message.chat.id, text="Стоп-слова сохранены", reply_markup=markup)
        # back(message.chat.id)

def creatingWGR(message):
    filt.camp_name=get_comp_nm(filt.id)
    words_dim=[]
    words_dim=str(message.text).split(',')
    for x in words_dim:
        insert_table_wgr(filt.camp_name,x)
    markup = InlineKeyboardMarkup()
    bnt_back = InlineKeyboardButton(text=f'Главное меню', callback_data=f'back')
    markup.add(bnt_back)
    bot.send_message(message.chat.id, text="Группы отслеживания сохранены", reply_markup=markup)
        # back(message.chat.id)

def creatingSGR(message):
    filt.camp_name=get_comp_nm(filt.id)
    words_dim=[]
    words_dim=str(message.text).split(',')
    for x in words_dim:
        insert_table_sgr(filt.camp_name,x)
    markup = InlineKeyboardMarkup()
    bnt_back = InlineKeyboardButton(text=f'Главное меню', callback_data=f'back')
    markup.add(bnt_back)
    bot.send_message(message.chat.id, text="Группа/чат для рассылки информации сохранена", reply_markup=markup)
        # back(message.chat.id)

def back(chatId):
    markup0 = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text=f'Создать', callback_data=f'createCmp')
    btn2 = InlineKeyboardButton(text=f'Список', callback_data=f'listCmp')
    markup0.add(btn1,btn2)
    bot.send_message(chatId, text="Главное меню", reply_markup=markup0)
    

#--------------------------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    # req = call.data.split('_')

    if(call.data=='createCmp'):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        mesg = bot.send_message(call.message.chat.id, text="Введите название", reply_markup=markup)
        call.data=''
        bot.register_next_step_handler(mesg,naming)
    
    elif(call.data=='listCmp'):
        filt.camp_name=''
        markup = InlineKeyboardMarkup()
        records=if_table()
        for x in records:
            markup.add(InlineKeyboardButton(text=f'{x[1]}', callback_data=f'list_{x[0]}'))
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        bot.send_message(call.message.chat.id, text=f"Всего сохранено: {len(records)}", reply_markup=markup)
        # bot.register_next_step_handler(mesg,listing)

    elif(call.data=='addKey'):
        
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        mesg = bot.send_message(call.message.chat.id, text=f"ID_Name: Введите ключи через запятую. Для составных ключей используйте |", reply_markup=markup)
        call.data=''
        bot.register_next_step_handler(mesg,creatingKey)

    elif(call.data=='back'):
        filt.camp_name=''
        filt.group_id=''
        filt.status=''
        filt.words=''
        filt.stops=''
        filt.filteer_table=''
        back(call.message.chat.id)
    
    elif(call.data.find('list_')!=-1):
        filt.id=call.data[5:]
        filt.camp_name=get_comp_nm(filt.id)
        markup = InlineKeyboardMarkup()
        bnt_back = InlineKeyboardButton(text=f'Главное меню', callback_data=f'back')
        btn0 = InlineKeyboardButton(text=f'Удалить ID', callback_data=f'idDel')
        stat=get_status(filt.camp_name)
        if(stat==1):
            btn5 = InlineKeyboardButton(text=f'Выключить ID', callback_data=f'idCh')
        if(stat==0):
            btn5 = InlineKeyboardButton(text=f'Включить ID', callback_data=f'idCh')
        btn1 = InlineKeyboardButton(text=f'Ключевые слова', callback_data=f'listKey')
        btn2 = InlineKeyboardButton(text=f'Стоп-слова', callback_data=f'listStop')
        btn3 = InlineKeyboardButton(text=f'Группы отслеживания', callback_data=f'listWatchGroup')
        btn4 = InlineKeyboardButton(text=f'Группы рассылки', callback_data=f'listSndGroup')
        markup.add(btn1,btn2)
        markup.add(btn3, btn4)
        markup.add(btn5)
        markup.add(btn0)
        markup.add(bnt_back)
        bot.send_message(call.message.chat.id, text=f"ID_Name: {filt.camp_name}", reply_markup=markup)
    
    
    elif(call.data=='idDel'):
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""DELETE from company WHERE name='{filt.camp_name}'"""
            print(sqlite_select_query)
            db.execute(sqlite_select_query)
            db_connection.commit()
            
            
            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        bot.send_message(call.message.chat.id, text=f"ID_Name: {filt.camp_name} удалено", reply_markup=markup)
        call.data=''

    elif(call.data=='idCh'):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""SELECT status from company WHERE name='{filt.camp_name}'"""
            print(sqlite_select_query)
            db.execute(sqlite_select_query)
            db_connection.commit()
            records = db.fetchall()
            print("Всего строк:  ", len(records))
            if(records[0][0]==1):
                sqlite_select_query = f"""UPDATE company SET status=0 WHERE name='{filt.camp_name}'"""
                print(sqlite_select_query)
                db.execute(sqlite_select_query)
                db_connection.commit()
                bot.send_message(call.message.chat.id, text=f"ID_Name: {filt.camp_name} статус: не активно", reply_markup=markup)
            if(records[0][0]==0):
                sqlite_select_query = f"""UPDATE company SET status=1 WHERE name='{filt.camp_name}'"""
                print(sqlite_select_query)
                db.execute(sqlite_select_query)
                db_connection.commit()
                bot.send_message(call.message.chat.id, text=f"ID_Name: {filt.camp_name} статус: активно", reply_markup=markup)

            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
        
        
        call.data=''    

    elif(call.data=='listKey'):
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""SELECT word from words WHERE cmp_id='{filt.id}'"""
            db.execute(sqlite_select_query)
            db_connection.commit()
            records = db.fetchall()
            print("Всего строк:  ", len(records))
            
            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
        
        if len(records)>0:
            markup = InlineKeyboardMarkup()
            word_list='Ключи: \n'
            for x in records:
                word_list+=f'{x[0]}\n'
            markup.add(InlineKeyboardButton(text='Добавить ключи', callback_data='addKey'))
            markup.add(InlineKeyboardButton(text='Удалить ключи', callback_data='delKey'))
            bot.send_message(call.message.chat.id, text=f"{word_list}", reply_markup=markup)
        else:
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text='Добавить ключи', callback_data='addKey'))
            # markup.add(InlineKeyboardButton(text='Удалить ключи', callback_data='delKey'))
            bot.send_message(call.message.chat.id, text=f"Ключей нет", reply_markup=markup)
        call.data=''
    
    elif(call.data=='delKey'):
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""SELECT word from words WHERE cmp_id='{filt.id}'"""
            db.execute(sqlite_select_query)
            db_connection.commit()
            records = db.fetchall()
            print("Всего строк:  ", len(records))
            
            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
        
        if len(records)>0:
            markup = InlineKeyboardMarkup()
            word_list='Выберите ключ для удаления: \n'
            for x in records:
                markup.add(InlineKeyboardButton(text=f'{x[0]}', callback_data=f'dK_{x[0]}'))
            markup.add(InlineKeyboardButton(text='Удалить все ключи', callback_data='delAllKey'))
            bot.send_message(call.message.chat.id, text=f"{word_list}", reply_markup=markup)
        call.data=''
        
    
    elif(call.data.find('dK_')!=-1):  
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""DELETE from words WHERE word='{call.data[3:]}'"""
            db.execute(sqlite_select_query)
            db_connection.commit()
            
            
            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        bot.send_message(call.message.chat.id, text=f"Ключ для ID_Name: {filt.camp_name} удален", reply_markup=markup)
        call.data=''



    
    elif(call.data=='delAllKey'):    
        
        
        ########
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""DELETE from words WHERE cmp_id='{filt.id}'"""
            db.execute(sqlite_select_query)
            db_connection.commit()
            
            
            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        bot.send_message(call.message.chat.id, text=f"Ключи для ID_Name: {filt.camp_name} удалены", reply_markup=markup)
        call.data=''



################### list stop
    elif(call.data=='listStop'):
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""SELECT word from stops WHERE cmp_id='{filt.id}'"""
            db.execute(sqlite_select_query)
            db_connection.commit()
            records = db.fetchall()
            print("Всего строк:  ", len(records))
            
            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
            
        if len(records)>0:
            markup = InlineKeyboardMarkup()
            word_list='Стоп слова: \n'
            for x in records:
                word_list+=f'{x[0]}\n'
            markup.add(InlineKeyboardButton(text='Добавить стоп-слова', callback_data='addStop'))
            markup.add(InlineKeyboardButton(text='Удалить стоп-слова', callback_data='delStop'))
            bot.send_message(call.message.chat.id, text=f"{word_list}", reply_markup=markup)
        else:
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text='Добавить стоп-слова', callback_data='addStop'))
            # markup.add(InlineKeyboardButton(text='Удалить стоп-слова', callback_data='delStop'))
            bot.send_message(call.message.chat.id, text=f"Стоп-слов нет", reply_markup=markup)
        call.data=''
    
    
    
    
    
    elif(call.data=='delStop'):
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""SELECT word from stops WHERE cmp_id='{filt.id}'"""
            db.execute(sqlite_select_query)
            db_connection.commit()
            records = db.fetchall()
            print("Всего строк:  ", len(records))
            
            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
            
        if len(records)>0:
            markup = InlineKeyboardMarkup()
            word_list='Выберите стоп-слово для удаления \n'
            for x in records:
                markup.add(InlineKeyboardButton(text=f'{x[0]}', callback_data=f'dS_{x[0]}'))
            markup.add(InlineKeyboardButton(text='Удалить все стоп-слова', callback_data='delAllStop'))
            bot.send_message(call.message.chat.id, text=f"{word_list}", reply_markup=markup)
    

    elif(call.data.find('dS_')!=-1):  
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""DELETE from stops WHERE word='{call.data[3:]}'"""
            db.execute(sqlite_select_query)
            db_connection.commit()
            
            
            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        bot.send_message(call.message.chat.id, text=f"Стоп-слово для ID_Name: {filt.camp_name} удалено", reply_markup=markup)
        call.data=''    

    elif(call.data=='delAllStop'):
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""DELETE from stops WHERE cmp_id='{filt.id}'"""
            db.execute(sqlite_select_query)
            db_connection.commit()
            
            
            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        bot.send_message(call.message.chat.id, text=f"Стоп слова для ID_Name: {filt.camp_name} удалены", reply_markup=markup)
        call.data=''

    elif(call.data=='addStop'):
        
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        mesg = bot.send_message(call.message.chat.id, text=f"ID_Name: Введите стоп-слова через запятую.", reply_markup=markup)
        call.data=''
        bot.register_next_step_handler(mesg,creatingStop) 

############################### list watch
    elif(call.data=='listWatchGroup'):
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""SELECT group_id from groups WHERE company_id='{filt.camp_name}'"""
            db.execute(sqlite_select_query)
            db_connection.commit()
            records = db.fetchall()
            print("Всего строк:  ", len(records))
            
            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
            
        if len(records)>0:
            markup = InlineKeyboardMarkup()
            word_list='Группы отслеживания: '
            for x in records:
                word_list+=f'{x[0]}\n'
            markup.add(InlineKeyboardButton(text='Добавить группу', callback_data='addWGr'))
            markup.add(InlineKeyboardButton(text='Удалить группу', callback_data='delWGr'))
            bot.send_message(call.message.chat.id, text=f"{word_list}", reply_markup=markup)
        else:
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text='Добавить группу', callback_data='addWGr'))
            # markup.add(InlineKeyboardButton(text='Удалить стоп-слова', callback_data='delWGr'))
            bot.send_message(call.message.chat.id, text=f"Групп отслеживания нет", reply_markup=markup)
        call.data=''
    
    elif(call.data=='delWGr'):
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""DELETE from groups WHERE company_id='{filt.camp_name}'"""
            db.execute(sqlite_select_query)
            db_connection.commit()
            
            
            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        bot.send_message(call.message.chat.id, text=f"Группы отслеживания для ID_Name: {filt.camp_name} удалены", reply_markup=markup)
        call.data=''
    
    elif(call.data=='addWGr'):
        
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        mesg = bot.send_message(call.message.chat.id, text=f"ID_Name: Введите номера групп через запятую.", reply_markup=markup)
        call.data=''
        bot.register_next_step_handler(mesg,creatingWGR) 

#################### list Snd
    elif(call.data=='listSndGroup'):
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""SELECT group_id from company WHERE name='{filt.camp_name}'"""
            db.execute(sqlite_select_query)
            db_connection.commit()
            records = db.fetchall()
            print("Всего строк:  ", len(records))
            
            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
            
        if len(records)>0:
            markup = InlineKeyboardMarkup()
            word_list='Группа/Чат для рассылки информации: '
            for x in records:
                word_list+=f'{x[0]}\n'
            print(records[0][0])
            if (records[0][0]==0):
                markup.add(InlineKeyboardButton(text='Добавить группу или чат', callback_data='addSGr'))
                # markup.add(InlineKeyboardButton(text='Удалить группу или чат', callback_data='delSGr'))
                bot.send_message(call.message.chat.id, text=f"не заданы", reply_markup=markup)
            else:
                markup.add(InlineKeyboardButton(text='Добавить группу или чат', callback_data='addSGr'))
                markup.add(InlineKeyboardButton(text='Удалить группу или чат', callback_data='delSGr'))
                bot.send_message(call.message.chat.id, text=f"{word_list}", reply_markup=markup)
        else:
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text='Добавить группу или чат', callback_data='addSGr'))
            # markup.add(InlineKeyboardButton(text='Удалить стоп-слова', callback_data='delWGr'))
            bot.send_message(call.message.chat.id, text=f"Групп отслеживания нет", reply_markup=markup)
        call.data=''
    
    elif(call.data=='delSGr'):
        try:
            # scriptDir = os.path.dirname(os.path.realpath(__file__))
            db_connection = sqlite3.connect("database.db")
            db = db_connection.cursor()
            # print("1 Подключен к SQLite")
            sqlite_select_query = f"""UPDATE company SET group_id='0' WHERE name='{filt.camp_name}'"""
            db.execute(sqlite_select_query)
            db_connection.commit()
            
            
            db.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite 1", error)

        finally:
            if (db_connection):
                db_connection.close()
                # print("Соединение с SQLite закрыто 1")
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        bot.send_message(call.message.chat.id, text=f"Группа/чат для ID_Name: {filt.camp_name} удалена", reply_markup=markup)
        call.data=''
    
    elif(call.data=='addSGr'):
        
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'Главное меню', callback_data=f'back'))
        mesg = bot.send_message(call.message.chat.id, text=f"ID_Name: Введите номер группы или чата", reply_markup=markup)
        call.data=''
        bot.register_next_step_handler(mesg,creatingSGR) 



bot.polling(non_stop='true')