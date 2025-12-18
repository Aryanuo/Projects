from tkinter import *

# ===================== FUNCTIONS =====================
def button_press(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except:
        equation_label.set("Error")
        equation_text = ""

def clear_all():
    global equation_text
    equation_text = ""
    equation_label.set("")

# ===================== WINDOW =====================
window = Tk()
window.title("Calculator")
window.geometry("360x520")
window.configure(bg="#0f172a")  # Deep dark blue
window.resizable(False, False)

equation_text = ""
equation_label = StringVar()

# ===================== DISPLAY =====================
display = Label(
    window,
    textvariable=equation_label,
    font=("Segoe UI", 26),
    bg="#1e293b",          
    fg="#e5e7eb",
    anchor="e",
    padx=15,
    height=2,
    bd=0,
    relief="flat"
)
display.pack(fill="both", padx=15, pady=18)

# ===================== BUTTON FRAME =====================
frame = Frame(window, bg="#0f172a")
frame.pack()

# ===================== GLASS BUTTON STYLES =====================
btn_num = {
    "bg": "#1e293b",
    "fg": "#e5e7eb",
    "activebackground": "#334155",
    "activeforeground": "white",
    "font": ("Segoe UI", 15),
    "width": 5,
    "height": 2,
    "bd": 0,
    "relief": "flat"
}

btn_op = {
    "bg": "#0ea5e9",       
    "fg": "white",
    "activebackground": "#38bdf8",
    "font": ("Segoe UI", 15),
    "width": 5,
    "height": 2,
    "bd": 0,
    "relief": "flat"
}

btn_eq = {
    "bg": "#22c55e",        
    "fg": "white",
    "activebackground": "#4ade80",
    "font": ("Segoe UI", 15),
    "width": 5,
    "height": 2,
    "bd": 0,
    "relief": "flat"
}

# ===================== NUMBER BUTTONS =====================
buttons = [
    (1, 0, 0), (2, 0, 1), (3, 0, 2),
    (4, 1, 0), (5, 1, 1), (6, 1, 2),
    (7, 2, 0), (8, 2, 1), (9, 2, 2),
    (0, 3, 0)
]

for (num, r, c) in buttons:
    Button(frame, text=num, command=lambda n=num: button_press(n), **btn_num)\
        .grid(row=r, column=c, padx=8, pady=8)

# ===================== OPERATORS =====================
Button(frame, text="+", command=lambda: button_press("+"), **btn_op).grid(row=0, column=3, padx=8, pady=8)
Button(frame, text="-", command=lambda: button_press("-"), **btn_op).grid(row=1, column=3, padx=8, pady=8)
Button(frame, text="*", command=lambda: button_press("*"), **btn_op).grid(row=2, column=3, padx=8, pady=8)
Button(frame, text="/", command=lambda: button_press("/"), **btn_op).grid(row=3, column=3, padx=8, pady=8)

Button(frame, text=".", command=lambda: button_press("."), **btn_num).grid(row=3, column=1, padx=8, pady=8)
Button(frame, text="=", command=equals, **btn_eq).grid(row=3, column=2, padx=8, pady=8)

# ===================== CLEAR BUTTON (Glass Red) =====================
Button(
    window,
    text="CLEAR",
    command=clear_all,
    bg="#ef4444",
    fg="white",
    activebackground="#f87171",
    font=("Segoe UI", 15),
    height=2,
    bd=0,
    relief="flat"
).pack(fill="x", padx=25, pady=18)

window.mainloop()
