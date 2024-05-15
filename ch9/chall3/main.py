def get_test_score(answer_sheet, student_answers):
    counter = 0
    
    for i in range(0, len(student_answers)):
        if answer_sheet[i] == student_answers[i]:
            counter += 1

    result = (counter / len(answer_sheet)) * 100

    return result