from aip import AipNlp
#注意：这个运行环境是python3.6
APP_ID = '11793791'
API_KEY = 'iaTErc4r5GXNT56tYnlVtVtk'
SECRET_KEY = '24P7ImcU7kEaOmoBxDy9giNe6evkYca4'

nlp_client = AipNlp(APP_ID,API_KEY,SECRET_KEY)     #创建实例。注意，这里是哎楼L，不是1

res = nlp_client.simnet("你叫什么名字","你的名字叫什么")  #相似度测试
print(res)

if res.get("score") > 0.7:
    print("我叫赵振伟")



#相似度测试，智能自动回复