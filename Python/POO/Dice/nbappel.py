class Nbappel :
    def __init__(self,f):
        self.appel=0
        self.f=f
    
    def __call__(self,*t,**d):
        self.appel +=1
        s = f'{self.f.__name__} a été appelé {self.appel} fois'
        print(s)
        return self.f(*t,**d)