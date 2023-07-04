from tkinter import *
import math
PINK = "#FF90BB"
RED = "#FF2171"
GREEN = "#8EAC50"
YELLOW = "#FFFAD7"
BLUE = "#C5DFF8"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", font=(
        FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
    check_label.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        cnt_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        cnt_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        cnt_down(work_sec)


def cnt_down(cnt):
    cnt_min = math.floor(cnt/60)
    cnt_sec = cnt % 60
    if cnt_sec < 10:
        cnt_sec = f"0{cnt_sec}"
    canvas.itemconfig(timer_text, text=f"{cnt_min}:{cnt_sec}")
    if cnt > 0:
        global timer
        timer = window.after(1000, cnt_down, cnt-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_label.config(text=marks)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(
    100, 100, text="00:00", fill=BLUE, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(
    FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

check_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)

window.mainloop()
