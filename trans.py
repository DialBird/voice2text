import os
import openai

# 入力する音声ファイル
fname = "nft-dao.mp3"
# APIキーが格納されたファイルへのパス
openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file = open(fname, "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
txt = transcript['text']
f = open(fname + ".txt", "w")
f.write(txt)
f.close()
