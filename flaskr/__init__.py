import os
import sys
from flask import Flask
from flask import request
from flaskr.WXBizMsgCrypt3 import WXBizMsgCrypt
from flask import url_for


# Token = "Token"


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    create_routers(app=app)

    return app


def create_routers(app:Flask):
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    # a simple page that says hello
    @app.get('/')
    def check_url_validation():
        msg_signature,timestamp,nonce,echostr = request.args.get('msg_signature'),request.args.get('timestamp'),request.args.get('nonce'),request.args.get('echostr')
        print(msg_signature,timestamp,nonce,echostr)
        wxcpt=WXBizMsgCrypt(Token,EncodingAESKey,CorpID)
        ret,echoStr=wxcpt.VerifyURL(msg_signature, timestamp,nonce,echostr)
        if(ret!=0):
            app.logger.error("ERR: VerifyURL ret: " + str(ret))
            return str(ret)
        print(echoStr)
        return echoStr
    

    with app.test_request_context():
        print(url_for('check_url_validation',method="get",msg_signature="msg_signature",timestamp="timestamp",nonce="nonce",echostr="echostr"))
        # print(url_for('login'))
        # print(url_for('login', next='/'))
        # print(url_for('profile', username='John Doe'))
