#import tkinter as tk   # python3
import Tkinter as tk   # python
from Tkinter import *
import os
import time
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import strpdate2num
from PIL import *
import tkMessageBox
import tkFont
from PIL import Image,ImageTk,ImageDraw,ImageFont
TITLE_FONT = ("Helvetica", 18, "bold")
FONT = ("Helvetica", 15, "bold")
users=['y','youssef.lazreg30@gmail.com']
S ="/"
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
    	#self.Loading = Loading(self)
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login, Mainpage, Survey,Contact,
                  Mesure, Temperature, AirFlow,Electrocardiogram,Galvanic,
                          Position,Bloodpressure,
                  Specialite,GeneralPractitioner,Pediatre,Contactemail):

            
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()  

#



class Login (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #self.controller = controller
        self.image1 = Image.open("images"+S+"splash.gif")
        self.img_copy1 = self.image1.copy()
        self.background_image1 = ImageTk.PhotoImage(self.image1)
        self.background1 = Label(self, image=self.background_image1)
        self.background1.pack(expand=True,fill=BOTH)
        self.background1.bind('<Configure>', self.resize_image)
        self.background1.place(x=0, y=0, relwidth=1, relheight=1)
        self.background1.bind('<Button-1>', self.skip)
        #Background image
        self.image = Image.open("images"+S+"Login_bg.gif")
        self.img_copy = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.bind('<Configure>', self.resize_image)

        #button to attempt to login
        self.b = tk.Button(self, borderwidth=4,font=FONT, text="Login",
                      width=10, pady=8, command=lambda :controller.show_frame("Mainpage"))
        
        
    
    def skip(self,event):
    	lambda:self.background1.pack.forget()
    	self.background.pack(expand=True,fill=BOTH)
    	self.background.place(x=0, y=0, relwidth=1, relheight=1)
    	self.user = self.make_entry("User name:", 16, show='*',font=FONT)
    	self.user.bind('<Return>', self.enter)
    	self.b.pack()

    	
    def resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image1 = self.img_copy1.resize((new_width, new_height))
        self.background_image1 = ImageTk.PhotoImage(self.image1)
        self.background1.configure(image =  self.background_image1)

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)



    def make_entry(self, caption, width=None, **options):
        tk.Label(self, text=caption,font=FONT).pack(side=tk.TOP)
        entry = tk.Entry(self, **options)
        if width:
            entry.config(width=width)
        entry.pack(side=tk.TOP, pady=30)
        return entry

    def enter(self,event):
        lambda :controller.show_frame("Mainpage")

    def check_password(self):
        
        #Collect 1's for every failure and quit program in case of failure_max failuresself.controller = controller
        print self.user.get()
        if self.user.get() in users:
            lambda :controller.show_frame("Mainpage")
            print('Logged in')
            return

class Mainpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Background image
        fond = ImageTk.PhotoImage(Image.open("images"+S+"1.gif"))
        label1=tk.Label(self,image=fond)
        label1.image=fond
        label1.pack()
  
        label1.place(x=0, y=0, relwidth=1, relheight=1)

        label = tk.Label(self, text="ROBOT DOCTEUR", font="Castellar 36 bold italic",fg="red")
        label.pack(side="top",pady=35)
        
        button1 = tk.Button(self, text="Survey",height= 1,font="Arial 24 bold italic",
                            command=lambda: controller.show_frame("Survey"))
        button2 = tk.Button(self, text="Mesure",height= 1,font="Arial 24 bold italic",
                            command=lambda: controller.show_frame("Mesure"))
        button3 = tk.Button(self, text="Take an appointment",height= 1,font="Arial 24 bold italic",
                            command=lambda: controller.show_frame("Specialite"))
        button4 = tk.Button(self, text="Quit",height= 1,font="Algerian 27 bold",
                            command=lambda: quit())
        button1.pack(side="top", pady=10)
        button2.pack(side="top", pady=10)
        button3.pack(side="top", pady=10)
        button4.pack(side="bottom", pady=10)
    def quit():
        tk.destroy()    

