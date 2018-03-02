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


if __name__ == '__main__':
    cur_path = os.path.split(os.path.realpath(__file__))[0]
    disease_path = cur_path + "/data/my_dictionary/disease.txt"
    relationship_path = cur_path + "/data/my_dictionary/relationship_dictionary.txt"
    jieba.load_userdict(disease_path)
    jieba.load_userdict(relationship_path)
    app.run(debug=True)
