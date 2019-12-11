
import requests
import urllib
from bs4 import BeautifulSoup
import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.label import Label
import sys
try:
	url = "https://www.shmoop.com/{}/".format(sys.argv[1])
	page = urllib.request.urlopen(url)
	html_doc = str(page.read())

	soup = BeautifulSoup(html_doc, 'html.parser')
	description = (str(soup.find(id='div_PrimaryContent').text))
  # takes the primary content description and takes the text

	class MyApp(App):
	    def build(self):
	        return TextInput(text=description) # opens up text area with the description in the text

	if __name__ == '__main__':
	    MyApp().run()
except:
	print("description not found!")

