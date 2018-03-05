import jieba
import main
import os
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'OSPA',
        'description': u'This is ospaf-api test',
        'done': False
    },
    {
        'id': 2,
        'title': u'Garvin',
        'description': u'I am garvin',
        'done': False
    }
]


@app.route('/get_answer', methods=['POST'])
def get_answer():
    msg_json = request.json
    if type(msg_json) is str:
        msg_json = json.loads(msg_json)
    sentence = msg_json['message']['text']
    user_id = msg_json["userInfo"]["userId"]
    answer = main.pre_dict(sentence, user_id)
    answer_json = json.dumps({'answer': answer})
    return answer_json


@app.route('/mi_answer', methods=['POST'])
def mi_answer():
    """

    :return:
    """
    msg_json = request.json
    if type(msg_json) is str:
        msg_json = json.loads(msg_json)
    sentence = msg_json["query"]
    user_id = msg_json["session"]["user"]["user_id"]
    answer = main.pre_dict(sentence, user_id)
    return_json = {
      "version": "1.0",  # (string required)
      "session_attributes": {  # (jsobject optional) 持久化的内容可以放这
      },
      "response": {  # (jsobject required)
        "open_mic": False,  # (Boolean optional)，指示客户端是否需要关闭mic, true，打开麦克风；false，关闭麦克风
        "to_speak": {  # (jsobject required, 和directive 二选一，复杂的用directive，简单的用tospeak
          "type": 0,  # (int required) TTS: 0, 1: Audio, 2: ssml
          "text": answer  # (string required)
        },
        "to_display": {  # (jsobject optional)
          "type": 0,  # (int required) plainText: 0, 1: url of html, 2: native ui, 3: widgets
          "text": answer  # (string required)
        },
        # "directives": [  # 例如播放音频, 和tospeak 二选一，复杂的用directive，简单的用tospeak
        # {
        #   "type": "audio",  # (string required) audio, tts
        #   "audio_item": {  # (object optional)
        #     "stream": {   # (object required)
        #       "token": "iiiiiiiiiii",   # (string optional)
        #       "url": "http: #xxxxx.mp3",  # (string required)
        #       "offset_in_milliseconds": 0   # (int optional)
        #     }
        #   }
        # },
        # {
        #   "type": "tts",   # (string required) audio, tts
        #   "tts_item": {  # (object required)
        #       "type": "text",  # (string required), tts type
        #       "text": "xxxx"  # (string optional), tts text
        #   }
        # }
        # ]
      },
      "is_session_end": False  # (boolean required)e
    }
    return_json = json.dumps(return_json)
    return return_json


if __name__ == '__main__':
    cur_path = os.path.split(os.path.realpath(__file__))[0]
    disease_path = cur_path + "/data/my_dictionary/disease.txt"
    relationship_path = cur_path + "/data/my_dictionary/relationship_dictionary.txt"
    jieba.load_userdict(disease_path)
    jieba.load_userdict(relationship_path)
    app.run(debug=True)
