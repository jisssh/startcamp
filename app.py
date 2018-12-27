#  https://ide.c9.io/jisssh/startcamp
#       'DOMAIN'
# export FLASK_ENV='development'  개발자 모드 on 수정 사항 바로 반영 된다.
# flask run -h 0.0.0.0 -p 8080   

from flask import Flask, jsonify, render_template,request
from random import sample
import random
import requests

app = Flask(__name__)

@app.route("/")
def index():
    lunch =random.choice (['20층','Diet'])
    return render_template('index.html',lunch=lunch)

@app.route("/ide/<string:username>/<string:workspace>") #변수 설정 한거임
def username_workspace(username, workspace):
    return render_template(
        'ide.html',
        name=username, space=workspace
        )

@app.route("/hi")
def hi():
    return 'Hello SSAFY'
    
@app.route("/pick_lotto")
def pick_lotto():
    return jsonify(sample(range(1,46),6))
   
@app.route("/get_lotto/<int:draw_no>")
def get_lotto():
    data = {
        'numbers': [1,2,3,4,5,6],
        'bonus': 7
    }
    return jsonify(data)


@app.route("/get_number/<string:username>/<string:number>")
def get_number(username,number):
    return "{}'s number is {}".format(username,number)

#@app.route("/please_subscibe_me")
@app.route("/ide/please_subcribe_me/<string:jisssh>")
def please_subcribe_me(jisssh):
    url="https://www.youtube.com/channel/UC6guR0-vNBvPE2QP1f9TEmw?view_as=subscriber"
   
    return "<a href={}>지쓰 구독해줘!!</a>".format(url)
    
@app.route("/info")
def info():
    
    return render_template('info.html')
    
@app.route("/info/jisssh")
def jisssh():
    return render_template('jiss.html')    
    


@app.route("/reservation")
def reservation():
    
    return render_template('reservation.html')

 
@app.route("/reservation/jisssh")
def reservationjisssh():
    
    nick = request.args.get('nick')
    date = request.args.get('date')
    # time = requests.args.get('time')
    result = str(nick)+ '님은' +str(date) +'에 예약하셨습니다.'
     
    MY_CHAT_ID = '596061047'
    BOT_TOKEN = '665281718:AAHfEP0k9mu7aEh0sWQML1JCZaLnsdVuZE4'
    url = "https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN,MY_CHAT_ID,result)    
 
    response = requests.get(url)
    
    return render_template('reservation_jiss.html', nick=nick, date=date)

# @app.route("reservation/jisssh/time")
# def reservationjisssh_time():
    
#     return render_template('reservationjisssh_time.html')

# @app.route("/reservation/jisssh/dec21")
# def dec21():
#     name = request.args.get('name')
#     return render_template('dec21.html')

# @app.route("/reservation/jisssh/dec22")
# def dec22():
#     name = request.args.get('name')
#     return render_template('dec22.html')
    
# @app.route("/reservation/jisssh/dec23")
# def dec23():
#     name = request.args.get('name')
#     return render_template('dec23.html')
    
# @app.route("/reservation/jisssh/dec24")
# def dec24():
#     name = request.args.get('name')
#     return render_template('dec24.html')

@app.route("/ping")
def ping():
    return render_template('ping.html')



@app.route("/pong")
def pong():
    ssum = request.args.get('ssum')
    me = request.args.get('me')
    result=me +'=>'+ssum
    match_point = random.choice(range(1, 100))
   
     
    MY_CHAT_ID = '596061047'
    BOT_TOKEN = '665281718:AAHfEP0k9mu7aEh0sWQML1JCZaLnsdVuZE4'
    url = "https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN,MY_CHAT_ID,result)    
 
    response = requests.get(url)
    return render_template('pong.html', match_point=match_point, ssum=ssum)

    
if __name__ == '__main__' :
    app.run(host= '0.0.0.0' , port=8080 )

# export FLASK_ENV='development'
# $ python3 app.py 
    
    
    