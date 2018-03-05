import json
import requests


def post():
    url = "https://chat.jojen.org/get_answer"
    msg_json = {
      "message": {
        "text": "你好"
      },
      "userInfo": {
        "userId": 1
      }
    }
    response = requests.post(url, json=json.dumps(msg_json))
    print(response.json()['answer'])


def mi_post():
    url = "https://chat.jojen.org/mi_answer"
    msg_json = {
        "version": "1.0",
        "query": "记得，我写给你的情书",
        "session": {  # 请求的上下文信息都放这
            "session_id": "xxxxxxxxxxxxx",
            "application": {
                "app_id": "123"
            },
            "attributes": { # 给第三方APP持久化字段用的
            },
            "user": {
                "user_id": "456",
                "access_token": "yyyyyyyyyyyyy"
            }
        },
        "context": {
           "passport": {}
        },
        "request": {
            "type": 1,
            "request_id": "tttttttttt",
            "timestamp": 452453534523,
            "locale": "zh-CN",
            "intent": {
                "is_direct_wakeup": False  # (boolean optional) 是否为直接唤醒技能，例如让菜谱查一下鱼香肉丝怎么做　这时候会设置为true
            },
            "no_response": False
        }
    }
    response = requests.post(url, json=json.dumps(msg_json))
    print(response)
    print(response.json()['answer'])


if __name__ == '__main__':
    mi_post()

