# this is a wheather app that uses api to get information and uses a tkinter app to display it
import requests
from tkinter import *
import threading
from tkinter import font
import random
import time


class weather_app():

	def __init__(self):
		self.win = Tk()
		self.win.title("Weather It")
		self.win.geometry("1300x700")
		self.win.resizable(0,0)  #stop user from resizing
		self.run_app() # make sure that run_app() runs everytime no matter what, cause its the main part of source code

	def infoplacement(self, info):
		coords = self.mycanvas.bbox(info)
		setx = abs((coords[0] - coords[2])/2)+2
		return setx

	def getweather(self, city_entered, images):
		# requesting and storing data from API
		weather_key='your personal api key goes here'
		url='http://api.openweathermap.org/data/2.5/weather'
		parameters = {'APPID':weather_key, 'q':city_entered, 'units': 'imperial'}
		# website will return the results in JSON code so we convert it using json() function
		try:
			response = requests.get(url, params=parameters)
			#if this goes wrong
			city=response.json()['name']
			temp=response.json()['main']['temp']
			humidity=response.json()['main']['humidity']
			country=response.json()['sys']['country']
			weather=response.json()['weather'][0]['description']
			self.wallpaper=response.json()['weather'][0]['main']
				
			self.change_wallpaper(self.wallpaper)
			self.mycanvas.itemconfig(self.city_name_n_country, text='Location: '+city+', '+country)
			self.mycanvas.itemconfig(self.temperature_n_humidity, text= 'Temperature: '+str(temp)+'°, '+str(humidity)+'% humidity')
			self.mycanvas.itemconfig(self.weather_rn, text ='Weather: ' + weather)

			# placing info to the left of frame using infoplacement(self) function
			self.mycanvas.coords(self.city_name_n_country, self.infoplacement(self.city_name_n_country), 250)
			self.mycanvas.coords(self.temperature_n_humidity, self.infoplacement(self.temperature_n_humidity), 275)
			self.mycanvas.coords(self.weather_rn, self.infoplacement(self.weather_rn), 300)

			# keeping the search button off for 5 seconds to prevent too much requesting
			self.searchbutton.configure(state='disabled')
			threading.Timer(5.0, self.reactivate).start()

		except:		# this is triggered
			self.mycanvas.itemconfig(self.wall_change, image = self.images['no_connection'][0])
			self.mycanvas.itemconfig(self.city_name_n_country, text='Something is not right')
			self.mycanvas.itemconfig(self.temperature_n_humidity, text="please check your internet connection")
			self.mycanvas.itemconfig(self.weather_rn, text = 'make sure city name is spelled properly')

			self.mycanvas.coords(self.city_name_n_country, self.infoplacement(self.city_name_n_country), 250)
			self.mycanvas.coords(self.temperature_n_humidity, self.infoplacement(self.temperature_n_humidity), 275)
			self.mycanvas.coords(self.weather_rn, self.infoplacement(self.weather_rn), 300)


	def reactivate(self):
		self.searchbutton.configure(state = 'active')

	def change_wallpaper(self, wallpaper):
		mylist = ['Rain', 'Thunderstorm', 'Snow', 'Clouds', 'Clear','Drizzle'] # list of basic weather conditions
		if wallpaper in mylist:
			self.myimg = self.images[self.wallpaper][random.randint(0, len(self.images[self.wallpaper])-1)]
			self.mycanvas.itemconfig(self.wall_change, image = self.myimg)
		else: # wallpapers for when there are different conditions
			self.myimg = self.images['Regular'][random.randint(0, len(self.images['Regular'])-1)]
			self.mycanvas.itemconfig(self.wall_change, image = self.myimg)

	#the main tkinter source code	
	def run_app(self):
		# SEARCH FRAME
		self.searchframe = Frame(self.win)
		self.searchframe.place(relheight=1, relwidth=0.5)

		# RESULT FRAME
		self.resultframe = Frame(self.win, height=100, width =100)
		self.resultframe.place(relheight=1, relwidth=0.5,relx=0.5 )

		# Canvas for weather background
		self.mycanvas =Canvas(self.resultframe, width=300, height = 300)
		self.mycanvas.place( relwidth=1, relheight=1)

		# Images to be used for weather background
    # if images not in same folder as the source code then you need to add path before filename
		self.images = 	{'Rain':[PhotoImage(master = self.mycanvas, file='rsz_luke-stackpoole-fa8hewo9vd8-unsplash.png'),
							 PhotoImage(master = self.mycanvas, file='rsz_josh-hild-yvnrtc04qyy-unsplash.png')],
					'Clouds':[PhotoImage(master = self.mycanvas, file ='rsz_joshua-sukoff-kmlol0c7q_y-unsplash.png'),
							PhotoImage(master = self.mycanvas, file ='rsz_jason-an-ahzyloe7-nm-unsplash.png')],
					'Thunderstorm':[PhotoImage(master = self.mycanvas, file ='rsz_eberhard-grossgasteiger-v4cdzjblb9e-unsplash.png')],
					'Clear':[PhotoImage(master = self.mycanvas, file ='rsz_chrissie-kremer-lecl0oyhxni-unsplash.png'),
							PhotoImage(master = self.mycanvas, file ='rsz_grace-lim-db0o2nybynu-unsplash.png'),
							PhotoImage(master = self.mycanvas, file ='rsz_michal-kubalczyk-bcnzxvvbf_u-unsplash.png'),
							PhotoImage(master = self.mycanvas, file ='rsz_lucrezia-de-agro-4eyry0ujabg-unsplash.png')],
					'Snow':[PhotoImage(master = self.mycanvas, file ='rsz_belkacem-makhloufi-xiltuzxzueg-unsplash.png')],
					'Drizzle':[PhotoImage(master = self.mycanvas, file ='rsz_element5-digital-kydm2kwnrzm-unsplash.png'),
							PhotoImage(master = self.mycanvas, file ='rsz_adam-birkett-laid6efkzn4-unsplash.png')],
					'Regular':[PhotoImage(master = self.mycanvas, file ='rsz_sebastian-pociecha-e1zotaz7o2o-unsplash.png'),
							PhotoImage(master = self.mycanvas, file ='rsz_tanjir-ahmed-chowdhury-5gi0y45rgk4-unsplash.png'),
							PhotoImage(master = self.mycanvas, file ='rsz_omer-sonido-9mlvy3cxyxc-unsplash.png'),
							PhotoImage(master = self.mycanvas, file ='rsz_lucrezia-de-agro-4eyry0ujabg-unsplash.png'),
							PhotoImage(master = self.mycanvas, file ='rsz_kyle-cottrell-h45mrm-u4km-unsplash.png'),
							PhotoImage(master = self.mycanvas, file ='rsz_andreas-pajuvirta-2bliurnjcqa-unsplash.png')],
					'Main_menu':[PhotoImage(master = self.mycanvas, file ='rsz_rsz_20200624_030025.png'),
								PhotoImage(master = self.mycanvas, file ='rsz_rsz_20200624_030102.png'),
								PhotoImage(master = self.mycanvas, file ='rsz_rsz_20200624_030126.png')],
					'no_connection':[PhotoImage(master = self.mycanvas, file ='rsz_download.png')]
					}
		# Default weather background when app is launched		
		img =self.images['Main_menu'][random.randint(0,len(self.images['Main_menu'])-1)]
		self.wall_change = self.mycanvas.create_image(0, 0, anchor=NW, image=img)

		# result texts
		self.city_name_n_country = self.mycanvas. create_text(0, 0, text ='', font=("Consolas", 19), fill='white')
		self.temperature_n_humidity = self.mycanvas.create_text(0, 0, text ='' , font=("Consolas", 19), fill='white')
		self.weather_rn = self.mycanvas. create_text(0, 0, text ='', font=("Consolas", 19), fill='white')

		#Searchbar
		self.searchbar = Entry(self.searchframe, font=("Consolas", 18))
		self.searchbar.place(rely= 0.3, relx=0.15, relheight=0.05, relwidth=0.7)

		#Searchbutton
		self.searchbutton = Button(self.searchframe, text="SEARCH", command=lambda:self.getweather(self.searchbar.get(), self.images))
		self.searchbutton.place(relx=0.45, rely=0.4, relheight=0.05, relwidth=0.11)

		# Instruction
		app_title = Label(self.searchframe, text= "Weather It", font=("Consolas", 30))
		app_title.place(relx=0.35, rely=0.17)

		# Instruction
		statement1='Please enter the name of your city in search bar'
		statement2 = 'and click the "SEARCH" button to get weather of that city'
		txt =statement1.center(len(statement2),' ') +'\n'+statement2.center(len(statement2),' ')

		instructions=Label(self.searchframe, text=txt, font= ("Consolas", 12), fg='black')
		instructions.place(relx = 0.09, rely =0.6)

		instruct_title ='Instructions'.center(len(statement2),' ')
		instructions_title = Label(self.searchframe, text=instruct_title, font=("Consolas", 15), fg='black')
		instructions_title.place(relx = 0.01, rely= 0.56)

		thanks = "Thanks to 'openweathermaps.org' for their amazing api services"
		thanksptg = 'and all the photographers for these amazing backgrounds'
		tytxt = thanks.center(len(thanks),' ') + '\n' + thanksptg.center(len(thanksptg),' ')
		tynote = Label(self.searchframe, text=tytxt, font =('Consolas', 12), fg='#7E7E7E')
		tynote.place(relx=0.07, rely=0.9)

		dev_signature = Label(self.searchframe, text = 'by prathamesh_takane', font = ('Consolas', 12), fg='#7E7E7E')
		dev_signature.place(relx=0, rely=0)

		self.win.mainloop()

oop = weather_app()
oop.win.mainloop()

