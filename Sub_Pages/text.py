import ttkbootstrap as ttk

def info_om_meg(vindu):
    content_frame = vindu
    about_me_label_h1 = ttk.Label(
        content_frame, 
        text = "Hello", 
        font= ("Arial", 20)
    )
    about_me_label_h1.pack()

    about_me_label_t1 = ttk.Label(
        content_frame,
        text = "Hi, \nMy name is Danni Spriet and I am a 'programmer'.\nI'm studying programming via my high school, Olsvikåsen VGS ",
        font = ("Arial", 12)
    )
    about_me_label_t1.pack()

def viktig_om_meg(vindu):
    content_frame = vindu

    a = ("Csv Shit")

    viktig_label = ttk.Label(
        content_frame,
        text = a
    )
    viktig_label.pack()

def keys_info(vindu):
    content_frame = vindu

    b = ("M = Meny \nEsc = Close Program ")

    help_keys_label = ttk.Label(
        content_frame, 
        text = b, 
        font= ("Arial", 20)
    )
    help_keys_label.pack()