from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import *
from kivy.uix.floatlayout import FloatLayout
import time

class StartScreen(Screen):
	def build(self):
		#fl = FloatLayout(size = (360,640))	
		
		#return fl
		pass
class LoadScreen(Screen):
	pass
class RegScreen(Screen):
	pass
class AdminPage(Screen):
	pass
class ClubPage(Screen):
	pass
class UserPage(Screen):
	pass
class News(ScreenManager):                     #Root screen
	pass
class Clubs(Screen):
	pass
class Chats(Screen):
	pass
class Users(Screen):
	pass
class Table(Screen):
	pass

Config.set("graphics","resizable","0")
Config.set("graphics","width","360")
Config.set("graphics","height", "640")

from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
	def build(self):
		with self.canvas:
			Color(1.,0,0)
			Rectangle(pos = (0,0), size = (360,640))
		#return StartScreen()
		"""time.sleep(4)
								return News()"""
if __name__ == "__main__":
	MyApp().run()
	#полная хуита