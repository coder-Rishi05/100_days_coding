li = [20,40,5,60,90]

for i in li:
    print(i, li)

# explicit iterable object

it = iter(li)

while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break

print("completed")

