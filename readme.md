# pyzunfinity
VOICEVOXのキャラクターがマルコフ連鎖で様々なことをしゃべります。
## セットアップ
### コンソール
```
$ pip install MeCab simpleaudio
```
### コード
- 冒頭のaddr変数を、VOICEVOXのサーバー・ポート設定に応じて変えてください
- 冒頭のspeaker変数を、[VOICEVOX API](http://127.0.0.1:50021/speakers)からずんだもん、または好みのキャラの番号に変えてください
## 使い方
```
$ python main.py [path]
```
pathには喋らせる内容を入れたテキストファイルパスを入れてください
サンプルとしてGoogleへの愚痴とか書いたtextがあるのでそちらをご利用ください
## 止め方
コンソールでCtrl+Cで強制終了