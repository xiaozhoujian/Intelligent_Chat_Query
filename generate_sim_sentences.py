import itertools


def generate_sentences(front_end_combo, front_combo, sim_words):
    sentences = []
    for combo in front_end_combo:
        front_words = combo[0]
        end_words = combo[1]
        for begin in front_words:
            for mid in sim_words:
                for end in end_words:
                    sentence = begin + mid + end
                    sentences.append(sentence)
    if front_combo:
        for pre_word in front_combo:
            for mid in sim_words:
                sentences.append(pre_word + mid)
    print(len(sentences))
    # print(sentences)
    write_content = "\n".join(sentences)
    return write_content


def combine_words(sim_words):
    """
    This function is used to generate all possible sentences according to the list of words
    :param sim_words: string list, a list of possible words,
                    for example: ["", "大概", "大约"], ["是", "需要"], ["多少", "多少钱", "多少钱左右"]
    :return: string list, all possible sentences according to the list of sim_words
    """
    first = sim_words[0]
    sim_words = sim_words[1:]
    for words in sim_words:
        first = [i+j for i, j in list(itertools.product(first, words))]
    # print(len(first))
    return first


def generate_introduction():
    front_end_combo = [[["请", "麻烦"], ["一下ij", "一下ij是怎样的一种病", "一下ij是一种怎样的疾病", "一下ij是怎样的一种疾病", "一下ij是一种怎样的病", "一下ij是怎样的一种病", "一下ij是怎样的一种疾病"]],
                       [["可以"], ["一下ij吗", "一下ij是怎样的一种病吗", "一下ij是一种怎样的病吗", "一下ij是一种怎样的疾病吗", "一下ij是怎样的一种疾病吗", "一下ij是怎样的一种病吗", "一下ij是怎样的一种疾病吗"]]]
    sim_words = ["介绍", "讲解", "讲述", "详述", "概述", "简述", "解说", "说明", "简单介绍", "简要概括", "简要地描述"]

    front_combo = ["请作关于ij的"]

    write_content = generate_sentences(front_end_combo, front_combo, sim_words)
    write_content += "我想了解一下ij"
    path = "./data/question/简介.txt"
    return path, write_content


def generate_heal_method():
    front_end_combo = [[["ij的"], ["有", "有哪些", "是什么"]]]
    front_combo = ["ij有哪些", "ij有多少种", "ij存在哪些", "ij存在多少种", "ij有几种",
                   "ij患者一般要接受怎样的", "ij病人一般要接受怎样的", "ij病患一般要接受怎样的", "ij病患者一般要接受怎样的"]

    sim_words = ["治疗方式", " 治疗手段", "治疗方法", "治疗策略", "治疗方针",
                 "治病方式", " 治病手段", "治病方法", "治病策略", "治病方针",
                 "医治方式", " 医治手段", "医治方法", "医治策略", "医治方针",
                 "医疗方式", " 医疗手段", "医疗方法", "医疗策略", "医疗方针",
                 "诊治方式", " 诊治手段", "诊治方法", "诊治策略", "诊治方针"]
    write_content = generate_sentences(front_end_combo, front_combo, sim_words)
    path = "./data/question/治疗方式.txt"
    return path, write_content


def generate_inspection():
    front_end_combo = [[["ij"], ["有", "有哪些", "方式有", "方法有", "手段有", "方式有哪些", "方法有哪些", "手段有哪些"]],
                       [["ij有哪些"], ["方法", "方式", "手段"]]]
    front_combo = ["ij患者要接受哪些", "ij病人要接受哪些", "ij病患要接受哪些", "ij病患者要接受哪些",
                   "ij患者一般要接受哪些", "ij病人一般要接受哪些", "ij病患一般要接受哪些", "ij病患者一般要接受哪些",
                   "ij有哪些", "ij一般有"]
    sim_words = ["常用的检查", "常规的检查", "常见的检查"]
    write_content = generate_sentences(front_end_combo, front_combo, sim_words)
    front_end_combo_2 = [[["有哪些", "如何", "哪种", "进行哪种", "通过哪些", "什么"],
                          ["可以检查出是否ij了", "可以检测出是否ij了", "可以检查是否得了ij", "可以检测是否得了ij", "能检查出是否ij了", "可以检测出是否ij了", "能检查是否得了ij", "能检测是否得了ij"]],
                         [["与ij相关的", "与ij有关的"], ["有", "手段有", "方式有", "方法有", "手段有哪些", "方式有哪些", "方法有哪些", "有哪些"]]]
    sim_words_2 = ["检查", "常用的检查", "常规的检查", "常见的检查"]
    write_content2 = generate_sentences(front_end_combo_2, [], sim_words_2)
    write_content += "\n" + write_content2
    path = "./data/question/常用检查.txt"
    return path, write_content


