from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_click():
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=205, height = 224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
canvas.create_text(103, 125, text="00:00", fill="white", font= (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_timer = Label(text="Timer", font= (FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

button_start = Button(text="Start", command=timer_click)
button_start.grid(column=0, row=2)

button_stop = Button(text="Stop", command=timer_click)
button_stop.grid(column=2, row=2)

label_timer = Label(text="v", font= (FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=3)

window.mainloop()
