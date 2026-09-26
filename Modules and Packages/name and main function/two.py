import one

print("top-level in two.py")
one.func()

if __name__ == "__main__":
    print("will be executed when two.py is being run directly")
else:
    print("this part of two.py will be executed for IMPORT CONTEXT")



O/P : 
#import one --> these 2 below lines are printed 
Always run ths part of one.py
this part of one.py will be executed for IMPORT CONTEXT
#print("top-level in two.py")
top-level in two.py
#one.func()
func() in one.py
this part of two.py will be executed for IMPORT CONTEXT