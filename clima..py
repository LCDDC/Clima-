from tkinter import *
from PIL import Image
import requests
import time

class Ventana(Frame):
    def __init__(self, master, *args):
        super().__init__(master,  *args)
        self.click = True
        
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.frame = Frame(self.master, bg="white", highlightbackground="deep pink", highlightthickness=2)
        self.frame.grid(columnspan=3, row=0, sticky='nsew', padx=5, pady=5)
        
        self.frame1 = Frame(self.master, bg="SeaGreen1", highlightbackground="dark violet", highlightthickness=2)
        self.frame1.grid(column=0, row=1, sticky='nsew', padx=5, pady=5)
        
        self.frame2 = Frame(self.master, bg="SeaGreen1", highlightbackground="dark violet", highlightthickness=2)
        self.frame2.grid(column=1, row=1, sticky='nsew', padx=5, pady=5)
        
        self.frame3 = Frame(self.master, bg="SeaGreen1", highlightbackground="dark violet", highlightthickness=2)
        self.frame3.grid(column=2, row=1, sticky='nsew', padx=5, pady=5)
        
        self.frame4 = Frame(self.master, bg="SeaGreen1", highlightbackground="dark violet", highlightthickness=2)
        self.frame4.grid(column=0, row=2, sticky='nsew', padx=5, pady=5)
        
        self.frame5 = Frame(self.master, bg="SeaGreen1", highlightbackground="dark violet", highlightthickness=2)
        self.frame5.grid(column=1, row=2, sticky='nsew', padx=5, pady=5)
        
        self.frame6 = Frame(self.master, bg="SeaGreen1", highlightbackground="dark violet", highlightthickness=2)
        self.frame6.grid(column=2, row=2, sticky='nsew', padx=5, pady=5)
        
        self.widgets()
    
    def animacion(self):
        self.frame1.config(highlightbackground="red")
        self.frame2.config(highlightbackground="green")
        self.frame3.config(highlightbackground="blue")
        self.frame4.config(highlightbackground="orange")
        self.frame5.config(highlightbackground="violet")
        self.frame6.config(highlightbackground="pink")
        self.obtener_tiempo()
        gif = (Image.open("buscar.png"))
        if self.click == True:
            for i in range (1, frames):
                self.inicio = PhotoImage(file="buscar.png", format='gif -index %i' %(i))
                self.bt_inicio['image'] = self.inicio
                time.sleep(0.04)
                self.master.update()
                self.click = False
                if i+1==frames:
                    self.click = True
    def obtener_tiempo(self):
        ciudad = self.ingresa_ciudad.get()
        API = "http://api.openweathermap.org/data/2.5/weather?q="+ciudad+"&appid=6eb02bfdcc39cc8cf9ad8a494eb2bbcf"
        try:
            json_datos = requests.get(API).json()
    def widgets(self):
        self.inicio=PhotoImage(file = "buscar.png")
        self.clima=PhotoImage(file = "clima.png")
        self.menor=PhotoImage(file = "menor.png")
        self.mayor=PhotoImage(file = "mayor.png")
        self.humedad=PhotoImage(file = "humedad.png")
        self.viento=PhotoImage(file = "viento.png")
        self.presion=PhotoImage(file = "presion.png")
        
        self.bt_inicio = Button(self.frame, image=self.inicio,bg = "red", highlightthickness="0", activebackground="white", bd="0", command=self.animacion)
        self.bt_inicio.grid(column=0, row=0, padx=2, pady=2)
        
        
        self.ingresa_ciudad = Entry(self.frame, highlightbackground="DarkOrchid1", highlightcolor="green2", highlightthickness=2)
        self.ingresa_ciudad.grid(column=1, row=0)
        Label(self.frame, text="buscar", fg="gray55", bg="white").grid(column=2, row=0, padx=5)
        self.aviso=Label(self.frame, fg="gray55", bg="white").grid(column=3, row=0, padx=5)
        self.localidad=Label(self.frame, fg="gray55", bg="white").grid(column=3, row=0, padx=5)
        
        Label(self.frame1, text="Temperatura", bg="palegreen").pack(expand=True)
        Label(self.frame2, text="Temperatura Maxima", bg="palegreen").pack(expand=True)
        Label(self.frame3, text="Temperatura Minima", bg="palegreen").pack(expand=True)
        Label(self.frame4, text="Humedad", bg="palegreen").pack(expand=True)
        Label(self.frame5, text="Viento", bg="palegreen").pack(expand=True)
        Label(self.frame6, text="Presion", bg="palegreen").pack(expand=True)
        
        Label(self.frame1, image=self.clima, bg="palegreen").pack(expand=True, side="left")
        Label(self.frame2, image=self.mayor, bg="palegreen").pack(expand=True, side="left")
        Label(self.frame3, image=self.menor, bg="palegreen").pack(expand=True, side="left")
        Label(self.frame4, image=self.humedad, bg="palegreen").pack(expand=True, side="left")
        Label(self.frame5, image=self.viento, bg="palegreen").pack(expand=True, side="left")
        Label(self.frame6, image=self.presion, bg="palegreen").pack(expand=True, side="left")
        
        

if __name__ == "__main__":
    ventana = Tk()
    ventana.title("")
    ventana.config(bg="white")
    ventana.minsize(height=300, width=500)
    ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file="clima.png"))
    ventana.geometry("500x300+180+80")
    app = Ventana(ventana)
    app.mainloop()