import tkinter as tk
from tkinter import ttk
import tkinter.font as font
 

class Distconverter(tk.Tk):
    def __init__(self,*args, **kwargs ):
        super().__init__(*args,**kwargs)

        self.title("Distance Converter")

        self.frames = dict()

        container=ttk.Frame(self)
        container.grid(padx=10, pady=15,  sticky="EW")


        feet_to_meters = FeettoMeteres(container,self) 
        feet_to_meters.grid(row=0, column=0, sticky="NSEW") 
 
        meters_to_feet = MetertoFeet(container,self)
        meters_to_feet.grid(row=0,column=0,sticky="NSEW")

        self.frames[FeettoMeteres]=feet_to_meters
        self.frames[MetertoFeet]=meters_to_feet


    
    def show_frame(self,container):
        frame=self.frames[container]
        frame.tkraise() 
      
class MetertoFeet(ttk.Frame):
    def __init__(self, container,controller, **kwargs):
        super().__init__(container, **kwargs)
        self.meter_var=tk.StringVar()
        self.feets_value=tk.StringVar()
        self.feets_value.set("Feet shown here...")
        meters_entry= ttk.Entry(self, width=20, textvariable=self.meter_var )
        feets_label = ttk.Label(self, text="In Feet : ")
        feets_display=ttk.Label(self, textvariable=self.feets_value )
        calc_button= ttk.Button(self, text="Calculate",command=self.calculate)

        switch_page_button = ttk.Button(
            self, 
            text="Switch to feet conversion",
            command = lambda : controller.show_frame(FeettoMeteres)

        )

        meters_label=ttk.Label(self, text="Meters :")

        meters_label.grid(column=0,row=0,sticky="EW",padx=5, pady=5)
        meters_entry.grid(column=1, row=0,sticky="EW",padx=5, pady=5)
        meters_entry.focus()
        feets_label.grid(column=0, row=1,sticky="EW",padx=5, pady=5)
        feets_display.grid(column=1,row=1,sticky="EW ",padx=5, pady=5)
        calc_button.grid(column=0, row=3, columnspan=2,sticky="EW")
        switch_page_button.grid(column=0,row=4,columnspan=2,sticky="EW")

    def calculate(self, *args):
        try:
            meter=float(self.meter_var.get())
            feets = meter*3.28084
            #print(f"{meter} meters is equal to {feets:.3f} feet.")
            self.feets_value.set(f"{feets:.3f}")
        except ValueError:
            pass 

class FeettoMeteres(ttk.Frame):
    def __init__(self, container,controller, **kwargs):
        super().__init__(container, **kwargs)
        self.feet_var=tk.StringVar()
        self.meter_value=tk.StringVar()
        self.meter_value.set("meter shown here...")
        feet_label=ttk.Label(self, text="Feet :")
        feet_entry= ttk.Entry(self, width=20, textvariable=self.feet_var )
        meter_label = ttk.Label(self, text="In meters : ")
        meter_display=ttk.Label(self, textvariable=self.meter_value )
        calc_button= ttk.Button(self, text="Calculate",command=self.calculate)
        switch_page_button = ttk.Button(
            self, 
            text="Switch to feet conversion",
            command = lambda : controller.show_frame(MetertoFeet)

        )

        feet_label.grid(column=0,row=0,sticky="EW",padx=5, pady=5)
        feet_entry.grid(column=1, row=0,sticky="EW",padx=5, pady=5)
        feet_entry.focus()

        meter_label.grid(column=0, row=1,sticky="EW",padx=5, pady=5)
        meter_display.grid(column=1,row=1,sticky="EW ",padx=5, pady=5)
        calc_button.grid(column=0, row=3, columnspan=2,sticky="EW")
        switch_page_button.grid(column=0,row=4,columnspan=2,sticky="EW")

    def calculate(self, *args):
        try:
            feet=float(self.feet_var.get())
            meter = feet/3.28084
            #print(f"{meter} meters is equal to {feets:.3f} feet.")
            self.meter_value.set(f"{meter:.3f}")
        except ValueError:
            pass 

root= Distconverter() 

font.nametofont("TkDefaultFont").configure(size=15)

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)  

root.mainloop()