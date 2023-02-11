from dingtalkchatbot.chatbot import DingtalkChatbot
import requests
import json
import os

def Gethtml() : # 获取并返回 早报的 json , via : https://www.alapi.cn/api/view/93
    url = "https://v2.alapi.cn/api/zaobao" # 早报地址
    ALAPI_TOKEN = os.getenv("ALAPI_TOKEN")
    payload = "token=" + str(ALAPI_TOKEN) + "&format=json"  # 此处填写 早报的token
    headers = {'Content-Type': "application/x-www-form-urlencoded"}

    response  = requests.request("POST", url, data = payload, headers = headers)
    return response.text

def texter(page) : # 根据 json 生成并返回 markdown 文本
    jsoner = json.loads(page) 
    msg = jsoner["msg"] 
    if msg != "success" :
        return "每日 60s 早报申请失败, 请尽快检修"
    
    data = jsoner["data"]

    date = data["date"]

    weiyu = list(data["weiyu"])
    del weiyu[0], weiyu[0], weiyu[0], weiyu[0] # 删除 "【微语】"
    weiyu = "".join(weiyu)
#   print(weiyu)

    image = data["image"]
    image = "![60s](" + image + ")"

    res = weiyu + "欢迎来到 " + date + "，以下是今日早报：" + image
    return res

def sendmsg(text) : # 发送信息到 dingbot
    DING_WEBHOOK = os.getenv("DING_WEBHOOK") # webhook
    DING_SECRET = os.getenv("DING_SECRET")  # 加签

    dingbot = DingtalkChatbot(DING_WEBHOOK, secret = DING_SECRET) # init
    dingbot.send_markdown(title = "今日 60s 早报已送达, 送报员 905 持续为您服务！", text = text, is_at_all = False)

if __name__ == "__main__":
    page = Gethtml()
    text = texter(page) 
    print(text)
    sendmsg(text)