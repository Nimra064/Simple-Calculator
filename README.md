# Simple-Calculator
Create a contemporary user interface with the Tkinter Python library.<br>
I want to write an article on Creating a contemporary user interface with the Tkinter Python library which helps readers to understand the importance and syntax of the Python Tkinder Library in detail.
Create a contemporary user interface with the Tkinter Python libraryWhy do I choose Tkinter Python Library? <br>
I choose this Library Tkinter is considered to be one of the easiest GUI library to learn, especially for beginners. It has a simple syntax and provides a range of widgets that can be easily added to the GUI.
 Tkinter is available on multiple platforms, including Windows, Linux, and macOS. This means that applications built with Tkinter can run on different operating systems without any major modifications. 
Tkinter offers a high degree of customization, allowing developers to create unique and visually appealing interfaces. It also provides support for themes and styles, making it easy to change the look and feel of the GUI. That is why, I choose Tkinter Library to develop the GUI of Simple Calculator.
<br> What is Tkinter Python Library?<br>
Python provides a variety of choices for GUI development (Graphical User Interface). Tkinter is the approach used the most frequently among all GUI approaches. It is a typical Python interface for the Python-supplied Tk GUI toolkit. The fastest and simplest approach to constructing GUI apps is with Python and Tkinter. It's simple to build a GUI of Simple Calculator using Tkinter.
1. Install the Tkinter Library in System (Linux, Windows,macOS)<br>
2. Open a command prompt or terminal window.<br>
<img width="863" alt="cmd" src="https://user-images.githubusercontent.com/71897920/230414892-4aa23164-1c8d-40b7-b1fa-fcf7bdadca44.png"> <br>
3. Use the following command to install Tkinter via pip:<br>

pip install tk <br>

If you are using Python 2, you may need to use the following command instead:
pip2 install tk
Once the installation is complete, you should be able to import the Tkinter library in your Python code using the following line:
import tkinter as tk
4. Create the main window (container)
window = tk.Tk()
5. Set the Dimension of the window
window.geometry("200x200")
6. Disable the resize the window
window.resizable(False, False)
7. Add the Title on the top of the window
window.title("Calculator")
title( ) Function is used to display the title at the top of the application.
8. Create a Framework To Display
display=tk.Frame(window , width=312, height=30, bd=8 , highlightbackground="Grey", highlightcolor="Grey", highlightthickness=1)
display.pack(side = tk.TOP)
These lines of code create a frame widget called display using the Frame class from the Tkinter library. The frame has a width of 312 pixels, a height of 30 pixels, and a border width of 8 pixels. The highlightbackground, highlightcolor, and highlightthickness options are used to create a grey-coloured highlight around the frame, which helps to visually distinguish it from the other widgets in the window.
The pack() the method is called on the frame object to add it to the window and display it at the top of the window (side=tk.TOP). The pack() a method is one of the geometry managers in Tkinter that arranges widgets in a block or row according to their order of creation and the options specified. In this case, the display frame is placed at the top of the window and occupies the full width of the window
9. Display the input field inside the frame
output_display=tk.Entry(display , state='disabled', font=('arial' , 20 , 'bold') , textvariable= dis_res , fg='black' , bg="#eee"  , justify=tk.LEFT)
output_display.grid(row=0 , column=0)
These lines of code create a Tkinter entry widget in the 'display' container with the following specifications:
state='disabled' makes the widget read-only and unresponsive to user input.
font=('arial', 20, 'bold') sets the font family, size, and weight of the text displayed in the widget.
textvariable=dis_res associates a Tkinter variable named dis_res with the widget. Any changes to dis_res will automatically update the text displayed in the widget.
fg='black' sets the text colour to black.
bg='#eee' sets the background colour to a light grey.
justify=tk.LEFT aligns the text to the left side of the widget.

