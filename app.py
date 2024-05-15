import numpy as np
import tkinter as tk
from PIL import ImageTk, Image
from app_functions import add_faces
from verify import *
import threading
from tkinter import filedialog, messagebox,simpledialog
import time

def add():
    id1 = len(os.listdir('input_faces'))
    name = simpledialog.askstring("Name Input", "Enter the person's name")
    with open ("people.txt",'a+') as f:
        f.write(","+name)
    id1 = take_photos_input(id1)
    if id1<2:
        name = simpledialog.askstring("Name Input", "Enter the person's name")
        #people.append(name)
        id1 = take_photos_input(id1)
    X,Y = add_faces(id1)
    train_model(X,Y)
    messagebox.showinfo("Results", "SUCESS")

def veriffyy():
    result = verify()
    messagebox.showinfo("Results",f"You are {result}")
    
def resett():
    global received_data
    received_data = ""

import tkinter as tk
import serial
import threading
import psutil

# Global variable to hold received data
received_data = ""

def read_from_serial(ser):
    global received_data
    while True:
        try:
            if ser.in_waiting > 0:
                received_data = ser.readline().decode().strip()
                print("Received:", received_data)  # Optional: Print received data for debugging
            if received_data=="Authorized":
                ser.close()
                return
            time.sleep(0.1)
        except serial.SerialException as e:
            print(f"SerialException occurred: {e}")
            break  # Exit the loop if serial error occurs

def update_gui():
    global received_data
    # Update label text with received data
    label_serial.config(text=received_data)
    root1.lift()
    # Schedule the update_gui function to run again after 100 milliseconds
    root1.after(100, update_gui)
def finger():
    try:
        if 'ser' in locals() and ser.is_open:
            ser.close()
        # Set process priority to high
        psutil.Process().nice(psutil.HIGH_PRIORITY_CLASS)

        # Open serial port
        ser = serial.Serial('COM3', 9600)  # Replace 'COM8' with your Arduino's serial port

        # Create and start thread to continuously read from serial port
        serial_thread = threading.Thread(target=read_from_serial, args=(ser,), daemon=True)
        serial_thread.start()
        serial_thread.join()

        # Start updating the GUI
        update_gui()

        # Run the Tkinter main loop

    except serial.SerialException as e:
        print(f"SerialException occurred: {e}")
def recognizee():
    try:
        finger()
        veriffyy()
    except:
        print("error")
        

 # Create Tkinter window
root1 = tk.Tk()
root1.title("Serial Data Stream")

# Create label to display received data
label_serial = tk.Label(root1, text="", font=("Arial", 12))
label_serial.pack(pady=20)



# Create the main window
root = tk.Tk()
root.title("Biometric Authentication System")
root.geometry("500x400")

# Create a label
label = tk.Label(root, text="Welcome to the Biometric Authentication System", font=("Arial", 16), bg="white")
label.pack(pady=20)

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=20)

# Create buttons
add_button = tk.Button(button_frame, text="Add", width=15, bg="white",command=add)
add_button.pack(side=tk.LEFT, padx=10)

face_recognition_button = tk.Button(button_frame, text="Face Recognition", width=15, bg="white",command=veriffyy)
face_recognition_button.pack(side=tk.LEFT, padx=10)

fingerprint_button = tk.Button(button_frame, text="Fingerprint", width=15, bg="white",command=finger)
fingerprint_button.pack(side=tk.LEFT, padx=10)

# Create a frame for the Recognize button
recognize_frame = tk.Frame(root, bg="white")
recognize_frame.pack(pady=20)

recognize_button = tk.Button(recognize_frame, text="Recognize", width=15, bg="white",command=recognizee)
recognize_button.pack()

reset_button = tk.Button(recognize_frame, text="Reset", width=15, bg="white",command=resett)
reset_button.pack()


root.mainloop()
# Run the main event loop
root.mainloop()