def generate_health_care():
    front_end_combo = [[["ij属于", "ij是"], ["疾病吗", "病吗", "范围吗"]],
                       [["ij在"], ["范围内吗", "报销范围内吗", "中可以报销吗", "中能够报销吗"]],
                       [combine_words([["ij"], ["患者", "病人", "病患", "病患者"], ["能够", "可以"], ["使用", "享受", "享用"]]), ["吗"]],
                       [combine_words([["ij"], ["患者", "病人", "病患", "病患者"], ["属于"]]), ["对象吗", "可报销对象吗"]],
                       [["ij是否属于", "ij是否是"], ["疾病", "病"]]]
    front_combo = []
    sim_words = ["医保", "医疗保险", "医疗保障", "疾病医疗保险", "社会医疗保险"]
    write_content = generate_sentences(front_end_combo, front_combo, sim_words)
    path = "./data/question//是否医保.txt"
    return path, write_content


def generate_dish():
    front_end_combo = [[combine_words([["ij", "ij了", "ij患者", "ij病人", "ij病患", "ij病患者"], ["吃", "适合吃", "应该吃", "应当吃"],
                                       ["些什么", "什么", "怎样的", "哪些"]]), ["", "好", "比较好", "会比较好"]]]
    front_combo = []
    sim_words = ["菜式", "菜肴"]
    write_content = generate_sentences(front_end_combo, front_combo, sim_words)
    path = "./data/question//菜谱.txt"
    return path, write_content


def generate_high_risk_group():
    sentences = "\n".join(combine_words([["ij的"], ["高发", "好发", "高危"], ["人群", "群体", "群众"], ["有", "有哪些", "有哪一些"]]))
    # write_content = generate_sentences(front_end_combo, front_combo, sim_words)
    sentences += "\n" + "\n".join(combine_words([["ij"], ["常见", "高发", "好发", "常出现"], ["在", "于"], ["哪些", "哪一种", "那一些", "哪类", "哪一类", "什么样的", "哪种"],
                                                 ["人", "人群", "群体", "群众"], ["", "身上"]]))
    sentences += "\n" + "\n".join(combine_words([["哪些", "那一些", "哪类", "哪一类", "什么样的", "哪种", "哪一种"], ["人", "人群", "群体", "群众"],
                                                 ["易得", "容易得", "易患", "容易患"], ["ij"]]))

    path = "./data/question//好发人群.txt"
    return path, sentences


def generate_cost():
    front_end_combo = [[["ij的"], combine_words([["", "大概", "大约"], ["是", "需要"], ["多少", "多少钱", "多少钱左右"]])]]
    front_combo = []
    sim_words = combine_words([["", "治疗", "治病", "医治", "医疗", "诊治", "看病"], ["费用", "开销", "支出", "开支", "花费", "花销"]])
    write_content = generate_sentences(front_end_combo, front_combo, sim_words)
    extra_content = "\n".join(combine_words([["治疗", "医治", "医疗", "诊治", ""], ["好ij", "ij"], ["要", "需要", "得"], ["花", "花费"],
                                             ["多少", "多少钱", "多少钱左右"]]))
    write_content += "\n" + extra_content
    path = "./data/question//费用.txt"
    return path, write_content


