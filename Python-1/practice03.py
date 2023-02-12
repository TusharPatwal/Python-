# lists and functions of list

l1 = ['apple', 'banana', 'cherry']
print(l1)

# concatenation of two lists
l2 = ['kiwi' , 2,4,5,2]
print(l1+l2)

# max in list
lst = [1,2,3,4,5,6,7,7,8,5,3]
print(max(lst))


# min in list
print(min(lst))

# length of list
print(len(lst))

# sum of list
print(sum(lst))

# append in list
lst.append(6)
print(lst)

# extend in list
l1.extend(l2)
print(l1)

# count in list
print(lst.count(5))

# remove in list
print(lst.remove(5))
print(lst)

# pop in list
lst.pop(0)
print(lst)

# index in list
print(lst.index(4))

# insert in list
lst.insert(0, 55)
print(lst)

# reverse the list
lst.reverse()
print(lst)

# sort the list
lst.sort()
print(lst)