import kivy
import backend24 as Backend
import random
kivy.require('1.0.5')

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager

class Card24 (BoxLayout):
	"""docstring for 24Card """
	
	cardNum = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
	special = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
	cardSym = ['C', 'S', 'H', 'D']
	cardList = ['green_back.png', 'green_back.png', 'green_back.png', 'green_back.png']
	source_image = cardList[0]
	answer = '-'
	point = 0

	def update(self):
		self.ids.answer_label.text = self.answer
		self.ids.point_label.text = self.point

	def startgame(self):
		self.cardList.clear()
		symRandom = random.sample(self.cardSym,4)
		numList = []
		for i in range(4):
			x = random.choice(self.cardNum)
			if (type(x) != str):
				numList.append(x)
			else:
				numList.append(self.special[x])
			self.cardList.append("{}{}.png".format(x, symRandom[i]))
		self.ids.shown1.source = self.cardList[0]
		self.ids.shown2.source = self.cardList[1]
		self.ids.shown3.source = self.cardList[2]
		self.ids.shown4.source = self.cardList[3]
		opList = Backend.calc(numList)
		tempPoint = Backend.calcop(opList)
		mathEx = Backend.satuinAngkaOp(numList, opList)
		finalPoint = Backend.hitungPoinAkhir(mathEx, tempPoint)
		self.point = str(finalPoint)
		self.answer = mathEx + '=' + str(eval(mathEx))
		self.ids.play_button.text = 'Shuffle'
	
	def exit(self):
		App.get_running_app().stop()


class Card24App(App):
	
	def build(self):
		return Card24()


if __name__ == '__main__':
    Card24App().run()
		


