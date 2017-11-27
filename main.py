import tkinter
from TM1LoginGUI import Application
from TM1py import TM1Service

app = Application()
app.master.title=('Sample Application')
app.mainloop()

with TM1Service(address=app.TM1AddressEntry.get(), port=app.TM1PortEntry.get(), user=app.TM1UsernameEntry.get()
            , password=app.TM1PasswordEntry.get(), ssl=app.sslvar.get()) as tm1:

    cubelist=tm1.cubes.get_all_names()
    for cube in cubelist:
        print ("Cube name: ", cube)


# Get directory of TM1 instances
# The variable 'name', here, should be selected from a VBS script or something and fed as such.

