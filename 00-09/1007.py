"""
题目描述
成绩分析
成绩与等级之间是这样转换的：
成绩在 90~100 分之间是 A;
成绩在 80~89 分之间是 B;
成绩在 70~79 分之间是 C;
成绩在 60~69 分之间是 D;
成绩在 0~59 分之间是 F。
请你根据成绩计算等级。当然，可能会输入一个错误的值，这时候请输出 "Error!" 。

输入
输入一行一个整数，表示成绩

输出
输出一个字母或者 "Error!" 表示结果。

样例输入
100

样例输出
A
"""
a = int(input())

if 0 <= a <= 59:
    print("F")
elif 60 <= a <= 69:
    print("D")
elif 70 <= a <= 79:
    print("C")
elif 80 <= a <= 89:
    print("B")
elif 90 <= a <= 100:
    print("A")
else:
    print("Error!")

"""
无脑嵌套/字典映射
"""

"""
score = int(input())

# 成绩等级映射
grade_map = {
    (90, 100): "A",
    (80, 89): "B",
    (70, 79): "C",
    (60, 69): "D",
    (0, 59): "F"
}

# 判断成绩等级
for (min_score, max_score), grade in grade_map.items():
    if min_score <= score <= max_score:
        print(grade)
        break
else:
    print("Error!")

"""