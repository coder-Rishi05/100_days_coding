import keyword as kw

kw.kwlist

a =  len(kw.kwlist)
print(a)


# softkeyword
b = kw.softkwlist

print(b)


"""
b = ['_', 'case', 'match', 'type']
why these called softword.

It is because we can use these keyword as variable and class name, 
ex : 
if = 5
print(if)
  if = 5
       ^
SyntaxError: invalid syntax

case = 34
print('val of case',case)
val of case 34

in python we dont have switch case concept in earlier days so match case was created for it.

it is known as keyword when used as special syntax. 



"""




"""def f1():
    return 1
action = f1()

match action:
    case "hello":
        print("Hello learner")
    case 10:
        print("My lucky num is 10 ")
    case 3+4j:
        print("this is a complex number")

    case _: # this is used as default
        print("this is default case trap")

# now here as we are using every soft keyword as keyword now if i try to use them as variable inside this match case block they will not act like normal variable, they will act like hard keyword. 
match = 12


match _ case are used in switch case type syntax.
"""

# type  : it is also a function

type point = tuple[float, float]

p1:point=(3.0,4.0)

type list_of_points=list[point]

mylist:list_of_points=[
    p1
]
print(p1)

print(type(p1))
