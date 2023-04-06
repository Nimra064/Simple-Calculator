#import the Library
import tkinter as tk

#Creat a window 
window = tk.Tk()

#Set the Dimension of the window 
window.geometry("200x200")

#Disable the resize the window 
window.resizable(False, False)

#Title  
window.title("Calculator")

#calculate function
input_value=''
dis_res=tk.StringVar()
# Click button action Function
def click_button_action(value):
    global dis_res
    global input_value
    input_value=input_value+value
    print(dis_res.set(input_value))
# Clear Function
def clear():
    global input_value
    input_value=''
    dis_res.set(input_value)
# CE Function
def CE():
    global input_value
    input_value = '0'
    dis_res.set(input_value)
def x():
    global input_value
    if len(input_value)==1:
        input_value = ''
        dis_res.set(input_value)

    else:
        input_value=input_value[:-1]
        dis_res.set(input_value)

# Equal Function
def equal():
    global input_value
    input_value=str(eval(input_value))
    dis_res.set(input_value)
    input_value=''


#Creat a Framework To Display
display=tk.Frame(window , width=312, height=30, bd=8 , highlightbackground="Grey", highlightcolor="Grey", highlightthickness=1)
display.pack(side = tk.TOP)

#Display the input_field inside the frame

output_display=tk.Entry(display , state='disabled', font=('arial' , 20 , 'bold') , textvariable= dis_res , fg='black' , bg="#eee"  , justify=tk.LEFT)
output_display.grid(row=0 , column=0)
# output_display.pack()

#Creat a Framework To Clickable Button
input_frame=tk.Frame(window , width=312 , height=800, highlightbackground="Grey", highlightcolor="Grey", highlightthickness=1 )
input_frame.pack()

#Creat a button inside a input frame
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
input_frame_button=tk.Button(input_frame , text='%' , command= lambda : click_button_action('%') ,activebackground='grey' , width=5 , height= 1 , justify=tk.LEFT).grid(row=4 , column=3 , padx=1 , pady=1)



window.mainloop()
