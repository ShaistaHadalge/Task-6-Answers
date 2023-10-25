#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###you have been given a python list [10,501,22,37,100,999,87,351],you have to create two lists one which will
##have all the even numbers and another one which will have all the odd numbers.


# In[1]:


n=int(input("enter the total number of elements you wish to enter: "))
l=[]
l_e=[]
l_o=[]
for i in range(n):
    ele=int(input("enter the element: "))
    l.append(ele)
print("my list",l)
for i in l:
    if i%2==0:
        l_e.append(i)
    else:
        l_o.append(i)
        
        
        
print("even list ",l_e)
print("odd list ",l_o)


# In[ ]:


###you have been given a python list [10,501,22,37,100,999,87,351],your task is to count all the prime numbers and create 
###list which will have all the prime numbers.


# In[27]:


n=int(input("enter the total number of elements you wish to enter: "))
l=[]
prime=[]
no_prime=[]
for i in range(n):
    ele=int(input("enter the element: "))
    l.append(ele)
print("my list",l)
for i in l:
    if i%2==0:
        no_prime.append(i)
     
    else:
        prime.append(i)
        
print("prime numbers ",prime)
print("non prime numbers ",no_prime)


# In[ ]:


###you have been given a python list [10,501,22,37,100,999,87,351],how many numbers are given in the python list which
###are happy numbers.


# In[47]:


n=int(input("enter the number "))
l=[]
x=n
while x>=10:
    sum=0
    while x>0:
        r=x%10
        sum=sum+(r**2)
        x=x//10
    x=sum
if x==1:
    print(n,"is a happy number")
else:
    print(n,"is not a happy number")


# In[ ]:


###Write a python program to find out the sum of first and last digit of a python program###


# In[49]:


num=int(input("Enter the number : "))
last=num%10
while num!=0:
    first=num%10
    num=num//10
sum=last+first
print("the sum of first and last digit is: ",sum)


# In[ ]:


###you have been given a list of N integers which represents the number of mangoes in a bag each 
###bag has a vairable number of mangoes there are M students in a class your 
###task is to distribute mangoes in such a way that each student gets one bag the difference 
##between number of mangoes in a bag with maximum mangoes and bag 
##with minimum mangoes given to the student is minimum


# In[ ]:


N=[2,3,4,5,6,7,8]
M=[6,5,6,7,5,4,6]


# In[ ]:





# In[ ]:


###you have been given three lists,your task is to find the duplicates in the three lists.write a python program 
###for the same,you can use your own python lists.


# In[54]:


data1=[10,20,30,30,40,90,50]
data2=[2,3,4,4,5,6,7]
data3=[1,2,2,3,3,6,7]
def remove_duplicates(duplist):
    noduplist=[]
    for element in duplist:
        if element not in noduplist:
            noduplist.append(element)
        
    return noduplist
print(remove_duplicates(data1))
print(remove_duplicates(data2))
print(remove_duplicates(data3))


# In[ ]:


###Write a python program to find the first non-repeating elements in a given list of integers###


# In[24]:


my_string=("pythonprogram")
def firstNonRepeatCharacter(my_string):
     chars = {}         
    
for i in my_string:
    if chars.get(i):
        chars[i]+=1
    else:
        chars[i]=1 
for i in my_string:
    if chars[i]==1:
        return i 
return None


print(firstNonRepeatCharacter(my_string))


# In[ ]:


###Write a python program to find a minimum element in a rated and sorted list###


# In[23]:


nums=[1,2,3,4,6,7,8]
max1=nums[0]
for ele in nums:
    if ele>max1:
        max1=ele
min1=nums[0]
for ele in nums:
    if ele<min1:
        min1=ele
print("maximum value is: ",max1 )
print("minimum value is: ",min1)


# In[ ]:


###You have been given a python list [10,20,30,9] and a value of 59.Write the python program to find a triplet in the 
##list whose sum is equal to the given value.


# In[ ]:


list=[10,20,30,9]


# In[ ]:


###Given a list [4,2,-3,1,6],to find if there is a sub list with sum equal to zero.


# In[31]:


size=int(input())
numbers=list(map(int,input().split()))
sublists=[]
result=0
for i in range(0,size+1):
    for j in range (i+1,size+1):
        sublists.append(numbers[i:j])
for i in sublists:
    if sum(i)==0:
        print("yes")
        print(i)
        result=1
    if result==0:
        print("NO")
    
    


# In[ ]:





# In[ ]:




