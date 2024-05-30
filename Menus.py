import subprocess
from User import User
from DbUtils import DbUtils
import time
import sys
try:
    import PySimpleGUI as sg
except:
    subprocess.check_call(["pip", "install", "PySimpleGUI==4.27.4"])
    import PySimpleGUI as sg

class Menu:
    
    def __init__(self, user):
        self.__run=True
        self.__user=None
        self.__db=DbUtils()
        self.__trys = 3
        self.__root = sg
    
    def login(self):
        while self.__trys>0:
            data=self.__db.getLogIn(self.values)
            if data:
                self.__user=User(data[0],data[1],data[2],data[3],data[4])
                if self.__user.admin():
                    self.admin()
                else:
                    self.votes()
            else:
                self.__trys-=1
                print(f"DNI invalido por favor vuelva a intentarlo\nIntentos restantes {self.__trys}")
                time.sleep(2)
    
    def layout(self, layout):
        self.window = self.__root.Window('Aplicacion de control de datos y estado de los empleados', layout)
             
    def ui(self, cabezera, texto):
        self.button = [  [self.__root.Text(cabezera)],
            [self.__root.Text(texto)],
            [self.__root.InputText()],
            [self.__root.Button('Enviar'), self.__root.Button('Salir')] ]
        self.layout(self.button)
        self.events()
                
    def votes(self):
        self.button[2] = self.__root.Button('dd')
        self.button.pop()
        self.button.append(self.__root.Button('csoe'))
        self.button.append(self.__root.Button('box'))
        self.button.append(self.__root.Button('personas'))
        self.button.append(self.__root.Button('lo conseguimos'))
        self.button.append(self.__root.Button('pac-man'))
        
        self.ui("Panel de Votacion", "Eligue a quien quieres votar")

    def admin(self):
        cabezera = [""]
        tabla = [   [self.root.Table(values=self.__db.getVotes(), 
                                     headings=cabezera,
                                     auto_size_columns=True,
                                     display_row_numbers=False,
                                     justification='center',
                                     row_height=35,
                                     num_rows = 8)],
            [self.root.Button('Salir')] ]
    
    def printVotes(self):
        votes=self.__db.getVotes()
        print(votes)
        
    def events(self):
        self.event, self.values = self.window.read()
        if self.event == self.root.WIN_CLOSED or self.event == 'Salir':
            self.window.close()
            sys.exit()
        elif self.event == 'Enviar':
            self.login()
        elif self.event == 'dd':
            self.__db.vote('dd')
        elif self.event == 'csoe':
            self.__db.vote('csoe')
        elif self.event == 'box':
            self.__db.vote('box')
        elif self.event == 'personas':
            self.__db.vote('personas')
        elif self.event == 'lo conseguimos':
            self.__db.vote('lo conseguimos')
        elif self.event == 'pac-man':
            self.__db.vote('pac-man')
            
        self.window.close()
        
    def run(self):
        self.events()
        self.ui("Login", "introduzca su DNI")