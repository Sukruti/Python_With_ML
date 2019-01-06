#PYTHON FILE HANDLING
#file_obj=open("D:\DataScience\Python\Programs\9Sep\ReadFile.txt")
#print(file_obj.read())

#----------------------------------------------------------------------------------------------------------------

#file_obj=open("D:\DataScience\Python\Programs\9Sep\WriteFileEg.txt" ,"a")
#file_obj.write("\nH am good")
#file_obj.close()

#----------------------------------------------------------------------------------------------------------------


file_obj=open("D:\DataScience\Python\Programs\9Sep\WriteFileEg1.txt" ,"a+")
file_obj.write("\nThis is an exampl of a+ operation")
#seek alow to move to any point in file
file_obj.seek(0)
read_value=file_obj.read()
#print(read_value)

print(file_obj.readline())
file_obj.close()



# convert binary to normal and normal to binary string
#10 lines in txt files read singl line by line and print 
