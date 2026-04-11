# # playing with print statement print(    sep = " ", end = \n, file = sys.stdio, flush = True/false)

# with open("my_file.txt", "w") as f:
#     print("I am your little secret", file = f)
    
# # u won't see any output here but u will find that it either creates or if already there a file named my file.txt and there u can see the output so the file output in print statement tell the python interpreter where to show the output.

# ''' for flush'''
# import time
# for i in range(5, 0, -1):
#     print(i, flush = True, end = " ")
# time.sleep(1)

# # when flush true u will notice it gives the op fast and when false it shows nothing on the console window for 2-5 sec then shows the op as it doesn't wait for the buffer mem to filled in order to show the op when true


''' Escape seq char'''
print("i am a very \"good girl\".\nI like reading books") # here we know ki agar bina \ ke likhte to error ata hence we use escape seq char



