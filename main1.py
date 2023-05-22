import tkinter as tk
import pyglet
import sqlite3
import database_management as dm
import heapq
from math import ceil
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

#frame
frame0 = tk.Frame(root,width=1440,height=1024,bg=bg_color)
frame1 = tk.Frame(root,width=1440,height=1024,bg=bg_color)
get_deck_name = tk.StringVar()
weight = tk.StringVar()
id = tk.StringVar()
font = tk.StringVar()
back = tk.StringVar()
font_type = tk.StringVar()
back_type = tk.StringVar()
all_card = tk.StringVar()
deck_name1 = tk.StringVar()    
def clear_widget(frame):
    for widget in frame.winfo_children():
        widget.destroy()
def load_deck_button(frame):
    frame.deck_photo = tk.PhotoImage(file = r"assets\frame0\button_1.png")
    deck_button = tk.Button(
        frame,
        image = frame.deck_photo,
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
def load_add_button(frame):
    frame.add_photo = tk.PhotoImage(file = r"assets\frame1\button_3.png")
    add_button = tk.Button(
        frame,
        image = frame.add_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: add_fuction(),
        relief="flat"
    ).place(
        x=735.0,
        y=60.0,
        width=189.0,
        height=90.0
    )
def alert_widget():
        alert_message = tk.Toplevel(
            frame0,
            bg = "#D4A373",
            height = 90,
            width=510,
            relief = "ridge"
        )
        tk.Label(
            alert_message,
            text = "Please select Deck",
            font = ("Lekton-Bold",40),
            anchor="nw",
            bg = "#D4A373",
            fg = "#7A5E43",
        ).place(
            x=20,
            y=20,
        )
def digit_alert_widget():
        alert_message = tk.Toplevel(
            frame0,
            bg = "#D4A373",
            height = 90,
            width=760,
            relief = "ridge"
        )
        tk.Label(
            alert_message,
            text = "Please start with a-z or A-Z",
            font = ("Lekton-Bold",40),
            anchor="nw",
            bg = "#D4A373",
            fg = "#7A5E43",
        ).place(
            x=20,
            y=20,
        )
def reset_alert_widget():
        alert_message = tk.Toplevel(
            frame0,
            bg = "#D4A373",
            height = 90,
            width=650,
            relief = "ridge"
        )
        tk.Label(
            alert_message,
            text = "Please reset the Deck",
            font = ("Lekton-Bold",40),
            anchor="nw",
            bg = "#D4A373",
            fg = "#7A5E43",
        ).place(
            x=20,
            y=20,
        )
def choose_deck_function():
    popup = tk.Toplevel(
            frame0,
            bg = bg_color,
            height = 774,
            width=699,
            relief = "ridge"
            )
    popup.title("choose deck")
    popup.resizable(False, False)
    
    frame0.deck_list_popup_photo = tk.PhotoImage(file = r"assets\frame0\deck_list.png")
    tk.Label(
        popup,
        bd = 0,
        relief="flat",
        image=frame0.deck_list_popup_photo,
        activeforeground = bg_color,
        activebackground = bg_color,
        background=bg_color,
    ).place(
        x = 35,
        y = 36
    )
    def return_selected():
        selected_items = name_listbox.curselection()
        for index in selected_items:
            item = name_listbox.get(index)
            get_deck_name.set(str(item))
            popup.destroy()
    frame0.select_button_popup_photo = tk.PhotoImage(file = r"assets\frame0\select.png")
    tk.Button(
        popup,
        command=lambda :return_selected(),
        image=frame0.select_button_popup_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        relief="flat",
        background="#CCD5AE",
        activeforeground = "#CCD5AE",
        activebackground = "#CCD5AE",
        ).place(
            x=287.0,
            y=671.0,
            width=126.0,
            height=43.0)
    name_listbox = tk.Listbox(
        popup,
        bg="#CCD5AE",
        cursor="hand2",
        font=("Lekton-Bold",32 * -1,),
        fg = "#737B58",
        bd = 0,
        highlightthickness = 0,
        selectbackground = "#CCD5AE",
        selectborderwidth=0,
        activestyle="none",
        selectmode=tk.SINGLE
    )
    name_listbox.place(
        x=58,
        y=193,
        width=584,
        height=444,
    )
    table_name = dm.get_table_names()
    for i in table_name:
        name_listbox.insert(tk.END, i[0])
def add_fuction():
    popup = tk.Toplevel(
            frame0,
            bg = bg_color,
            height = 768,
            width=1080,
            relief = "ridge"
            )
    
    popup.title("Add Flashcard")
    popup.resizable(False, False)
    frame0.font_popup_photo = tk.PhotoImage(file = r"assets\frame0\font.png")
    tk.Label(
        popup,
        bd = 0,
        relief="flat",
        image=frame0.font_popup_photo,
        activeforeground = bg_color,
        activebackground = bg_color,
        background=bg_color,
    ).place(
        x = 61.5,
        y = 165.75
    )
    frame0.back_popup_photo = tk.PhotoImage(file = r"assets\frame0\back.png")
    tk.Label(
        popup,
        bd = 0,
        relief="flat",
        image=frame0.back_popup_photo,
        activeforeground = bg_color,
        activebackground = bg_color,
        background=bg_color,
    ).place(
        x = 556.5,
        y = 165.75
    )
    frame0.choose_deck_popup_photo = tk.PhotoImage(file = r"assets\frame0\choose_deck.png")
    choose_deck_button = tk.Button(
        popup,
        command=lambda :choose_deck_function(),
        image=frame0.choose_deck_popup_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        relief="flat",
        background=bg_color,
        activeforeground = bg_color,
        activebackground = bg_color,
        )
    choose_deck_button.place(
            x=385.0,
            y=47.0,
            width=297.0,
            height=67.5
        )
    font_entry = tk.Text(
        popup,
        bd = 0,
        cursor = "hand2",
        font = ("Lekton-Bold",32),
        fg = "#737B59",
        relief="flat",
        bg="#CCD5AE",
        wrap="word"
        )
    font_entry.place(
        x=105.0,
        y=250.0,
        width=385.0,
        height=351.0
        )
    back_entry = tk.Text(
        popup,
        bd = 0,
        cursor = "hand2",
        font = ("Lekton-Bold",32),
        fg = "#7A5E43",
        relief="flat",
        bg="#D4A373",
        wrap="word"
        )
    back_entry.place(
        x=608.0,
        y=250.0,
        width=385.0,
        height=351.0
        )
    frame0.small_add_button_photo = tk.PhotoImage(file = r"assets\frame0\small_add.png")
    submit_button = tk.Button(
        popup,
        command=lambda : get_input(),
        image=frame0.small_add_button_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        relief="flat",
        background=bg_color,
        activeforeground = bg_color,
        activebackground = bg_color,
        )
    submit_button.place(
            x=490.0,
            y=680.0,
            width=116.0,
            height=55.0
        ) 
    def get_input():
        if get_deck_name.get()=="":
            alert_widget()
        else:
            table_name = get_deck_name.get()
            font_input = font_entry.get("1.0", tk.END).strip()
            back_input = back_entry.get("1.0", tk.END).strip()
            dm.add_flashcard(table_name,font_input,back_input)
            font_entry.delete("1.0", tk.END)
            back_entry.delete("1.0",tk.END)
    popup.protocol("WM_DELETE_WINDOW", get_deck_name.set(""))

def load_frame1(before_frame,heap):
    clear_widget(before_frame)
    frame1.tkraise()
    frame1.pack_propagate(False)
    
    load_deck_button(frame1)
    load_add_button(frame1)

    frame1.agian_photo = tk.PhotoImage(file=r"assets\frame1\button_5.png")
    agian_button = tk.Button(
        frame1,
        image = frame1.agian_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: calculator_click(weight.get(),0.05),
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
        command=lambda: calculator_click(weight.get(),0.25),
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
        command=lambda: calculator_click(weight.get(),0.5),
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
        command=lambda: calculator_click(weight.get(),0.75),
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
        command=lambda: calculator_click(weight.get(),1),
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
        command=lambda: reveal_it(back.get()),
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
    
    frame1.delete_button_photo = tk.PhotoImage(file=r"assets\frame1\deletebutton.png")
    delete_button = tk.Button(
        frame1,
        image = frame1.delete_button_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: delete_click(),
        relief="flat",
        bg = bg_color
    ).place(
        x=27.0,
        y=957.0,
        width=126.0,
        height=43.0
    )
    frame1.edit_button_photo = tk.PhotoImage(file=r"assets\frame1\editbutton.png")
    edit_button = tk.Button(
        frame1,
        image = frame1.edit_button_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: edit_click(),
        relief="flat",
        bg = bg_color
    ).place(
        x=1273.0,
        y=957.0,
        width=126.0,
        height=43.0
    )

    questions_text_box = tk.Text(   frame1,
                                    bd = 0,
                                    #cursor = "hand2",
                                    font = ("Lekton-Bold",32),
                                    fg = "#737B59",
                                    relief="flat",
                                    bg="#CCD5AE",
                                    wrap="word",
                                    state="disabled"
                                 )
    questions_text_box.place(
        x=122,
        y=320,
        width=535,
        height=463
    )
    reveal_text_box = tk.Text(   frame1,
                                    bd = 0,
                                    #cursor = "hand2",
                                    font = ("Lekton-Bold",32),
                                    fg = "#7A5E43",
                                    relief="flat",
                                    bg="#D4A373",
                                    wrap="word",
                                    state="disabled"
                                 )
    reveal_text_box.place(
        x=782,
        y=320,
        width=535,
        height=463
    )
    def fetch_data():
        if heap:
            cur = heapq.heappop(heap)
            #print(cur)
            weight.set(cur[0])
            id.set(cur[1])
            font.set(cur[2])
            back.set(cur[3])
            font_type.set(cur[4])
            back_type.set(cur[5])
        else:
            weight.set("")
            id.set("")
            font.set("")
            back.set("")
            font_type.set("")
            back_type.set("")
            load_frame0(frame1)
    fetch_data()
    
    def show_questions(data):
        try:
            questions_text_box.config(state="normal")
            questions_text_box.delete("1.0",tk.END)
            questions_text_box.insert(tk.END,data)
            questions_text_box.config(state="disabled")
            reveal_text_box.config(state="normal")
            reveal_text_box.delete("1.0",tk.END)
            reveal_text_box.config(state="disabled")
        except:
            pass
    show_questions(font.get())

    def reveal_it(data):
        reveal_text_box.config(state="normal")
        reveal_text_box.delete("1.0",tk.END)
        reveal_text_box.insert(tk.END,data)
        reveal_text_box.config(state="disabled")

    def edit_click():
        questions_text_box.config(state="normal")
        reveal_text_box.config(state="normal")
        popup = tk.Toplevel(
            frame1,
            bg = bg_color,
            height = 120,
            width=120,
            relief = "ridge"
            )
        popup.title("confirm button")
        popup.resizable(False, False)
        frame1.confirm_button = tk.PhotoImage(file = r"assets\frame0\entry_2.png")
        comfirm_button = tk.Button(
            popup,
            command=lambda :action(),
            image=frame1.confirm_button,
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2",
            relief="flat",
            background=bg_color,
            activeforeground = bg_color,
            activebackground = bg_color,
            ).place(
                x=12.0,
                y=12.0,
                width=96.0,
                height=96.0
            )
        
        def action():
            #print(deck_name1.get(),id.get(),questions_text_box.get("1.0", tk.END).strip(),reveal_text_box.get("1.0", tk.END).strip(),font_type.get(),back_type.get(),weight.get())
            dm.edit_flashcard(deck_name1.get(),id.get(),questions_text_box.get("1.0", tk.END).strip(),reveal_text_box.get("1.0", tk.END).strip(),font_type.get(),back_type.get(),weight.get())
            heapq.heappush(heap,(int(weight.get()),int(id.get()),questions_text_box.get("1.0", tk.END).strip(),reveal_text_box.get("1.0", tk.END).strip(),font_type.get(),back_type.get()))
            questions_text_box.config(state="disabled")
            reveal_text_box.config(state="disabled")
            popup.destroy()
            fetch_data()
            if len(heap) >= 0:
                show_questions(font.get())
    def Eliminate_excess(data):
        if data < 0:
            return True
        else:
            return False
    def calculator_click(weight,percent):
        new_weight = int(weight)+ceil(int(all_card.get())*percent)
        print(len(heap))
        if Eliminate_excess(new_weight):
            heapq.heappush(heap,(new_weight,id.get(),font.get(),back.get(),font_type.get(),back_type.get()))
            print("am here")
        dm.edit_flashcard(deck_name1.get(),id.get(),font.get(),back.get(),font_type.get(),back_type.get(),new_weight)
        fetch_data()
        print(len(heap))
        if len(heap) >= 0:
            show_questions(font.get())
    def delete_click():
        dm.delete_flashcard(deck_name1.get(),id.get())
        fetch_data()
        if len(heap) >=0:
            show_questions(font.get())
def load_frame0(before_frame):
    clear_widget(before_frame)
    frame0.tkraise()
    frame0.pack_propagate(False)
    # Store deck_photo as an attribute of frame1 because the gabage collector always clean data.
    load_deck_button(frame0)
    load_add_button(frame0)
    frame0.deck_list_photo = tk.PhotoImage(file=r"assets\frame0\image_1.png")
    tk.Label(frame0, image=frame0.deck_list_photo ,bg = bg_color).place(
        x=334.0,
        y=231.0,
        width=770.0,
        height=704.0,
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
        highlightthickness = 0,
        selectbackground = "#CCD5AE",
        selectborderwidth=0,
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
    def delete_click():
        selected_items = name_listbox.curselection()
        if selected_items == tuple():
            alert_widget()
        for index in selected_items:
            item = name_listbox.get(index)
            split1 = item.split()
            dm.delete_flashcard_table(split1[0])
            load_frame0(frame0)
    def reset_click():
        selected_items = name_listbox.curselection()
        if selected_items == tuple():
            alert_widget()
        for index in selected_items:
            item = name_listbox.get(index)
            split1 = item.split()
            len = dm.get_flashcard_count(split1[0])*-1
            dm.reset_weight(split1[0],len)
            load_frame0(frame0)
    def start_click():
        selected_items = name_listbox.curselection()
        if selected_items == tuple():
            alert_widget()
            return
        for index in selected_items:
            item = name_listbox.get(index)
            split1 = item.split()
            table_name = split1[0]
            deck_name1.set(table_name)
        if dm.get_flashcard_count(split1[0])-dm.count_rows_with_weight(split1[0]) == 0:
            reset_alert_widget()
            return
        else:
            flash_card_zone(dm.query_all_rows(table_name))
        
    def create_click():
        popup = tk.Toplevel(
            frame0,
            bg = bg_color,
            height = 126,
            width=651,
            relief = "ridge"
            )
        popup.title("Rename")
        popup.resizable(False, False)
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
        def get_input():
            user_input = entry.get()
            converted_input = user_input.replace(" ", "_")
            try:
                if converted_input[0].isdigit():
                    digit_alert_widget()
                else:
                    dm.create_flashcard_table(converted_input[:18])
                    load_frame0(frame0)
            except Exception as e:
                alert_widget()
            popup.destroy()
    def rename_popup():
        popup = tk.Toplevel(
            frame0,
            bg = bg_color,
            height = 126,
            width=651,
            relief = "ridge"
            )
        popup.title("Rename")
        popup.resizable(False, False)
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
            
            try:
                if converted_input[0].isdigit():
                    digit_alert_widget()
                else:
                    dm.rename_table(old_name,converted_input[:18])
                    load_frame0(frame0)
            except Exception as e:
                alert_widget()
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
        x=530.0,
        y=861.0,
        width=126.0,
        height=43.0
    )
    frame0.delete_photo = tk.PhotoImage(file = r"assets\frame0\delete.png")
    delete_button = tk.Button(
        frame0,
        image = frame0.delete_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        bg = "#CCD5AE",
        command=lambda: delete_click(),
        relief="flat",
        activeforeground = "#CCD5AE",
        activebackground = "#CCD5AE"
    ).place(
        x=404.0,
        y=861.0,
        width=126.0,
        height=43.0
    )
    frame0.create_photo = tk.PhotoImage(file = r"assets\frame0\button_7.png")
    create_button = tk.Button(
        frame0,
        image = frame0.create_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        bg = "#CCD5AE",
        command=lambda: create_click(),
        relief="flat",
        activeforeground = "#CCD5AE",
        activebackground = "#CCD5AE"
    ).place(
        x=908.0,
        y=861.0,
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
        command=lambda: start_click(),
        relief="flat",
        activeforeground = "#CCD5AE",
        activebackground = "#CCD5AE"
    ).place(
        x=656.0,
        y=861.0,
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
        x=782.0,
        y=861.0,
        width=126.0,
        height=43.0
    )
def flash_card_zone(all_row):
    heap = []
    for each in all_row:
        id_1 = each[0]
        font_1 = each[1]
        back_1 = each[2]
        font_type_1 = each[3]
        back_type_1 = each[4]
        weight_1 = each[5]
        if weight_1 < 0:
            heapq.heappush(heap,(weight_1,id_1,font_1,back_1,font_type_1,back_type_1))
    all_card.set(dm.get_flashcard_count(deck_name1.get()))
    load_frame1(frame0,heap)
for frame in (frame0,frame1):
    frame.grid(row=0,column=0,sticky="nesw")



load_frame0(frame0)
root.mainloop()
