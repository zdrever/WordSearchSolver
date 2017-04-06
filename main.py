import UI
from tkinter import *
from tkinter import filedialog
from chararray import CharArray
from foundword import FoundWord
import findwords 

# print("hello1")
# a = 0
# print("hello2")
# def gotonextfunction():
#     print("hello7")
#     #print("I'm here")
#     global a
#     a = a + 1
#     print(a)
#     return a
#
#
# print("hello3")
# print("a outside:  ", a)
if __name__ == "__main__":
    root = Tk()
    frame = Frame(width=1500, height=950, bg="", colormap="new")
    frame.pack()

    # print("hello5")
    # print("a inside:  ", a)
    #
    # if a == 0:
    #     print("hello6")
    # UI.startscreen(root,frame)
    # continue_button = Button(master = frame, text="Continue",font = (16), command = lambda : UI.continuetopage2)
    # continue_button.pack()
    # continue_button.place(relx=0.5, rely=0.6, anchor = "center")
    from UI import openfile
    wordarray, heightofarray, widthofarray = openfile()
    UI.printtextfiletoUI(wordarray, heightofarray, widthofarray, frame)
    #UI.highlightsolution((15,8), (1,0), 7, frame)
    # print("hello8")
    # #print("im here 2")
    # if a == 1:
    #     UI.continuetopage2(root, frame)
    # file_button = Button(master = root, text = "Choose File", font = 16, command = lambda : )
    # file_button.pack()
    # file_button.place(relx=0.5, rely=0.6, anchor="center")

    # print("hello9")


root.mainloop()
