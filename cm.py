# importing os module 
import os 

# importing shutil module 
import shutil 

# path 
path = 'C:/Users/Kaif/Documents/kaif'

# List files and directories 

print("Before moving/copying file:") 
print(os.listdir(path)) 


# Source path 
source = 'C:/Users/Kaif/Documents/kaif/python'

# Destination path 
destination = 'C:/Users/Kaif/Desktop/destination'

# Move all the content of 
# source to destination 
dest =shutil.move(source, destination) 

# Copy all the content of
# source to destination
#dest =shutil.copytree(source, destination)

# If you want to copy a particular file
# from source to destination
#dest =shutil.copyfile(source + "/example.txt", destination)

# List files and directories 
 
print("After moving/copying file:") 
print(os.listdir(path)) 

# Print path of newly 
# created file 
print("Destination path:", dest) 
