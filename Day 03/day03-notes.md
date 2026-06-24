'''
datatypes

--------

int

float

num_2=7.835
num=80.90
print(num//9)


strings

-------
-->string is squence of char that are enclosed in '',"","""
--->str is immutable

concatination
----------

-->here,the (+) operator act as to concatinate more than 2 string......
eg:
so="python"
any=" is a language"
print(so+any)


indexing
--------

--->this is used to access the particular char in the string by pass index position value...

-->index start from 0...
-->we have negative indexing to count position from last to first...

so="python is alanguage
print(so[-3])
print(so[5])


methods
-------

1.replace
---------
-->this method is used to change any substring in that particular string..

syntax-->varible_name.replace("old string","new string",count
eg:-
so="python is language
print(so.replace("python",java))

eg:-
so="python is language
print(so.replace("a","A"))

2.join()
-------
-->this method used to add new substring after each char in the string...
syntax-->"string".join(varible_name)
eg:-
 so="pyhton is a language"
 print("-".join(so))

3.split()

----------
--->this method can divide the string into different index into list,based on the string pass by us....

syntax-->variable_name.split('substring')

eg:-
so="pyhton is a language"
 print(so.split("is")

 4.count()
---------
-->used to count the substring in the particular string also specify the index position
syntax-->variable_name.count("substring",strt index,ending index)
eg:-
  so="pyhton is a language"
 print(so.count("a",0,12))



 string built in functions

 ----------
 1.len():

 --->this will find the length of the string,which is number char present in the that string.

 eg:-
   so="pyhton is a language"
 print(len(so))

max():
------
-->will get the max charactor in the string.
