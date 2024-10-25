from sys import argv
from urllib import request, parse
import MeCab
import tntmarkov
import simpleaudio

addr = "http://127.0.0.1:50021/"
speaker = "3"

def req(path,data=[],head=dict()):
    if (data == None) | (head == None):
        req = request.Request(path)
    else:
        req = request.Request(path,data,head)
    body = ""
    with request.urlopen(req) as res:
        body = res.read()
    return body

def main(path):
    with open(path, "r", encoding='utf-8') as file:
        text = file.read()
    model = tntmarkov.MakeModel(MeCab.Tagger("-Owakati").parse(text).split(" "))
    def gen():
        return tntmarkov.MakeMarkovText(model,"、","。")[1:]
    # http://127.0.0.1:50021/speakers
    # 3
    play:simpleaudio.PlayObject = simpleaudio.WaveObject.from_wave_file("snd.wav").play()
    while True:
        text = gen()
        q = req(addr + "audio_query?text={}&speaker="+speaker
            .format(parse.quote(text)))
        snd = req(addr + "synthesis?speaker="+speaker,q,{"content-type":"application/json"})
        with open("snd.wav","wb") as file:
            file.write(snd)
        play.wait_done()
        print(text)
        play = simpleaudio.WaveObject.from_wave_file("snd.wav").play()

if __name__ == "__main__":
    if(len(argv) <= 1):
        print("usage: python main.py [path]")
    else:
        main(argv[1])