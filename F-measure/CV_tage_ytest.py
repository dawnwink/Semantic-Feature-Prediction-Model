__author__ = 'user'
version = 'CV\Eclipse UI'
#project_list = ['1','2','3','4','5']
F = []
for pro in range(100):
    tage = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s\tage_%s.txt'%(version,pro)).readlines()
    for i in range(len(tage)):
        tage[i] = int(tage[i].replace('\n',''))
    #print tage
    y_test = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s\y_test_%s.txt'%(version,pro)).readlines()
    for i in range(len(y_test)):
        y_test[i] = int(y_test[i].replace('\n',''))
    #print y_test
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
    #print num
    #print res
    output = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s\yres.txt'%version, 'w')
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
    #print precision(2)
    try:
        F0 = 2*(precision(0)*recall(0))/(precision(0)+recall(0))
    except:
        F0 = 0
    try:
        F1 = 2*(precision(1)*recall(1))/(precision(1)+recall(1))
    except:
        F1 = 0
    try:
        F2 = 2*(precision(2)*recall(2))/(precision(2)+recall(2))
    except:
        F2 = 0
    K = (num[0]*F0+num[1]*F1+num[2]*F2)/sum(num)
    F.append(K)
    print pro, F0, F1, F2, K
print 'mean: ', sum(F)/100

