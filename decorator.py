def func_1(a):
    print("start func_1")
    yield "Hi"
    yield "Hello"

def func_2(b):
    print("start func_2")
    yield "It's func_2"
    yield "Bye"

def func_3(a, b):
    print("start task_4")
    yield "It's func_3"
    yield "Bye"

def test():
    yield func_1(2)
    yield func_2(2)
    yield func_3(2, 3)

for i in test():
    print("next")
    for j in i:
        print(j)
