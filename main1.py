import tkinter as tk

#base 
root = tk.Tk()
root.title("Flash Card")
bg_color = "#E3FFD1"
#root.eval("tk::PlaceWindow . center")
root.geometry("1440x1024")
root.resizable(False, False)
#root.configure(bg = bg_color)

#frame
frame0 = tk.Frame(root,width=1440,height=1024,bg=bg_color)
frame1 = tk.Frame(root,width=1440,height=1024,bg=bg_color)

def load_frame1():
    frame1.tkraise()
    frame1.pack_propagate(False)
    # Store deck_photo as an attribute of frame1 because the gabage collector always clean data.
    frame1.deck_photo = tk.PhotoImage(file = r"assets\frame1\button_2.png")
    deck_button = tk.Button(
        frame1,
        image = frame1.deck_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: print("deck_button_has_click"),
        relief="flat"
    ).place(
        x=516.0,
        y=60.0,
        width=189.0,
        height=90.0
    )

    frame1.add_photo = tk.PhotoImage(file = r"assets\frame1\button_3.png")
    add_button = tk.Button(
        frame1,
        image = frame1.add_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: print("add_button_has_click"),
        relief="flat"
    ).place(
        x=735.0,
        y=60.0,
        width=189.0,
        height=90.0
    )

    frame1.agian_photo = tk.PhotoImage(file=r"assets\frame1\button_5.png")
    agian_button = tk.Button(
        frame1,
        image = frame1.agian_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: print("again_button_has_click"),
        relief="flat"
    ).place(
        x=405.0,
        y=921.0,
        width=126.0,
        height=43.0
    )

    frame1.hard_photo = tk.PhotoImage(file=r"assets\frame1\button_6.png")
    hard_button = tk.Button(
        frame1,
        image = frame1.hard_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: print("hard_button_has_click"),
        relief="flat"
    ).place(
        x=531.0,
        y=921.0,
        width=126.0,
        height=43.0
    )

    frame1.medium_photo = tk.PhotoImage(file=r"assets\frame1\button_4.png")
    medium_button = tk.Button(
        frame1,
        image = frame1.medium_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: print("medium_button_has_click"),
        relief="flat"
    ).place(
        x=657.0,
        y=921.0,
        width=126.0,
        height=43.0
    )

    frame1.easy_photo = tk.PhotoImage(file=r"assets\frame1\button_7.png")
    easy_button = tk.Button(
        frame1,
        image = frame1.easy_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: print("easy_button_has_click"),
        relief="flat"
    ).place(
        x=783.0,
        y=921.0,
        width=126.0,
        height=43.0
    )

    frame1.remember_photo = tk.PhotoImage(file=r"assets\frame1\button_8.png")
    remember_button = tk.Button(
        frame1,
        image = frame1.remember_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: print("remember_button_has_click"),
        relief="flat"
    ).place(
        x=909.0,
        y=921.0,
        width=126.0,
        height=43.0
    )

    frame1.reveal_photo = tk.PhotoImage(file=r"assets\frame1\button_1.png")
    reveal_button = tk.Button(
        frame1,
        image = frame1.reveal_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: print("reveal_button_has_click"),
        relief="flat",
        bg = bg_color
    ).place(
        x=735.0,
        y=221.0,
        width=630.0,
        height=630.0
    )

    frame1.questtion_photo = tk.PhotoImage(file=r"assets\frame1\image_1.png")
    tk.Label(frame1, image=frame1.questtion_photo,bg = bg_color).place(
        x=75.0,
        y=221.0,
        width=630.0,
        height=630.0,
    )


for frame in (frame1,frame0):
    frame.grid(row=0,column=0,sticky="nesw")


load_frame1()

root.mainloop()
