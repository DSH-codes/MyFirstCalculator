from tkinter import *


from tkinter.tix import *

import os

import sys



sys.path.append("C:\\ProgramData\\")

full = os.path.join("C:\\ProgramData", "FW_Calculator_settings.py") # This helps you to create a file, a text file for example, into another directory of the system


try:
    settings_variables = open(full, "x") # with x it will create a file if there is no file with such name, else it will raise FileExistsError
    settings_variables.write("# this file is settings log for Quick_calculator!\n")
    settings_variables.write("# It is not a malware or trojan file! So do not delete it!\n")
    settings_variables.write("# If you do, the setting of the calculator will be restored to default!\n")
    settings_variables.write("last_theme = None\n")
    settings_variables.write("last_button_color = None\n")
    settings_variables.write("last_rounding = None\n")
    settings_variables.write("last_language = None\n")
    settings_variables.close()
except (ValueError, FileExistsError):
    pass


import FW_Calculator_settings as sv



root = Tk()
root.title(" " * 45 + "Calculator 1. 0. 0")
root.geometry('503x550')
root.resizable(0, 0)
root.config(bg = sv.last_theme)
size = 0  # 0 for closed condition, 1 for opened - wide condition when settings part is visible


if sv.last_rounding:
    round_till = sv.last_rounding
else:
    round_till = 2  # here I keep a variable to define how short the app has to round a division result



info_message = Balloon(root)  # Balloon message widget for the outer scope


def open_settings():
    global size
    global root
    if size == 0:
        root.geometry("840x550")
        size = 1
    else:
        root.geometry("503x550")
        size = 0


def set_russian():
    """setting all available buttons and balloon messages into russian language"""
    globals()["button_white_theme"].config(text=globals()["светлая_тема"])
    globals()["button_dark_theme"].config(text=globals()["темная_тема"])
    globals()["language_button_rus"].config(text=globals()["русский_язык"])
    globals()["language_button_eng"].config(text=globals()["английский_язык"])
    globals()["user_theme_button"].config(text=globals()["применить"])
    globals()["buttons_active_bg_button"].config(text=globals()["применить"])
    globals()["round_button"].config(text=globals()["округлить_до"])
    globals()["the_company_label"].config(text=globals()["компания"])
    globals()["info_message"].bind_widget(globals()["settings_button"], balloonmsg=globals()["кнопка_настройки_б"])
    globals()["info_message"].bind_widget(globals()["button_divide"], balloonmsg=globals()["деление_без_остатка_б"])
    globals()["info_message"].bind_widget(globals()["user_theme_button"], balloonmsg=globals()["рбг_тема_б"])
    globals()["info_message"].bind_widget(globals()["buttons_active_bg_button"],
                                          balloonmsg=globals()["ргб_тема_кнопки_нажатие_б"])
    globals()["info_message"].bind_widget(globals()["round_button"], balloonmsg=globals()["округление_б"])
    globals()["g_mistake_in_a_math_expression_or_letters"] = globals()["ошибка_в_математическом_выражении_или_буквы"]
    globals()["g_setting_label_error"] = globals()["ошибка_в_настройках"]
    with open(full, "a") as f:
        f.write("last_language = 'R'\n")


def set_english():
    """setting all available buttons and balloon messages into russian language"""
    globals()["button_white_theme"].config(text=globals()["white_theme"])
    globals()["button_dark_theme"].config(text=globals()["black_theme"])
    globals()["language_button_rus"].config(text=globals()["russian_language"])
    globals()["language_button_eng"].config(text=globals()["english_language"])
    globals()["user_theme_button"].config(text=globals()["s_apply"])
    globals()["buttons_active_bg_button"].config(text=globals()["s_apply"])
    globals()["round_button"].config(text=globals()["round_till_"])
    globals()["the_company_label"].config(text=globals()["company"])
    globals()["info_message"].bind_widget(globals()["settings_button"], balloonmsg=globals()["button_setting_b"])
    globals()["info_message"].bind_widget(globals()["button_divide"],
                                          balloonmsg=globals()["division_with_no_remainder_b"])
    globals()["info_message"].bind_widget(globals()["user_theme_button"], balloonmsg=globals()["rgb_theme_b"])
    globals()["info_message"].bind_widget(globals()["buttons_active_bg_button"],
                                          balloonmsg=globals()["rgb_theme_for_buttons_active_b"])
    globals()["info_message"].bind_widget(globals()["round_button"], balloonmsg=globals()["rounding_b"])
    globals()["g_mistake_in_a_math_expression_or_letters"] = globals()["mistake_in_a_math_expression_or_letters"]
    globals()["g_setting_label_error"] = globals()["setting_label_error"]
    with open(full, "a") as f:
        f.write("last_language = 'E'\n")


