import subprocess
import sys
from User import User
from DbUtils import DbUtils
try:
    import PySimpleGUI as sg
except:
    subprocess.check_call(["pip", "install", "PySimpleGUI==4.27.4"])
    import PySimpleGUI as sg

class Menu:
    
    def __init__(self):
        self.__run = True
        self.__user = None
        self.__db = DbUtils()
        self.__root = sg
    
    def login(self):
        data = self.__db.getLogIn(self.values)
        print(data)
        if data:
            self.__user = User(data[0], data[1], data[2], data[3], data[4])
            if self.__user.admin():
                self.admin()
            else:
                self.votes()
        else:
            self.ui()
    
    def layout(self, layout):
        self.window = self.__root.Window('Aplicacion de control de datos y estado de los empleados', layout)
             
    def ui(self):
        layout = [
            [self.__root.Text("Login")],
            [self.__root.Text("introduzca su DNI")],
            [self.__root.InputText()],
            [self.__root.Button('Enviar'), self.__root.Button('Salir')]
        ]
        self.layout(layout)
        self.events()
                
    def votes(self):
        layout = [
            [self.__root.Text("Panel de Votacion")],
            [self.__root.Text("Elige a quien quieres votar")],
            [self.__root.Button('dd')],
            [self.__root.Button('csoe')],
            [self.__root.Button('box')],
            [self.__root.Button('personas')],
            [self.__root.Button('lo conseguimos')],
            [self.__root.Button('pac-man')]
        ]
        self.layout(layout)
        self.events()
        
    def admin(self):
        cabezera = ["id", "voto", "fecha", "hash", "preshash"]
        tabla = [
            [self.__root.Table(values=self.__db.getVotes(), 
                               headings=cabezera,
                               auto_size_columns=True,
                               display_row_numbers=False,
                               justification='center',
                               row_height=35,
                               num_rows=8)],
            [self.__root.Button('Salir')]
        ]
        self.layout(tabla)
        self.events()
    
    def printVotes(self):
        votes = self.__db.getVotes()
        print(votes)
        
    def events(self):
        self.event, self.values = self.window.read()
        if self.event == self.__root.WIN_CLOSED or self.event == 'Salir':
            self.window.close()
            sys.exit()
        elif self.event == 'Enviar':
            self.login()
        elif self.event in ['dd', 'csoe', 'box', 'personas', 'lo conseguimos', 'pac-man']:
            self.__db.vote(self.event)
            
        self.window.close()
        
    def run(self):
        self.ui()
        self.events()

menu = Menu()
menu.run()