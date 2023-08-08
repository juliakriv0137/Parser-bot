from pyrogram import Client
import sqlite3

def get_words():
    try:
        
        db_connection = sqlite3.connect("database.db")
        db = db_connection.cursor()
        
        sqlite_select_query = """SELECT * from words"""
        db.execute(sqlite_select_query)
        db_connection.commit()
        records = db.fetchall()
        
        if(len(records)==0): return
        db.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite 1", error)

    finally:
        if (db_connection):
            db_connection.close()
            
    return records

def get_stops(xx):
    try:
        
        db_connection = sqlite3.connect("database.db")
        db = db_connection.cursor()
        
        sqlite_select_query = f"""SELECT * from stops WHERE cmp_id={xx}"""
        db.execute(sqlite_select_query)
        db_connection.commit()
        records = db.fetchall()
        
        if(len(records)==0): return
        db.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite 1", error)

    finally:
        if (db_connection):
            db_connection.close()
            
    return records

def get_all_stops():
    try:
        # scriptDir = os.path.dirname(os.path.realpath(__file__))
        db_connection = sqlite3.connect("database.db")
        db = db_connection.cursor()
        # print("1 Подключен к SQLite")
        sqlite_select_query = f"""SELECT * from stops """
        db.execute(sqlite_select_query)
        db_connection.commit()
        records = db.fetchall()
        # print("Всего строк:  ", len(records))
        if(len(records)==0): return
        db.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite 1", error)

    finally:
        if (db_connection):
            db_connection.close()
            # print("Соединение с SQLite закрыто 1")
    return records

def get_ch(x):
    try:
        
        db_connection = sqlite3.connect("database.db")
        db = db_connection.cursor()
        
        sqlite_select_query = f"""SELECT * from company WHERE id={x} AND status=1 """
        db.execute(sqlite_select_query)
        db_connection.commit()
        records = db.fetchall()
        
        if(len(records)==0): return
        db.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite 1", error)

    finally:
        if (db_connection):
            db_connection.close()
           
    return records


#21157313 99fc0386578ff93214d5e73320623cee +995 591019980
app = Client('her_session', api_id=21157313, api_hash='99fc0386578ff93214d5e73320623cee')
# app = Client('her_session')

@app.on_message()
async def my_handler(client, message):
    un_res=[]
    k_w=[]
    w_stop=[]
    
    if(message.photo): new_message=message.caption
    else: new_message=message.text
    if(message.text): new_message=message.text
    if(new_message):
        # print(new_message)
        print(message.link)
        new_message = new_message.lower()
        records=get_words()
        trig=1
        stop_id=[]
        all_stop=get_all_stops()
        if all_stop:
            for x in all_stop:
                if(new_message.find(x[1].lower())!=-1):
                    stop_id.append(x[0])
        
        if(trig!=0 and records):
            for x in records:       
                for y in (x[1].split(',')):
                    if (new_message):
                        
                        if(y.strip().find('|')!=-1):
                            
                            w01=y.strip().split('|')
                            
                            if(new_message.find(w01[0])!=-1 and new_message.find(w01[1])!=-1):
                            
                                to_ch=get_ch(x[0])
                                
                                if(to_ch):
                                    if(to_ch[0][0] not in stop_id):
                                        ch_id = to_ch[0][3]
                                        
                                        un_res.append(ch_id)
                                        k_w.append(y)
                        elif(new_message.find(y.strip())!=-1):
                            
                            to_ch=get_ch(x[0])
                            if(to_ch):
                                if(to_ch[0][0] not in stop_id):
                                    ch_id = to_ch[0][3]
                                    
                                    un_res.append(ch_id)
                                    k_w.append(y)

            if(len(un_res)>0):       

                this_dict={
                }

                for x in range(len(un_res)):
                    this_dict[un_res[x]]= ''
                
                for x in range(len(un_res)):
                    this_dict[un_res[x]]= f'{this_dict[un_res[x]]} {k_w[x]}'

                for xx in this_dict.keys():
                    key_w = this_dict[xx]


                    try:
                        if (message.photo):
                            if (message.sender_chat):
                                # await app.send_message(xx, f'✅{key_w}\n💬@{message.sender_chat.title}\n🙋‍♂️@{message.chat.username}\n🔗{message.link}\n\n{message.text}\n{message.photo}')
                                await app.send_photo(chat_id=xx, photo = f'{message.photo.file_id}', caption=f'✅{key_w}\n🙋‍♂️@{message.chat.username}\n💬@{message.sender_chat.title}\n🔗{message.link}\n\n{message.caption}')
                            else:
                                # await app.send_message(xx, f'✅{key_w}\n💬@{message.from_user.username}\n🙋‍♂️@{message.chat.username}\n🔗{message.link}\n\n{message.text}\n{message.photo}')
                                await app.send_photo(chat_id=xx, photo = f'{message.photo.file_id}', caption=f'✅{key_w}\n🙋‍♂️@{message.chat.username}\n💬@{message.from_user.username}\n🔗{message.link}\n\n{message.caption}')
                        else:
                            if (message.sender_chat):
                                await app.send_message(xx, f'✅{key_w}\n🙋‍♂️@{message.chat.username}\n💬@{message.sender_chat.title}\n🔗{message.link}\n\n{message.text}')
                            else:
                                await app.send_message(xx, f'✅{key_w}\n🙋‍♂️@{message.chat.username}\n💬@{message.from_user.username}\n🔗{message.link}\n\n{message.text}')
                    except: pass


app.run()