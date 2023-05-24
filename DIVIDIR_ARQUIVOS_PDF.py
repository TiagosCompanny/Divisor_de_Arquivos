from PySimpleGUI import PySimpleGUI as sg
import os
import shutil
from tkinter import filedialog
import fitz
import PyPDF2
from PyPDF2 import *
from tkinter import messagebox
import webbrowser


usuario = os.getlogin() #Importando nome do Usuiario
lista_numeros = [2, 4, 6, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,3,5,7,9]

#Link_linkledin//#referencia: https://stackoverflow.com/questions/66866390/in-pysimplegui-how-can-i-have-a-hyperlink-in-a-text-field
urls = {
    'Meu LinkedIn':'www.linkedin.com/in/tiagoscompanny',
}

items = sorted(urls.keys())#referencia: https://stackoverflow.com/questions/66866390/in-pysimplegui-how-can-i-have-a-hyperlink-in-a-text-field




# --------------------------INTERFACE GRAFICA--------------------------
sg.theme('LightGray')

layout = [


    [sg.Text("   🪓 DIVIDIR ARQUIVOS PDF 🪓""\n\n      ✂ ✂ ✂ ✂ ",
             font=('Arial', 16,'bold'), text_color='#3B8DDA',justification='center' ),
             sg.Image('ico.png')],

    [sg.Text("_____________________________________________________________")],

    [sg.Text("Arquivo:     "),
    sg.Input(key="caminho",font=('Arial', 8,), size=(40, 20)), sg.FileBrowse()],

    [sg.Text("Dividir em: "),
     sg. Combo(values=lista_numeros, key="partes",size=(3, 6))],

    [sg.Text("_____________________________________________________________")],
    
    [sg.Text("\n")],
    
    [sg.Button('DIVIDIR ARQUIVO', font=('Arial', 12),mouseover_colors = ("black", "#58E3FF"),
               size=(50, 2), key="repartir_arquivo")],

    [sg.Text(" ")],#Espaço

    [[sg.Text("By: Tiago H.S. Carvalho                                              ",font=('Calibre', 8,"bold")),
    sg.Image('logo_link_resized.png'),
    sg.Text(txt, tooltip=urls[txt], enable_events=True, font=('Arial', 10,'bold',"underline"), text_color="#0017FF",key=f'URL {urls[txt]}')] for txt in items] #referencia: https://stackoverflow.com/questions/66866390/in-pysimplegui-how-can-i-have-a-hyperlink-in-a-text-field
    

]


# Janela
janela = sg.Window('Tiago´s-Company Presents : DIVISOR DE ARQUIVOS', layout, size=(450, 380))
# Ler os eventos

while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos.startswith("URL "):#referencia: https://stackoverflow.com/questions/66866390/in-pysimplegui-how-can-i-have-a-hyperlink-in-a-text-field
        url = eventos.split(' ')[1] #referencia: https://stackoverflow.com/questions/66866390/in-pysimplegui-how-can-i-have-a-hyperlink-in-a-text-field
        webbrowser.open(url)#referencia: https://stackoverflow.com/questions/66866390/in-pysimplegui-how-can-i-have-a-hyperlink-in-a-text-field
    

    numero_paginas = PyPDF2.PdfFileReader(valores["caminho"]).numPages
# ------------------------------------------------------FUNTIONS----------------------------------------------

    def dividir_arquivo_():

        
        file = valores["caminho"]

        with open(file, 'rb') as f:
            numero_paginas = PyPDF2.PdfFileReader(f).numPages
    
        #Primeira divisão estática
        pdf = fitz.open(file)
        pdf2 = fitz.open()
        pdf2.insert_pdf(pdf, from_page=0, to_page=int(numero_paginas/valores["partes"]-1))
        pdf2.save("C:\\Users\\"+ usuario+"\\Desktop\\"+os.path.basename(file)+"_PARTE 1.pdf")
        num_partes = valores ["partes"]
        n = 0 #Trava

        while n < num_partes:

            pdf = fitz.open(file)
            pdf2 = fitz.open()
            pdf2.insert_pdf(pdf, from_page=int(numero_paginas/valores["partes"]*n), to_page=int((numero_paginas/valores["partes"])*(n+1)-1))
            pdf2.save("C:\\Users\\"+ usuario+"\\Desktop\\"+os.path.basename(file)+"_PARTE "+str(n+1)+".pdf")
            n = n+1

        
# ----------------------------------------------BOTÃO DIVIDIR ARQUIVO-----------------------------------------
    
    if eventos == 'repartir_arquivo':

        if valores["caminho"] == "" or valores["partes"] == "":
            messagebox.showinfo('AVISO', 'Preencha todas as informações \n ( ͡❛ ₒ ͡❛)') # put a error mesage

        elif numero_paginas < valores["partes"]:

            messagebox.showinfo('AVISO', "Você não pode dividir esse aquivo em "+str(valores["partes"])+" partes."+" Pois o PDF tem apenas "+str(numero_paginas)+" paginas"+
            "\n Tente dividir em menos partes\n ( ͡❛ ₒ ͡❛)") # put a error mesage
         
        else:
            dividir_arquivo_()
            
            
              
            
