import tkinter as tk

class VirtualDesktop:
    def __init__(self, master):
        self.master = master
        master.title("Virtual Desktop")

        self.label = tk.Label(master, text="Welcome to Virtual Desktop!")
        self.label.pack()

        self.text_area = tk.Text(master)
        self.text_area.pack()

        self.button = tk.Button(master, text="Close", command=master.quit)
        self.button.pack()

def main():
    root = tk.Tk()
    app = VirtualDesktop(root)
    root.mainloop()

if __name__ == "__main__":
    main()
