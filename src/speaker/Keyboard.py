import tkinter as tk

from Word_predictor import Word_predictor

from Functions_keyboard import Functions_keyboard as fk

from Symbol_keyboard import Symbol_keyboard as sk
class Keyboard:
    def __init__(self, frame_keyboard, text_field):
        self.text_field = text_field
        self.is_activated_sk = False
        wp = Word_predictor(frame, self.text_field, self.text_field)
        position_last_line = 130
        self.sk = sk(frame_keyboard, self.text_field)
        ButtonQ = tk.Button(frame_keyboard, text="q", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("q"), fk(text_field=self.text_field).control_button("q", 400, position_last_line+190)]).place(x=400, y=position_last_line-90)
        ButtonW = tk.Button(frame_keyboard, text="w", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("w"), fk(text_field=self.text_field).control_button("w", 425, position_last_line+190)]).place(x=425, y=position_last_line-90)
        ButtonE = tk.Button(frame_keyboard, text="e", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("e"), fk(text_field=self.text_field).control_button("e", 450, position_last_line+190)])
        ButtonE.bind("<Button-3>", lambda event: fk.control_accents("e", 450, position_last_line-90))
        ButtonE.place(x=450, y=position_last_line-90)
        ButtonR = tk.Button(frame_keyboard, text="r", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("r"), fk(text_field=self.text_field).control_button("r", 475, position_last_line+190)]).place(x=475, y=position_last_line-90)
        ButtonT = tk.Button(frame_keyboard, text="t", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("t"), fk(text_field=self.text_field).control_button("t", 500, position_last_line+190)]).place(x=500, y=position_last_line-90)
        ButtonY = tk.Button(frame_keyboard, text="y", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("y"), fk(text_field=self.text_field).control_button("y", 525, position_last_line+190)]).place(x=525, y=position_last_line-90)
        ButtonU = tk.Button(frame_keyboard, text="u", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("u"), fk(text_field=self.text_field).control_button("u", 550, position_last_line+190)]).place(x=550, y=position_last_line-90)
        ButtonI = tk.Button(frame_keyboard, text="i", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("i"), fk(text_field=self.text_field).control_button("i", 575, position_last_line+190)])
        ButtonI.bind("<Button-3>", lambda event: fk.control_accents("i", 575, position_last_line-90))
        ButtonI.place(x=575, y=position_last_line-90)
        ButtonO = tk.Button(frame_keyboard, text="o", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("o"), fk(text_field=self.text_field).control_button("o", 600, position_last_line+190)])
        ButtonO.bind("<Button-3>", lambda event: fk.control_accents("o", 600, position_last_line-90))
        ButtonO.place(x=600, y=position_last_line-90)
        ButtonP = tk.Button(frame_keyboard, text="p", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("p"), fk(text_field=self.text_field).control_button("p", 625, position_last_line+190)]).place(x=625, y=position_last_line-90)
      
        
        ButtonBackspace = tk.Button(frame_keyboard, text="Backspace", height=2, width=10, background="light blue",
                                    command=lambda: fk(text_field=self.text_field).backspace()).place(x=650, y=position_last_line-90)
        global ButtonCapsLock
        ButtonCapsLock = tk.Button(frame_keyboard, text="Caps", height=2, width=10, background="light blue",
                                   command=lambda: [fk(text_field=self.text_field).set_uppercase(), self.change_color()])
        ButtonCapsLock.place(x=320, y=position_last_line-45)
        global ButtonSymbols
        ButtonSymbols = tk.Button(frame_keyboard, text="?123", height=2, width=10, background="light blue",
                                   command=lambda: self.control_buttonSymbols())
        ButtonSymbols.place(x=320, y=position_last_line+60)
        ButtonA = tk.Button(frame_keyboard, text="a", height=2, width=2, background="light blue",
                            command=lambda: fk(text_field=self.text_field).control_button("a", 400, position_last_line+225))
        ButtonA.bind("<Button-3>", lambda event: fk.control_accents("a", 650, position_last_line-60))
        ButtonA.place(x=400, y=position_last_line-45)

        ButtonS = tk.Button(frame_keyboard, text="s", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("s"), fk(text_field=self.text_field).control_button("s", 425, position_last_line+235)]).place(x=425, y=position_last_line-45)
        ButtonD = tk.Button(frame_keyboard, text="d", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("d"), fk(text_field=self.text_field).control_button("d", 450, position_last_line+235)]).place(x=450, y=position_last_line-45)
        ButtonF = tk.Button(frame_keyboard, text="f", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("f"), fk(text_field=self.text_field).control_button("f", 475, position_last_line+235)]).place(x=475, y=position_last_line-45)
        ButtonG = tk.Button(frame_keyboard, text="g", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("g"), fk(text_field=self.text_field).control_button("g", 500, position_last_line+235)]).place(x=500, y=position_last_line-45)
        ButtonH = tk.Button(frame_keyboard, text="h", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("h"), fk(text_field=self.text_field).control_button("h", 525, position_last_line+235)]).place(x=525, y=position_last_line-45)
        ButtonJ = tk.Button(frame_keyboard, text="j", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("j"), fk(text_field=self.text_field).control_button("j", 550, position_last_line+235)]).place(x=550, y=position_last_line-45)
        ButtonK = tk.Button(frame_keyboard, text="k", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("k"), fk(text_field=self.text_field).control_button("k", 575, position_last_line+235)]).place(x=575, y=position_last_line-45)
        ButtonL = tk.Button(frame_keyboard, text="l", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("l"), fk(text_field=self.text_field).control_button("l", 600, position_last_line+235)]).place(x=600, y=position_last_line-45)
        Buttonç = tk.Button(frame_keyboard, text="ç", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("ç"), fk(text_field=self.text_field).control_button("ç", 625, position_last_line+235)]).place(x=625, y=position_last_line-45)
        ButtonEnter = tk.Button(frame_keyboard, text="Enter", height=2, width=10, background="light blue",
                                command=lambda: fk.print_value("\n")).place(x=650, y=position_last_line-45)
        ButtonZ = tk.Button(frame_keyboard, text="z", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("z"), fk(text_field=self.text_field).control_button("z", 400, position_last_line+280)]).place(x=400, y=position_last_line)
        ButtonX = tk.Button(frame_keyboard, text="x", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("x"), fk(text_field=self.text_field).control_button("x", 425, position_last_line+280)]).place(x=425, y=position_last_line)
        ButtonC = tk.Button(frame_keyboard, text="c", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("c"), fk(text_field=self.text_field).control_button("c", 450, position_last_line+280)]).place(x=450, y=position_last_line)
        ButtonV = tk.Button(frame_keyboard, text="v", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("v"), fk(text_field=self.text_field).control_button("v", 475, position_last_line+280)]).place(x=475, y=position_last_line)
        ButtonB = tk.Button(frame_keyboard, text="b", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("b"), fk(text_field=self.text_field).control_button("b", 500, position_last_line+280)]).place(x=500, y=position_last_line)
        ButtonN = tk.Button(frame_keyboard, text="n", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("n"), fk(text_field=self.text_field).control_button("n", 525, position_last_line+280)]).place(x=525, y=position_last_line)
        ButtonM = tk.Button(frame_keyboard, text="m", height=2, width=2, background="light blue",
                            command=lambda: [wp.control_prediction("m"), fk(text_field=self.text_field).control_button("m", 550, position_last_line+280)]).place(x=550, y=position_last_line)

        ButtonComma = tk.Button(frame_keyboard, text=",", height=2, width=2, background="light blue",
                                command=lambda: fk.print_value(",")).place(x=575, y=position_last_line)
        ButtonDot = tk.Button(frame_keyboard, text=".", height=2, width=2, background="light blue",
                              command=lambda: fk.print_value(".")).place(x=600, y=position_last_line+60)
        ButtonSpace = tk.Button(frame_keyboard, text=" ", height=2, width=10, background="light blue",
                                command=lambda: fk.print_value(" ")).place(x=475, y=position_last_line+60)
        ButtonSeven = tk.Button(frame_keyboard, text="7", height=2, width=2, background="light blue",
                                command=lambda: fk.print_value(7)).place(x=725, y=position_last_line-90)
        # TODO: Implement the arrow buttons
        ButtonEight = tk.Button(frame_keyboard, text="8", height=2, width=2, background="light blue",
                                command=lambda: fk.print_value(8)).place(x=750, y=position_last_line-90)
        ButtonNine = tk.Button(frame_keyboard, text="9", height=2, width=2, background="light blue",
                               command=lambda: fk.print_value(9)).place(x=775, y=position_last_line-90)
        ButtonSix = tk.Button(frame_keyboard, text="6", height=2, width=2, background="light blue",
                              command=lambda: fk.print_value(6)).place(x=775, y=position_last_line-45)
        ButtonFive = tk.Button(frame_keyboard, text="5", height=2, width=2, background="light blue",
                               command=lambda: fk.print_value(5)).place(x=750, y=position_last_line-45)
        ButtonFour = tk.Button(frame_keyboard, text="4", height=2, width=2, background="light blue",
                               command=lambda: fk.print_value(4)).place(x=725, y=position_last_line-45)
        ButtonThree = tk.Button(frame_keyboard, text="3", height=2, width=2, background="light blue",
                                command=lambda: fk.print_value(3)).place(x=775, y=position_last_line)
        ButtonTwo = tk.Button(frame_keyboard, text="2", height=2, width=2, background="light blue",
                              command=lambda: fk.print_value(2)).place(x=750, y=position_last_line)
        ButtonOne = tk.Button(frame_keyboard, text="1", height=2, width=2, background="light blue",
                              command=lambda: fk.print_value(1)).place(x=725, y=position_last_line)
        ButtonZero = tk.Button(frame_keyboard, text="0", height=2, width=2, background="light blue",
                               command=lambda: fk.print_value(0)).place(x=750, y=position_last_line+45)

    def change_color(self):
        if ButtonCapsLock["background"] == "light blue":
            ButtonCapsLock.configure(background="#0752F2")
        else:
            ButtonCapsLock.configure(background="light blue")

    def control_buttonSymbols(self):
        if self.is_activated_sk is False:
            self.sk.build_keyboard()
            self.is_activated_sk =  True
        else:
            self.sk.destroy_keyboard()
            self.is_activated_sk =False
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    