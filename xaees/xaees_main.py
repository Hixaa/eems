import sys
from components.app import App
myapp = App()


try:
	myapp.run()
except:
    print("xaees App exited safely!")
    sys.exit()