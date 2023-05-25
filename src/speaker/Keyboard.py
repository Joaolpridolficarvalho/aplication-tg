import tkinter as tk

from Functions_keyboard import *


# import Editor
class Keyboard:
    def __init__(self, frame_keyboard):
        self.amount_of_words = 0
        fk = Functions_keyboard(frame_keyboard)


        ButtonQ = tk.Button(frame_keyboard, text="q", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("q", 0, 300)).place(x=0, y=300)
        ButtonW = tk.Button(frame_keyboard, text="w", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("w", 25, 300)).place(x=25, y=300)
        ButtonE = tk.Button(frame_keyboard, text="e", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("e", 50, 300))
        ButtonE.bind("<Button-3>", lambda event: fk.control_accents("e", 50, 300))
        ButtonE.place(x=50, y=300)
        ButtonR = tk.Button(frame_keyboard, text="r", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("r", 75, 300)).place(x=75, y=300)
        ButtonT = tk.Button(frame_keyboard, text="t", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("t", 100, 300)).place(x=100, y=300)
        ButtonY = tk.Button(frame_keyboard, text="y", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("y", 125, 300)).place(x=125, y=300)
        ButtonU = tk.Button(frame_keyboard, text="u", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("u", 150, 300)).place(x=150, y=300)
        ButtonI = tk.Button(frame_keyboard, text="i", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("i", 175, 300))
        ButtonI.bind("<Button-3>", lambda event: fk.control_accents("i", 175, 300))
        ButtonI.place(x=175, y=300)
        ButtonO = tk.Button(frame_keyboard, text="o", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("o", 200, 300))
        ButtonO.bind("<Button-3>", lambda event: fk.control_accents("o", 200, 300))
        ButtonO.place(x=200, y=300)
        ButtonP = tk.Button(frame_keyboard, text="p", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("p", 225, 300)).place(x=225, y=300)
        ButtonBackspace = tk.Button(frame_keyboard, text="Backspace", height=2, width=10, background="light blue",
                                    command=lambda: fk.backspace()).place(x=250, y=300)
        ButtonA = tk.Button(frame_keyboard, text="a", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("a", 0, 345))
        ButtonA.bind("<Button-3>", lambda event: fk.control_accents("a", 0, 345))
        ButtonA.place(x=0, y=345)
        # testing
        ButtonS = tk.Button(frame_keyboard, text="s", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("s", 25, 345)).place(x=25, y=345)
        ButtonD = tk.Button(frame_keyboard, text="d", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("d", 50, 345)).place(x=50, y=345)
        ButtonF = tk.Button(frame_keyboard, text="f", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("f", 75, 345)).place(x=75, y=345)
        ButtonG = tk.Button(frame_keyboard, text="g", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("g", 100, 345)).place(x=100, y=345)
        ButtonH = tk.Button(frame_keyboard, text="h", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("h", 125, 345)).place(x=125, y=345)
        ButtonJ = tk.Button(frame_keyboard, text="j", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("j", 150, 345)).place(x=150, y=345)
        ButtonK = tk.Button(frame_keyboard, text="k", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("k", 175, 345)).place(x=175, y=345)
        ButtonL = tk.Button(frame_keyboard, text="l", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("l", 200, 345)).place(x=200, y=345)
        Buttonç = tk.Button(frame_keyboard, text="ç", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("ç", 225, 345)).place(x=225, y=345)
        ButtonEnter = tk.Button(frame_keyboard, text="Enter", height=2, width=10, background="light blue",
                                command=lambda: fk.print_value("\n")).place(x=250, y=345)
        ButtonZ = tk.Button(frame_keyboard, text="z", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("z", 0, 390)).place(x=0, y=390)
        ButtonX = tk.Button(frame_keyboard, text="x", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("x", 25, 390)).place(x=25, y=390)
        ButtonC = tk.Button(frame_keyboard, text="c", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("c", 50, 390)).place(x=50, y=390)
        ButtonV = tk.Button(frame_keyboard, text="v", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("v", 75, 390)).place(x=75, y=390)
        ButtonB = tk.Button(frame_keyboard, text="b", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("b", 100, 390)).place(x=100, y=390)
        ButtonN = tk.Button(frame_keyboard, text="n", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("n", 125, 390)).place(x=125, y=390)
        ButtonM = tk.Button(frame_keyboard, text="m", height=2, width=2, background="light blue",
                            command=lambda: fk.control_button("m", 150, 390)).place(x=150, y=390)
        ButtonComma = tk.Button(frame_keyboard, text=",", height=2, width=2, background="light blue",
                                command=lambda: fk.print_value(",")).place(x=175, y=390)
        ButtonDot = tk.Button(frame_keyboard, text=".", height=2, width=2, background="light blue",
                              command=lambda: fk.print_value(".")).place(x=200, y=390)
        ButtonSpace = tk.Button(frame_keyboard, text=" ", height=2, width=10, background="light blue",
                                command=lambda: fk.print_value(" ")).place(x=75, y=435)
        ButtonSeven = tk.Button(frame_keyboard, text="7", height=2, width=2, background="light blue",
                                command=lambda: fk.print_value(7)).place(x=330, y=300)
        # TODO: Implement the arrow buttons
        ButtonEight = tk.Button(frame_keyboard, text="8", height=2, width=2, background="light blue",
                                command=lambda: fk.print_value(8)).place(x=355, y=300)
        ButtonNine = tk.Button(frame_keyboard, text="9", height=2, width=2, background="light blue",
                               command=lambda: fk.print_value(9)).place(x=380, y=300)
        ButtonSix = tk.Button(frame_keyboard, text="6", height=2, width=2, background="light blue",
                              command=lambda: fk.print_value(6)).place(x=380, y=345)
        ButtonFive = tk.Button(frame_keyboard, text="5", height=2, width=2, background="light blue",
                               command=lambda: fk.print_value(5)).place(x=355, y=345)
        ButtonFour = tk.Button(frame_keyboard, text="4", height=2, width=2, background="light blue",
                               command=lambda: fk.print_value(4)).place(x=330, y=345)
        ButtonThree = tk.Button(frame_keyboard, text="3", height=2, width=2, background="light blue",
                                command=lambda: fk.print_value(3)).place(x=380, y=390)
        ButtonTwo = tk.Button(frame_keyboard, text="2", height=2, width=2, background="light blue",
                              command=lambda: fk.print_value(2)).place(x=355, y=390)
        ButtonOne = tk.Button(frame_keyboard, text="1", height=2, width=2, background="light blue",
                              command=lambda: fk.print_value(1)).place(x=330, y=390)
        ButtonZero = tk.Button(frame_keyboard, text="0", height=2, width=2, background="light blue",
                               command=lambda: fk.print_value(0)).place(x=355, y=435)