def generate_complication():
    sentences = combine_words([["ij"], ["容易", "可能", "可能会", "有可能", "或许会", "也许会"], ["导致", "造成", "引致", "引发", "诱发"],
                               ["哪些", "什么", "哪一些"], ["病", "疾病", "并发症", "常见并发症", "常见的并发症"]])

    # print(len(sentences))
    sentences = "\n".join(sentences)
    sentences += "\n" + "\n".join(combine_words([["ij"], ["病人", "患者", "病患", "病患者"], ["容易", "可能", "可能会", "有可能", "或许会", "也许会"],
                                                 ["得"], ["哪些", "什么", "哪一些"], ["病", "疾病", "并发症", "常见并发症", "常见的并发症"]]))
    sentences += "\n" + "\n".join(combine_words([["ij"], ["有哪些", "有什么"], ["并发症", "常见并发症", "常见的并发症"]]))
    sentences += "\n" + "\n".join(combine_words([["ij的"], ["并发症", "常见并发症", "常见的并发症"], ["有哪些", "有什么"]]))
    path = "./data/question//常见并发症.txt"
    return path, sentences


def generate_symptom():
    sentences = combine_words([["ij"], ["容易", "可能", "可能会", "有可能", "或许会", "也许会"], ["导致", "造成", "引致", "引发", "诱发"],
                               ["哪些", "什么", "哪一些"], ["病征", "症状", "副作用", "常见副作用", "常见症状", "常见病征"]])
    print(len(sentences))
    sentences = "\n".join(sentences)
    sentences += "\n" + "\n".join(combine_words([["ij"], ["病人", "患者", "病患", "病患者"], ["容易", "可能", "可能会", "有可能", "或许会", "也许会"],
                                                 ["出现"], ["哪些", "什么", "哪一些"], ["病征", "症状", "副作用", "常见副作用", "常见症状", "常见病征"]]))
    sentences += "\n" + "\n".join(combine_words([["ij"], ["有哪些", "有什么"], ["病征", "症状", "副作用", "常见副作用", "常见症状", "常见病征"]]))
    sentences += "\n" + "\n".join(combine_words([["ij的"], ["病征", "症状", "副作用", "常见副作用", "常见症状", "常见病征"], ["有哪些", "有什么"]]))
    path = "./data/question//常见症状.txt"
    return path, sentences


def generate_related_disease():
    sentences = "\n".join(combine_words([["跟", "与", "和"], ["ij"], ["有关", "相关"], ["的"], ["病", "疾病"], ["有", "有哪些", "有哪一些"]]))
    sentences += "\n" + "\n".join(combine_words([["ij"], ["具体", "一般", "", "经常", "常常", "常"], ["跟", "与", "和"], ["哪些", "什么", "哪一些"],
                                                 ["病", "疾病"], ["有关", "相关"]]))
    sentences += "\n" + "\n".join(combine_words([["ij"], ["一般", ""], ["存在", "有"], ["哪些", "什么", "哪一些"],
                                                 ["有关", "相关"], ["病", "疾病"]]))
    sentences += "\n" + "\n".join(combine_words([["ij的"], ["有关", "相关"], ["病", "疾病"], ["一般", ""], ["有"],
                                                 ["", "哪些", "什么", "哪一些"]]))
    path = "./data/question//相关疾病.txt"
    return path, sentences


def generate_departments():
    sentences = "\n".join(combine_words([["ij"], ["属于", "归属于", "从属于", "隶属于"], ["哪个", "哪一个"], ["科室", "科"]]))
    sentences += "\n" + "\n".join(combine_words([["ij"], ["", "患者", "病人", "病患", "病患者"], ["应", "应该", "应当"], ["去", "到"],
                                                 ["哪个", "哪一个"], ["科室", "科"], ["看", "看病", "诊治", "就医", "治病", "求医", "医治", "挂号", "就诊"]]))
    path = "./data/question//所属科室.txt"
    return path, sentences


def generate_another_name():
    sentences = "\n".join(combine_words([["ij"], ["", "通常", "一般", "常", "经常", "常常", "往往", "平常"], ["", "被", "又被"],
                                         ["叫", "称作", "叫做", "叫作", "称为"], ["什么"], ["呢", ""]]))
    sentences += "\n" + "\n".join(combine_words([["ij的"], ["别名", "别称", "常称", "代称", "惯称"], ["", "通常", "一般"], ["有", "是", "有哪些", "有哪一些", "是什么"]]))
    sentences += "\n" + "\n".join(combine_words([["ij"], ["", "通常", "一般"], ["有哪些", "有哪一些"], ["别名", "别称", "常称", "代称", "惯称"], ["呢", ""]]))
    path = "./data/question//别名.txt"
    return path, sentences


