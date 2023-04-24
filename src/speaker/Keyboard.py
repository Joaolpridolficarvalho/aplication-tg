import tkinter as tk
import Terminal
import Functions_keyboard
import Frame_keyboard

# import Editor
def __init__(self):
    self.amount_of_words = 0



root = tk.Tk()
terminal = Terminal.Terminal()
root.geometry("1024x600")
root.title("Keyboard")
fk = Functions_keyboard.Functions_keyboard()
frameKey = Frame_keyboard.Frame_keyboard(root)
text_field = tk.Text(root, height=10, width=20, font=("Arial", 18))
text_field.place(x=0, y=0)
buttonSpeake = tk.Button(frameKey, text="Speak", height=20, width=10,
                         command=lambda: terminal.speake(fk.get_text(text_field))).place(x=410, y=0)
sugestion1 = tk.Text(root, height=5, width=10).place(x=0, y=260)
sugestion2 = tk.Text(root, height=5, width=10).place(x=100, y=260)
sugestion3 = tk.Text(root, height=5, width=10).place(x=200, y=260)
sugestion4 = tk.Text(root, height=5, width=10).place(x=300, y=260)
sugestion5 = tk.Text(root, height=5, width=10).place(x=400, y=260)
sugestion6 = tk.Text(root, height=5, width=10).place(x=500, y=260)
sugestion7 = tk.Text(root, height=5, width=10).place(x=600, y=260)
sugestion8 = tk.Text(root, height=5, width=10).place(x=700, y=260)
sugestion9 = tk.Text(root, height=5, width=10).place(x=800, y=260)
ButtonQ = tk.Button(frameKey, text="q", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("q", text_field, 0,300)).place(x=0, y=300)
ButtonW = tk.Button(frameKey, text="w", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("w", text_field, 25,300)).place(x=25, y=300)
ButtonE = tk.Button(frameKey, text="e", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("e", text_field, 50, 300))
ButtonE.bind("<Button-3>", lambda event: fk.control_accents("e", 50, 300))
ButtonE.place(x=50, y=300)
ButtonR = tk.Button(frameKey, text="r", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("r", text_field, 75, 300)).place(x=75, y=300)
ButtonT = tk.Button(frameKey, text="t", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("t", text_field, 100, 300)).place(x=100, y=300)
ButtonY = tk.Button(frameKey, text="y", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("y", text_field, 125, 300)).place(x=125, y=300)
ButtonU = tk.Button(frameKey, text="u", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("u", text_field, 150, 300)).place(x=150, y=300)
ButtonI = tk.Button(frameKey, text="i", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("i", text_field, 175, 300))
ButtonI.bind("<Button-3>", lambda event: fk.control_accents("i", 175, 300))
ButtonI.place(x=175, y=300)
ButtonO = tk.Button(frameKey, text="o", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("o", text_field, 200, 300))
ButtonO.bind("<Button-3>", lambda event: fk.control_accents("o", 200, 300))
ButtonO.place(x=200, y=300)
ButtonP = tk.Button(frameKey, text="p", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("p", text_field, 225, 300)).place(x=225, y=300)
ButtonBackspace = tk.Button(frameKey, text="Backspace", height=2, width=10, background="light blue",
                            command=lambda: backspace(text_field)).place(x=250, y=300)
