from flask import Flask
from flask import Flask, request, render_template, url_for
from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import hashlib
import uuid


 

# def hash_password(password):
#     # uuid используется для генерации случайного числа
#     salt = uuid.uuid4().hex
#     return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
# def check_password(hashed_password, user_password):
#     password, salt = hashed_password.split(':')
#     return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
# new_pass = input('Введите пароль: ')
# hashed_password = hash_password(new_pass)
# print('Строка для хранения в базе данных: ' + hashed_password)
# old_pass = input('Введите пароль еще раз для проверки: ')
 
# if check_password(hashed_password, old_pass):
#     print('Вы ввели правильный пароль')
# else:
#     print('Извините, но пароль не подходит')

app = Flask(__name__)

data = b'Hello, world!'
@app.route('/login/', methods =["GET", "POST"])
def login():
    hashpass = "21232f297a57a5a743894a0e4a801fc3"
    if request.method == "POST":
        name = request.form.get("fname") 
        password = request.form.get("lname")
        hash_object = hashlib.md5(password.encode())
        passr = hash_object.hexdigest()
        print(passr, hashpass)
        if name == "admin" and passr == hashpass:
            if not request.cookies.get('foo'):
                res = make_response("загрузил куки")
                res.set_cookie('foo', 'lolo', max_age=60*60*24*365*2)
            else:
                res = make_response("этот куки уже есть в браузере {}".format(request.cookies.get('foo')))
            return res
        else:
            return "Пароль, блять, не верный"
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run()