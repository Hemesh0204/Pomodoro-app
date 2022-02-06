import threading
import time

from win10toast import ToastNotifier
import tkinter as tk

class CountDownTimer:

    def __init__(self):
        ## Creating the window
        self.root = tk.Tk()
        
        self.root.geometry("460x250") ## Dimension of the output

        self.root.title("Pomodoro Timer")


        self.time_entry = tk.Entry(self.root, font = ("Arial", 30))
        self.time_entry.grid(row=0, column=0, columnspan= 2, padx=5, pady = 5)

        self.start_button = tk.Button(self.root, font = ("Arial", 30),text = "Start",  command = self.start_thread)
        self.start_button.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.stop_button = tk.Button(self.root, font = ("Arial", 30), text = "Stop", command = self.stop)
        self.stop_button.grid(row = 1, column= 1, padx= 5, pady = 5)

        self.time_label = tk.Label(self.root,font = ("Arial", 30), text="00:00:00")
        self.time_label.grid(row = 2, column= 0, columnspan =2, padx =  5, pady=5)

        self.stop_loop = False

        self.root.mainloop()


    def start_thread(self):
        t = threading.Thread(target = self.start)
        t.start()

    def start(self):
        self.stop_loop = False

        hours, minutes, seconds = 0 ,0, 0

        string_split =  self.time_entry.get().split(":")
        print(string_split)
        if len(string_split) == 3:
            hours = int(string_split[0])
            minutes = int(string_split[1])
            seconds = int(string_split[2])

        elif len(string_split) == 2:
            minutes = int(string_split[0])
            seconds = int(string_split[1])
            

        elif len(string_split) == 1:
            seconds = int(string_split[0])
        else:
            print("Enter a valid string")
            return
        
        full_time = hours *3600 + minutes * 60 + seconds
        
        while full_time > 0 and not self.stop_loop:
            print(full_time)
            self.stop_loop = False
            full_time -= 1
            
            minutes, seconds = divmod(full_time, 60)
            hours, minutes = divmod(minutes, 60)

            self.time_label.config(text=f"Time : {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)
        
        if not self.stop_loop:
            toast = ToastNotifier()
            toast.show_toast("Pomodoro Session is Over"," Session is Over", duration = 10)



    def stop(self):
        self.stop_loop = True
        self.time_label.config(text="00:00:00")



CountDownTimer()

