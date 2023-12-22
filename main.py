import sys
import sqlite3

def menu():  
    print ('Выберите действие для работы с контактами:')  
    print('1. Добавить новый')  
    print('2. Показать имеющиеся')  
    print('3. Исправить / Модифицировать')  
    print('4. Удалить безвозвратно')
    print('5. Найти контакт')
    print('6. Завершить работу')

def addcontact():
    while True:
        name = input("Имя человека: ") 
        if len(name) != 0:  
            break
        else:  
            print("Введите имя: ")     
    while True:
        surname = input("Фамилия человека: ")  
        if len(surname) != 0:  
            break
        else:
            print("Введите фамилию")    
    while True:
        num = input("Номер телефона (исключительно цифрами): ")  
        if not num.isdigit():  
            print("Введите номер цифрами")  
            continue
        elif len(num) != 10:
            print("Введите 10-значный номер без специальных символов и пробелов")  
            continue
        else:
            break
    while True:
        email = input("Адрес электронной почты: ")  
        if len(email) != 0 and '@' in email:
            break
        else:
            print("Введите почту используя спецсимвол \"@\"")
    cursor.execute('''INSERT INTO pbook (name, surname, phone_number, email) VALUES (?,?,?,?)''',
                                                                         (name, surname, num, email))  
    conn.commit()      
    print("Контакт " + surname + ' ' + name + " был успешно добавлен в базу")

def displaybook():
    cursor.execute("SELECT surname, name, phone_number, email FROM pbook ORDER BY name")
    results = cursor.fetchall()
    print(results)

def key_pair_reception(str):
    print ("Пожалуйста, укажите ключевое слово " + str + " (от 1 до 3х)")  
    print('1. Имя')
    print('2. Фамилия')
    print('3. Телефонный номер')
    print('4. Адрес e-mail')
    print('5. Вернуться в меню')
    n = int(input('Выберите: '))
    if n == 1:
        field = "name"
    elif n == 2:
        field = "surname"
    elif n == 3:
        field = "phone_number"
    elif n == 4:
        field = "email"
    else:
        return None
    keyword = input("Пожалуйста, укажите ключевое слово поиска: " + field + " = ")
    keypair = field + "='" + keyword + "'"
    return keypair

def editcontacts():
    s = key_pair_reception('поиска')
    u = key_pair_reception('обновления')
    if s != None:
        sql = "UPDATE pbook SET " + u + " WHERE " + s
        cursor.execute(sql)
        conn.commit()
        print("Запись " + s + " обновлена.")

def deletecontacts():
    s = key_pair_reception('поиска')
    if s != None:
        sql = 'DELETE FROM pbook WHERE ' + s
        cursor.execute(sql)
        conn.commit()
        print("Запись " + s + " удалена.\n")

def findcontacts():
    s = key_pair_reception('поиска')
    if s != None:
        sql = 'SELECT surname, name, phone_number, email FROM pbook WHERE ' + s + ' ORDER BY name'
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)

# Основное тело программы
print ('Телефонный справочник (в. 0.1)')
conn = sqlite3.connect('pbook.db')  
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS pbook (
                id integer PRIMARY KEY,
                name text NOT NULL,
                surname text,
                phone_number text,
                email text)''');
m = -1  
while m != 6:
    menu()  
    m = int(input('Выберите: '))  
    if m == 1:  
        addcontact()
        continue
    elif m == 2:  
        displaybook()
        continue
    elif m == 3:  
        editcontacts()
        continue
    elif m == 4:  
        deletecontacts()
        continue
    elif m == 5:  
        findcontacts()
        continue
    elif m == 6:  
        print('Программа завершена.\n')
        conn.close()
        sys.exit(0)  
    else:  
        print('Пожалуйста, следуйте инструкциям')