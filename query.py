from py2neo import Graph
import requests
import json


def disease_query(disease, relationship):
    """
    This function is used to make a specific query in neo4j database.
    :param disease: string, the name of disease, for example "糖尿病"
    :param relationship: string, the query relationship about the disease, for example "费用"
    :return: string, answer about the query, for example "糖尿病的费用为糖尿病的费用为：根据不同医院，收费标准不一致，市三甲医院约1000-3000元 "
    """
    graph = Graph("http://localhost:7474/db/data", username="neo4j", password="456897231")
    contents = graph.run("MATCH (n{name:\"%s\"})-[r:%s]-(n2) RETURN n2.name" % (disease, relationship)).data()
    # print(contents)
    # answer = disease + "的" + relationship + "为："
    answer = ""
    if contents:
        for content in contents:
            values = content.values()
            for value in values:
                answer += value + " "
    else:
        answer = "抱歉，我们暂时还没有关于%s的%s这方面的数据" % (disease, relationship)
    return answer


def normal_query(sentence, user_id):
    """

    :param sentence:
    :param user_id:
    :return:
    """
    post_data = {
        "perception": {
            "inputText": {
                "text": sentence
            },
        },
        "userInfo": {
            "apiKey": "29c53744b78a4f9d934e226b8526e6b0",
            "userId": user_id
        }
    }
    post_data = json.dumps(post_data)
    response = requests.post('http://openapi.tuling123.com/openapi/api/v2', data=post_data)
    response = response.json()
    error_code = [5000, 6000, 4000, 4001, 4002, 4003, 4005, 4007, 4100, 4200, 4300, 4400, 4500, 4600, 4602, 7602, 8008]
    if response["intent"]["code"] in error_code:
        return "请求错误，错误代码 %d" % response["intent"]["code"]
    else:
        return response["results"][0]["values"]["text"]

