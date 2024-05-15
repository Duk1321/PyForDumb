def merge(dict1, dict2):
    result = {}
    for data in dict1:
        result[data] = dict1[data]
    
    for data in dict2:
        result[data] = dict2[data]
    
    return result 


def total_score(score_dict):
    sum = 0
    for data in score_dict:
        sum += score_dict[data]

    return sum
