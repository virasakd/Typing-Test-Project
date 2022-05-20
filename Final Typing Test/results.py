import time


while True:

    red_file = open("res_coms.txt", "r")

    if (red_file.readline().isnumeric()):
        print("true")

        red_file.seek(0)

        words_per = int(red_file.readline())
        red_file.close()

        write_to = open("res_coms.txt", "w")


        if words_per > 5 and words_per < 110:

            if words_per > 5 and words_per < 40:
                write_to.write("You are below average.Lol")

            elif words_per >= 40 and words_per < 55:
                write_to.write("You are Averge, Congrats.")

            else:
                write_to.write("Congrats!!, You are Above Average")
        else:
            write_to.write("Invalid attempt!!")
        
        write_to.close()
            



