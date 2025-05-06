str = []
stopword = ''
try:
    for line in iter(input, stopword):
        str.append(line)
except:
    pass
for i in str:
    if i[-2:] == '11' or i[-2:] == '12' or i[-2:] == '13':
        print(i+'th')
    elif i[-1] =='1':
        print(i+'st')
    elif i[-1] == '2':
        print(i+'nd')
    elif i[-1] == '3':
        print(i+'rd')
    else:
        print(i+'th')

