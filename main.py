#Dictionary
#1
d = {7: 10, 5: 20, 3: 30, 1: 40, 9: 50}
def keypres(x):
  if x in d:
      print('Key exists')
  else:
      print('Key does not exist')
keypres(5)
keypres(2)
#2
d1 = {'a': 150, 'b': 500}
d2 = {'x': 30, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)
#3
dict = {'a1':10,'a2':-89,'a3':988}
print(sum(dict.values()))
#4
p = {1:10, 3:20}
print(p)
p.update({5:30})
print(p)
#5
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
#tuple
#1
tuplex = ("tuple", True, 0.7, 5)
print(tuplex)
#2
tuplex = 1, 3, 5, 7, 9
print(tuplex)
tuplex = 5,
print(tuplex)
#3
tuplex = (0, 2, 4, 6, 8, 1)
print(tuplex)
tuplex = tuplex + (9,)
print(tuplex)
#4
tup = ('p', 'y', 't', 'h', 'o', 'n')
str =  ''.join(tup)
print(str)
#5
tuplex = tuple("helloworld")
print(tuplex)
print(len(tuplex))
#set
#1
day = set()
print(day)
print("\nAdd elements:")
day.add("Saturday,Sunday")
print(day)
day.clear()
#2
number = set([1,3,5,7,9])
print("Original set elements:")
print(number)
print("\nRemove 0 from the set:")
number.discard(4)
print(number)
print("\nRemove 5 from the said set:")
number.discard(3)
print(number)
#3
P = {0,2,4,6,8};
Q = {1,2,3,4,5};
# union
print("Union :", P | Q)
# intersection
print("Intersection :", P & Q)
# difference
print("Difference :", P - Q)
#4
odd = {1,3,5,7,9}
print("Original set of elements:")
print(odd)
print("\nMaximum value:")
print(max(odd))
print("\nMinimum value:")
print(min(odd))
#5
mostfreq = [1,1,2,3,4,4,4,5]
print("\nList:",mostfreq)
ctr = max(set(mostfreq), key = mostfreq.count)
print("\nElement with the highest frequency:",ctr)