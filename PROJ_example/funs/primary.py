

class primary(object):
    def __init__(self,model=None):
        self.model = model
        self.res = None
        self.res_b = None
        self.data = None


    def predict(self):
        self.res = self.model.predict_proba(self.data)
        self.res_b = self.model.predict(self.data)
        return (self.res[:,1],self.res_b)
        
        
