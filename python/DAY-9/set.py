set1=set()                  #inbuilt collection 
set1.add(1)
set1.add(3)                 #mutable
set1.add(5)
set1.add(2)
print(set1)
set2={8,9,6}
print(set2)
set3=(set1)|(set2)         #union
print(set3)
set4=(set1)&(set3)          #intersection
print(set4)
set5=(set3)-(set1)
print(set5)