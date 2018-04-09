import jieba
import time
import jieba.posseg as seg


def process(problem):
    """
    This function used to abstract the query information in problem
    :param problem: string, the problem of user asked. For example: "我想请问一下，糖尿病的治疗费用为多少"
    :return:
        problem: string, the abstract of the asking problem. For example: "我想请问一下，ij的治疗ik为多少"
        diseases: string list, a list of disease that the user have noticed. For example: "糖尿病"
        relationships: string list, a list of the wanted known information about the diseases: "费用"
    """
    result = seg.cut(problem)
    diseases = []
    relationships = []
    for word, flag in result:
        if flag == "ij":
            diseases.append(word)
            problem = problem.replace(word, "ij")
        elif flag == "ik":
            problem = problem.replace(word, "ik")
            relationships.append(word)
    return problem, diseases, relationships


# 读取并生成同义词表
def generate_sim_words(path="./data/同义词.txt"):
    file = open(path)
    lines = file.readlines()
    sim_dict = {}
    for line in lines:
        if ';' in line:
            word_seg = line.strip("\n").split(';')

            relationship = ""
            for i in range(0, len(word_seg)):
                relationship += word_seg[i].split(" ")[0]
            all_words = []
            for i in range(0, len(word_seg)):
                words = word_seg[i].split(" ")
                all_words.append(words)
            word = ""
            if len(all_words) == 2:
                for pre_word in all_words[0]:
                    for back_word in all_words[1]:
                        sim_dict[pre_word + back_word] = relationship
            elif len(all_words) == 3:
                for pre_word in all_words[0]:
                    for mid_word in all_words[1]:
                        for back_word in all_words[2]:
                            sim_dict[pre_word + mid_word + back_word] = relationship
        elif line:
            words = line.strip("\n").split(" ")
            for word in words:
                sim_dict[word] = words[0]
    return sim_dict


def generate_relationships_file(path="./data/my_dictionary/relationship_dictionary.txt"):
    file = open(path, "w")
    sim_dict = generate_sim_words()
    for key in sim_dict.keys():
        file.write("%s 1000 ik\n" % key)