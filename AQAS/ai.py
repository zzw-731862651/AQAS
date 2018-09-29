from flask import Flask,request,render_template,send_file
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket
import zuoyeti

# 备注：1：需要登录百度人工智能获取三个：
# APP_ID = '11793791'
# API_KEY = 'iaTErc4r5GXNT56tYnlVtVtk'
# SECRET_KEY = '24P7ImcU7kEaOmoBxDy9giNe6evkYca4'
#  2，修改index.html里面的：
# get_file = "http://192.168.11.41:9527/get_file/";
# WebSocket("ws://192.168.11.41:9527/index/zilong");
# 然后运行这个文件，登录http://127.0.0.1:9527/，就可以录音了
app = Flask(__name__)

@app.route("/index/<uid>")
def index(uid):
    user_socket = request.environ.get("wsgi.websocket")  #type:WebSocket
    # print(user_socket)   #

    while True:
        msg = user_socket.receive()
        if type(msg) == bytearray:
            with open("123.wav","wb")as f:
                f.write(msg)
            res_q = zuoyeti.audio2text("123.wav")
            res_a = zuoyeti.my_nlp(res_q,uid)
            file_name = zuoyeti.text2audio(res_a)
            print('--->',file_name)
            user_socket.send(file_name)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/get_file/<file_name>")
def get_file(file_name):
    return send_file(file_name)

if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0",9527),app,handler_class = WebSocketHandler)
    http_serv.serve_forever()

# 备注：1：需要登录百度人工智能获取三个：
# APP_ID = '11793791'
# API_KEY = 'iaTErc4r5GXNT56tYnlVtVtk'
# SECRET_KEY = '24P7ImcU7kEaOmoBxDy9giNe6evkYca4'
#  2，修改index.html里面的：
# get_file = "http://192.168.11.41:9527/get_file/";
# WebSocket("ws://192.168.11.41:9527/index/zilong");
# 然后运行这个文件，登录http://127.0.0.1:9527/，就可以录音了


#bug,ffmpeg重新配置一下环境变量；