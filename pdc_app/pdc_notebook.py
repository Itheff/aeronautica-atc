from tkinter import END
from tkinter.ttk import Notebook

from pdc_frame import PDCFrame

class PDCNotebook(Notebook):
    faa_frame: PDCFrame
    caa_frame: PDCFrame
    icao_frame: PDCFrame

    def __init__(self, master):
        super().__init__(master)
        faa_frame = PDCFrame(self, "faa")
        caa_frame = PDCFrame(self, "caa")
        caa_frame.pdc_output.config(state="normal")
        caa_frame.pdc_output.insert(END, "State the ATIS phonetically (ALPHA not A) below before using.")
        caa_frame.pdc_output.config(state="disabled")
        icao_frame = PDCFrame(self, "icao")
        icao_frame.flight_plan_input.insert(END, "INOP")
        icao_frame.flight_plan_input.config(state="disabled", background="gray75")
        icao_frame.pdc_output.config(state="disabled", background="gray75")
        self.add(faa_frame, text="FAA")
        self.add(caa_frame, text="CAA")
        self.add(icao_frame, text="ICAO")
