import query
import preprocess


def pre_dict(sentence, userId):
    """

    :param sentence:
    :param userId:
    :return:
    """
    answer = []
    problem, diseases, relationships = preprocess.process(sentence)
    print(diseases, relationships)
    if diseases:
        for disease in diseases:
            if relationships:
                for relationship in relationships:
                    # print(relationship)
                    answer.append(query.disease_query(disease, relationship))
            else:
                answer.append('''
                         请确认你要查询的疾病的相关信息，我们提供介绍, 正常值, 临床意义, 注意事项, 检查过程, 不良反应, 不适宜人群,
                         费用, 相关疾病, 相关科室, 相关症状, 专科分类, 检查分类, 适用性别, 是否空腹, 提示, 所属科室, 挂号科室,
                         常见症状, 好发人群, 常用检查, 常见并发症, 治疗方式, 常用药品, 护理, 菜谱, 宜吃, 忌吃, 是否医保, 别名,
                         相关检查, 简介, 宜吃食物, 忌吃食物, 分析结果, 正常值（分析结果）, 阴性（分析结果）, 阳性（分析结果）,
                         低于正常值时（分析结果）, 高于正常值时（分析结果）等40项信息的查询
                         ''')
        answer = "\n".join(answer)
    else:
        call_sentence = ["打开智能医疗助手", "进入智能医疗助手", "打开医疗助手", "进入医疗助手"]
        if sentence in call_sentence:
            answer = "欢迎使用智能医疗助手，我能回答你关于疾病的相关问题！"
        else:
            answer = query.normal_query(sentence, userId)
    print(answer)
    return answer
