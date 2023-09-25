from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#eb4d4b"
RED = "#e7305b"
GREEN = "#9bdeac"
GREEN2 = "#618264"
YELLOW = "#f7f5dd"
BLUE = "#686de0"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(time_text, text="00:00")
    ticks.config(text='', font=(FONT_NAME, 20, 'bold'), fg=GREEN2, bg=YELLOW)
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        timer_label.config(text="Enjoy a long break", fg=GREEN)
        countdown(long_sec)
    elif REPS % 2 == 0:
        timer_label.config(text="Short break", fg=BLUE)
        countdown(short_sec)
    else:
        timer_label.config(text="Time to work", fg=RED)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        window.deiconify()  # Maximizes the window after the cycle is finished
        # Adding checkmarks after every work session
        if REPS > 0 and REPS % 2 == 0:
            ticks.config(text='🗸'*int(REPS/2), font=(FONT_NAME, 20, 'bold'), fg=GREEN2, bg=YELLOW)

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100, pady=50, bg=YELLOW)  # Spaces on the sides of the object

canvas = Canvas(width=200, height=224, bg=YELLOW,
                highlightthickness=0)  # Creating a canvas
tom_img = PhotoImage(file="tomato.png")  # Reading an image with PhotoImage, to use it with canvas object
canvas.create_image(100, 112, image=tom_img)  # Inserting img in canvas. Specifying x,y and img variable
time_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)


# Start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)


# Reset button
def reset():
    print("Reset")


reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

# Ticks
ticks = Label(fg=GREEN2, bg=YELLOW)
ticks.grid(column=1, row=3)


window.mainloop()
