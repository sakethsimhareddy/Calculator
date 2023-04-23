# Calculator
This is a Python program that uses the Tkinter module to create a simple calculator GUI. The calculator has a text input box, an entry widget, with a width of 40 and a border width of 5. It also has several buttons for the user to input numbers and mathematical operations.

The program starts by importing the Tkinter module, and then creating an instance of the Tkinter class, named 'root'.

Next, a global variable 'math' is initialized to 'num', indicating that the user has not yet entered any mathematical operation. The 'num1' variable is also initialized to 0.

The program defines several functions to handle the user's button clicks. The 'bottom_click(num)' function takes a number as an argument and appends it to the end of the text input box.

The 'bottom_clear()' function clears the text input box.

The 'bottom_add()', 'bottom_sub()', 'bottom_mul()', and 'bottom_div()' functions set the 'math' variable to 'add', 'sub', 'mul', and 'div', respectively, and store the current value of the text input box in the 'num1' variable.

The 'bottom_power()' function sets the 'math' variable to 'power', and stores the current value of the text input box in the 'num1' variable.

The 'bottom_equall()' function performs the appropriate mathematical operation based on the value of the 'math' variable, using the 'num1' variable as the first operand and the current value of the text input box as the second operand. The result of the operation is displayed in the text input box, and the 'math' variable is set back to 'num'.

Finally, the program creates several buttons for the user to input numbers and mathematical operations. Each button is created using the Button widget and is assigned a command function that is called when the button is clicked. The buttons are then placed in the GUI using the grid() method.

The program ends by calling the mainloop() method on the 'root' instance, which starts the event loop and keeps the program running until the user closes the window.
