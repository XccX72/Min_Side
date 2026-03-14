import ttkbootstrap as ttk

class liste():
    def __init__(self):
        self.window = ttk.Window(themename= "minty")
        self.window.state("zoomed")
        self.window.title("List")
        self.window.grid_columnconfigure(1, weight= 1)

        self.frame_list = ttk.Frame(
            self.window
        )
        self.frame_list.grid(
            sticky= "nswe",
        )


        self.window.mainloop()

if __name__ == "__main__":
    liste()

