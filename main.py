import tkinter
from GUI import Application
from TM1py import TM1Service

app = Application()
app.master.title=('Sample Application')
app.mainloop()

with TM1Service(address=app.TM1AddressEntry.get(), port=app.TM1PortEntry.get(), user=app.TM1UsernameEntry.get()
            , password=app.TM1PasswordEntry.get(), ssl=app.sslvar.get()) as tm1:

    cubelist=tm1.cubes.get_all_names()
    for cube in cubelist:
        print ("Cube name: ", cube)

### Simple cube list print. Parameters being used are:
### address = localhost, port = 8002, user = admin, password = '', ssl = True

