from tkinter import Tk

from pdc_notebook import PDCNotebook

class App(Tk):
    """
    The App class is the root component of the UI and contains the notebooks which then contain the tabs. It is mostly
    a basic Tk class but with extra steps added to the __init__ to create the unique UI of the program.
    """

    pdc_notebook: PDCNotebook

    def __init__(self):
        super().__init__()
        self.geometry("512x512")
        self.resizable(False, False)
        self.title("Aeronautica ATC")
        pdc_notebook = PDCNotebook(self)
        pdc_notebook.pack()


def main() -> None:
    """
    This function holds the root of the program and runs the main loop of the window
    """
    root: App = App()
    root.mainloop()


if __name__ == '__main__':
    main()
