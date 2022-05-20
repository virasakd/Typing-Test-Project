import time
from typing import final
from bs4 import BeautifulSoup
import requests
import re
import random
import json


#random words for website.

words = ["dogs","cats","sports","jazz","music","football","food","time","texas","earth","birds"]

# function
def cleanUp(final_string):
   
   # remove all citiations and other speical characters
    final_string = re.sub(r'\[[0-9]*\]',' ',final_string)
    final_string = re.sub(r'\s+',' ',final_string)
    final_string = re.sub(r"[^A-Za-z0-9,.']"," ",final_string)
    final_string = re.sub(r'\s+',' ',final_string)
    
    # create a new string to hold the new result.
    temp_string = final_string

    # loop through each character and remove all non-english characters.
    for x in range(len(final_string)):
        if final_string[x].isascii() == False:
            
            temp_string = final_string.replace(final_string[x],"")
            
        
    return temp_string


def proccess(word):
    url = "https://en.wikipedia.org/wiki/" + word

    # request to interact with the website, them implement html scraper.
    res = requests.get(url)
    doc = BeautifulSoup(res.text, "html.parser")

    # grab all the passeges from the webpage.
    passages = doc.find_all(["p"])
    
    possible_list = []

    # search for pass with long text.
    for i in range(len(passages)):
        length = passages[i].text.split(" ")

        if len(length) > 60 and len(length) < 120:
            possible_list.append(i)

    print(len(possible_list))
        
    # choose one of the selected passeges
    index = random.choice(possible_list)   

        
    #print(passages[index].text)
    # break up the string, and recombine them
    pass_text = passages[index].text.split(" ")
    final_string = ""

    for x in range(len(pass_text)):
        final_string += pass_text[x]

        if(x != len(pass_text)-1):
            final_string += " "

    return final_string

while True:

    #read in the request from the text file.
    read_com = open("gen_comm.txt", "r")
    line = read_com.readline()

    # check if the request is valid.
    if(line == "request"):

        read_com.close()

        # if so, generate a random work to search the webfor
        keyW = random.choice(words)
    
        print(keyW)

        #call function the webscrapes for text
        gen_string = proccess(keyW)

        #remove all extra charaters and additional isses in the passage
        string = cleanUp(gen_string)
        
    
        write_to = open("gen_comm.txt", "w")
        write_to.write(string)
        write_to.close()
         