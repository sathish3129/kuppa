import numpy as np

a = np.array([1, 2,2.9, 3, 4])

print(np.mean(a))
print(np.median(a))

a = np.array([[1, 2], [3, 4]])
print(np.mean(a, axis=0))
x = list(range(5))
print(*x, sep=", ")

def join_(*args):
    rv = ""
    for _string in args:
        rv += '_'+ _string
    return(rv)
print(join_("first", "second", "third"))

def join_2(args):
    rv = ""
    for _string in args:
        rv += '|'+ _string
    return(rv)
print(join_2(["first", "second", "third"]))

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

def greet_me_other(*args, **kwargs):
  for  value in args:
    print("{0} test".format(value))
  greet_me(**kwargs)

  # greet_me(*args)

greet_me_other("a","v", name="yasoob",aname="ayasoob")
print("-------")
greet_me(name="yasoob",aname="ayasoob")
high = None
low = 1
if high == None:
  low, high = 0, low 

print("{0} = {1}".format(low, high))
