__author__ = 'user'
project = 'birt raw'
issue = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s/issue.txt'%project).readlines()

for i in range(len(issue)):
    issue[i] = issue[i].replace('\n','')
print issue
token = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s/token.txt'%project).readlines()
print token
#it = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s/it.txt'%project, 'w')
#for ele in issue:
#    it.writelines(token[int(ele)-1])
cocomo2 = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s/cocomo2.txt'%project).readlines()
print cocomo2
itv = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s/test.txt'%project).readlines()
print len(itv)
for i in range(len(cocomo2)):
    cocomo2[i] = cocomo2[i].replace('\n','')
s = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s/endata/s/1.txt'%project, 'w')
m = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s/endata/m/2.txt'%project, 'w')
l = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s/endata/l/3.txt'%project, 'w')
print len(cocomo2), len(itv)
for i in range(len(cocomo2)):
    if int(cocomo2[i]) == 0:
        s.writelines(itv[i])
    if int(cocomo2[i]) == 1:
        m.writelines(itv[i])
    if int(cocomo2[i]) == 2:
        l.writelines(itv[i])