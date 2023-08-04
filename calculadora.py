import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('320x330')
        self.resizable(0,0)
        self.title('calciuladora')
        self.iconbitmap('calculadora_icono.ico')
        self.expresion=''
        self.entrada=None
        self.entrada_texto=tk.StringVar()

        self._crear_componentes()

    def _crear_componentes(self):
        entrada_frame=tk.Frame(self, width=400, height=50, bg='grey',)
        entrada_frame.pack(side=tk.TOP)
        entrada=tk.Entry(entrada_frame, font=('arial', 18, 'bold'), textvariable=self.entrada_texto, width=24, justify=tk.RIGHT)
        entrada.grid(column=0, row=0, ipady=10)

        botonera= tk.Frame(self, width=400, height=450, bg='grey')
        botonera.pack()


        botonC=tk.Button(botonera, text='C',width=32, height=3,bd=0, bg='#eee',cursor='hand2',
                         command= self._boton_limpiar )
        botonC.grid(column=0, row=0, columnspan=3, padx=1, pady=1)

        boton_dividir=tk.Button(botonera, text='/',width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                                command= lambda:self._evento_click('/'))
        boton_dividir.grid(column=3, row=0 ,pady=1, padx=1)

        boton_7 = tk.Button(botonera, text='7', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click('7'))
        boton_7.grid(column=0, row=1, pady=1, padx=1)

        boton_8 = tk.Button(botonera, text='8', width=10, height=3, bd=0, bg='#FFF', cursor='hand2',
                            command=lambda: self._evento_click('8'))
        boton_8.grid(column=1, row=1, pady=1, padx=1)

        boton_9 = tk.Button(botonera, text='9', width=10, height=3, bd=0, bg='#FFF', cursor='hand2',
                            command=lambda: self._evento_click('9'))
        boton_9.grid(column=2, row=1, pady=1, padx=1)

        boton_multiplicar = tk.Button(botonera, text='x', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                            command=lambda: self._evento_click('*'))
        boton_multiplicar.grid(column=3, row=1, pady=1, padx=1)

        boton_4 = tk.Button(botonera, text='4', width=10, height=3, bd=0, bg='#FFF', cursor='hand2',
                            command=lambda: self._evento_click('4'))
        boton_4.grid(column=0, row=2, pady=1, padx=1)

        boton_5 = tk.Button(botonera, text='5', width=10, height=3, bd=0, bg='#FFF', cursor='hand2',
                            command=lambda: self._evento_click('5'))
        boton_5.grid(column=1, row=2, pady=1, padx=1)

        boton_6 = tk.Button(botonera, text='6', width=10, height=3, bd=0, bg='#FFF', cursor='hand2',
                            command=lambda: self._evento_click('6'))
        boton_6.grid(column=2, row=2, pady=1, padx=1)

        boton_restar = tk.Button(botonera, text='-', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                            command=lambda: self._evento_click('-'))
        boton_restar.grid(column=3, row=2, pady=1, padx=1)

        boton_1 = tk.Button(botonera, text='1', width=10, height=3, bd=0, bg='#FFF', cursor='hand2',
                            command=lambda: self._evento_click('1'))
        boton_1.grid(column=0, row=4, pady=1, padx=1)

        boton_2 = tk.Button(botonera, text='2', width=10, height=3, bd=0, bg='#FFF', cursor='hand2',
                            command=lambda: self._evento_click('2'))
        boton_2.grid(column=1, row=4, pady=1, padx=1)

        boton_3 = tk.Button(botonera, text='3', width=10, height=3, bd=0, bg='#FFF', cursor='hand2',
                            command=lambda: self._evento_click('3'))
        boton_3.grid(column=2, row=4, pady=1, padx=1)

        boton_sumar = tk.Button(botonera, text='+', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                            command=lambda: self._evento_click('+'))
        boton_sumar.grid(column=3, row=4, pady=1, padx=1)

        boton_0= tk.Button(botonera, text='0', width=21, height=3, bd=0, bg='#FFF', cursor='hand2',
                            command=lambda: self._evento_click('0'))
        boton_0.grid(column=0, row=5, columnspan=2, pady=1, padx=1)

        boton_punto = tk.Button(botonera, text='.', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                            command=lambda: self._evento_click('.'))
        boton_punto.grid(column=2, row=5, pady=1, padx=1)

        boton_igual = tk.Button(botonera, text='=', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                            command= self._evento_igual)
        boton_igual.grid(column=3, row=5, pady=1, padx=1)


    def _boton_limpiar(self):
        self.expresion=''
        self.entrada_texto.set(self.expresion)


    def _evento_click(self, evento):

        self.expresion=f'{self.expresion}{evento}'
        self.entrada_texto.set(self.expresion)

    def _evento_igual(self):
        try:
            if self.expresion:
                resultado=str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showinfo('error', f'ocurrio un error{e}')
            self.entrada_texto.set('')
        finally:
            self.expresion=''





if __name__=='__main__':
    calculadora=Calculadora()
    calculadora.mainloop()



