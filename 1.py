import tkinter as tk
from tkinter import messagebox
import sys
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
root=tk.Tk()
#root.geometry("400x400") - не нужно объявление постоянного размера доски
root.title("Крестики-нолики")
iconPath = resource_path('icon.ico')
root.iconbitmap(iconPath)

#----------Создание переменных------------#
buttons=[] #место сохранения кнопок
current_player="X" #первый ходит крестик

#----------Создание функций------------#
def reset_game(): #-функция сброса игры
    global current_player
    current_player="X" #Первый ходит X
    for button in buttons:
        button.config(text="",bg="SystemButtonFace")
def check_win(): #-функция проверки на победу
    win_comb = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Победные индексы по горизонтальным линиям
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # победные линии по вертикальным линиям
        [0, 4, 8], [2, 4, 6]              # Победные индексы диагональным линиям
    ]
    for i in win_comb:
        a,b,c=i
        if buttons[a]["text"]==buttons[b]["text"]==buttons[c]["text"]!="":
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")
            return True
    return False
def click(index): #-функция обработки клика
    global current_player #использование глобальной переменной
    #---Проверка, пустая ли кнопка---#
    if buttons[index]["text"]=="":
        buttons[index]["text"]=current_player #запись Х или 0
        if check_win():
            messagebox.showinfo("Победа!",f"Победил {current_player}")
        elif all(button["text"]!="" for button in buttons): #проверка на ничью
            messagebox.showinfo("Ничья!","Игра окончена ничьёй!")
    #----Менияю игрока----#
        else:
            if current_player=="X":
                current_player="0"
            else:
                current_player="X"

#----------Создание кнопок------------#
for i in range(9): #создание 9-и кнопок
    button=tk.Button(
        root,
        text="",
        font=("Arial",30), #Создание крупного шрифта
        width=5, #Ширина кнопки
        height=2, #Высота кнопки
        command=lambda idx=i: click(idx) #при клике вызывает функцию click(i)
    )
    button.grid(row=i//3,column=i%3) #размещение кнопки в сетке
    buttons.append(button) #добавление кнопки в список
reset_button=tk.Button(root,text="Новая игра",font=("Arial",14),command=reset_game) #создание кнопки "новая игра"
reset_button.grid(row=3,column=0,columnspan=3,sticky="we") #размещение кнопки под игровым полем
root.mainloop()
сема="семаf ghljmm,.hmmbnn,mvbb,.,l,.jlhb;jl/k.,/lg;k; ykrjtrtktmhjkl;kl;][oil,j.gg';[tpy[ypoi;p]]]"