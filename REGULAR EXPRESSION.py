import re
txt ="Use of python in Machine Learning"
x=re.search("^Use.*Learning$",txt)#$ either use it or not
if (x):
    print("YES!We have a match")
else:
    print("NO match")



txt = "Use of python in Machine Learning"
x = re.findall("in", txt)  # $ either use it or not
print(x)

txt="Python is one of the most popular languages"
searchObj=re.search("\s",txt)
print("The first white space character is loacated")