class Survey(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Survey", font="Castellar 36 bold italic",fg="red")
        label.pack(side="top", pady=0)

        #instruction pour l'utilisateur
        label = tk.Label(self, text="Please check one alternative :",font="Arial 18 bold italic")
        label.pack(side="top", padx=10, pady=5)

        #1ere question
        label1 = tk.Label(self, text="1) Do you work ?",font=FONT)
        label1.pack(side="top", padx=10, pady=3)
        self.question_1 = StringVar()
        
        # create domicile radiobutton
        domicile= tk.Radiobutton(self,text="Unemployed",font=FONT,variable=self.question_1,value="Unemployed")
        domicile.pack(side="top",padx=2,pady=2)
    
        # create bureau radiobutton
        bureau= tk.Radiobutton(self,text="Office",font=FONT,variable=self.question_1,value="Office")
        bureau.pack(side="top",padx=2,pady=2)

        # create magasin radiobutton
        magasin= tk.Radiobutton(self,text="Waiter/waitress",font=FONT,variable=self.question_1,
                                value="Waiter/waitress")
        magasin.pack(side="top",padx=2,pady=5)


        #2eme question
        label2 = tk.Label(self, text="2) Do you consume alcohol ?",font=FONT)
        label2.pack(side="top", padx=10, pady=3)
        self.question_2 = StringVar()
        
        # create touslesjours radiobutton
        touslesjours= tk.Radiobutton(self,text="Daily",variable=self.question_2,
                                     value="Daily",font=FONT)
        touslesjours.pack(side="top",padx=2,pady=2)
    
        # create rarement radiobutton
        rarement= tk.Radiobutton(self,text="rarely",variable=self.question_2,value="rarely",font=FONT)
        rarement.pack(side="top",padx=2,pady=2)

        # create j'aiarrete radiobutton
        jaiarrete= tk.Radiobutton(self,text="I stopped drinking",variable=self.question_2,value="jaiarrete",font=FONT)
        jaiarrete.pack(side="top",padx=2,pady=5)


        #3eme question
        label3 = tk.Label(self, text="3) Your daily water intake ?",font=FONT)
        label3.pack(side="top", padx=10, pady=3)
        self.question_3 = StringVar()
        
        # create domicile radio button
        tk.Radiobutton(self,text="Less than 1L per day",variable=self.question_3,
                       value="Less than 1L per day",font=FONT).pack(side="top",padx=2,pady=2)
    
        # create bureau radio button
        tk.Radiobutton(self,text="Between 1L and 2L per day",variable=self.question_3,
                       value="Between 1L and 2L per day",font=FONT).pack(side="top",padx=2,pady=2)

        # create magasin radio button
        tk.Radiobutton(self,text="More than 2L per day",variable=self.question_3,
                       value="More than 2L per day",font=FONT).pack(side="top",padx=2,pady=5)

        Mainpage = tk.Button(self, text="Main page",height= 1,font=FONT,bg='white',
                           command=lambda: controller.show_frame("Mainpage"))
        Mainpage.pack(side="bottom" ,pady=10)

        Submit = tk.Button(self, text="Submit",height= 1,font=FONT,bg='white',
                           command=self.submit)
        Submit.pack(side="bottom" ,pady=10)

    def submit(self):
    	file = open("Data"+S+"Survey.txt",'w')
    	file.write("1) Do you work ? : "+self.question_1.get() +"\n")
    	file.write("2) Do you consume alcohol ? : "+self.question_2.get() +"\n")
    	file.write("3) Your daily water intake ? : "+self.question_3.get() )
    	file.close()
    	os.system("start \"\" \"Data\\Survey.txt\" ")


class Mesure(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Mesure", font="Castellar 36 bold italic", fg="brown")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Main page",height= 1,font="Algerian 14 bold",bg="white",
                           command=lambda: controller.show_frame("Mainpage"))
        button.pack(side = "bottom",pady=20)

        #Temperature
        button_temperature = tk.Button(self, text="Temperature",font="Arial 18 bold",bg="white",height= 1,
                           command=lambda: controller.show_frame("Temperature"))
        button_temperature.pack(side = "top",pady=10)

        #Breath
        button_breathing = tk.Button(self, text="Air Flow :Breathing",font="Arial 18 bold",height= 1,bg="white",
                           command=lambda: controller.show_frame("AirFlow"))
        button_breathing.pack(side = "top",pady=10)

        #Electrocardiogram
        button_breathing = tk.Button(self, text="Electrocardiogram",font="Arial 18 bold",height= 1,bg="white",
                           command=lambda: controller.show_frame("Electrocardiogram"))
        button_breathing.pack(side = "top",pady=10)

        #Galvanic
        button_galvanic = tk.Button(self, text="Galvanic skin",font="Arial 18 bold",height= 1,bg="white",
                           command=lambda: controller.show_frame("Galvanic"))
        button_galvanic.pack(side = "top",pady=10)

        #Position
        button_galvanic = tk.Button(self, text="Body Position",font="Arial 18 bold",height= 1,bg="white",
                           command=lambda: controller.show_frame("Position"))
        button_galvanic.pack(side = "top",pady=10)
        #Bloodpressure
        button_bloodpressure = tk.Button(self, text="Blood Pressure",font="Arial 18 bold",height= 1,bg="white",
                           command=lambda: controller.show_frame("Bloodpressure"))
        button_bloodpressure.pack(side = "top",pady=10)
        
        
class Temperature(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Title
        label = tk.Label(self, text="Temperature", font=TITLE_FONT)
        label.pack(side="top", pady=10)

        #Instruction
        label = tk.Label(self, text="To mesure your temperature, \nplease put the sensor on top your finguer and press the button below", font=TITLE_FONT)
        label.pack(side="top", pady=10)
       

        self.temp_image = ImageTk.PhotoImage(Image.open("images"+S+"temperature.png"))
        b=tk.Label(self,image=self.temp_image)
        b.pack(pady=5)
  
  #Mesure button
        temp=tk.Button(self,text="Mesure",height= 1,font=FONT,
                           command= lambda: self.get_temp())
        temp.pack(pady=10)
        #History button
        history=tk.Button(self,text="History",height= 1,font=FONT,
                           command=lambda: self.get_history())
        history.pack()

        #startpage
        button = tk.Button(self, text="Start Page",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Mainpage"))
        button.pack(side = "bottom",pady=10)
        #Return button
        button = tk.Button(self, text="Return",height= 1,width=9,font=FONT,
                           command=lambda: controller.show_frame("Mesure"))
        button.pack(side = "bottom",pady=10)
        

    def get_history(self):       

        days, data = np.loadtxt("Data"+S+"temperaturedata.txt",
                               unpack=True,
                               converters={ 0: mdates.strpdate2num('%Y-%m-%d')}) #strpdate2num

        plt.plot_date(x=days, y=data, fmt="r*")
        plt.axis()
        plt.xticks(rotation=25)
        plt.title("Your temperature")
        plt.ylabel("Celsius")
        plt.grid(True)
        plt.savefig("Data"+S+"temperaturefig.png")
        os.system("start \"\" \"Data\\temperaturefig.png\"")
                        

    def get_temp(self):
        os.system("./temperature")
        a=open("Data"+S+"temperaturedata.txt","rb")
        lines=a.readlines()
        if lines :
            last_line=lines[-1]
        tkMessageBox.showinfo(message="Votre temperature est :\n" + last_line[0:4] + "-" + last_line[5:14]+" Celsius" )
        

class AirFlow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AirFlow Breathing", font=TITLE_FONT)
        label.pack(side="top", pady=10)
        
        button = tk.Button(self, text=" Main Page",font=FONT,
                           command=lambda: controller.show_frame("Mainpage"))
        button.pack(side = "bottom",pady=10)
        button = tk.Button(self, text="Back",font=FONT,
                           command=lambda: controller.show_frame("Mesure"))
        button.pack(side = "bottom",pady=10)

        label = tk.Label(self, text="Press the button below and breath for 10s",font=FONT)
        label.pack(pady=10)
#
        self.image1 = ImageTk.PhotoImage(Image.open("images"+S+"airflow.png"))
        b1=tk.Label(self,image=self.image1)
        b1.pack()
#
        breath = tk.Button(self, text="Press and Breath regularly",font=FONT,
                           command=lambda: self.get_airflow())
        breath.pack()

    
    
    
    def get_airflow(self):
        
        os.system("./airflow")
        pic=plt.plotfile("Data"+S+"airflowdata.txt",
                     delimiter=' ', cols=(1, 0),linestyle='-')
        plt.savefig("Data"+S+"airflowfig.png")
        plt.title("Breathing Rhythm")
        plt.grid(True)
        os.system("start \"\" \"Data\\airflowfig.png\"")


class Electrocardiogram(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Electrocardiogram", font=TITLE_FONT)
        label.pack(side="top", pady=10)

        #startpage
        button = tk.Button(self, text="Main Page",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Mainpage"))
        button.pack(side = "bottom",pady=10)
        #Return button
        button = tk.Button(self, text="Back",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Mesure"))
        button.pack(side = "bottom",pady=10)
        
        button = tk.Button(self, text="Mesure",height= 1,font=FONT,
                           command=lambda: self.get_ecg())
        button.pack()
#
        controller.image1 = ImageTk.PhotoImage(Image.open("images"+S+"ecg.png"))
        b1=tk.Label(self,image=controller.image1)
        b1.pack()
#


    def get_ecg(self):
        os.system("./ecg")
        pic=plt.plotfile("Data"+S+"ecgdata.txt",
                     delimiter=' ', cols=(1, 0),linestyle='-')
        plt.savefig("Data"+S+"ecgfig.png")
        plt.title("Electrocardiogram")
        plt.grid(True)
        photo1=PhotoImage(file="Data"+S+"ecgfig.png")
        os.system("start \"\" \"Data\\ecgfig.png\"")

class Galvanic(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Title
        label = tk.Label(self, text="Skin condanctance & resistance", font=FONT)
        label.pack(side="top", pady=10)

        #Instruction
        label = tk.Label(self, text="To mesure your Galvanic skin response, \nplease put the sensor on your finguers and press the button below", font=TITLE_FONT)
        label.pack(side="top", pady=10)
        #Mesure button
        temp=tk.Button(self,text="Mesure",height= 1,font=FONT,
                           command= lambda: self.get_galvanic())
        temp.pack()

        #startpage
        button = tk.Button(self, text="Start Page",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Mainpage"))
        button.pack(side = "bottom",pady=10)
        #Return button
        button = tk.Button(self, text="Back",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Mesure"))
        button.pack(side = "bottom",pady=10)
#
        controller.image1 = ImageTk.PhotoImage(Image.open("images"+S+"galvanic.png"))
        b1=tk.Label(self,image=controller.image1)
        b1.pack()
                                
#
    def get_galvanic(self):
        os.system("./galvanic")
        a=open("Data"+S+"galvanicdata.txt","rb")
        lines=a.readlines()
        if lines :
            last_line=lines[-1]
        tkMessageBox.showinfo(message="Skin Resistance = " + last_line[5:14] + "\nConductance Voltage = " + last_line[0:4] )
        
class Position(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Title
        label = tk.Label(self, text="Skin condanctance & resistance", font=TITLE_FONT)
        label.pack(side="top", pady=10)

        #Instruction
        label = tk.Label(self, text="Press the button below",font=FONT)
        label.pack(side="top", pady=10)
        
        #Mesure button
        temp=tk.Button(self,text="Mesure",height= 1,font=FONT,
                           command= lambda: self.get_position())
        temp.pack()

        #startpage
        button = tk.Button(self, text="Start Page",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Mainpage"))
        button.pack(side = "bottom",pady=10)
        #Return button
        button = tk.Button(self, text="Return",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Mesure"))
        button.pack(side = "bottom",pady=10)
        controller.image1 = ImageTk.PhotoImage(Image.open("images"+S+"position.png"))
        b1=tk.Label(self,image=controller.image1)
        b1.pack()
                        

    def get_position(self):
        os.system("./positionometer")
        a=open("Data"+S+"positionometerdata.txt","rb")
        lines=a.readlines()
        if lines :
            last_line=lines[-1]
        tkMessageBox.showinfo(message=lines)


class Bloodpressure(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Title
        label = tk.Label(self, text="Blood presssure", font=FONT)
        label.pack(side="top", pady=10)

        #Instruction
        label = tk.Label(self, text="To mesure your blood pressure, \nplease use the sensor then press the button", font=TITLE_FONT)
        label.pack(side="top", pady=10)
        #Mesure button
        temp=tk.Button(self,text="Mesure",height= 1,font=FONT,
                           command= lambda: self.get_bloodpressure())
        temp.pack()
       
        self.image4 = ImageTk.PhotoImage(Image.open("images"+S+"bloodpreseure.png"))
        b4=tk.Label(self,image=self.image4,compound="left")
        b4.pack()

   #History button
        history=tk.Button(self,text="History",height= 1,font=FONT,
                           command=lambda: self.get_history())
        history.pack()

        #startpage
        button = tk.Button(self, text="Start Page",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Mainpage"))
        button.pack(side = "bottom",pady=10)
        #Return button
        button = tk.Button(self, text="Return",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Mesure"))
        button.pack(side = "bottom",pady=10)
        
        
        history.pack()

    def get_history(self):       

        days, systolic, diastolic,pulse  = np.loadtxt("Data"+S+"bloodpressuredata.txt",
                               unpack=True,
                               converters={ 0: mdates.strpdate2num('%Y-%m-%d')})

        plt.plot_date(x=days, y=systolic,linestyle='-')
        plt.plot_date(x=days, y=diastolic,linestyle='-')
        plt.plot_date(x=days, y=pulse,linestyle='-')
        plt.axis()
        plt.xticks(rotation=25)
        plt.title("Your data")
        plt.grid(True)
        plt.axis('auto')
        plt.savefig("Data"+S+"bloodpressurefig.png")

        os.system("start \"\" \"Data\\bloodpressurefig.png\"")
                        

    def get_bloodpressure(self):
        os.system("./bloodpressure")
        a=open("Data"+S+"bloodpressuredata.txt","rb")
        lines=a.readlines()
        if lines :
            last_line=lines[-1]
        date,hour,systolic,diastolic,pulse=last_line.rstrip().split(' ')
        
        tkMessageBox.showinfo(message=date+" "+hour +"\nSystolic value : " +systolic+ " mmHg\nDiastolic value : " + diastolic+" mmHg\nPulse value : "+pulse+ " bpm" )





class Specialite(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Specialite", font="Castellar 36 bold italic",fg="brown",bg="darkturquoise")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="General Practitioner",height= 1,font=FONT,
                           command=lambda: controller.show_frame("GeneralPractitioner"))
        

        button2 = tk.Button(self, text="Pediatre",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Pediatre"))
        
        
        button3 = tk.Button(self, text="Main page",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Mainpage"))
        button1.pack(side = "top",pady=10)
        button2.pack(side = "top",pady=10)
        button3.pack(side = "bottom",pady=10)


class GeneralPractitioner(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="General Practitioner", font="Castellar 36 bold italic",fg="brown",bg="darkturquoise")
        label.pack(side="top", pady=10)
		#self.photo5 = ImageTk.PhotoImage(Image.open("images"+S+"youssef.gif"))

        button1 = tk.Button(self,text="" ,height= 1,font=FONT,
                           command=lambda: controller.show_frame("Contact"))
        button1.pack(side = "top",pady=10)
        #photo2 = PhotoImage(file='/home/pi/Documents/robotdocteur/images/Logo-bouton-temperature.png')
        button2 = tk.Button(self,text="docteur 2",font=FONT,
                           command=lambda: controller.show_frame("Contact"))
        #button2.image=photo2
        #button2.pack(side = "top",pady=10)
        button2.config(height=1,width=20)
    
        
        button = tk.Button(self, text="Main page",height= 3,font=FONT,
                           command=lambda: controller.show_frame("Mainpage"))
        button.pack(side = "bottom",pady=10)

        
        button = tk.Button(self, text="Back",height= 3,font=FONT,
                           command=lambda: controller.show_frame("Specialite"))
        button.pack(side = "bottom",pady=10)
        
        


class Pediatre(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Doctor", font="Castellar 36 bold italic",fg="brown",bg="darkturquoise")
        label.pack(side="top", pady=10)

        button = tk.Button(self, text="Doctor1",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Contact"))
        button.pack(side = "top",pady=10)

        button = tk.Button(self, text="Docteur 2",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Contact"))
        button.pack(side = "top",pady=10)
        

        button = tk.Button(self, text="Main page",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Mainpage"))
        button.pack(side = "bottom",pady=10)
        
        button = tk.Button(self, text="Back",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Specialite"))
        button.pack(side = "bottom",pady=10)


class Contact(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Doctor x", font=TITLE_FONT)
        label.pack(side="top", pady=10)

        button = tk.Button(self, text="Send E-Mail",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Contactemail"))
        button.pack(side = "top",pady=10)

        button = tk.Button(self, text="Call Via Skype",height= 1,font=FONT,
                           command=lambda: self.skype())
        button.pack(side = "top",pady=10)
        

        button = tk.Button(self, text="Start Page",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Mainpage"))
        button.pack(side = "bottom",pady=10)
        
        button = tk.Button(self, text="Back",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Specialite"))
        button.pack(side = "bottom",pady=10)
        """ FOr windows 
    def skype(self):
        os.system("start \" C:\\Program Files (x86)\\Skype\\ \" skype.exe")
    """
    def skype(self):
        os.system("skypeforlinux")
        


class Contactemail(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Contact", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="Your @ :",font=FONT)
        label.pack(side="top", pady=10)

        mail=Entry(self).pack()

        label = tk.Label(self, text="Text :",font=FONT)
        label.pack(side="top", pady=10)
        
        text=Text(self,width=50,height=15,wrap=WORD).pack()
        
        Send = tk.Button(self,height= 1, text="Send",font=FONT)
        Send.pack()

        
        button = tk.Button(self, text="Main page",height= 1,font=FONT,
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side = "bottom",pady=10)
        
        button = tk.Button(self, text="Back",height= 1,font=FONT,
                           command=lambda: controller.show_frame("Pediatre"))
        button.pack(side = "bottom",pady=10)


if __name__ == "__main__":
    app = SampleApp()
    Tk.attributes(app,"-fullscreen",True)
    #app.maxsize(900	, 500)
    #app.minsize(1800, 900)
    app.title("E-Doctour") #Change title
    #app.iconbitmap(default="images"+S+"1.ico") #Change Icone
    app.mainloop()
