from flask import Flask
from flask import Flask, request, render_template, url_for
from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import hashlib
import uuid

p = "36fb1e4a062f2f8ac2e8f889e986614682dc19e5912b0cfcb6776f958076c743:93ec32d3d0014b4ab5fe05b0405a2e32"

hash_object = hashlib.sha1(b'admin')
hex_dig = hash_object.hexdigest()
 
print(hex_dig)

def hash_password(password):
    # uuid используется для генерации случайного числа
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
new_pass = input('Введите пароль: ')
hashed_password = hash_password(new_pass)
print('Строка для хранения в базе данных: ' + hashed_password)
old_pass = input('Введите пароль еще раз для проверки: ')
 
if check_password(hashed_password, old_pass):
    print('Вы ввели правильный пароль')
else:
    print('Извините, но пароль не подходит')

app = Flask(__name__)


@app.route('/login/', methods =["GET", "POST"])
def login():
    if request.method == "POST":
       name = request.form.get("fname") 
       password = request.form.get("lname")
       hashpass =  hash_password(password)
       print(hashpass)
       print(p)
       if name == "admin" and hashpass == p:
            if not request.cookies.get('36fb1e4a062f2f8ac2e8f889e986614682dc19e5912b0cfcb6776f958076c743:93ec32d3d0014b4ab5fe05b0405a2e32'):
                res = make_response("загрузил куки")
                res.set_cookie('36fb1e4a062f2f8ac2e8f889e986614682dc19e5912b0cfcb6776f958076c743:93ec32d3d0014b4ab5fe05b0405a2e32', 'lolo', max_age=60*60*24*365*2)
            else:
                res = make_response("этот куки уже есть в браузере {}".format(request.cookies.get('36fb1e4a062f2f8ac2e8f889e986614682dc19e5912b0cfcb6776f958076c743:93ec32d3d0014b4ab5fe05b0405a2e32')))
            return res
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run()