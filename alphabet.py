import tkinter as tk

# Данные о динозаврах
dinosaurs = [
    {"буква": "T", "название": "тираннозавр", "описание": "Один из крупнейших хищников Земли, известный мощными челюстями."},
    {"буква": "S", "название": "спинозавр", "описание": "Самый крупный из известных плотоядных динозавров, отличается высоким гребнем на спине."},
    {"буква": "C", "название": "стегозавр", "описание": "Растительноядный динозавр с костными пластинами вдоль спины и шипастым хвостом."},
    {"буква": "T", "название": "трицератопс", "описание": "Хищники называли его настоящим танком: крупные размеры, мощный череп с рогами."},
    {"буква": "V", "название": "велоцираптор", "описание": "Быстроходный охотник, знаменит своей высокой скоростью и смертоносными когтями."},
    {"буква": "B", "название": "брахиозавр", "описание": "Высокий гигант с невероятно длинной шеей и огромными размерами тела."}
]

# Цвета
bg_color = "#282c34"
fg_color = "#ffffff"
button_bg = "#61afef"
button_fg = "#282c34"
title_color = "#e06c75"

def create_main_window():
    global root
    root = tk.Tk()
    root.title("Энциклопедио Динозавры")
    root.geometry("500x400")
    root.configure(bg=bg_color) # устанавливаем цвет фона для root

def start_page():
    frame_start = tk.Frame(root, bg=bg_color)  # Задаём цвет фона для фрейма
    label = tk.Label(frame_start, text="Добро пожаловать в Энциклопедио!\n\nНажмите ниже, чтобы начать путешествие.",
                       font=('Helvetica', 16), fg=fg_color, bg=bg_color)
    label.pack(pady=(50, 20))
    btn_open = tk.Button(frame_start, text="Открыть энциклопедию", command=show_alphabet_screen,
                          bg=button_bg, fg=button_fg, relief=tk.RAISED, bd=2, font=('Helvetica', 12))
    btn_open.pack()
    frame_start.pack(fill=tk.BOTH, expand=True)

def show_alphabet_screen():
    # Уничтожаем предыдущий фрейм, если он существует
    for widget in root.winfo_children():
        widget.destroy()

    frame_letters = tk.Frame(root, bg=bg_color)
    letters = set([d["буква"] for d in dinosaurs])  # Уникальные буквы алфавита
    for i, ltr in enumerate(sorted(letters)):
        btn = tk.Button(frame_letters, text=ltr, command=lambda x=ltr: show_dinosaurs(x, frame_letters),
                           bg=button_bg, fg=button_fg, relief=tk.RAISED, bd=2, font=('Helvetica', 12))
        btn.grid(row=i//4, column=i%4, padx=10, pady=10)  # Использовать grid для расположения в виде сетки
    frame_letters.pack(fill=tk.BOTH, expand=True)


def show_dinosaurs(letter, frame_letters):
    # Уничтожаем предыдущий фрейм, если он существует
    frame_letters.destroy()

    frame_dinosaurs = tk.Frame(root, bg=bg_color)
    filtered_names = [d["название"] for d in dinosaurs if d["буква"] == letter]
    for name in filtered_names:
        btn = tk.Button(frame_dinosaurs, text=name.capitalize(), command=lambda n=name: show_description(n, frame_dinosaurs),
                           bg=button_bg, fg=button_fg, relief=tk.RAISED, bd=2, font=('Helvetica', 12))
        btn.pack(pady=5)
    frame_dinosaurs.pack(fill=tk.BOTH, expand=True)

def show_description(name, frame_dinosaurs):
    # Уничтожаем предыдущий фрейм, если он существует
    frame_dinosaurs.destroy()

    frame_descr = tk.Frame(root, bg=bg_color)
    title = tk.Label(frame_descr, text=name.capitalize(), font=('Helvetica', 18), fg=title_color, bg=bg_color) # меняем цвет title
    title.pack(pady=10)
    descr_text = ""  # Инициализируем пустой строкой
    for d in dinosaurs:
        if d["название"] == name:
            descr_text += f"{d['название'].capitalize()}:\n{d['описание']}"
            break # Если нашли описание, то выходим из цикла, нет необходимости продолжать поиск
    desc_label = tk.Label(frame_descr, text=descr_text, wraplength=400, justify=tk.LEFT, fg=fg_color, bg=bg_color, font=('Helvetica', 12)) # меняем цвет label
    desc_label.pack(pady=10)
    back_btn = tk.Button(frame_descr, text="Назад", command=lambda: [frame_descr.destroy(), show_alphabet_screen()],
                          bg=button_bg, fg=button_fg, relief=tk.RAISED, bd=2, font=('Helvetica', 12))
    back_btn.pack()
    frame_descr.pack(fill=tk.BOTH, expand=True)


create_main_window()
start_page()
root.mainloop()