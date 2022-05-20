import time


while True:


    red_file = open("res_coms.txt", "r")

    # if a number has been sent through the communication pipe, then a request has been sent.
    if (red_file.readline().isnumeric()):
        print("true")

        red_file.seek(0)

        # convert the first line to a string
        words_per = int(red_file.readline())
        red_file.close()


        write_to = open("res_coms.txt", "w")

        # check to see if the results are irregular
        if words_per > 5 and words_per < 110:

            # if the score is less than 40, write back "below average"
            if words_per > 5 and words_per < 40:
                write_to.write("You are below average.Lol")

             # if the score is in between 40 and 55, write back "average"
            elif words_per >= 40 and words_per < 55:
                write_to.write("You are Averge, Congrats.")

            #if the score is greater than 55, then write back" above average"
            else:
                write_to.write("Congrats!!, You are Above Average")
        else:
            write_to.write("Invalid attempt!!")
        
        write_to.close()
            