def generate_frequent_drug():
    sentences = "\n".join(combine_words([["ij"], ["", "患者", "病人", "病患", "病患者"], ["一般", "通常", "常常", "常", "往往", "经常", "不时", ""],
                                         ["", "要", "需要", "会"], ["使用", "用"], ["到", ""], ["哪些", "哪种", "什么"], ["药", "药品", "药物", "药剂", "处方药"]]))
    sentences += "\n" + "\n".join(combine_words([["ij的"], ["常用", "常见"], ["药", "药品", "药物", "药剂", "处方药"],
                                                 ["", "通常", "一般"], ["有", "是", "有哪些", "有哪一些", "是什么"]]))
    sentences += "\n" + "\n".join(combine_words([["ij"], ["", "通常", "一般"], ["有哪些", "有哪一些"], ["常用", "常见"], ["药", "药品", "药物", "药剂", "处方药"]]))
    sentences += "\n" + "\n".join(combine_words([["", "通常", "一般"], ["有哪些", "有哪一些"], ["ij"], ["常用", "常见"], ["药", "药品", "药物", "药剂", "处方药"]]))
    path = "./data/question//常用药品.txt"
    return path, sentences


def generate_should_eat():
    sentences = "\n".join(combine_words([["ij", "ij了", "ij患者", "ij病人", "ij病患", "ij病患者", "得了ij"],
                                         ["", "应", "适合", "应该", "应当", "可以", "最好", "适宜"],
                                         ["吃", "吃些"], ["什么", "什么食物"], ["", "好", "比较好", "会比较好"]]))
    sentences += "\n" + "\n".join(combine_words([["", "有"], ["哪些", "什么"], ["东西", "食物"], ["适合", "适宜", "是"],
                                                 ["ij患者", "ij病人", "ij病患", "ij病患者"], ["吃"]]))
    # print(len(sentences))
    path = "./data/question//宜吃.txt"
    return path, sentences


def generate_should_not_eat():
    sentences = "\n".join(combine_words([["ij", "ij了", "ij患者", "ij病人", "ij病患", "ij病患者", "得了ij"],
                                         ["不应", "不适合", "不应该", "不应当", "不可以", "不好", "不适宜", "忌", "不能"],
                                         ["吃", "吃些"], ["什么", "什么食物", "什么东西"]]))
    sentences += "\n" + "\n".join(combine_words([["", "有"], ["哪些", "什么"], ["东西", "食物"], ["是"], ["ij患者", "ij病人", "ij病患", "ij病患者"],
                                                 ["不应", "不适合", "不应该", "不应当", "不可以", "不好", "不适宜", "忌", "不能"], ["吃的"]]))
    path = "./data/question//忌吃.txt"
    return path, sentences


def generate_nurse():
    sentences = "\n".join(combine_words([["ij", "ij了", "得了ij", "ij患者", "ij病人", "ij病患", "ij病患者"], ["有"], ["哪些", "什么"],
                                         ["要", "需要"], ["注意", "留意", "警惕", "特别注意"], ["的", "的吗"]]))
    sentences += "\n" + "\n".join(combine_words([["ij", "ij了", "得了ij", "ij患者", "ij病人", "ij病患", "ij病患者"], ["", "平日", "平时", "平常"],
                                                 ["要", "需要"], ["怎么"], ["护理", "做", "照护", "照顾"], ["", "自己"]]))
    sentences += "\n" + "\n".join(combine_words([["ij", "ij了", "得了ij", "ij患者", "ij病人", "ij病患", "ij病患者"], ["", "平日", "平时", "平常"],
                                                 ["有"], ["哪些", "什么"], ["注意事项"], ["", "吗"]]))
    path = "./data/question//护理.txt"
    return path, sentences


if __name__ == '__main__':
    write_path, content = generate_cost()
    file = open(write_path, "w")
    file.write(content)

