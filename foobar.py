for i in range(1, 100 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FooBar", end=" ")
    elif i % 3 == 0:
        print("Foo", end=" ")
    elif i % 5 == 0:
        print("Bar", end=" ")
    else:
        print(i, end=" ")