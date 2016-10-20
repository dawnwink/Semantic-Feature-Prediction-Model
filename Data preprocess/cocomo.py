__author__ = 'user'
import sys

reload(sys)
sys.setdefaultencoding('utf8')

project = 'AspectJ'

txt = open(r'D:\effort-awareness\%s project\timestrap_effort.txt'%project).readlines()
result = []
low = 1.45*3600
high = 41.44*3600
for ele in txt:
    if float(ele)<low:
        result.append(0)
    else:
        if float(ele)>high:
            result.append(2)
        else:
            result.append(1)
rs = open(r'D:\effort-awareness\%s project\COCOMO_output.txt'%project, 'w')
for ele in result:
    rs.writelines(str(ele))
    rs.writelines('\n')