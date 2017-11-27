#Get target cube and dimensions


import tkinter as tk


#GUI for user input to login to the TM1 server.
#Should be used as the first user-facing side of the application.
#Currently, I just want to focus on getting replicate to work. Then,
#I would like to have a toolkit that has multiple useful TM1 tools that
#may or may not be readily available in TM1 Architect.
class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.grid()

    def createWidgets(self):
        top = self.winfo_toplevel()
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

        self.sslvar=tk.BooleanVar(value=True)
        self.TM1SSLLabel=tk.Label(self, text="Using SSL?")
        self.TM1SSLFALSE=tk.Radiobutton(self, text="False", variable=self.sslvar, value=False)
        self.TM1SSLTRUE=tk.Radiobutton(self, text="True", variable=self.sslvar, value=True)
        self.TM1SSLLabel.grid(column=1, row=5)
        self.TM1SSLFALSE.grid(column=7, row=6)
        self.TM1SSLTRUE.grid(column=7, row=7)

        self.submitButton=tk.Button(self, text="Submit", command=self.submitButton)
        self.submitButton.grid(column=10, row=9)

        self.quitButton=tk.Button(self, text="Quit", command=self.quit)
        self.quitButton.grid(column=1, row = 9)

    def submitButton(self):
        print(self.TM1AddressEntry.get())
        print(self.TM1PortEntry.get())
        print(self.TM1UsernameEntry.get())
        print(self.TM1PasswordEntry.get())
        print("%r" % (self.sslvar.get()))
