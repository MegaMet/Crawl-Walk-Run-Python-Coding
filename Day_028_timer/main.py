import datetime
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMAGE_PATH = "tomato.png"
CHECKMARK = "✓"

reps = 0
timer = None



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

    count_down(work_sec)
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_title.config(text="Break", fg= RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_title.config(text="Break", fg= PINK)
    else:
        count_down(work_sec)
        label_title.config(text="Work", fg= GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text= "%02d:%02d" % (count_min, count_sec))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += CHECKMARK
        label_checkmarks.config(text= mark)

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer")
    label_checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady= 20, padx= 50, bg= YELLOW)

canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness= 0)
image = PhotoImage(file= IMAGE_PATH)
canvas.create_image(100, 112, image= image)
timer_text = canvas.create_text(100, 130, text= "00:00", fill= "white", font= (FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label_title = Label(text="Timer", fg= GREEN, font= (FONT_NAME, 50, "bold"), bg= YELLOW)
label_title.grid(row= 0, column= 1)

label_checkmarks = Label(text="", fg= GREEN, font=(FONT_NAME, 20, "bold"), bg= YELLOW)
label_checkmarks.grid(row= 3, column= 1)

button_start = Button(text= "START", command= start_timer)
button_start.grid(row= 2, column= 0)

button_reset = Button(text= "RESET", command= reset_timer)
button_reset.grid(row= 2, column= 2)


window.mainloop()