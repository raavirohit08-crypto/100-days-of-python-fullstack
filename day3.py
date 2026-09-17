'''
pop (procedure Oriented programming)--> Dividing the entire code into
blocks-->procedures-->functions(def)
Functions-->A reusable block of code (A block of statements which perform a specific task)

syntax:

def <funcname>(parameters): #funs defn
   """DOc String"""
   statement(s)...
   ........          #body of funs
   return value(s)...
fname(args) #func call

#simple scenario to understand

def add(a,b):
    """Addition funcction"""
    c=a+b
    return c
print(add(4,6))
c,d='bharat',' ''shankar'
print(add(c,d))
e,f=map(str,input("enter the values").split(','))
print(add(e,f))
print(add[1,2,3,4],[4,6,7])


#variable length arguments-->*args we can pass any number of positional
#arguments-->data will be stored in tuple...()

def sample(*a):
    print(a)
    print(type(a))
sample()
sample(2,3,4,5)
sample('codegnan',[2,3],2+5j)

marks=[20,15,25,18]
sample(marks)
sample(*marks)
*a,b,c=12,'code','poll',23,4,9
print(a)
print(b)
print(c)

def add(*a):
    print(a)
    result=0
    for i in a:
        if type(i) in [int,float]:
            result=result+i
    return result
print(add(2,3,4))
print(add(2,'shankar',3,4))


#keyword arguments-->we can pass the name for the arguments
def batch(name,age,place):
    "keyword argument usage"
    print(f'{name} is in {place} and is {age} years')
batch('codgnan',1,'vizag')
batch(place='hyderabad',name='codegnan',age=1)

print(4,5)
print(4,5,sep=':')#here keyword argument is sep and we are changing
#the default value for sep
'''
#keyword varible length arguments(**kwargs)-->Any number of
#keyword arguments,data is stored in dictionary

def batch(**a):
    "keyword variable length argument usage"
    print(a)
    print(type(a))
batch(name="bharat",age=21,place="vizag",branch="cse")

data={'names':['shankar','varma'],'place':['vizag','hyd']}

data.update({'batch':'PFS-VSP-004'})
batch(**data)

























