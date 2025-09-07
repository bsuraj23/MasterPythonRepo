if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = 0.000
    # print("Scores are",scores)
    dictLen = len(student_marks)
    if query_name in student_marks:
        for temp in student_marks[query_name]:
            #  print("temp  is ",temp)
            result = result + temp
        #  print("result in if is ",result)
    # print(result)
    result = result / len(scores)

    print("%.2f" % round(result, 2))
