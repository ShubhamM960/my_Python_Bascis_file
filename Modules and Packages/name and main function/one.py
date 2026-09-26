def func():
    print("func() in one.py")

print("Always run ths part of one.py")

if __name__ == "__main__":
    print("will be executed when one.py is being run directly")
    func()
else:
    print("this part of one.py will be executed for IMPORT CONTEXT")


# o/p : 
# Always run ths part of one.py
# will be executed when one.py is being run directly
# func() in one.py