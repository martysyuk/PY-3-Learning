# import prityaz_support
#
# try:
#     from Tkinter import *
# except ImportError:
#     from tkinter import *
#
# try:
#     import ttk
#     py3 = 0
# except ImportError:
#     import tkinter.ttk as ttk
#     py3 = 1
#
#
# def vp_start_gui():
#     '''Starting point when module is the main routine.'''
#     global val, w, root
#     root = Tk()
#     prityaz_support.set_Tk_var()
#     top = gui_window(root)
#     prityaz_support.init(root, top)
#     root.mainloop()
#
#
# w = None
#
#
# def create_gui_window(root, *args, **kwargs):
#     '''Starting point when module is imported by another program.'''
#     global w, w_win, rt
#     rt = root
#     w = Toplevel (root)
#     prityaz_support.set_Tk_var()
#     top = gui_window (w)
#     prityaz_support.init(w, top, *args, **kwargs)
#     return (w, top)
#
#
# def destroy_gui_window():
#     global w
#     w.destroy()
#     w = None
#
#
# def calculate():
#     gui_window.Spinbox1 = 10
#     print('asd')
#
#
# class gui_window:
#     def __init__(self, top=None):
#         '''This class configures and populates the toplevel window.
#            top is the toplevel containing window.'''
#         _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
#         _fgcolor = '#000000'  # X11 color: 'black'
#         _compcolor = '#d9d9d9' # X11 color: 'gray85'
#         _ana1color = '#d9d9d9' # X11 color: 'gray85'
#         _ana2color = '#d9d9d9' # X11 color: 'gray85'
#
#         top.geometry("575x194+616+278")
#         top.title("Самооценка уровня притязания по методике Шварцландера ")
#         top.configure(background="#d9d9d9")
#         top.configure(height="175")
#         top.configure(highlightbackground="#f0f0f0f0f0f0")
#         top.configure(width="572")
#
#         self.Message1 = Message(top)
#         self.Message1.place(relx=0.3, rely=0.1, relheight=0.1, relwidth=0.41)
#         self.Message1.configure(background="#d9d9d9")
#         self.Message1.configure(foreground="#000000")
#         self.Message1.configure(highlightbackground="#d9d9d9")
#         self.Message1.configure(highlightcolor="black")
#         self.Message1.configure(text='''Введите данные данные исследования:''')
#         self.Message1.configure(width=237)
#
#         self.Labelframe1 = LabelFrame(top)
#         self.Labelframe1.place(relx=0.03, rely=0.31, relheight=0.34
#                 , relwidth=0.17)
#         self.Labelframe1.configure(relief=GROOVE)
#         self.Labelframe1.configure(foreground="black")
#         self.Labelframe1.configure(text='''1-я попытка''')
#         self.Labelframe1.configure(background="#d9d9d9")
#         self.Labelframe1.configure(width=100)
#
#         self.Spinbox1 = Spinbox(self.Labelframe1, from_=1.0, to=100.0)
#         self.Spinbox1.place(relx=0.1, rely=0.31, relheight=0.26, relwidth=0.85)
#         self.Spinbox1.configure(activebackground="#f9f9f9")
#         self.Spinbox1.configure(background="white")
#         self.Spinbox1.configure(buttonbackground="#d9d9d9")
#         self.Spinbox1.configure(disabledforeground="#a3a3a3")
#         self.Spinbox1.configure(foreground="black")
#         self.Spinbox1.configure(from_="1.0")
#         self.Spinbox1.configure(highlightbackground="black")
#         self.Spinbox1.configure(highlightcolor="black")
#         self.Spinbox1.configure(insertbackground="black")
#         self.Spinbox1.configure(selectbackground="#c4c4c4")
#         self.Spinbox1.configure(selectforeground="black")
#         self.Spinbox1.configure(textvariable='spinbox1')
#         self.Spinbox1.configure(to="100.0")
#         self.Spinbox1.configure(width=85)
#
#         self.Spinbox2 = Spinbox(self.Labelframe1, from_=1.0, to=100.0)
#         self.Spinbox2.place(relx=0.1, rely=0.62, relheight=0.26, relwidth=0.85)
#         self.Spinbox2.configure(activebackground="#f9f9f9")
#         self.Spinbox2.configure(background="white")
#         self.Spinbox2.configure(buttonbackground="#d9d9d9")
#         self.Spinbox2.configure(disabledforeground="#a3a3a3")
#         self.Spinbox2.configure(foreground="black")
#         self.Spinbox2.configure(from_="1.0")
#         self.Spinbox2.configure(highlightbackground="black")
#         self.Spinbox2.configure(highlightcolor="black")
#         self.Spinbox2.configure(insertbackground="black")
#         self.Spinbox2.configure(selectbackground="#c4c4c4")
#         self.Spinbox2.configure(selectforeground="black")
#         self.Spinbox2.configure(textvariable='spinbox2')
#         self.Spinbox2.configure(to="100.0")
#         self.Spinbox2.configure(width=85)
#
#         self.Labelframe2 = LabelFrame(top)
#         self.Labelframe2.place(relx=0.23, rely=0.31, relheight=0.34
#                 , relwidth=0.17)
#         self.Labelframe2.configure(relief=GROOVE)
#         self.Labelframe2.configure(foreground="black")
#         self.Labelframe2.configure(text='''2-я попытка''')
#         self.Labelframe2.configure(background="#d9d9d9")
#         self.Labelframe2.configure(highlightbackground="#d9d9d9")
#         self.Labelframe2.configure(highlightcolor="black")
#         self.Labelframe2.configure(width=100)
#
#         self.Spinbox3 = Spinbox(self.Labelframe2, from_=1.0, to=100.0)
#         self.Spinbox3.place(relx=0.1, rely=0.31, relheight=0.26, relwidth=0.85)
#         self.Spinbox3.configure(activebackground="#f9f9f9")
#         self.Spinbox3.configure(background="white")
#         self.Spinbox3.configure(buttonbackground="#d9d9d9")
#         self.Spinbox3.configure(disabledforeground="#a3a3a3")
#         self.Spinbox3.configure(foreground="black")
#         self.Spinbox3.configure(from_="1.0")
#         self.Spinbox3.configure(highlightbackground="black")
#         self.Spinbox3.configure(highlightcolor="black")
#         self.Spinbox3.configure(insertbackground="black")
#         self.Spinbox3.configure(selectbackground="#c4c4c4")
#         self.Spinbox3.configure(selectforeground="black")
#         self.Spinbox3.configure(textvariable='spinbox3')
#         self.Spinbox3.configure(to="100.0")
#
#         self.Spinbox4 = Spinbox(self.Labelframe2, from_=1.0, to=100.0)
#         self.Spinbox4.place(relx=0.1, rely=0.62, relheight=0.26, relwidth=0.85)
#         self.Spinbox4.configure(activebackground="#f9f9f9")
#         self.Spinbox4.configure(background="white")
#         self.Spinbox4.configure(buttonbackground="#d9d9d9")
#         self.Spinbox4.configure(disabledforeground="#a3a3a3")
#         self.Spinbox4.configure(foreground="black")
#         self.Spinbox4.configure(from_="1.0")
#         self.Spinbox4.configure(highlightbackground="black")
#         self.Spinbox4.configure(highlightcolor="black")
#         self.Spinbox4.configure(insertbackground="black")
#         self.Spinbox4.configure(selectbackground="#c4c4c4")
#         self.Spinbox4.configure(selectforeground="black")
#         self.Spinbox4.configure(textvariable='spinbox4')
#         self.Spinbox4.configure(to="100.0")
#
#         self.Labelframe3 = LabelFrame(top)
#         self.Labelframe3.place(relx=0.42, rely=0.31, relheight=0.34
#                 , relwidth=0.17)
#         self.Labelframe3.configure(relief=GROOVE)
#         self.Labelframe3.configure(foreground="black")
#         self.Labelframe3.configure(text='''3-я попытка''')
#         self.Labelframe3.configure(background="#d9d9d9")
#         self.Labelframe3.configure(highlightbackground="#d9d9d9")
#         self.Labelframe3.configure(highlightcolor="black")
#         self.Labelframe3.configure(width=100)
#
#         self.Spinbox5 = Spinbox(self.Labelframe3, from_=1.0, to=100.0)
#         self.Spinbox5.place(relx=0.1, rely=0.31, relheight=0.26, relwidth=0.85)
#         self.Spinbox5.configure(activebackground="#f9f9f9")
#         self.Spinbox5.configure(background="white")
#         self.Spinbox5.configure(buttonbackground="#d9d9d9")
#         self.Spinbox5.configure(disabledforeground="#a3a3a3")
#         self.Spinbox5.configure(foreground="black")
#         self.Spinbox5.configure(from_="1.0")
#         self.Spinbox5.configure(highlightbackground="black")
#         self.Spinbox5.configure(highlightcolor="black")
#         self.Spinbox5.configure(insertbackground="black")
#         self.Spinbox5.configure(selectbackground="#c4c4c4")
#         self.Spinbox5.configure(selectforeground="black")
#         self.Spinbox5.configure(textvariable='spinbox5')
#         self.Spinbox5.configure(to="100.0")
#
#         self.Spinbox6 = Spinbox(self.Labelframe3, from_=1.0, to=100.0)
#         self.Spinbox6.place(relx=0.1, rely=0.62, relheight=0.26, relwidth=0.85)
#         self.Spinbox6.configure(activebackground="#f9f9f9")
#         self.Spinbox6.configure(background="white")
#         self.Spinbox6.configure(buttonbackground="#d9d9d9")
#         self.Spinbox6.configure(disabledforeground="#a3a3a3")
#         self.Spinbox6.configure(foreground="black")
#         self.Spinbox6.configure(from_="1.0")
#         self.Spinbox6.configure(highlightbackground="black")
#         self.Spinbox6.configure(highlightcolor="black")
#         self.Spinbox6.configure(insertbackground="black")
#         self.Spinbox6.configure(selectbackground="#c4c4c4")
#         self.Spinbox6.configure(selectforeground="black")
#         self.Spinbox6.configure(textvariable='spinbox6')
#         self.Spinbox6.configure(to="100.0")
#
#         self.Labelframe4 = LabelFrame(top)
#         self.Labelframe4.place(relx=0.61, rely=0.31, relheight=0.34
#                 , relwidth=0.17)
#         self.Labelframe4.configure(relief=GROOVE)
#         self.Labelframe4.configure(foreground="black")
#         self.Labelframe4.configure(text='''4-я попытка''')
#         self.Labelframe4.configure(background="#d9d9d9")
#         self.Labelframe4.configure(highlightbackground="#d9d9d9")
#         self.Labelframe4.configure(highlightcolor="black")
#         self.Labelframe4.configure(width=100)
#
#         self.Spinbox7 = Spinbox(self.Labelframe4, from_=1.0, to=100.0)
#         self.Spinbox7.place(relx=0.1, rely=0.31, relheight=0.26, relwidth=0.85)
#         self.Spinbox7.configure(activebackground="#f9f9f9")
#         self.Spinbox7.configure(background="white")
#         self.Spinbox7.configure(buttonbackground="#d9d9d9")
#         self.Spinbox7.configure(disabledforeground="#a3a3a3")
#         self.Spinbox7.configure(foreground="black")
#         self.Spinbox7.configure(from_="1.0")
#         self.Spinbox7.configure(highlightbackground="black")
#         self.Spinbox7.configure(highlightcolor="black")
#         self.Spinbox7.configure(insertbackground="black")
#         self.Spinbox7.configure(selectbackground="#c4c4c4")
#         self.Spinbox7.configure(selectforeground="black")
#         self.Spinbox7.configure(textvariable='spinbox7')
#         self.Spinbox7.configure(to="100.0")
#
#         self.Spinbox8 = Spinbox(self.Labelframe4, from_=1.0, to=100.0)
#         self.Spinbox8.place(relx=0.1, rely=0.62, relheight=0.26, relwidth=0.85)
#         self.Spinbox8.configure(activebackground="#f9f9f9")
#         self.Spinbox8.configure(background="white")
#         self.Spinbox8.configure(buttonbackground="#d9d9d9")
#         self.Spinbox8.configure(disabledforeground="#a3a3a3")
#         self.Spinbox8.configure(foreground="black")
#         self.Spinbox8.configure(from_="1.0")
#         self.Spinbox8.configure(highlightbackground="black")
#         self.Spinbox8.configure(highlightcolor="black")
#         self.Spinbox8.configure(insertbackground="black")
#         self.Spinbox8.configure(selectbackground="#c4c4c4")
#         self.Spinbox8.configure(selectforeground="black")
#         self.Spinbox8.configure(textvariable='spinbox8')
#         self.Spinbox8.configure(to="100.0")
#
#         self.Button1 = Button(top)
#         self.Button1.place(relx=0.8, rely=0.36, height=51, width=95)
#         self.Button1.configure(activebackground="#d9d9d9")
#         self.Button1.configure(activeforeground="#000000")
#         self.Button1.configure(background="#d9d9d9")
#         # self.Button1.configure(command=calculate())
#         self.Button1.bind("<Button-1>", calculate())
#
#         self.Button1.configure(disabledforeground="#a3a3a3")
#         self.Button1.configure(foreground="#000000")
#         self.Button1.configure(highlightbackground="#d9d9d9")
#         self.Button1.configure(highlightcolor="black")
#         self.Button1.configure(pady="0")
#         self.Button1.configure(text='Расчитать')
#         self.Button1.configure(width=95)
#
#         self.Entry1 = Entry(top)
#         self.Entry1.place(relx=0.38, rely=0.77, relheight=0.1, relwidth=0.25)
#         self.Entry1.configure(background="white")
#         self.Entry1.configure(disabledforeground="#a3a3a3")
#         self.Entry1.configure(font="TkFixedFont")
#         self.Entry1.configure(foreground="#000000")
#         self.Entry1.configure(insertbackground="black")
#
#         self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
#         top.configure(menu = self.menubar)
#
# #
# if __name__ == '__main__':
#     vp_start_gui()

while True:
    up_c = input('Результаты через запятую (без пробелов):\n').rstrip().split(',')
    if up_c == ['']:
        exit(0)
    up_ball = ((int(up_c[2]) - int(up_c[1])) + (int(up_c[4]) - int(up_c[3])) + (int(up_c[6])) - int(up_c[5])) / 3
    up_ball = round(up_ball, 2)

    print(up_ball)
