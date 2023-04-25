#open the needed files
with open("numbers.txt" , "r") as number_file, open("even.txt" , "a") as even_file, open("odd.txt" , "a") as odd_file:
    #for loops to read the lines
    for line in number_file:
        #convert the lines to integeers
        number = int(line)
        #check if even

            #convert to sring

            #write to even file

        #check if odd

            #convert to sring

            #write to even file
