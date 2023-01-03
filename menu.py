from tkinter import *

class Menu_Entry(Entry):
    def __init__(self,perant,*args,**kwargs):
        Entry.__init__(self,perant,*args,**kwargs)
        self.popup_menu=Menu(self,tearoff=0,background='#1c1b1a',fg='white',
                                     activebackground='#534c5c',
                             activeforeground='Yellow')
        self.popup_menu.add_command(label="Cut                     ",command=self.Cut,
                                    accelerator='Ctrl+V')
        self.popup_menu.add_command(label="Copy                    ",command=self.Copy,compound=LEFT,
                                    accelerator='Ctrl+C')
    
        self.popup_menu.add_command(label="Paste                   ",command=self.Paste,accelerator='Ctrl+V')
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Select all",command=self.select_all,accelerator="Ctrl+A")
        self.popup_menu.add_command(label="Delete",command=self.delete_only,accelerator=" Delete")
        self.popup_menu.add_command(label="Delete all",command=self.delete_selected,accelerator="Ctrl+D")
        self.bind('<Button-3>',self.popup)
        self.bind("<Control-d>",self.delete_selected_with_e1)
        self.bind('<App>',self.popup)
        self.context_menu = Menu(self, tearoff=0)
        self.context_menu.add_command(label="Cut")
        self.context_menu.add_command(label="Copy")
        self.context_menu.add_command(label="Paste")
         
    def popup(self, event):
      try:
        self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
      finally:
        self.popup_menu.grab_release()

    def Copy(self):
      self.event_generate('<<Copy>>')

    def Paste(self):
      self.event_generate('<<Paste>>')

    def Cut(self):
      self.event_generate('<<Cut>>')

    def delete_selected_with_e1(self,event):
      self.select_range(0, END)
      self.focus()
      self.event_generate("<Delete>")

    def delete_selected(self):
      self.select_range(0, END)
      self.focus()
      self.event_generate("<Delete>")

    def delete_only(self):
      self.event_generate("<BackSpace>")

    def select_all(self):
      self.select_range(0, END)
      self.focus()


class Menu_Text(Text):
    def __init__(self,perant,*args,**kwargs):
        Text.__init__(self,perant,*args,**kwargs)
        self.popup_menu=Menu(self,tearoff=0,background='#1c1b1a',fg='white',
                                     activebackground='#534c5c',
                             activeforeground='Yellow')
        self.popup_menu.add_command(label="Cut                     ",command=self.Cut,
                                    accelerator='Ctrl+V')
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Copy                    ",command=self.Copy,compound=LEFT,
                                    accelerator='Ctrl+C')
    
        self.bind('<Button-3>',self.popup)
        self.bind('<App>',self.popup)
        self.context_menu = Menu(self, tearoff=0)
        self.context_menu.add_command(label="Cut")
        self.context_menu.add_command(label="Copy")
         
    def popup(self, event):
      try:
        self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
      finally:
        self.popup_menu.grab_release()

    def Copy(self):
      self.event_generate('<<Copy>>')

    def Cut(self):
      self.event_generate('<<Cut>>')

