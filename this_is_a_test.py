import os

root = r'C:\Users\Dawn\Desktop\Bobby\Python'

files = "Testing"

print(os.path.join(root, files))

print(os.getcwd())

os.chdir(r'C:\\')
print(os.getcwd())