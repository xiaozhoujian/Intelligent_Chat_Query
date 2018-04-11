import glob
import jieba
import os
import jieba.posseg as seg


def process(problem):
    """
    This function is used to abstract the query information in problem
    :param problem: string, the problem of user asked. For example: "我想请问一下，糖尿病的治疗费用为多少"
    :return:
        problem: string, the abstract of the asking problem. For example: "我想请问一下，ij的治疗费用为多少"
        diseases: string list, a list of disease that the user have noticed. For example: ["糖尿病"]
        relationships: string list, a list of the wanted known information about the diseases: ["费用"]
    """
    result = seg.cut(problem)
    diseases = []
    relationships = []
    for word, flag in result:
        if flag == "ij":
            diseases.append(word)
            problem = problem.replace(word, "ij")
        elif flag == "ik":
            # problem = problem.replace(word, "ik")
            relationships.append(word)
    return problem, diseases, relationships


# 读取并生成同义词表
def generate_sim_words(path="./data/同义词.txt"):
    """
    This function is used to generate the similar word of relationships
    :param path: string, the path of dictionary of "similar word" text file
    :return: dictionary, contains the similar word of relationships
    """
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
    """
    This function is used to generate the custom relationship dictionary of jieba.
    :param path: string, the file path of custom relationship dictionary
    :return:
    """
    file = open(path, "w")
    sim_dict = generate_sim_words()
    for key in sim_dict.keys():
        file.write("%s 1000 ik\n" % key)


def load_dict():
    """
    This function is used to load the pre-defined dictionary file in jieba.
    :return:
    """
    cur_path = os.path.split(os.path.realpath(__file__))[0]
    disease_path = cur_path + "/data/my_dictionary/disease.txt"
    relationship_path = cur_path + "/data/my_dictionary/relationship_dictionary.txt"
    jieba.load_userdict(disease_path)
    jieba.load_userdict(relationship_path)


def generate_train_text(path="./data/question/disease", write_path="./data/fast_text_train.txt"):
    """
    This function is used to generate the train data of fasttext according to the pre-generated question of diseases.
    :param path: string, the path of pre-generated disease questions.
    :param write_path: string, the path to save the fasttext training data
    :return: string, the path of fasttext training data
    """
    load_dict()
    if path[-1] == "/":
        path += "*"
    else:
        path += "/*"
    paths = glob.glob(path)
    write_file = open(write_path, "w")
    write_line = set()
    for p in paths:
        file = open(p)
        label_name = p.split("/")[-1].replace(".txt", "")
        lines = [line.strip() for line in file.readlines()]
        for line in lines:
            seg_result = seg.cut(line)
            fasttext_line = ""
            for word in seg_result:
                fasttext_line += word.word + " "

            fasttext_line += "__label__" + label_name + "\n"
            write_line.add(fasttext_line)
    write_line = "".join(list(write_line))
    write_file.write(write_line)
    return write_path

