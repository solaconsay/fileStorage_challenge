# constant values
IMAGE_FILES = 100.0
EXECUTABLE_FILES = 2048.0
SYSTEM_FILES = 20.0

# get the inputs from the users
imageFiles = input("Please enter the number of image files: ")
executableFiles = input("Please enter the number of exectutable files: ")
systemFiles = input("Please enter the number of system files: ")


# get file sizes in KB
imageFiles = float(imageFiles) * IMAGE_FILES
executableFiles = float(executableFiles) * EXECUTABLE_FILES
systemFiles = float(systemFiles) * SYSTEM_FILES

# storage required in KB
storageRequried = imageFiles + executableFiles + systemFiles

# convert to MB
storageRequriedInMB = storageRequried / 1024.0

# output
print("The total storage required is " + str(storageRequried) + " Kilobytes or " + str(storageRequriedInMB) + " Megabytes")


