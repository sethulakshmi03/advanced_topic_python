def logged(Fun):
    def inner(*args,**kwargs):
        print("Here are the arguments passed!!!")
        Fun(*args,**kwargs)
    return inner
@logged
def Fun(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

Fun('hi','welcome','to','python','programming',first="all",mid="the",end="best")