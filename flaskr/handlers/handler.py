
from WXBizMsgCrypt3 import WXBizMsgCrypt

def check_url_validation(msg_signature,timestamp,nonce,echostr):
    wxcpt=WXBizMsgCrypt(Token,EncodingAESKey,CorpID)
    ret,sEchoStr=wxcpt.VerifyURL(msg_signature, timestamp,nonce,echostr)
    if(ret!=0):
        print("ERR: VerifyURL ret: " + str(ret))
    return 