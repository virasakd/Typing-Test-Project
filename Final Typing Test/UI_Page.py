from lib2to3.pytree import NegatedPattern
from tkinter import *
import time
import random
import threading
from turtle import color
from PIL import ImageTk, Image
import json
import requests

Gen_text = "Generate Text Button: Use this button to generate different passage for the typing test."
Res_text = "Result Button: Allows you to examine your scores in greater depth. Displaying words per minute(WPM), and accuracy."
Reset_text = "Reset/Save Button: This button allows you to reset your text box and save your previous results."
sent_text = "Text Analysis: This button provides a sentiment analysis of the random passage generated."
var = "Text will be generated here...."

# return if the paragraph is postive, negative or neutral.



class TypingTest:

    def __init__(self):

        self.window = Tk()
        self.window.geometry("1450x850+25+25")
        self.window.config(bg = "#18202A")
        self.window.title("Speed Typing Test")
        
        # title of the page
        self.main_title =  Label(self.window, text= "Speed Typing Test", font=("Times",50),fg="grey", bg="#18202A")
        self.main_title.place(x = 500,y= 10)

        # frame for generated text area
        self.area_frame = LabelFrame(self.window, text="Generated Text Area", font=("Times", 15),width=700,height=300)
        self.area_frame.place(x=425, y=150)
        self.area_frame.propagate(False)

        #message box, where the generated text will be displayed
        self.paragraph = Message(self.area_frame, text=var,font=("Times", 14), aspect=300)
        self.paragraph.pack(padx=10, pady=10)
      
        #Text area

        self.text_area = Text(self.window,height= 13,width=78, font=("Times", 14), wrap=WORD)
        self.text_area.place(x=425, y=500)
        self.text_area.bind("<KeyRelease>",self.start_typing)


        #Interactive buttons =============================================================

          #Instructions button.
        self.instruct = Button(self.window, text = "Instructions", font=("Times",20), bg = "grey", fg = "#18202A", command = self.display_instruct)
        self.instruct.config(width=11,height=2)
        self.instruct.place(x=50, y=50),


        # generate text button.
        self.generate = Button(self.window, text = "Generate Text", font=("Times",20),bg = "grey", fg = "#18202A",command= self.new_text)
        self.generate.config(width=11,height=2)
        self.generate.place(x=50, y=200)

        #reset page button.
        self.reset_page = Button(self.window, text = "Reset/Save",font=("Times", 20), bg = "grey", fg = "#18202A",command = self.reset_text)
        self.reset_page.config(width=11,height=2)
        self.reset_page.place(x=50, y=350)

        #sentiment analysis button.
        self.text_analysis =  Button(self.window, text = "Text Analysis",font=("Times", 20),bg = "grey", fg = "#18202A",command = self.sentiment_a)
        self.text_analysis.config(width=11,height=2)
        self.text_analysis.place(x=50, y=500)

        #result button.
        self.results = Button(self.window, text = "Test Results", font=("Times",20),bg = "grey", fg = "#18202A",command = self.show_res)
        self.results.config(width=11,height=2)
        self.results.place(x=50, y=650)

        #time label
        self.Timer = Label(self.window, text= "Rate of Chars: 0:00\nTIME:0:00", font=("Times", 20))
        self.Timer.place(x=1180,y=250)


        # addition variables
        self.count = 0
        self.isRunning = False
        self.previous_time = 0
        
   

        self.window.mainloop()


    # generate new text when user hit the "generate new text button"
    def new_text(self):

        #write a request to the file pipe for webscraper microservice
        write2_file = open("gen_comm.txt","w")
        write2_file.write("request")

        write2_file.close()
        time.sleep(2)

        #after 2 seconds read in the paragraph generated.
        readin_file = open("gen_comm.txt","r")
        string_holder = readin_file.readline()

        readin_file.close()
        self.paragraph['text'] = string_holder
    


    # sentiment analysis functionality
    def sentiment_a(self):

        if self.isRunning == False:
            string = self.paragraph['text']
        
        #request data from matthew's microservice
            url = f"https://projectmicroservices-7uy7oyn5ia-uc.a.run.app/sentiment/{string}"
            req = requests.get(url)
            data = json.loads(req.content)
            

            print(data)
            positive = data['pos']
            neutral = data['neu']
            negative = data['neg']
            comp = data['compound']

            result_string = sent_result(comp)

            #convert numbers to strings to print out
            positive = str(positive)
            neutral = str( neutral)
            negative = str( negative)
            comp = str(comp)

           

            #create popup
            popup = Toplevel(self.window)
            popup.title("Sentiment Analysis")
            popup.config(bg = "grey")
            popup.geometry("1000x600+300+50")


            #display sentiment analysis to the popup screen.
            title = Label(popup, text= "A Sentiment Analysis of the Text",font=("Times", 35),bg = "grey", fg = "#18202A")
            title.pack(pady=10)

            line_pos = Label(popup, text = "The overall Positivity of the text = " + positive,font=("Times", 25),bg = "grey", fg = "#18202A")
            line_pos.pack(pady= 10)

            line_nue = Label(popup, text = "The overall Nuetrality of the text = " + neutral,font=("Times", 25),bg = "grey", fg = "#18202A")
            line_nue.pack(pady= 10)

            line_neg = Label(popup, text = "The overall Negativity of the text = " + negative,font=("Times", 25),bg = "grey", fg = "#18202A")
            line_neg.pack(pady= 10)

            line_com = Label(popup, text = result_string + comp,font=("Times", 20),bg = "grey", fg = "#18202A")
            line_com.pack(pady= 10)

            destroy = Button(popup, text="Close!!",font=("Times", 25),bg = "#18202A", fg= "grey", command= popup.destroy)
            destroy.pack(pady=10)
            popup.mainloop()

        
    
    #display the instructions on a popup page when the user clicks the button.
    def display_instruct(self):

        #Create popup window.
        top_window = Toplevel(self.window)
        top_window.title("Instructions")
        top_window.config(bg = "grey")
        top_window.geometry("1000x600+300+50")


        #create lables and messages for the buttons
        instruct_label = Label(top_window, text= "Button Instructions:",font=("Times", 25),bg="grey",fg = "#18202A")
        instruct_label.pack(pady = 10)

        Gen_message1 = Message(top_window, text = Gen_text,font=("Times", 20), aspect=1000,bg = "grey",fg = "#18202A")
        Gen_message1.place(x= 50,y=100)

        
        res_message = Message(top_window, text = Res_text, font=("Times", 20), aspect=1000,bg = "grey",fg = "#18202A")
        res_message.place(x= 50,y=200)
        

        rest_mes =  Message(top_window, text = Reset_text, font=("Times", 20), aspect=1000, bg = "grey",fg = "#18202A")
        rest_mes.place(x= 50,y=300)
        
        sent_message =  Message(top_window, text = sent_text, font=("Times", 20), aspect=1000,bg = "grey",fg = "#18202A")
        sent_message.place(x= 50,y=400)
        
        # create a button to close the program.
        close = Button(top_window, text = "Close",font=("Times", 25),bg = "#18202A", fg= "grey",  command =top_window.destroy)
        close.place(x= 450,y=500)
        top_window.mainloop()


    #start typing exam, when the user starts typing
    def start_typing(self,event):
        if not self.isRunning:

            #set is running to true, if any button other than the shift button is hit.
            if not event.keycode in [16]:
                self.isRunning = True

                val = threading.Thread(target=self.time_thread)
                val.start()

        # check if the user spelling is correct, if so label the text blue. if not set red.
        if self.paragraph.cget('text').startswith(self.text_area.get("1.0",'end-1c')):
            self.text_area.config(fg="blue")
        else:
            self.text_area.config(fg="red")

        # if the user has completed the passage, set passage to green, and stop the timer.
        if self.text_area.get("1.0",'end-1c') == self.paragraph.cget('text'):
            self.isRunning = False
            self.text_area.config(fg="green")
            

    # start the times, when the variable "isRunning is true."
    def time_thread(self):
        while self.isRunning:
            time.sleep(0.1)
            # increment the timer by one second
            self.count += 0.1

            #calculate characters per minute
            characters_per_min = len(self.text_area.get("1.0",'end-1c')) / self.count

            characters_per_min =  characters_per_min * 60
            self.Timer.config(text=f"Rate of Chars: { characters_per_min:.2f}\n TIME: {self.count:.2f}")
    

    def reset_text(self):
        if self.count > 10:
            self.previous_time = self.count
            self.previous_time = int((len(self.text_area.get("1.0",'end-1c').split(" "))/ self.previous_time ) * 60)
        print(self.previous_time)
        self.count = 0.00
        self.isRunning = False
        self.Timer.config( text= f"Rate of Chars: {0.00},\n, TIME: {0.00}")
        self.text_area.delete("1.0",END)
    


    def show_res(self):

        if self.isRunning == False:

            write_file = open("res_coms.txt", "w")
            holder = str(self.previous_time)
            write_file.write(holder)
            write_file.close()
            time.sleep(1)

            read_res = open("res_coms.txt", "r")
            result_line = read_res.readline()

            #pop up screen
            res_window = Toplevel(self.window)
            res_window.title("Test Results")
            res_window.config(bg = "grey")
            res_window.geometry("600x600+500+100")

            label_wpm = Label(res_window,text= "Your WPM = " + holder,font=("Times", 40), bg = "grey", fg = "#18202A")
            label_wpm.pack(pady=10)
            text_wpm = Label(res_window,text=result_line,font=("Times", 30),bg = "grey", fg = "#18202A")
            text_wpm.pack(pady=10)
            close_button = Button(res_window,text="RETURN",font=("Times", 30), bg = "#18202A", fg= "grey", command=res_window.destroy)
            close_button.pack(pady=15)



    
def sent_result(comp_value):
    final_string = ""

    if comp_value > 0.51:
        final_string = "The generated paragraph is overall more positive, with a sentiment score of: "
    elif comp_value < 0.51 and comp_value > 0.49:
         final_string = "The generated paragraph is nuetral, with a sentiment score of: "
    else:
        final_string = "The generated paragraph is overall more negative, with a sentiment score of: "

    return final_string




#call the class and run the program.
TypingTest()        
