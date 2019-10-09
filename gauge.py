from kivy import require
require('1.7.1')
from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import time

class layout(FloatLayout):

    def __init__(self, **kwargs):
        super(layout, self).__init__(**kwargs)
        self.widgetSize=Window.size
        self.cadran=Image(source="cadran.png")
        self.add_widget(self.cadran)
        
        self.container = Scatter(
            size=self.widgetSize,
            do_rotation=False,
            do_scale=False,
            do_translation=False,
            )
        self.needle=Image(source="needle.png",size=self.widgetSize)
        self.container.add_widget(self.needle)
        self.add_widget(self.container)
       
        Clock.schedule_interval(self.move,1)
    def move(self,dt):
        print(self.container.center,self.cadran.center,self.needle.center)
        # self.container.center=self.cadran.center
        #self.container.rotation=45
        self.container.pos_hint={"center":(.5,.5)}
        self.rotateNeedle(int(time.time())%21*5)
    def rotateNeedle(self,speed):
        """rotates the value to something between minValue (mapped to 0°) to maxValue (mapped to 180°)"""
        minValue=0
        maxValue=100
        if speed<minValue or speed>maxValue:
            raise ValueError("can only display values between {} and {}",minValue, maxValue)
        self.container.size=Window.size
        self.container.rotation=speed/(maxValue-minValue)*180-90
        
class gauge(App):

    def build(self):
        # Window.fullscreen=True
        return layout()

gauge().run()
