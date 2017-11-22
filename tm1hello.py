# This is just a preliminary test...like a "Hello world" on a local machine for the 
# tm1 application
#Get target cube and dimensions
import glob
from TM1py.Services import TM1Service


with TM1Service(address='localhost', port=8002, user='admin', password='', ssl=True) as tm1:
    c=tm1.cubes.get('WAC')
    print(c.name)
    print(c.dimensions)

# Get directory of TM1 instances
# The variable 'name', here, should be selected from a VBS script or something and fed as such.

print ('Named explicitly:')
for name in glob.glob('C:\TM1/*'):
    print ('\t', name)
