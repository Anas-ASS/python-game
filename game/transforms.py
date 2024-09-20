def transform(self,x,y):
    return self.transfomperspective(x,y)
    

def transform2d(self,x,y):
    return int(x),int(y) 
    
def transfomperspective(self , x, y):
    liny= y*self.perspectiveY/self.height
    if liny> self.perspectiveY:
        liny=self.perspectiveY

    diffy=self.perspectiveY-liny
    diffx=x-self.perspectiveX
    facorty=diffy/self.perspectiveY
    facorty=pow(facorty,4)
    tr_x=self.perspectiveX+diffx*facorty
    tr_y=(1-facorty)*self.perspectiveY
    return int(tr_x), int(tr_y)