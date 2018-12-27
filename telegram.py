import requests
from flask import Flask

app = Flask(__name__)

MY_CHAT_ID = '596061047'
BOT_TOKEN = '665281718:AAHfEP0k9mu7aEh0sWQML1JCZaLnsdVuZE4'
message = 'Please let me go home'
msg = input("용")
url = "htts://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN,MY_CHAT_ID,message)

response = requests.get(url)
print(response.json())

if __name__ == '__main__' :
    app.run(host= '0.0.0.0' , port=8080 )
# export FLASK_ENV='development'
# $ python3 app.py 