ButtonA = tk.Button(frameKey, text="a", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("a", text_field, 0, 345))
ButtonA.bind("<Button-3>", lambda event: fk.control_accents("a", 0, 345))
ButtonA.place(x=0, y=345)
ButtonS = tk.Button(frameKey, text="s", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("s", text_field, 25, 345)).place(x=25, y=345)
ButtonD = tk.Button(frameKey, text="d", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("d", text_field, 50, 345)).place(x=50, y=345)
ButtonF = tk.Button(frameKey, text="f", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("f", text_field, 75, 345)).place(x=75, y=345)
ButtonG = tk.Button(frameKey, text="g", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("g", text_field, 100,345)).place(x=100, y=345)
ButtonH = tk.Button(frameKey, text="h", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("h", text_field, 125,345)).place(x=125, y=345)
ButtonJ = tk.Button(frameKey, text="j", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("j", text_field, 150,345)).place(x=150, y=345)
ButtonK = tk.Button(frameKey, text="k", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("k", text_field, 175,345)).place(x=175, y=345)
ButtonL = tk.Button(frameKey, text="l", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("l", text_field, 200,345)).place(x=200, y=345)
Buttonç = tk.Button(frameKey, text="ç", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("ç", text_field, 225,345)).place(x=225, y=345)
ButtonEnter = tk.Button(frameKey, text="Enter", height=2, width=10, background="light blue",
                        command=lambda: print_value("\n", text_field)).place(x=250, y=345)
ButtonZ = tk.Button(frameKey, text="z", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("z", text_field, 0,390)).place(x=0, y=390)
ButtonX = tk.Button(frameKey, text="x", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("x", text_field, 25,390)).place(x=25, y=390)
ButtonC = tk.Button(frameKey, text="c", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("c", text_field, 50,390)).place(x=50, y=390)
ButtonV = tk.Button(frameKey, text="v", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("v", text_field, 75,390)).place(x=75, y=390)
ButtonB = tk.Button(frameKey, text="b", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("b", text_field, 100,390)).place(x=100, y=390)
ButtonN = tk.Button(frameKey, text="n", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("n", text_field, 125, 390)).place(x=125, y=390)
ButtonM = tk.Button(frameKey, text="m", height=2, width=2, background="light blue",
                    command=lambda: fk.control_button("m", text_field,150,390)).place(x=150, y=390)
ButtonComma = tk.Button(frameKey, text=",", height=2, width=2, background="light blue",
                        command=lambda: print_value(",", text_field)).place(x=175, y=390)
ButtonDot = tk.Button(frameKey, text=".", height=2, width=2, background="light blue",
                      command=lambda: print_value(".", text_field)).place(x=200, y=390)
ButtonSpace = tk.Button(frameKey, text=" ", height=2, width=10, background="light blue",
                        command=lambda: print_value(" ", text_field)).place(x=75, y=435)
ButtonSeven = tk.Button(frameKey, text="7", height=2, width=2, background="light blue",
                        command=lambda: print_value(7, text_field)).place(x=300, y=300)
ButtonEight = tk.Button(frameKey, text="8", height=2, width=2, background="light blue",
                        command=lambda: print_value(8, text_field)).place(x=325, y=300)
ButtonNine = tk.Button(frameKey, text="9", height=2, width=2, background="light blue",
                       command=lambda: print_value(9, text_field)).place(x=350, y=300)
ButtonSix = tk.Button(frameKey, text="6", height=2, width=2, background="light blue",
                      command=lambda: print_value(6, text_field)).place(x=350, y=345)
ButtonFive = tk.Button(frameKey, text="5", height=2, width=2, background="light blue",
                       command=lambda: print_value(5, text_field)).place(x=325, y=345)
ButtonFour = tk.Button(frameKey, text="4", height=2, width=2, background="light blue",
                       command=lambda: print_value(4, text_field)).place(x=300, y=345)
ButtonThree = tk.Button(frameKey, text="3", height=2, width=2, background="light blue",
                        command=lambda: print_value(3, text_field)).place(x=350, y=390)
ButtonTwo = tk.Button(frameKey, text="2", height=2, width=2, background="light blue",
                      command=lambda: print_value(2, text_field)).place(x=325, y=390)
ButtonOne = tk.Button(frameKey, text="1", height=2, width=2, background="light blue",
                      command=lambda: print_value(1, text_field)).place(x=300, y=390)
ButtonZero = tk.Button(frameKey, text="0", height=2, width=2, background="light blue",
                       command=lambda: print_value(0, text_field)).place(x=325, y=435)



root.mainloop()













