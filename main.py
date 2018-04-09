import query
import preprocess
from test import sim_dict


def pre_dict(sentence, userId):
    """

    :param sentence:
    :param userId:
    :return:
    """
    answer = []
    problem, diseases, relationships = preprocess.process(sentence)
    print(diseases, relationships, [sim_dict[relationship] for relationship in relationships])
    if diseases:
        for disease in diseases:
            if relationships:
                for relationship in relationships:
                    # print(relationship)
                    answer.append(query.disease_query(disease, sim_dict[relationship]))
            else:

                answer.append("请确认你要查询的疾病的相关信息，我们提供是否医保,宜吃食物,费用,常用药品,挂号科室,相关疾病,常见并发症,"
                              "忌吃食物,治疗方式,忌吃,宜吃,菜谱,常见症状,所属科室,常用检查,叫作,相关检查,好发人群,简介,提示,护理,别名等21项信息的查询 ")
        answer = "\n".join(answer)
    else:
        call_sentence = ["打开智能医疗助手", "进入智能医疗助手", "打开医疗助手", "进入医疗助手"]
        if sentence in call_sentence:
            answer = "欢迎使用智能医疗助手，我能回答你关于疾病的相关问题！"
        else:
            answer = query.normal_query(sentence, userId)
    print(answer)
    return answer
