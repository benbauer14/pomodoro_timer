from tkinter import *
import time
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
timer_running = False


# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global timer_running
    timer_running = False
    canvas.itemconfig(canvas_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_click():
    global timer_running
    timer_running = True
    print(timer_running)
    countdown()

def update_canvas(minutes, seconds):
    canvas.itemconfig(canvas_text, text=f"{minutes}:{seconds}")
    canvas.update()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown():
    print("in") 
    seconds = 0
    session = 600
    session_count = 0
    print(timer_running)
    while timer_running == True:
        time.sleep(1)
        seconds += 1
        session_time_remaining = session - seconds
        print(session_time_remaining)
        #format time
        if(session_time_remaining <= 0):
            session_count += 1
            if(session_count == 2 or session_count == 4 or session_count == 6):
                session = 600
            elif(session_count == 8):
                session = 1200
            else:
                session = 1200


        if(session_time_remaining > 60):       
            minutes = int(math.floor(session_time_remaining / 60))
            second = session_time_remaining % 60
        else:
            second = session_time_remaining
        if(second < 10):
            second = "0" + str(second)
        else:
            second = str(second) 
        if(minutes < 10):
            minutes = "0" + str(minutes)
        else:
            minutes = str(minutes)

        update_canvas(minutes, second)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=205, height = 224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
canvas_text = canvas.create_text(103, 125, text="00:00", fill="white", font= (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_timer = Label(text="Timer", font= (FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

button_start = Button(text="Start", command=timer_click)
button_start.grid(column=0, row=2)

button_reset = Button(text="Stop", command=timer_reset)
button_reset.grid(column=2, row=2)

label_timer = Label(text="v", font= (FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=3)

window.mainloop()
