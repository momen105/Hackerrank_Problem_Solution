def get_average_mark(student_marks, query_name):
    marks = student_marks.get(query_name)
    average = sum(marks) / len(marks)
    print("%.2f" % average)


if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # ________________another answer_____________________
    # marks = student_marks.get(query_name)
    # print("%.2f", sum(marks) / len(marks))

    get_average_mark(student_marks, query_name)
