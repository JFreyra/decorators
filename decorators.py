import time

def printArg(*arg):
    return arg

def nameArgs(func):
    def inner(*arg):
        print func.func_name+": "+str(printArg(*arg))
        return func(*arg)
    return inner

def runtime(func):
    def inner(*arg):
        t1 = time.time()
        ret = func(*arg)
        print "time taken: "+str(time.time()-t1)+" seconds"
        return ret
    return inner

@nameArgs
@runtime
def test(x,y,z):
    time.sleep(1)
    return x+y+z    

print test(1,2,3)
