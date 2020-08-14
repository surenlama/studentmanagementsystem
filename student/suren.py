import tkinter 
import PIL
from PIL import Image

class Login_System:
    def _init_(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350*600+0+0")
        
root=tkinter.Tk()
obj=Login_System(root)
root.mainloop(obj)