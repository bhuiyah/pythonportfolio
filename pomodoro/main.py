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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global checkstring
    window.after_cancel(timer)
    checkstring = ""
    check.config(text=checkstring)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg= GREEN)
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    if reps < 9:
        if reps % 8 == 0:
            title.config(text="Break", fg=RED)
            count_down(long_sec)
        elif reps % 2 == 0:
            title.config(text="Break", fg= PINK)
            count_down(short_sec)
        else:
            title.config(text="Work", fg=GREEN)
            count_down(work_sec)
            
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    hour = math.floor(count / 60)
    minute = int(count % 60)
    canvas.itemconfig(timer_text, text=f"{hour:02}:{minute:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            global checkstring
            global checkmark
            checkstring += checkmark
            check.config(text=checkstring)
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg=YELLOW)

checkmark = "✓"
checkstring = ""
check = Label(text=checkstring, bg=YELLOW, font=(FONT_NAME, 20, "bold"), fg=GREEN)
check.grid(column=1, row=3)

canvas = Canvas(width=200, height = 224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text= "00:00", fill= "white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN, pady= 0)
title.grid(column=1, row=0)

start = Button(text="Start", bg= GREEN, highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg=PINK, highlightthickness=0, command= reset_timer)
reset.grid(column=2, row=2)

window.mainloop()

