from aip import AipSpeech
import sys
import os
#注意：这个运行环境是python3.6
""" 你的 APPID AK SK """
APP_ID = '11793791'
API_KEY = 'iaTErc4r5GXNT56tYnlVtVtk'
SECRET_KEY = '24P7ImcU7kEaOmoBxDy9giNe6evkYca4'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
filePath = "wyn.m4a"

def get_file_content(filePath):
    os.system(f"ffmpeg -y -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm")
    with open(f"{filePath}.pcm", 'rb') as fp:
        return fp.read()

# 识别本地文件
liu = get_file_content(filePath)
res = client.asr(liu, 'pcm', 16000, {     #打开并识别本地文件
    'dev_pid': 1536,
})

if res.get("result"):
    print(res.get("result")[0])
else:
    print(res)

#这个是自己练习用的，自己用录音机录了一段语音，这段代码自动将录音识别成汉字