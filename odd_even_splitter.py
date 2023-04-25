#open the needed files
with open("numbers.txt" , "r") as number_file, open("even.txt" , "a") as even_file, open("odd.txt" , "a") as odd_file:
    #for loops to read the lines
    print("\033[1;34;40m ~" *134)
    print("\033[1;34;40m Hello, this program will now check the numbers in the numbers.txt file")
    import time
    time.sleep(5)
    for line in number_file:
        #convert the lines to integeers
        number = int(line)
        #check if even
        if number % 2 == 0:
            #convert to sring
            even = str(number)
            #write to even file
            even_file.write(even + "\n")
        #check if odd
        elif number % 2 == 1:
            #convert to sring
            odd = str(number)
            #write to even file
            odd_file.write(odd + "\n")
    print("\033[1;34;40m Hello this program is now completed pls check the even.txt and odd.txt now")
    print("\033[1;34;40m ~" *134)