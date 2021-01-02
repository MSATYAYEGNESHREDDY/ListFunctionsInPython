#CREATING LIST 
list=[524,'RAJU','CSE',83.5]
print(type(list))
print('LIST IS {0} \n'.format(list))

list1=[10,20,1,2,3,4,50,60,]
print(type(list))
print('LIST1 IS {0}'.format(list1))

#CHANGING ELEMENT IN LIST
list1[6]=5
print('LIST1 VALUES AFTER CHANGING AN ELEMENT AT  INDEX POSITION 6 IS {0} \n'.format(list1))

#SLICING OF LIST1
print('silicing list1 values from index 0 to 5 is {0}'.format(list1[0:5]))
print('silicing list1 values to get last element in list is {0}\n'.format(list1[-1:]))

#EXISTENCE OF ELEMENT IN LIST
if 60 in list1:
    print('{0} IS FOUND IN THE LIST \n'.format(60))
else:
    print('{0} is found in the list \n'.format(60))

#FINDING THE LENGTH OF LIST 
list_length=len(list1)
print('LENGTH OF LIST 1 IS {0} \n'.format(list_length))

#ADDING ELEMENT IN LIST
#METHOD 1
#APPEND METHOD
list.append('FIRST CLASS')
print('list value after append is {0} \n'.format(list))
#METHOD 2
#INSERT METHOD
list1.insert(1,0)
print('THE LIST1 VALUE AFTER INSERTION AT INDEX 1 is{0}\n'.format(list1))

#REMOVING ELEMENT FROM LIST
#METHOD 1
#REMOVE 
list2=[1,2,3,4,5,6]
print('The list2 is - {0}'.format(list2))
list2.remove(6)
print('The list after removing 6 is - {0}'.format(list2))
#METHOD 2
#POP
list2.pop()
print('The list after pop is - {0}'.format(list2))
#METHOD 3
#POPING ELEMENT WITH INDEX
list2.pop(3)
print('The list after pop with index 3 is - {0}'.format(list2))
#METHOD 4
#CLEAR
list2.clear()
print('The list after clear is - {0} \n'.format(list2))
#METHOD 5
#DELETE
#del list2
#print('The list after del keyword used is - {0}'.format(list2))

#COUNTING THE NUMBER OF TIME A VALUE APPEARS IN LIST
list3=[1,2,3,4,5,6,5,5,2,4,6]
print('list 3 value is {0}'.format(list3))
print('The value 5 appears {0} times in the list 3 \n'.format(list3.count(5)))

#EXTENDING THE LIST
list4=[4,5,9,10,2]
print('the value of list4 is {0}'.format(list4))
list3.extend(list4) 
print('the value of list3 after extending is{0}\n'.format(list3))

#FINDING THE INDEX OF A VALUE IN LIST
print('THE INDEX OF THE VALUE 9 IN LIST3 IS {0} \n'.format(list3.index(9)))

#FINDING MAXIMUM AND MINIMUM VALUE IN LIST 
print('The maximum value in the list3 is  {0} '.format(max(list3)))
print('The minimum value in the list3 is {0} \n' .format(min(list3))) 

#REVERSING OF A LIST
list3.reverse()
print('Reverse of the list3 is  {0} \n'.format(list3))

#SORTING OF VALUES IN LIST
#ASCENDING ORDER
list5 = [12, 2, 5, 90, 30, 40, 3]
print('The list is  {0}'.format(list5))
list5.sort()
print('Ascending order of the list5 is  {0}'.format(list5))
#DECREASING ORDER
list5.sort(reverse=True)
print('Decreasing order of the list5 is  {0} \n'.format(list5))

#CREATING NESTED LIST
nested_list=["abcd",[1,2,3,4,5,6]]
print('NESTED LIST  is {0}'.format(nested_list))

#ACCESSING NESTED LIST BY INDEX
print('NESTED LIST VALUE AT INDEX 0 is {0}'.format(nested_list[0]))
print('NESTED LIST VALUE AT INDEX 1 is {0}'.format(nested_list[1]))
print('NESTED LIST VALUE AT INDEX 0 , 0 is {0}'.format(nested_list[0][0]))
print('NESTED LIST VALUE AT INDEX 0 , 1 is {0}'.format(nested_list[0][1]))
print('NESTED LIST VALUE AT INDEX 1 , 0 is {0}'.format(nested_list[1][0]))
print('NESTED LIST VALUE AT INDEX 1 , 1 is {0}\n'.format(nested_list[1][1]))

#UNPACKING LIST
print('UNPACKING THE LIST')
for element in nested_list:
    print(element)
    for subelement in element:
        print(subelement)
        
        





