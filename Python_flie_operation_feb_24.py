##class A(object):
##
##    def fun(self):
##        print("a")
##
##class B(A):
##
##    def fun(self):
##        print("b")
##
##class C(A):
##
##    def fun(self):
##        print("c")
##
##class D( c,B): #Multiple Inheritance
##
##    def fun1(self):
##        print("d")
##
##
##
##d = D()
##d.fun()

##Method Resolution Order
#It will give priority to the near by search (during 3.X version of python)
#During old of python i.e., 2.x search would have gone the deep search


##file_obj = open("devi.txt", "w")
##file_obj.write("hello")
##file_obj.close()

##file_obj.close() = open(r"c:\User\91897\Desktop\Netzert_Academy\Corporate_November\devi.txt", "w")
##file_obj.write("hello")
##file_obj.close()


import tkinter #GUI, Forms, Frames, Buttons, Labels
from tkinter import filedialog
import os

root = tkinter.Tk()
root.withdraw()

folder = filedialog.askdirectory()
print(folder)

file = os.path.join(folder,"devi.txt")

file_obj = open(file, "a")
file_obj.write("\n")
file_obj.write("bnbnbnbnbnbnbnbnbn")
file_obj.close()




