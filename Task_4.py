# open("Task.txt",'xt')
try:
    with open("Task.txt", 'w') as file_handler:
        file_handler.write("reading file content:\n")
        file_handler.write("Line 1: this is a sample text file.\n")
        file_handler.write("Line 2: it contains multiple lines.\n")
    print("File written successfully!")

# print("file written Done!.")
except FileNotFoundError:
    print("Error:The file 'Task.txt' was not found.")




