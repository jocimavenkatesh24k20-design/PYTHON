from collections import defaultdict
'''
a=defaultdict(list)
words=["cat","apple","dog","banana","carrot"]
for w in words:
    a[len(w)].append(w)
print(list(a.values()))
'''
grp_ana=defaultdict(list)
words=["eat","tea","ate","nat","bat","cat"]
for w in words:
    key=''.join(sorted(w))
    grp_ana[key].append(w)
print(list(grp_ana.values()))