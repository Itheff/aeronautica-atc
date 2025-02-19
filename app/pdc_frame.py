from typing import Literal
from tkinter import Text, Button, Widget, Frame, END
from traceback import format_exception

from pdc_builder import PDCBuilder

class PDCFrame(Frame):
    """
    The PDCFrame class is the main component of the UI and is the content seen in the 3 tabs.
    """
    flight_plan_input: Text
    submit_button: Button
    pdc_output: Text
    phraseology: Literal["faa", "caa", "icao"]
    pdc_builder: PDCBuilder
    atis_information: Text

    def __init__(self, master: Widget, phraseology: Literal["faa", "caa", "icao"]):
        super().__init__(master)
        self.phraseology = phraseology
        self.pdc_builder = PDCBuilder()
        self.flight_plan_input: Text = Text(self, height=10, borderwidth=2)
        self.submit_button = Button(self, text="Submit", command=self.submit)
        self.pdc_output = Text(self, height=10, borderwidth=2, wrap="word")
        self.pdc_output.config(state="disabled")
        self.pack()
        self.flight_plan_input.pack(padx=10, pady=10)
        self.submit_button.pack()
        self.pdc_output.pack(padx=10, pady=10, expand=True)
        if self.phraseology == "caa":
            self.atis_information = Text(self, height=1, borderwidth=2, wrap="none")
            self.atis_information.pack(padx=10, pady=10)

    def submit(self):
        """
        The submit method is called every time the submit button is pressed. It generates a PDC from the PDCBuilder and
        outputs it to the pdc_output.
        """
        try:
            self.pdc_output.config(state="normal")
            self.pdc_output.delete("1.0", END)
            if self.phraseology == "caa":
                self.pdc_output.insert(1.0, self.pdc_builder.build_pdc(self.flight_plan_input.get("1.0", END),
                                                                   self.phraseology,
                                                                   self.atis_information.get("1.0", END)))
            else:
                self.pdc_output.insert(1.0, self.pdc_builder.build_pdc(self.flight_plan_input.get("1.0", END),
                                                                   self.phraseology, ""))
            self.pdc_output.config(state="disabled")
        except Exception as e:
            for tb in format_exception(e):
                print(tb)
