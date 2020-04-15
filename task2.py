
a = {1}
b = {2 }
print(a)
print(b)
a.update([7,8,9,1,2,3,4,5,0])
b.update([4,5,6,7,8])
print(a)
print(b)
#subset
print(a.issubset(b))
#disjiont
print(a.isdisjoint(b))
#remove
a.remove(8)
print(a)
#discard
a.discard(0)
print(a)

#union

c =  a.union(b)
print(c)
