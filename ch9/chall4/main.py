def get_test_score(answer_sheet, student_answers):
    name = student_answers[0]
    counter = 0
    for i in range(1, len(student_answers)):
        if student_answers[i] == answer_sheet[i - 1]:
            counter += 1
    
    result = (counter / len(answer_sheet)) * 100

    return name, result