# Все русские сообщения начинаются здесь
# буква _б добавлена в конце чтобы отличать переменные в которых сообщения для баллун мессенджей

ошибка_в_математическом_выражении_или_буквы = "Пожалуйста используйте только цифры\nили доступные символы приложения\nизбегайте ошибок в выражении"
компания = "FreeWind Interactive © 2022\nВсе права защищены"
светлая_тема = "Светлая тема"
темная_тема = "Темная тема"
русский_язык = "Русский язык"
английский_язык = "Английский язык"
применить = "Применить"
округлить_до = "Округлить до..."
ошибка_в_настройках = "Введите что-нибудь! HTML название цвета,\n RGB код, или цифру для округления!\nПроверьте правильность введенного\n HTML цвета и RGB кода"

кнопка_настройки_б = "НАСТРОЙКИ\n"
деление_без_остатка_б = "Добавьте этот знак дважды, чтобы получить деление без остатка!\n"  # finish this
округление_б = "Округлить результат деление после точки\nбазовый = 2, не ниже чем = 1, не выше = 16\n"
ргб_тема_кнопки_нажатие_б = "Добавьте цвет для кнопок при нажатии используя доступные РГБ коды к примеру как -> #FFCCE5\nили доступные html цвета\n"
рбг_тема_б = "Добавьте свою РГБ тему используя доступные коды к примеру как -> #FFCCE5\nили доступные html цвета\n"

# All english messages start here
# The _b letter added to distinguish variables which contain messages for the balloon messages

mistake_in_a_math_expression_or_letters = "Please use only digits and \navailable symbols of app's keyboard\nand avoid mistakes in your expressions"
company = "FreeWind Interactive © 2022\nAll rights reserved"
white_theme = "White theme"
black_theme = "Black theme"
russian_language = "Russian language"
english_language = "English language"
s_apply = "Apply"
round_till_ = "Round till..."

button_setting_b = "SETTINGS"
rgb_theme_for_buttons_active_b = "Apply button's push highlight color using RGB code like - > #FFCCE5\nor an available html color name"
rgb_theme_b = "Apply your theme using RGB code like - > #FFCCE5\nor an available html color name"
rounding_b = "Round the fractional result after the dot\ndefault = 2, lowest = 1, highest = 16"
division_with_no_remainder_b = "Add this symbol twice to get division with no remainder!\n"
setting_label_error = "Enter something! An HTML color name,\n RGB code or a value for rounding\n Make sure your HTML color name\n and RGB code are correct!"

# All global messages start here
g_mistake_in_a_math_expression_or_letters = mistake_in_a_math_expression_or_letters
g_company = company
g_setting_label_error = setting_label_error




def theme_dark():
    global settings_variables
    root.config(bg="Black")  # setting color for main window's background
    frame_2.config(bg="Black")  # setting color for a frame which is at the main window
    round_frame.config(bg = "Black")
    setting_buttons_frame.config(bg = "Black")
    the_entry.config(bg="Black", foreground="White")  # setting background color for an entry at the main window
    the_text.config(bg="Black", foreground="White")  # setting background color for a label at the main window
    the_company_label.config(bg="Black",
                             foreground="White")  # setting background color for a company label at the main window
    for buttons in button_list:  # setting background and for ground color for all buttons at the main window
        buttons.config(bg="Black", foreground="White", activebackground="Lime green")
    for i in all_entries:
        i.config(bg = "Black")
        i.config(fg = "White")


    with open("C:\\ProgramData\\FW_Calculator_settings.py", "a") as f:
        f.write("last_theme = 'Black'\n")


