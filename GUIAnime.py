# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:48:02 2021

@author: usuario
"""
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from mal import Anime, AnimeSearch
from PIL import ImageTk, Image
import os
import requests
import io

#Ventana
window = tk.Tk()
window.title("My AniManga app")

#Canvas
canvas = tk.Canvas(window, height= 600, width=500, bg='#263042')
canvas.pack()

#Cuadro de info
frame = tk.Frame(canvas, bg = 'White')
frame.place(relwidth=0.8, relheight=0.9, relx=0.1   , rely=0.2)

lbl = tk.Label(canvas, text="ANIME GUI")
lbl.pack(side='left')

#Pregunta
lbl1 = tk.Label(canvas, text="Hello, What are u looking 4?")
lbl1.pack(side='left')

#Cuadro de texto
txt = tk.Entry(canvas, width = 15)
txt.pack(side='right')

size = 30,20

filename = r'C:\Users\usuario\Desktop\MyData\My-AniManga-GUI\Toph.jpg'

image = Image.open(filename)
# The (450, 350) is (height, width)
image = image.resize((100, 70), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)

#my_img = tk.Label(frame, image = my_img)
#my_img.pack()

#img = ImageTk.PhotoImage(Image.open(filename))
#img = img.subsample(2, 2)

#Función obtener las 5 primeras coincidencias
def clicked():
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    anime = txt.get()
    search = AnimeSearch(anime)
    animes = []
    for i in range(5):
        animes.append(search.results[i].title)
    
    def info():
        for widget in frame.winfo_children():
            if isinstance(widget, Label):
                widget.destroy()

        
        selected = combo.get()
        index = 0
        
        for i in range(len(animes)):
            if selected == animes[i]:
                index = i

        anime_id = search.results[index].mal_id
        

        lbl_title = Label(frame, text = 'Title: ' + Anime(anime_id).title).pack()
        
        lbl_syp = Label(frame, text = 'Synopsis: ' + Anime(anime_id).synopsis[0:50]).pack()

        img_url = Anime(anime_id).image_url
        response = requests.get(img_url)
        image_bytes = io.BytesIO(response.content)
        
        img = Image.open(image_bytes)
        render = ImageTk.PhotoImage(img)
    
        img = Label(frame, image=render)
        img.image = render
        img.pack()
        
    btn_go = Button(frame, text='Info!!', command=info)
    btn_go.pack()
    
    #Combobox que hará display de las 5 primeras coincidencias
    box_value=StringVar()
    combo = Combobox(frame, textvariable = box_value)
    combo['values'] = animes
    combo.pack()
    
    

btn = Button(canvas, text='Search!!', command=clicked)

canvas.create_window(200, 25, window=lbl)
canvas.create_window(200, 50, window=lbl1)
canvas.create_window(350, 50, window=txt)
canvas.create_window(450, 50, window=btn)
canvas.create_image(60,70, image=my_img)


window.mainloop()