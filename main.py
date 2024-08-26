from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():

  window.after_cancel(timer)
  canva.itemconfig(timer_text,text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    count_down(5 *60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  count_min = math.floor( count/60)
  count_sec =  count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"
  if count_min < 10:
    count_min = f"0{count_min}"
  canva.itemconfig(timer_text,text=f"{count_min}:{count_sec}")

  if count > 0:
    global timer
    timer = window.after(1000, count_down, count-1 )
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Timer App")
window.config(width=110, height=233, padx=100,pady=50, bg=YELLOW)
photo = PhotoImage(file="tomato.png")

lbl = Label(text = "Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,40,"bold"))
lbl.grid(column = 2, row = 0)


canva = Canvas(width=220, height=220, bg=YELLOW, highlightthickness=0)
canva.create_image(105,85, image=photo)
timer_text = canva.create_text(105,100, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canva.grid(column = 2, row = 2)



btn_start = Button(text="Start", command = start_timer)
btn_start.grid(column = 1, row= 3)

btn_reset = Button(text="Reset", command = reset_timer)
btn_reset.grid(column = 3, row= 3)

check_mark = Label(text="✔", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME,15,"bold"))
check_mark.grid(column=2, row=3)


window.mainloop()