def theme_white():  # this function does the same as Theme_dark func above
    root.config(bg="White")
    frame_2.config(bg="White")
    round_frame.config(bg = "White")
    setting_buttons_frame.config(bg = "White")
    the_entry.config(bg="White", foreground="Black")
    the_text.config(bg="White", foreground="Black")
    the_company_label.config(bg="White", foreground="Black")
    for buttons in button_list:
        buttons.config(bg="White", foreground="Black", activebackground="Blue")
    for i in all_entries:
        i.config(bg = "White")
        i.config(fg = "Black")

    with open(full, "a") as f:
        f.write("last_theme = 'White'\n")


def background_color_of_buttons(x):  # this func gets its values from "setting" func below,
    global g_setting_label_error, settings_variables
    try:
        for buttons in button_list:  # from buttons_active_bg_entry and buttons_active_bg_button
            buttons.config(activebackground=x)
        setting_error_label.config(text="-----")
        to_record = "last_button_color = '" + str(x) + "'\n"
        with open(full, "a") as f:
            f.write(to_record)
    except:
        setting_error_label.config(text=g_setting_label_error)


def user_theme(x):
    global g_setting_label_error
    try:
        to_record = "last_theme = '" + str(x) + "'\n"
        root.config(bg = x)
        frame_2.config(bg = x)
        round_frame.config(bg = x)
        setting_buttons_frame.config(bg = x)
        the_entry.config(bg=x, foreground="Black")
        the_text.config(bg=x, foreground="Black")
        the_company_label.config(bg=x, foreground="Black")
        for buttons in button_list:
            buttons.config(bg=x, foreground="Black", activebackground="Blue")
        for i in all_entries:
            i.config(bg = x)
        setting_error_label.config(text="-----")
        if x == "Black":
            for i in all_entries:
                i.config(fg = "White")
            for i in button_list:
                i.config(fg = "White")
            the_text.config(fg = "White")
            the_company_label.config(fg = "White")
        if x == "White":
            for i in all_entries:
                i.config(fg = "Black")
            for i in button_list:
                i.config(fg = "Black")
            the_text.config(fg = "Black")
            the_company_label.config(fg = "Black")



        with open(full, "a") as f:
            f.write(to_record)
    except:
        setting_error_label.config(text=g_setting_label_error)


def answer():
    global g_mistake_in_a_math_expression_or_letters
    try:
        x = eval(the_entry.get())
        the_text.place(x=10, y=75)
        the_text.configure(font=("Helvetica", 20), text=str(round(x, int(round_till))))
    except (NameError, SyntaxError, ZeroDivisionError):
        error = g_mistake_in_a_math_expression_or_letters
        the_text.configure(font=("Helvetica", 10), text=error)
        the_text.place(x=110, y=70)


def round_it(x):
    global round_till, g_setting_label_error
    to_record = "last_rounding = " + str(x) + "\n"
    try:
        if int(x) < 1:
            round_till = 1
            setting_error_label.config(text="-----")
        else:
            round_till = x
            setting_error_label.config(text="-----")
        with open(full, "a") as f:
            f.write(to_record)
    except:
        setting_error_label.config(text=g_setting_label_error)


def push(x):
    the_entry.insert(END, x)


def delete_all():
    the_entry.delete(0, END)
    the_text.config(text=">>>" + " " * 82 + "<<<", font=('Helvetica', 10))
    the_text.place(x=10, y=85)


def delete_at_end():
    the_entry.delete(the_entry.index(END) - 1)


general_height = 4
general_width = 10

frame_2 = Frame(root, relief=RIDGE, borderwidth=3, bg = sv.last_theme)
frame_2.place(x=-1, y=133)

the_entry = Entry(root, textvariable=None, width=18, font=("Helvetica", 30), bg = sv.last_theme)
the_entry.place(x=0, y=5)

the_text = Label(root, text=">>>" + " " * 82 + "<<<", font=('Helvetica', 10), bg = sv.last_theme)
the_text.place(x=10, y=85)

