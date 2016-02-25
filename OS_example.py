import os,time

currentDir = os.getcwd()  # get current working directory
print(currentDir)

try:
    os.mkdir('/home/abhishek/Desktop/newDir')
    time.sleep(4)
    os.rename('/home/abhishek/Desktop/newDir','/home/abhishek/Desktop/newDir1')
    time.sleep(4)
    os.rmdir('/home/abhishek/Desktop/newDir1')
except Exception as e:
    print(str(e))


