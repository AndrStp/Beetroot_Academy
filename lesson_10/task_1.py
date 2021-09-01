# Files

# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it. 
# Then write another script that opens myfile.txt, and reads and prints its contents. Run your two scripts from the system command line. 
# Does the new file show up in the directory where you ran your scripts? 
# What if you add a different directory path to the filename passed to open?

# Note: file write methods do not add newline characters to your strings; 
# add an explicit ‘\n’ at the end of the string if you want to fully terminate the line in the file.


def main():
    while True:
        command = input('Enter your command here:\n\
to create a text-file with text - type "w"\n\
to read file - type "r"\n\
to exit program - type "exit"\n\
command: ').lower()
        if command == 'w':
            file = input('Enter text-file name here (ex. text.txt): ')
            text = input('Enter your text here: ')
            write_to_file(file, text)
            print('\nOperation is successfull!\n')
        elif command == 'r':
            file = input('Enter text-file name here (ex. text.txt): ')
            print('\nFile content:', read_file(file), '\n')
        elif command == 'exit':
            print('\nBye!\n')
            quit()
        else:
            print(f'\nunexpected command "{command}", try again\n')
            continue


def write_to_file(f_name: str, text: str):
    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(text)
    return 


def read_file(f_name: str) -> str:
    with open(f_name, 'r', encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    main()