the_company_label = Label(root, text=g_company, relief=FLAT, pady=3, padx=10, bg = sv.last_theme)
the_company_label.place(x=152, y=500)

# first row of buttons
button_1 = Button(frame_2, text="1", font=("Helvetica", 10), width=general_width, height=general_height,
                  command=lambda: push("1"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_1.grid(row=0, column=0)

button_2 = Button(frame_2, text="2", font=("Helvetica", 10), width=general_width, height=general_height,
                  command=lambda: push("2"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_2.grid(row=0, column=1)

button_3 = Button(frame_2, text="3", font=("Helvetica", 10), width=general_width, height=general_height,
                  command=lambda: push("3"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_3.grid(row=0, column=2)

button_plus = Button(frame_2, text="+", font=("Helvetica", 10), width=general_width, height=general_height,
                     command=lambda: push("+"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_plus.grid(row=0, column=3)

button_right_bracket = Button(frame_2, text="(", font=("Helvetica", 10), width=general_width, height=general_height,
                              command=lambda: push("("), activebackground = sv.last_button_color, bg = sv.last_theme)
button_right_bracket.grid(row=0, column=4)

# second row of buttons
button_4 = Button(frame_2, text="4", font=("Helvetica", 10), width=general_width, height=general_height,
                  command=lambda: push("4"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_4.grid(row=1, column=0)

button_5 = Button(frame_2, text="5", font=("Helvetica", 10), width=general_width, height=general_height,
                  command=lambda: push("5"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_5.grid(row=1, column=1)

button_6 = Button(frame_2, text="6", font=("Helvetica", 10), width=general_width, height=general_height,
                  command=lambda: push("6"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_6.grid(row=1, column=2)

button_minus = Button(frame_2, text="-", font=("Helvetica", 10), width=general_width, height=general_height,
                      command=lambda: push("-"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_minus.grid(row=1, column=3)

button_left_bracket = Button(frame_2, text=")", font=("Helvetica", 10), width=general_width, height=general_height,
                             command=lambda: push(")"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_left_bracket.grid(row=1, column=4)

# third row of buttons
button_7 = Button(frame_2, text="7", font=("Helvetica", 10), width=general_width, height=general_height,
                  command=lambda: push("7"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_7.grid(row=2, column=0)

button_8 = Button(frame_2, text="8", font=("Helvetica", 10), width=general_width, height=general_height,
                  command=lambda: push("8"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_8.grid(row=2, column=1)

button_9 = Button(frame_2, text="9", font=("Helvetica", 10), width=general_width, height=general_height,
                  command=lambda: push("9"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_9.grid(row=2, column=2)

button_multiplication = Button(frame_2, text="*", font=("Helvetica", 10), width=general_width, height=general_height,
                               command=lambda: push("*"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_multiplication.grid(row=2, column=3)

settings_image = PhotoImage(file="settings.png")

settings_button = Button(frame_2, command=open_settings, image=settings_image, width=94, height=84, activebackground = sv.last_button_color, bg = sv.last_theme)

settings_button.grid(row=2, column=4)

info_message.bind_widget(settings_button, balloonmsg=button_setting_b)

# fourth row of buttons
button_0 = Button(frame_2, text="0", font=("Helvetica", 10), width=general_width, height=general_height,
                  command=lambda: push("0"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_0.grid(row=3, column=1)

button_divide = Button(frame_2, text="/", font=("Helvetica", 10), width=general_width, height=general_height,
                       command=lambda: push("/"), activebackground = sv.last_button_color, bg = sv.last_theme)
button_divide.grid(row=3, column=3)
info_message.bind_widget(button_divide, balloonmsg=division_with_no_remainder_b)

button_equal = Button(frame_2, text="=", font=("Helvetica", 10), width=general_width, height=general_height,
                      command=answer, activebackground = sv.last_button_color, bg = sv.last_theme)
button_equal.grid(row=3, column=4)

button_clear = Button(frame_2, text="C", font=("Helvetica", 10), width=general_width, height=general_height,
                      command=delete_all, activebackground = sv.last_button_color, bg = sv.last_theme)
button_clear.grid(row=3, column=2)

button_clear_at_end = Button(frame_2, text="<", font=("Helvetica", 10), width=general_width, height=general_height,
                             command=delete_at_end, activebackground = sv.last_button_color, bg = sv.last_theme)
button_clear_at_end.grid(row=3, column=0)

# SETTING SECTION STARTS HERE

setting_buttons_frame = Frame(root, relief=RAISED, bg = sv.last_theme)
setting_buttons_frame.place(x=530, y=135, height=140, width=300)

button_white_theme = Button(setting_buttons_frame, text=white_theme, command=theme_white, activebackground = sv.last_button_color, bg = sv.last_theme)
button_white_theme.pack(side=TOP, fill="x")
button_dark_theme = Button(setting_buttons_frame, text=black_theme, command=theme_dark, activebackground = sv.last_button_color, bg = sv.last_theme)
button_dark_theme.pack(side=TOP, fill="x")
language_button_rus = Button(setting_buttons_frame, text=russian_language, command=set_russian, activebackground = sv.last_button_color, bg = sv.last_theme)
language_button_rus.pack(side=TOP, fill="x")
language_button_eng = Button(setting_buttons_frame, text=english_language, command=set_english, activebackground = sv.last_button_color, bg = sv.last_theme)
language_button_eng.pack(side=TOP, fill="x")

round_frame = Frame(root, relief=RAISED, bg = sv.last_theme)
round_frame.place(x=530, y=300, height=107, width=300)

user_theme_entry = Entry(round_frame, font=("Ariel", 16), width=10, bg = sv.last_theme)
user_theme_entry.grid(row=0, column=0)

user_theme_button = Button(round_frame, text=s_apply, width=10, command=lambda: user_theme(user_theme_entry.get()), activebackground = sv.last_button_color, bg = sv.last_theme)
user_theme_button.grid(row=0, column=1, sticky="we")
info_message.bind_widget(user_theme_button,
                         balloonmsg="Apply your theme using RGB code like - > #FFCCE5\nor an available html color name")

buttons_active_bg_entry = Entry(round_frame, font=("Ariel", 16), width=10, bg = sv.last_theme)
buttons_active_bg_entry.grid(row=1, column=0)
buttons_active_bg_button = Button(round_frame, text=s_apply,
                                  command=lambda: background_color_of_buttons(buttons_active_bg_entry.get()), activebackground = sv.last_button_color, bg = sv.last_theme)
buttons_active_bg_button.grid(row=1, column=1, sticky="we")
info_message.bind_widget(buttons_active_bg_button,
                         balloonmsg="Apply your buttons highlight color using RGB code like - > #FFCCE5\nor an available html color name")

round_entry = Entry(round_frame, font=("Ariel", 16), width=10, bg = sv.last_theme)
round_entry.grid(row=2, column=0)
round_button = Button(round_frame, text=round_till_, command=lambda: round_it(round_entry.get()), activebackground = sv.last_button_color, bg = sv.last_theme)
round_button.grid(row=2, column=1, sticky="we")
info_message.bind_widget(round_button,
                         balloonmsg=rounding_b)

setting_error_label = Label(root, text="-----", bg = sv.last_theme)
setting_error_label.place(x=530, y=445)

round_frame.columnconfigure(1, weight=2)

button_list = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_0,
               button_plus, button_minus, button_divide, button_multiplication, button_clear, button_clear_at_end,
               button_right_bracket, button_left_bracket, settings_button, button_equal, setting_error_label,
               button_white_theme, button_dark_theme,
               language_button_eng, language_button_rus, buttons_active_bg_button, user_theme_button, round_button]

all_entries = [round_entry, user_theme_entry, buttons_active_bg_entry, the_entry]


if sv.last_theme == "Black":
    for i in button_list:
        i.config(foreground = "White")
    for i in all_entries:
        i.config(foreground = "White")
    the_text.config(foreground = "White")
    the_company_label.config(foreground = "White")


if sv.last_language == 'R':
    set_russian()
if sv.last_language == 'E':
    set_english()
else:
    pass



root.mainloop()



