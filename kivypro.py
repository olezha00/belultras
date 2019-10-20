from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config

Config.set("graphics","resizable","0")
Config.set("graphics","width","360")
Config.set("graphics","height", "640")

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class MyApp(App):
	def build(self):
		#s = Scatter()
		fl = FloatLayout(size = (300,300))
		#s.add_widget(fl)
		fl.add_widget(Button(text="пшол нах", 
			font_size = 30, 
			on_press = self.btn_press,
			background_color = [1,0,0,1],
			background_normal = '',
			size_hint = (.5, .25),
			pos = (160, 180)))
		
		return fl
	
	def btn_press(self, instance):
		print ("сам иди")
		instance.text = 'ацтань'

if __name__ == "__main__":
	MyApp().run()





"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.config import Config

Config.set("graphics","resizable","0")
Config.set("graphics","width","640")
Config.set("graphics","height", "480")

class MyApp(App):
	def build(self):
		bl = BoxLayout(orientation = "vertical")
		bl.add_widget(Button(text = "first button"))
		bl.add_widget(Button(text = "the second one"))
		bl.add_widget(Button(text = "the third"))
		return bl
if __name__ == "__main__":
	MyApp().run()"""