Finally, grid(row=0, column=0) places the widget in the first row and the first column of the 'display' container using the grid layout manager.
10. Create a Framework To Clickable Button
input_frame=tk.Frame(window , width=312 , height=800, highlightbackground="Grey", highlightcolor="Grey", highlightthickness=1 )
input_frame.pack()
These lines of code create a Tkinter frame widget with the following specifications:
tk.Frame(window, width=312, height=800, highlightbackground="Grey", highlightcolor="Grey", highlightthickness=1) creates a new frame widget with a width of 312 pixels, a height of 800 pixels, and a grey border of 1 pixel thickness. The frame is attached to the window widget.
input_frame.pack() displays the frame widget using the pack geometry manager. The pack() the method places the widget in the window according to the available space, which in this case means it will be centered and take up the full width of the window.

The purpose of these lines of code is to create a rectangular area within the window to contain other widgets that will be used for input. By using the frame widget, it's possible to group related widgets together and apply layout options to them as a group.
11. Create a button inside an input frame
input_frame_button=tk.Button(input_frame , text='x'  , command = lambda : x() , activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT ).grid(row=0 , column=0 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame ,  text='CE' , command = lambda : CE() , activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=0 , column=1 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='C' ,  command = lambda : clear() ,activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=0 , column=2 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='=' , command = lambda : equal() , activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=0 , column=3 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame ,text='7', command = lambda : click_button_action('7') ,activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=1 , column=0 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame ,text='8', command = lambda : click_button_action('8') , activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=1 , column=1 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='9', command = lambda : click_button_action('9') ,  activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=1 , column=2 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='*' ,  command= lambda : click_button_action('*') , activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=1 , column=3 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='4' ,command = lambda : click_button_action('4') ,activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=2 , column=0 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='5', command = lambda : click_button_action('5') , activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=2 , column=1 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='6' ,command = lambda : click_button_action('6'),activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=2 , column=2 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='-' , command= lambda : click_button_action('-') ,activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=2 , column=3 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='1' , command = lambda : click_button_action('1'),activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=3 , column=0 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='2', command = lambda : click_button_action('2') , activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=3 , column=1 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='3' , command = lambda : click_button_action('3') ,activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=3 , column=2 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='+' , command= lambda : click_button_action('+') ,activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=3 , column=3 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='0' , command = lambda : click_button_action('0') ,activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=4 , column=0 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='.', command =lambda : click_button_action('.') , activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=4 , column=1 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='/' , command= lambda : click_button_action('/') , activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=4 , column=2 , padx=1 , pady=1)
input_frame_button=tk.Button(input_frame , text='%' , command= lambda : click_button_action('%') ,activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=4 , column=3 , padx=1 , pady=1
This code block creates a calculator interface using the tkinter module in Python. It defines a grid layout for the buttons and assigns each button a specific function using lambda expressions.
The calculator interface consists of an input frame where the buttons are placed. The buttons are defined using the tk.Button() function and are given a text label, a command function to be executed when the button is clicked, an active background color, and a width and height.
The first row of buttons includes the 'x' button, which is not a standard calculator button, but is included here to represent the option to close the calculator. The 'CE' button clears the last entry in the input, while the 'C' button clears the entire input. The '=' button calculates the result of the input expression.

2. The second row of buttons includes the numbers 7, 8, and 9, as well as the multiplication operator '*'.
3. The third row of buttons includes the numbers 4, 5, and 6, as well as the subtraction operator '-'.
4. The fourth row of buttons includes the numbers 1, 2, and 3, as well as the addition operator '+'.
5. The fifth row of buttons includes the number 0, the decimal point '.', and the division operator '/' as well as the modulus operator '%'.
Each button is assigned a unique grid location using the grid() method, which specifies the row and column in which the button is placed. The padx and pady parameters define the padding around each button.
Overall, this code block creates a simple calculator interface with standard mathematical operations
window.mainloop()
Here, I have imported the project [project name] from GitHub repository [repository link]."

DEMO VIDEO
