#!/usr/bin/env python

import tkinter as tk
#GUI for user input to login to the TM1 server.
#Should be used as the first user-facing side of the application.
#Currently, I just want to focus on getting replicate to work. Then,
# I would like to have a menu selection with different actions for TM1 that
# are not exactly native to TM1.
class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.grid()
        
    def createWidgets(self):
        top = self.winfo_toplevel()
        v = tk.IntVar()

        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.TM1AddressLabel=tk.Label(self, text="Enter TM1 Address: ")
        self.TM1AddressEntry=tk.Entry(self, textvariable=tk.StringVar)
        self.TM1AddressLabel.grid(column=1, row=1)
        self.TM1AddressEntry.grid(column=10, row=1)

        self.TM1PortLabel=tk.Label(self, text="Enter TM1 HTTPS Port: ")
        self.TM1PortEntry=tk.Entry(self, textvariable=tk.StringVar)
        self.TM1PortLabel.grid(column=1, row=2)
        self.TM1PortEntry.grid(column=10, row=2)

        self.TM1UsernameLabel=tk.Label(self, text="Enter server username: ")
        self.TM1UsernameEntry = tk.Entry(self, textvariable=tk.StringVar)
        self.TM1UsernameLabel.grid(column=1, row=3)
        self.TM1UsernameEntry.grid(column=10, row=3)

        self.TM1PasswordLabel=tk.Label(self, text="Enter server password: ")
        self.TM1PasswordEntry = tk.Entry(self, textvariable=tk.StringVar)
        self.TM1PasswordLabel.grid(column=1, row=4)
        self.TM1PasswordEntry.grid(column=10, row=4)

        self.TM1SSLLabel=tk.Label(self, text="Using SSL?")
        self.TM1SSLFALSE=tk.Radiobutton(self, text="False", variable=v, value=0)
        self.TM1SSLTRUE=tk.Radiobutton(self, text="True", variable=v, value=1)
        self.TM1SSLTRUE.deselect()
        self.TM1SSLFALSE.deselect()
        self.TM1SSLLabel.grid(column=1, row=5)
        self.TM1SSLFALSE.grid(column=10, row=8)
        self.TM1SSLTRUE.grid(column=10, row=7)
        ### Set Radio Buttons default to off-set

        if self.TM1SSLTRUE.select():
            self.TM1SSLFALSE.deselect()
        if self.TM1SSLFALSE.select():
            self.TM1SSLTRUE.deselect()
app = Application()
app.master.title=('Sample Application')
app.mainloop()

"""def GetUserInput():
    with f as



from TM1py.Services import TM1Service
with TM1Service(address='localhost', port=8002, user='admin', password='', ssl=True) as tm1:

    cubelist=tm1.cubes.get_all_names()
    for cube in cubelist:
        print ("Cube name: ", cube)


# Get directory of TM1 instances
# The variable 'name', here, should be selected from a VBS script or something and fed as such.

print ('Named explicitly:')
for name in glob.glob('C:\TM1/*'):
    print ('', name)"""
