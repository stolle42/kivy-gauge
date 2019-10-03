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
from kivy.core.window import Window
import time

class layout(Widget):

    def __init__(self, **kwargs):
        super(layout, self).__init__(**kwargs)
        self.widgetSize=(600,600)
        self.cadran=Image(source="cadran.png",size=self.widgetSize)
        self.add_widget(self.cadran)
        
        
        self.needle = Scatter(
            size=self.widgetSize,
            #do_rotation=False,
            #do_scale=False,
            #do_translation=False
            )
        self.needle.add_widget(Image(source="needle.png",size=self.widgetSize))
        self.add_widget(self.needle)
       
        Clock.schedule_interval(self.move,1)
    def move(self,dt):
        self.needle.center=self.cadran.center
        self.rotateNeedle(int(time.time())%21*5)
    def rotateNeedle(self,speed):
        """rotates the value to something between minValue (mapped to 0°) to maxValue (mapped to 180°)"""
        minValue=0
        maxValue=100
        if speed<minValue or speed>maxValue:
            raise ValueError("can only display values between {} and {}",minValue, maxValue)
        self.needle.rotation=speed/(maxValue-minValue)*180-90
        
class gauge(App):

    def build(self):

        return layout()

gauge().run()