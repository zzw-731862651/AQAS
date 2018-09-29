from aip import AipSpeech
#注意：这个运行环境是python3.6
""" 你的 APPID AK SK """
APP_ID = '11793791'
API_KEY = 'iaTErc4r5GXNT56tYnlVtVtk'
SECRET_KEY = '24P7ImcU7kEaOmoBxDy9giNe6evkYca4'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('龟儿子地，俺也会点人工智能喽！这是一个多么重要的转折点啊！啊！这是一个晴朗的天气，我喜欢人工智能！', 'zh', 1, {
    'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):     #将上面的汉字，合成语音
    with open('auido1.mp3', 'wb') as f:    #写入文件
        f.write(result)


