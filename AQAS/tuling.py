import requests
import json
import zuoyeti

tuling_url = "http://openapi.tuling123.com/openapi/api/v2"    #图灵机器人api接口地址
data = {        #传的参数
    "reqType":0,
    "perception":{
        "inputText":{       #注意：T为大写
            "text":"太原今天天气怎么样"
        }
    },
    "userInfo":{
        "apiKey":"c631eb51aee742cdb6a2108d3d619068",   #注意，这里的K是大写；
        "userId":"zhao"   #注意：这里的I是大写；
    }
}

def to_tuling(q,user_id):
    data["perception"]["inputText"]["text"] = q
    data["userInfo"]["userId"] = user_id

    res = requests.post(tuling_url,json=data)   #模拟发送post请求
    res_dic = json.loads(res.content.decode("utf-8"))  #type:dict
    print(res_dic)   #{'intent': {'actionName': '', 'code': 10008, 'intentName': '', 'parameters': {'date': '2018-09-11', 'city': '太原'}}, 'results': [{'groupType': 1, 'resultType': 'text', 'values': {'text': '太原:周二,多云转阴 西南风微风,最低气温13度，最高气温26度'}}]}
    res_type = res_dic.get("results")[0].get("resultType")   #这里得到是"text"
    result = res_dic.get("results")[0].get("values").get(res_type)   #这里获取到的是最终要回答的语音的汉字翻译
    print(result)
    # zuoyeti.text2audio(result)    #这里调用作业题里面的text2audio函数；

    return result