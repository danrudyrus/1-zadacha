class Shape:
    def __init__(self, id_sh, x, y):
        self.id_sh, self.x , self.y = id_sh,x,y
    def id_sh(self):
        return self.id_sh
    def x (self,*new_x):
        if new_x:
            self.x = new_x
        else:
            return self.x
    def y(self, *new_y):
        if new_y:
            self.y = new_y
        else:
            return self.y
    def info(self):
        return '(%d,%d)'%(self.x,self.y)
class Circle(Shape):
    def __init__(self,id_sh,x,y,r):
        self.id_sh, self.x , self.y , self.r = id_sh,x,y,r
    def y(self, *new_r):
        if new_r:
            self.y = new_r
        else:
            return self.r
    def info(self):
        return '(%d,%d,%d)'%(self.x,self.y,self.r)
a = Circle(13415,1,58,8)
print(a.info())

