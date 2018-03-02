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
