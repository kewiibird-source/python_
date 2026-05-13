from tkinter import *

win = Tk()
win.geometry("300x300")
# 버튼
Button(win, text="클릭!", bg="yellow", fg="blue", width=80, height=3).pack()
# 텍스트 입력
Entry(win, text="클릭!", fg="blue", width=80).pack()
win.mainloop()