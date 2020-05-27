#---------------args-------------
def argsFun(*args):
    for i in  args:
        print(i)

argsFun(1,2,3,'a','b','c')


#----------------kwargs------------
def kwargsFun(**kwargs):
    for k,v in kwargs.items():
        print('{0} : {1}'.format(k,v))

kwargsFun(name='Saral',lang='Python', age=23)
