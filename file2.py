def hello_world():
    print("Hello World")
    with open('world.txt', 'w') as f:
        f.write('HELLO WORLD')
    return "Hello World"