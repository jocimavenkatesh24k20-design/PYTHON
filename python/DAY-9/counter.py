from collections import Counter     #from collections import Counter => mandatory
a=Counter("encyclopedia")           #counter is called as dictionary it is like a dict formate
print(a)
print(a.most_common(3))             #most common is the keyword it turns like a array formate
print(a.clear())
print(a.most_common(3))