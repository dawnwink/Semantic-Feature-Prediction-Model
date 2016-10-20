__author__ = 'user'
version = 'cross_project\AspectJ'
tage = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s\9 heat map/tage.txt'%version).readlines()
for i in range(len(tage)):
    tage[i] = int(tage[i].replace('\n',''))
print tage
y_test = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s\9 heat map/y_test.txt'%version).readlines()
for i in range(len(y_test)):
    y_test[i] = int(y_test[i].replace('\n',''))
print y_test
y1 = y_test
y2 = tage
res = [[0 for col in range(3)] for row in range(3)]
num = [0] * 3
for i in range(len(y1)):
    if y1[i] == 0:
        num[y1[i]] += 1
        res[0][y2[i]] += 1
    if y1[i] == 1:
        num[y1[i]] += 1
        res[1][y2[i]] += 1
    if y1[i] == 2:
        num[y1[i]] += 1
        res[2][y2[i]] += 1
print num
print res
output = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s\9 heat map/yres.txt'%version, 'w')
for i in range(len(res)):
    for j in range(len(res[i])):
        output.writelines(str(float(res[i][j])/float(num[i])))
        output.writelines(' ')
    output.writelines('\n')
def precision(index):
    pre = float(res[index][index])/(res[0][index]+res[1][index]+res[2][index])
    return pre
def recall(index):
    return float(res[index][index])/num[index]
print precision(0)
F0 = 2*(precision(0)*recall(0))/(precision(0)+recall(0))
F1 = 2*(precision(1)*recall(1))/(precision(1)+recall(1))
F2 = 2*(precision(2)*recall(2))/(precision(2)+recall(2))
F = (num[0]*F0+num[1]*F1+num[2]*F2)/sum(num)
print F0, F1, F2, F