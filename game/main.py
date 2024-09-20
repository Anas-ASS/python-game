import random
from kivy.config import Config
from kivy.graphics.vertex_instructions import Triangle
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')
from kivy.lang.builder import Builder
from kivy import platform
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.properties import Clock
from kivy.graphics.vertex_instructions import Quad
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty

Builder.load_file("menu.kv")
class cc(BoxLayout):
    pass
class mainwidget(RelativeLayout):
    from  transforms import transform,transfomperspective,transform2d
    from user_action import on_keyboard_down,on_keyboard_up,on_touch_down,on_touch_up,keyboard_closed
   

    menu_ti=StringProperty("G   A   L   A   X   Y")
    menu_buttonti=StringProperty("START")



    menu_widget=ObjectProperty()
    perspectiveX=NumericProperty(0)
    perspectiveY=NumericProperty(0)
    vertical_line=[]
    vertical__nline=10

    vertical_spacing=0.4


    horizantl_line=[]
    horizantl__nline=15
    horizantl_spacing=0.1
    speed=0.8
    curentoffesty=0

    speedx=3.0
    currentspeedx=0
    currentoffestx=0

    nbtiles=10
    tiles=[]
    tilescoordinat=[]


    currentyloop=0

    shipwidth=0.1
    shiphight=0.040
    shipbase_y=0.04
    ship=None
    shipcoordinate=[(0,0),(0,0),(0,0)]

    stategameover=False
    statgamehasstarted=False

    score_text=StringProperty()
    

    def __init__(self, **kwargs):
        super(mainwidget,self).__init__(**kwargs)
        #print("w: jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj "+str(self.width)+"H  "+str(self.height))
        self.init_vertical_line()
        self.init_horizantl_line()
        self.init_tiles()
        self.init_ship()
        self.resetgame()
        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)
        Clock.schedule_interval(self.update,1.0/60.0)


    def resetgame(self):
        self.curentoffesty=0
        self.currentyloop=0
        self.currentspeedx=0
        self.currentoffestx=0
        self.score_text="SCORE:  "+str(self.currentyloop)


        self.tilescoordinat=[]
        self.firtstraghttile()
        self.generatcoordinate_tiles()

        self.stategameover=False


    def on_size(self,*args):
       # print("w: jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj "+str(self.width)+"H  "+str(self.height))
        self.perspectiveX=self.width/2
        self.perspectiveY=self.height*0.75
        pass
    """def on_perspectiveX(self,widget,value):
        #print("px:  "+str(value)) 
        pass
    def on_perspectiveY(self,widget,value):
      #  print("py:  "+str(value)) 
     
      pass
    """
    def init_ship(self):
        with self.canvas:
            Color(0,0,0) 
            self.ship=Triangle()    

    def updateship(self):

        x=self.width/2
        basey=self.shipbase_y*self.height
        shiphalfwidth=self.shipwidth*self.width/2
        siphigh=self.shiphight*self.height
        #    2
        #  1    3

        self.shipcoordinate[0]=(x-shiphalfwidth,basey)
        self.shipcoordinate[1]=(x,basey+siphigh)
        self.shipcoordinate[2]=(x+shiphalfwidth,basey)

        x1,y1=self.transform(*self.shipcoordinate[0])
        x2,y2=self.transform(*self.shipcoordinate[1])
        x3,y3=self.transform(*self.shipcoordinate[2])
        self.ship.points=[x1,y1,x2,y2,x3,y3]   



    def checkshipcoolision(self):
        for i in range(0,len(self.tilescoordinat)):
            tix,tiy=self.tilescoordinat[i]
            if tiy>self.currentyloop+1:
                return False
            
            if self.checkshipcollisiontile(tix,tiy):
                return True
        return False


    def checkshipcollisiontile(self,tix,tiy):
        xmin,ymin=self.getcordenatefrom_index(tix,tiy)
        xmax,ymax=self.getcordenatefrom_index(tix+1,tiy+1)
        for i in range(0,3):
            px,py=self.shipcoordinate[i]
            if xmin<=px<=xmax and ymin<=py<=ymax:
                return True
        return False


    
    def init_tiles(self):       
        with self.canvas:
            Color(1,1,1)  
            for i in range(0,self.nbtiles):
                self.tiles.append(Quad())


    def firtstraghttile(self):
        for i in range(0,10):
            self.tilescoordinat.append((0,i))





    def generatcoordinate_tiles(self):
            lasty=0
            lastx=0
            for i in range(len(self.tilescoordinat)-1,-1,-1):
                if self.tilescoordinat[i][1]<self.currentyloop:
                    del self.tilescoordinat[i]
            if len(self.tilescoordinat)>0:
                lastcoordinate=self.tilescoordinat[-1]
                lastx=lastcoordinate[0]

                lasty=lastcoordinate[1]+1
                "generat another tile to make it infity"


            print(222222)

            for i in range(len(self.tilescoordinat),self.nbtiles):
                randomn=random.randint(0,2)
                "0> sraight     1-> right     2->left "


                startindex=-int(self.vertical__nline/2)+1
                endindex=startindex+self.vertical__nline-1 
                "to go to the right and stay on the track"
                if lastx<=startindex:
                    randomn=1          



                if lastx>=endindex:
                    randomn=2                       


                self.tilescoordinat.append((lastx,lasty))                

                if randomn==1:
                    lastx+=1
                    self.tilescoordinat.append((lastx,lasty))
                    lasty+=1
                    self.tilescoordinat.append((lastx,lasty))

                if randomn==2:
                    lastx-=1
                    self.tilescoordinat.append((lastx,lasty))
                    lasty+=1
                    self.tilescoordinat.append((lastx,lasty))
                lasty+=1

            print(1111111)

    
    
    def init_vertical_line(self):       
        with self.canvas:
            Color(1,1,1)   
           # self.Line=Line(points=[100, 0, 100 , 100])  

            for i in range(0, self.vertical__nline):
                self.vertical_line.append(Line())






    def getlin_xfromindex(self,index):
        x=self.perspectiveX
        start=self.vertical_spacing*self.width
        space=index-0.5
        linex=x+space*start+self.currentoffestx
        return linex



    def getlin_yyfromindex(self,index):
        spacingy=self.horizantl_spacing*self.height
        liney=index*spacingy-self.curentoffesty   
        return liney     



    def getcordenatefrom_index(self,tix,tiy):
        tiy=tiy- self.currentyloop
        x=self.getlin_xfromindex(tix)
        y=self.getlin_yyfromindex(tiy)
        return x,y 




    def updatetiles(self):
        for i in range(0,self.nbtiles):
            tile=self.tiles[i]
            tilescoordinat=self.tilescoordinat[i]
            xmin,ymin=self.getcordenatefrom_index(tilescoordinat[0],tilescoordinat[1])
            xmax,ymax=self.getcordenatefrom_index(tilescoordinat[0]+1,tilescoordinat[1]+1)

            x1,y1=self.transform(xmin,ymin)
            x2,y2=self.transform(xmin,ymax)
            x3,y3=self.transform(xmax,ymax)
            x4,y4=self.transform(xmax,ymin)

            tile.points=[x1,y1,x2,y2,x3,y3,x4,y4]

    def update_vertical_line(self):
        startindex=-int(self.vertical__nline/2)+1
        for i in range(startindex, startindex+self.vertical__nline):
            linex=self.getlin_xfromindex(i)
            x1,y1=self.transform(linex,0)
            x2,y2=self.transform(linex,self.height)
            self.vertical_line[i].points=[x1, y1,x2 ,y2]
        #self.Line.points=[x,0,x,100]


    def init_horizantl_line(self):       
        with self.canvas:
            Color(1,1,1)   
           # self.Line=Line(points=[100, 0, 100 , 100])  

            for i in range(0, self.horizantl__nline):
                self.horizantl_line.append(Line())

    def update_horizantl_line(self):
        startindex=-int(self.vertical__nline/2)+1
        endindex=startindex+self.vertical__nline-1

        xmin=self.getlin_xfromindex(startindex)
        xmax=self.getlin_xfromindex(endindex)
        for i in range(0, self.horizantl__nline):
            liney=self.getlin_yyfromindex(i)
            x1,y1=self.transform(xmin,liney)
            x2,y2=self.transform(xmax,liney)
            self.horizantl_line[i].points=[x1, y1,x2 ,y2]
        #self.Line.points=[x,0,x,100]




    
    
    

    def update(self,dt):
        timef=dt*60
        self.update_vertical_line()
        self.update_horizantl_line()
        self.updatetiles()
        self.updateship()

        if not self.stategameover and self.statgamehasstarted:
            speed_y=self.speed*self.height/100
            self.curentoffesty+=speed_y*timef



            spacingy=self.horizantl_spacing*self.height

            while self.curentoffesty>=spacingy:
                self.curentoffesty-=spacingy
                self.currentyloop+=1
                self.score_text="SCORE:  "+str(self.currentyloop)
                self.generatcoordinate_tiles()
            speed_x=self.currentspeedx*self.width/100
            self.currentoffestx+=speed_x*timef

        if not self.checkshipcoolision() and not self.stategameover:
            self.stategameover=True
            self.menu_ti="G  A  M  E     O  V  E  R"
            self.menu_buttonti="RESTART"
            self.menu_widget.opacity=1

            print(" game over")
    
    
    def onbuttonpressed(self):

        print("button")
        self.resetgame()
        self.statgamehasstarted=True
        self.menu_widget.opacity=0

    def is_desktop(self):
        if platform  in ('linux','win','macosx'):
            return True
        return False





class gameApp(App):
    pass






gameApp().run()