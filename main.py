import query
import preprocess
import fasttext
from post_entry import sim_dict, classifier
import jieba.posseg as seg


def cut(texts):
    """
    This function is used to cut a list of texts.
    :param texts: string list, a list of text to be cut, for example ["ij的治疗费用是多少"].
    :return: A list of segmented text, storage as ["ij 的 治疗 费用 是 多少"]
    """
    seg_texts = [seg.cut(text) for text in texts]
    seg_results = []
    for seg_text in seg_texts:
        seg_result = ""
        for word in seg_text:
            # if word.word not in stopwords:
            seg_result += word.word + " "
        seg_results.append(seg_result)
    return seg_results


def pre_dict(sentence, userId):
    """
    This function is used to generate the answer of the specific problem
    :param sentence: string, the sentence of problem, for example: "糖尿病的治疗费用是多少"
    :param userId: int, the Id of user, for example: 1
    :return: string list, a list of answer, for example: ['根据不同医院，收费标准不一致，市三甲医院约1000-3000元']
    """
    answer = []
    problem, diseases, relationships = preprocess.process(sentence)
    # print(diseases, relationships, [sim_dict[relationship] for relationship in relationships])
    if diseases:
        for disease in diseases:
            if len(relationships) <= 1:
                label, prob = fasttext_classifier(problem)
                # print(problem, label, prob)
                if prob > 0.5:
                    answer.append(query.disease_query(disease, label))
                else:
                    file = open("./data/fuzzy_problem.txt", "a")
                    file.write(problem)
                    file.close()
                    answer.append("请确认你要查询的疾病的相关信息，我们提供是否医保,宜吃食物,费用,常用药品,挂号科室,相关疾病,常见并发症,"
                                  "忌吃食物,治疗方式,忌吃,宜吃,菜谱,常见症状,所属科室,常用检查,叫作,相关检查,好发人群,简介,提示,护理,别名等21项信息的查询 ")
            else:
                for relationship in relationships:
                    # print(relationship)
                    answer.append(query.disease_query(disease, sim_dict[relationship]))
        answer = "\n".join(answer)
    else:
        call_sentence = ["打开智能医疗助手", "进入智能医疗助手", "打开医疗助手", "进入医疗助手"]
        if sentence in call_sentence:
            answer = "欢迎使用智能医疗助手，我能回答你关于疾病的相关问题！"
        else:
            answer = query.normal_query(sentence, userId)
    return answer


def fasttext_classifier(sentence):
    """
    This function is used to classify problem
    :param sentence: string, the sentence of un classify problem,for example: "糖尿病的治疗费用是多少"
    :return: tuple, storage two value (label, probability), for example: ("费用", 0.90)
    """
    result = classifier.predict_proba(cut([sentence]))
    return result[0][0]


def train_fasttext(data_path="./data/question/disease", model_path="./data/fasttext.model"):
    """
    This function is used to train the fasttext classifier
    :param data_path: string, the path of training data.
    :param model_path: string, the path to save the trained model of fasttext.
    :return:
    """
    path = preprocess.generate_train_text(data_path)
    fasttext.supervised(path, model_path, label_prefix="__label__")