import tkinter as tk
import pyglet
import sqlite3
import database_management as dm
#base 
root = tk.Tk()
root.title("Flash Card")
bg_color = "#E3FFD1"
#root.eval("tk::PlaceWindow . center")
root.geometry("1440x1024")
root.resizable(False, False)
#root.configure(bg = bg_color)

#font
pyglet.font.add_file(r"fonts\Lekton-Bold.ttf")
pyglet.font.add_file(r"fonts\Lekton-Italic.ttf")
pyglet.font.add_file(r"fonts\Lekton-Regular.ttf")


pyglet.font.load()
#frame
frame0 = tk.Frame(root,width=1440,height=1024,bg=bg_color)
frame1 = tk.Frame(root,width=1440,height=1024,bg=bg_color)

def clear_widget(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def load_frame1(before_frame):
    clear_widget(before_frame)
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
        command=lambda: load_frame0(frame1),
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
        relief="flat",
        
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

def load_frame0(before_frame):
    clear_widget(before_frame)
    frame0.tkraise()
    frame0.pack_propagate(False)
    # Store deck_photo as an attribute of frame1 because the gabage collector always clean data.
    frame0.deck_photo = tk.PhotoImage(file = r"assets\frame0\button_1.png")
    deck_button = tk.Button(
        frame0,
        image = frame0.deck_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: load_frame0(frame0),
        relief="flat"
    ).place(
        x=516.0,
        y=60.0,
        width=189.0,
        height=90.0
    )

    frame0.add_photo = tk.PhotoImage(file = r"assets\frame0\button_2.png")
    add_button = tk.Button(
        frame0,
        image = frame0.add_photo,
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

    frame0.deck_list_photo = tk.PhotoImage(file=r"assets\frame0\image_1.png")
    tk.Label(frame0, image=frame0.deck_list_photo ,bg = bg_color).place(
        x=405.0,
        y=236.0,
        width=630.0,
        height=702.0,
    )
    tk.Label(
        frame0,
        text="Deck List",
        anchor="nw",
        bg="#CCD5AE",
        fg="#737B58",
        font=("Lekton-Bold", 64 * -1)
        ).place(
        x=573.0,
        y=260.0
        )
    
    tk.Label(
        frame0,
        text="Name",
        anchor="nw",
        bg="#CCD5AE",
        fg="#737B58",
        font=("Lekton-Bold", 32 * -1)
        ).place(
        x=425.0,
        y=349.0
        )
    tk.Label(
        frame0,
        text="Total",
        anchor="nw",
        bg="#CCD5AE",
        fg="#737B58",
        font=("Lekton-Bold", 32 * -1)
        ).place(
        x=720.0,
        y=349.0
        )
    tk.Label(
        frame0,
        text="Learn",
        anchor="nw",
        bg="#CCD5AE",
        fg="#737B58",
        font=("Lekton-Bold", 32 * -1)
        ).place(
        x=817.0,
        y=349.0
        )
    tk.Label(
        frame0,
        text="Remain",
        anchor="nw",
        bg="#CCD5AE",
        fg="#737B58",
        font=("Lekton-Bold", 32 * -1)
        ).place(
        x=915.0,
        y=349.0
        )
    name_listbox = tk.Listbox(
        frame0,
        bg="#CCD5AE",
        cursor="hand2",
        font=("Lekton-Bold",32 * -1,),
        fg = "#737B58",
        bd = 0,
        #highlightcolor = "#CCD5AE",
        highlightthickness = 0,
        selectbackground = "#CCD5AE",
        selectborderwidth=0,
        #selectforeground="#737B58",
        activestyle="none",
        selectmode=tk.SINGLE
    )
    name_listbox.place(
        x=428,
        y=400,
        width=584,
        height=444,
    )
    def update_deck():
        table_name = dm.get_table_names()
        for i in table_name:
            total = dm.get_flashcard_count(i[0])
            learn = dm.count_rows_with_weight(i[0])
            word = "{:<19}{:<6}{:<6}{}".format(i[0], total,learn,total-learn)
            name_listbox.insert(tk.END, word)
    update_deck()
    def reset_click():
        selected_items = name_listbox.curselection()
        for index in selected_items:
            item = name_listbox.get(index)
            split1 = item.split()
            len = dm.get_flashcard_count(split1[0])*-2
            dm.reset_weight(split1[0],len)
            load_frame0(frame0)
    def rename_popup():
        popup = tk.Toplevel(
            frame0,
            bg = bg_color,
            height = 126,
            width=651,
            relief = "ridge"
            )
        popup.title("Rename")
        #popup.resizable(False, False)
        # Create an Entry widget in the pop-up window
        frame0.rename_popup_photo = tk.PhotoImage(file = r"assets\frame0\entry_1.png")
        tk.Label(
            popup,
            bd = 0,
            relief="flat",
            image=frame0.rename_popup_photo,
            activeforeground = bg_color,
            activebackground = bg_color,
            background=bg_color,
        ).place(
            x = 183.0,
            y = 15.0
        )
        entry = tk.Entry(
            popup,
            bd = 0,
            cursor = "hand2",
            font = ("Lekton-Bold",32 * -1),
            fg = "#737B59",
            relief="flat",
            bg="#CCD5AE"
            )
        entry.place(
            x=231.0,
            y=15.0,
            width=237.0,
            height=94.0
            )
        tk.Label(
            popup,
            text="New name:",
            font = ("Lekton-Bold",32 * -1),
            fg = "#737B59",
            relief="flat",
            activeforeground = bg_color,
            activebackground = bg_color,
            background=bg_color,
        ).place(
            x = 26,
            y = 35,
        )
        frame0.ok_button_photo = tk.PhotoImage(file = r"assets\frame0\entry_2.png")
        submit_button = tk.Button(
            popup,
            command=lambda :get_input(),
            image=frame0.ok_button_photo,
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2",
            relief="flat",
            background=bg_color,
            activeforeground = bg_color,
            activebackground = bg_color,
            ).place(
                x=531.0,
                y=15.0,
                width=96.0,
                height=96.0
            )
        selected_items = name_listbox.curselection()
        for index in selected_items:
            item = name_listbox.get(index)
            split1 = item.split()
            old_name = split1[0]
        def get_input():
            user_input = entry.get()
            converted_input = user_input.replace(" ", "_")
            if converted_input[0].isdigit():
                dm.rename_table(old_name,"not_start_by_number")
            else:
                dm.rename_table(old_name,converted_input[:18])
            load_frame0(frame0)
            popup.destroy()  # Close the pop-up window
        
        
    frame0.rename_photo = tk.PhotoImage(file = r"assets\frame0\button_3.png")
    rename_button = tk.Button(
        frame0,
        image = frame0.rename_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        bg = "#CCD5AE",
        command=lambda: rename_popup(),
        relief="flat",
        activeforeground = "#CCD5AE",
        activebackground = "#CCD5AE"
    ).place(
        x=531.0,
        y=868.0,
        width=126.0,
        height=43.0
    )
    frame0.start_photo = tk.PhotoImage(file = r"assets\frame0\button_4.png")
    start_button = tk.Button(
        frame0,
        image = frame0.start_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        bg = "#CCD5AE",
        #command=lambda: button_click(),
        relief="flat",
        activeforeground = "#CCD5AE",
        activebackground = "#CCD5AE"
    ).place(
        x=657.0,
        y=868.0,
        width=126.0,
        height=43.0
    )
    frame0.reset_photo = tk.PhotoImage(file = r"assets\frame0\button_5.png")
    reset_button = tk.Button(
        frame0,
        image = frame0.reset_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        bg = "#CCD5AE",
        command=lambda: reset_click(),
        relief="flat",
        activeforeground = "#CCD5AE",
        activebackground = "#CCD5AE"        
    ).place(
        x=783.0,
        y=868.0,
        width=126.0,
        height=43.0
    )
    
for frame in (frame0,frame1):
    frame.grid(row=0,column=0,sticky="nesw")


load_frame0(frame1)

root.mainloop()
