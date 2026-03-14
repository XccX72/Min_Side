import ttkbootstrap as ttk

def liste_main():
    window = ttk.Window(themename= "minty")
    window.state("zoomed")
    window.title("List")
    window.grid_columnconfigure(1, weight= 1)

    frame_list = ttk.Frame(
        window
    )
    frame_list.grid(
        sticky= "nswe",
    )

    def first_list():
        first_frame = ttk.Frame(
            frame_list
        )
        first_frame.pack()

        first_text_input = ttk.Text(
            first_frame, 
            height = 2, 
            width= 40
        )
        first_text_input.grid(
            column = 0, 
            row = 0,
            sticky = "news"
        )

        first_lag_ny = ttk.Button(
            first_frame, 
            command = andre_liste,
            text = "New"
        )
        first_lag_ny.grid(
            column= 1, 
            row = 0, 
            sticky= "news"
        )

        first_slett = ttk.Button(
            first_frame,
            command= delete, 
            text= "Del"
        )
        first_slett.grid(
            column= 2, 
            row = 0,
            sticky= "nswe"
        )

    def andre_liste():
        pass

    def delete():
        pass

    def keys(event):
        key = event.keysym
        if key.lower() == "m":
            pass
        elif key == "Escape":
            window.destroy()
        else:
            return


    first_list()
    window.bind_all("<KeyPress>", keys)
    window.mainloop()




def liste_not_main(vindu):
    pass

if __name__ == "__main__":
    liste_main()