
class secondary(object):
    def __init__(self,model=None):
        self.model = model
        self.res = None
        self.data = None
        self.labels = None


    def predict(self):
        self.res = self.model.predict_proba(self.data)
        #self.model.predict(self.data)
        return (self.res,self.labels)
    
    def read_cat(self):
        with open('funs/available_cat.txt','r') as f:
            self.labels = f.readlines()[0].split()
            print(self.labels)
        
        
