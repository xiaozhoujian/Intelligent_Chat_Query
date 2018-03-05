import json
import requests


def post():
    url = "http://127.0.0.1:5000/get_answer"
    msg_json = {
      "message": {
        "text": "糖尿病的治疗费用"
      },
      "userInfo": {
        "userId": 1
      }
    }
    response = requests.post(url, json=json.dumps(msg_json))
    print(response.json()['answer'])

if __name__ == '__main__':
    post()

