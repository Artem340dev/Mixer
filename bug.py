from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from pygame import mixer

mixer.init()

mixer.music.load("Jojo2.mp3")
mixer.music.play()

class MusicApp(App):
	def build(self):
		bl = GridLayout(cols=3)
		bl.add_widget(Button(text="Пауза", on_press=self.p, background_color=[1, 0, 0, 1], background_normal=''))
		bl.add_widget(Button(text="Возобновить", on_press=self.q, background_color=[1, 1, 0, 1], background_normal=''))
		bl.add_widget(Button(text="Остановить", background_color=[0, 1, 0, 1], background_normal='', on_press=self.e))
		bl.add_widget(Button(text="Заного", on_press=self.z))
		return bl
		
	def p(self, instance):
		mixer.music.pause()
		
	def q(self, instance):
		mixer.music.unpause()
		
	def e(self, instance):
		mixer.music.stop()
		
	def z(self, instance):
		mixer.music.load("Jojo2.mp3")
		mixer.music.play()
		
if __name__ == '__main__':
	MusicApp().run()
