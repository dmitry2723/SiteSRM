from flask import Flask
from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/login/", methods=['post', 'get'])
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()