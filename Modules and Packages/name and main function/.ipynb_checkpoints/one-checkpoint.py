def func():
    print("func() in one.py")

print("Always run ths part of one.py")

if __name__ == "__main__":
    print("will be executed when one.py is being run directly")
else:
    print("will be executed when one.py is being imported into another module")