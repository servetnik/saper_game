from tkinter import *
import random

window = Tk()
window.geometry("800x900")
n = 1
m = 1
i1 = 0
b = 0
number = 0
rowk = 0
columnk = 0
red = '#ff5349'
green = '#19ff19'
game = True

kletki = []
pole = 88
mines = set(random.sample(range(0, 99), 10))
pkray = [9, 19, 29, 39, 49, 59, 69, 79, 89]
lkray = [10, 20, 30, 40, 50, 60, 70, 80]
vkray = [1, 2, 3, 4, 5, 6, 7, 8]
nkray = [91, 92, 93, 94, 95, 96, 97, 98]
ugly = [0, 9, 90, 99]

for f in range(1,11):
    window.grid_columnconfigure(f, minsize = 80)
    window.grid_rowconfigure(f, minsize = 60)

class Buttons():
    def __init__(self,number,row, column):
        self.number = number
        self.row = row #Строка
        self.column = column #Столбец
        self.color = '#ffffff'
        if self.number in pkray:
            self.around = [number-1, number-10, number+10, (number-10)-1, (number+10)-1]
        elif self.number in lkray:
            self.around = [number+1, number-10, number+10, (number-10)+1, (number+10)+1]
        elif self.number in vkray:
            self.around = [number-1, number+1, number+10, (number+10)+1,(number+10)-1]
        elif self.number in nkray:
            self.around = [number-1, number+1, number-10,(number-10)+1,(number-10)-1]
        elif self.number == 0:
            self.around = [number+1, (number + 10)+1, number+10]
        elif self.number == 9:
            self.around = [number-1, (number + 10)-1, number+10]
        elif self.number == 90:
            self.around = [number-10, (number - 10)+1, number+1]
        elif self.number == 99:
            self.around = [number-10, (number - 10)-1, number-1]    
        else:
            self.around = [number-1, number+1, number-10, number+10, (number-10)+1,
                           (number-10)-1, (number+10)+1,(number+10)-1]
            
        self.amountaround = 0
        if number == 99:
            for i in self.around:
                if i in mines:
                    self.amountaround += 1
            
        self.cheked = False
    def create_button(self):
        if self.cheked == True or self.number == 99:
            button = Button(text=(str(self.amountaround)),
                            command = lambda : click(self.number), background = "#d7d7d7")
        elif self.cheked == False:
            button = Button(text=(' '),
                            command = lambda : click(self.number), background = self.color)
        button.grid(row = self.row,column = self.column, stick = 'wens')
        
            
    def change_color(self, color):
        self.color = color
    def print_mines(self):
        for i in self.around:
            if i in mines:
                self.amountaround += 1
            self.cheked = True
                
def create_buttons():
    global n, m, kletki
    for i in range(0, 100):
        button = Buttons(i, n, m)
        kletki.append(button)
        kletki[i].create_button()
        m += 1
        if m % 11 == 0:
            n += 1
            m = 1
        
        
def click(number):
    global red
    global green
    global b
    global game
    global pole
    #print(kletki[number].row, kletki[number].column)
 
    if number in mines and game == True:
        for i in mines:
            kletki[i].change_color(red)
            kletki[i].create_button()
            game = False
    elif number not in mines and kletki[number].cheked == False and game == True and number != 99:
        while number not in mines and pole != 0 and kletki[number].cheked == False and game == True and number != 99:
            kletki[number].print_mines()
            kletki[number].create_button()
            number+=1
            pole -= 1
            print(pole)
    if pole == 0:
        for i in mines:
            kletki[i].change_color(green)
            kletki[i].create_button()
        game = False
        print('end')
        
                
           
print(mines)
print(pole)
create_buttons()
window.mainloop()