my_list=[1,2.5,True,"Harshitaa",[2,4,6,8,10]]
# print(my_list[3][1])
# print(my_list[0]+my_list[1]+my_list[2])
# print (int (str(my_list[1])[2]))

# #list methods
list_1=[1,2,3,4,5,6,7,8,9,10]
list_1.append(11)
# print(list_1)
count_1=list_1.count(6)
# print(count_1)
list_2=list_1.copy()
# print(list_2)
list_1.extend(list_2)
# print(list_1)
# print(list_1.index(11))
num=1
list_1.insert(num,"yoyo")
# print(list_1)
list_2=list_1.pop(2)
# print(list_1)
# print(list_2)
list_1.remove(3)
# print(list_1)
list_1.clear()
# print(list_1)
list_1.reverse()
# print(list_1)

li=["a","z","r","t","g"]
li.sort()
print(li)
li.sort(reverse=True)
print(li)




#tuple
sample_tuple=(1,2,1,4,5,6,7,8)
# print(sample_tuple.count(1))
# print(sample_tuple.index(8))