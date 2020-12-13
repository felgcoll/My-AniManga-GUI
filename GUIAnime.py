# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:56:39 2020

@author: felgcoll
"""

#Se importan librerías a utilizar
from tkinter import *
from tkinter.ttk import *
from mal import Anime, AnimeSearch
from PIL import ImageTk, Image
import os
import requests
import io


#Abrir ventana
window = Tk()

#Título de la ventana
window.title("My AniManga app")

#Geometría de la ventana
window.geometry('500x400')

#Lbl con un título de bienvenida
lbl = Label(window, text="Hello, What are u looking 4?")
#Ubicación
lbl.grid(column=0, row=0)

#Cuadro de texto para ingresar la búsqueda
txt = Entry(window, width = 15)
#Ubicación
txt.grid(column=1, row=0)

#Función del boton que va a buscar los 5 resultados más similares
def clicked():
    #Se obtiene el texto ingresado
    anime = txt.get()
    #Se utiliza la api para poder encontrar los resultados
    search = AnimeSearch(anime)
    #Se crea una lista para guardar los resultados
    animes = []
    #Se recorren las 5 primeras coincidencias de la búsqueda
    #Se pueden colocar más, pero el tiempo de request realentiza la operación
    for i in range(5):
        #Se guardan los resultados
        animes.append(search.results[i].title)
    
    #Funcion que va a hacer el display de la informacion del anime seleccionado
    def info():
        #Se obtiene el resultado seleccionado
        selected = combo.get()
        #Se hace el set de un índice que posteriormente va a permitir buscar el anime
        index = 0
        #Se recorre la lista de los nombres de los animes para encontrar su indice
        for i in range(len(animes)):
            if selected == animes[i]:
                index = i
        
        #Con el índice encontrado, es posible encontrar el id con el que
        #se encuentra guardado en la librería, este id nos permitirá acceder
        #a gran cantidad de información que posiblemente requeira la persona
        anime_id = search.results[index].mal_id
        
        #Se accede a diferente tipo de información, como lo son el título,
        #Synopsis, género, tipo, rating, puntuación, rank, animes relacionados, etc
    
        #Dentro de la nueva ventanda se definen lo que son diferentes labels
        #Se crea una nueva ventana

        
        #root.geometry('500x400')
        #Para el título
        lbl_title = Label(window)
        lbl_title.grid(column=0, row=3)
        lbl_title.configure(text = 'Title: ' + Anime(anime_id).title)
        
        #Sinopsis
        lbl_syp = Label(window)
        lbl_syp.grid(column=0, row=4)
        lbl_syp.configure(text = 'Synopsis: ' + Anime(anime_id).synopsis[0:50])
        
        #Imagen
        img_url = Anime(anime_id).image_url
        response = requests.get(img_url)
        image_bytes = io.BytesIO(response.content)
        
        img = Image.open(image_bytes)
        render = ImageTk.PhotoImage(img)
    
        img = Label(window, image=render)
        img.image = render
        img.grid(column=0, row=5)


    
    #Una vez dado click se crean los siguientes widgets
    #Boton para poder obtener la información
    btn_go = Button(window, text='Info!!', command=info)
    btn_go.grid(column=3, row=2)
    
    #Combobox que hará display de las 5 primeras coincidencias
    box_value=StringVar()
    combo = Combobox(window, textvariable = box_value)
    combo.grid(column=0, row=2)
    combo['values'] = animes

#Boton que va a realizar la busqueda del anime
btn = Button(window, text='Search!!', command=clicked)
#Ubicación
btn.grid(column=3, row=0)

#Loop de la ventana
window.mainloop()
