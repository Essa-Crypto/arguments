import os
shutdown = input("Do youm wish to shut down your compuet ? (yes or no):")

if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")