import phonebook_methods as methods


INSTRUCTIONS = [
    'To use phonebook use the following commands:', 
    '"read" to see the whole phonebook', 
    '"add" to add a record',
    '"search" to search for an entry',
    '"delete" to delete an entry from the phonebook',
    '"update" to change the info of an given entry',
    '"manual" to see this instruction again',
    '"exit" to save the phonebook and exit the programm'
    ]


book = methods.load_book()

print(*INSTRUCTIONS, sep='\n')
while True:
    command = input('Command: ').lower()
    print()

    if command == 'read':
        print(methods.read_book(book), '\n')

    elif command == 'add':
        methods.add_entry(book)
        print('Entry successfully added to the phonebook!\n')

    elif command == 'search':
        found = methods.search(book)
        if not found:
            print('Nothing has been found. Try using "read" to see the whole phonebook or use different query\n')
        else:
            print(found, '\n')
    
    elif command == 'delete':
        print('To delete a contact, please, provide the number')
        removed = methods.delete_contact(book)
        print('The following contact was removed from the phonebook:', removed, '\n', sep='\n',)
    
    elif command == 'update':
        mistake = methods.update(book)
        if not mistake:
            print('The contact has been updated successfully!\n')

    elif command == 'manual':
        print(*INSTRUCTIONS, sep='\n')

    elif command == 'exit':
        methods.save_book(book)
        print('Bye!\n')
        quit()

    else:
        print(f'\nUnexpected command "{command}". Type "manual" to see instructions\n')
        continue
    
