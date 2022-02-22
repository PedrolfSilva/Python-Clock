from tkinter import*
import time
root = Tk()
root.title("DIGITAL CLOCK")
root.geometry("450x180+0+0")
root.config(bg = "#944c00")


def digiclock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
 
    if int(h) >= 12 and int(h) < 24 and int(m) >= 0:
        meridian.config(text = "PM")
    else:
        meridian.config(text = "AM")
    if int(h) > 12:
        h = str((int(h) - 12))
    elif int(h) == 0:
        h=str(12)

    hour.config(text = h)
    minute.config(text = m)
    second.config(text = s)
    hour.after(200, digiclock)

hour = Label(root, text = "12", font = ("radioland",50, "bold"), bg = "#944c00", fg = "#1cff8a")
hour.place(x = 110, y = 50, width = 100, height = 75)

colon = Label(root, text = ":", font = ("radioland", 40, "bold"), bg = "#944c00", fg = "#1cff8a")
colon.place(x = 170, y =70, width = 50, height = 35)

minute = Label(root, text = "6", font = ("radioland", 50, "bold"), bg = "#944c00", fg = "#1cff8a")
minute.place(x = 200, y = 50, width = 100, height = 75)

second = Label(root, text = "6", font = ("radioland", 10, "bold"), bg = "#944c00", fg = "#1cff8a")
second.place(x = 290, y = 30, width = 25, height = 25)

meridian = Label(root, text = "PM", font = ("radioland", 10, "bold"), bg = "#944c00", fg = "#1cff8a")
meridian.place(x = 290, y = 100, width = 30, height = 15) 


digiclock()
root.mainloop()