import json


SEARCH_OPTIONS = ['number', 'first name', 'last name', 'full name', 'city']
JSON_NAME = 'contacts'


def load_book() -> dict:
    """Returns the phonebook"""
    with open('data_phonebook.json', 'r+') as data_ph:
        return json.load(data_ph)


def save_book(data: dict) -> None:
    """Saves the dict to json file and closes it"""
    with open('data_phonebook.json', 'w') as data_ph:
        json.dump(data, data_ph, indent=4)


def read_book(data: dict) -> str:
    """Returns the phonebook-json as a fancy string"""
    return json.dumps(data, indent=4)


def add_entry(data: dict):
    """Return the phonebook with a new entry added"""
    check = False
    while not check:
        number = input('Enter the phone number: ')
        validate = validate_number(number)
        duplicate = validate_duplicate(data, number)
        if validate and duplicate:
            check = True

    f_name = input('Enter the first name: ')
    l_name = input('Enter the last name: ')
    city = input('Enter the city: ')
    print()

    entry = {"number": number, "first_name": f_name, "last_name": l_name, "city": city}
    return data.get(JSON_NAME).append(entry)


def validate_number(number: str) -> bool:
    """Returns True if a correct number was given"""
    if not number.startswith('+'):
        print('The number should start with "+" sign')
        return False

    elif (l:=len(number.lstrip('+'))) < 10:
        print(f'The number should contain 10 digits. Yours contain {l} digits')
        return False

    elif not number.lstrip('+').isdigit():
        print('The number should contain digits only')
        return False

    else:
        return True


def validate_duplicate(data: dict, number: str) -> bool:
    """Returns whether there the given number is already in the phonebook"""
    book_numbers = [contact.get('number') for contact in data.get(JSON_NAME)]
    if number in book_numbers:
        print(f'The contact with the number {number} already exists!')
        return False
    else:
        return True

def search(data: dict) -> list:
    """Returns the list containing the search result"""
    print('Availiable search options are: ')
    print(*SEARCH_OPTIONS, sep='\n')

    while (search_option:= input('option: ')) not in SEARCH_OPTIONS:
        print('Such search option is availiable. Try again')
    
    query = input('Enter your query: ').lower()
    contacts = []

    if search_option == 'number':
        contacts = [contact for contact in data.get(JSON_NAME) if contact.get('number') == query]

    elif search_option == 'first name':
        contacts = [contact for contact in data.get(JSON_NAME) if contact.get('first_name').lower() == query]
        print(contacts)

    elif search_option == 'last name':
        contacts = [contact for contact in data.get(JSON_NAME) if contact.get('last_name').lower() == query]

    elif search_option == 'city':
        contacts = [contact for contact in data.get(JSON_NAME) if contact.get('city').lower() == query]

    elif search_option == 'full name':
        f_name, l_name = query.split()
        contacts = [contact for contact in data.get(JSON_NAME) if contact.get('first_name').lower() == f_name and contact.get('last_name').lower() == l_name]

    if len(contacts) < 1:
        return None
    else:
        return json.dumps(contacts, indent=4)


def delete_contact(data: dict) -> dict:
    """Returns the deleted contact"""
    validate = False
    while not validate:
        number = input('Enter the number: ')
        validate = validate_number(number)

    contacts = [contact for contact in data.get(JSON_NAME) if contact.get('number') == number]
    if not contacts:
        print('There is no contacts in the phonebook with the given number', number)

    else:
        entry: int = None
        for contact in data.get(JSON_NAME):
            if contact.get('number') == number:
                entry = data.get(JSON_NAME).index(contact)

        removed = data.get(JSON_NAME).pop(entry)

    return json.dumps(removed, indent=4)


def update(data: dict) -> int:
    """Updates the contact"""
    validate = False
    while not validate:
        number = input('Enter the number of a contact you want to update: ')
        validate = validate_number(number)
    
    contact = [contact for contact in data.get(JSON_NAME) if contact.get('number') == number][0]
    if len(contact) < 1:
        print('\Contact not found! Try using "read" to check the contact with such number exists')
        return 1
    else:
        print('\nContact found!\n')
        print(json.dumps(contact, indent=4))
    
    fields = ['number', 'first_name', 'last_name', 'city']
    while True:
        field = input('Enter what field you want to update: ').lower()
        if field not in fields:
            print('Incorrect field! Try again!\n')
        else:
            break
    
    if field == 'number':
        validate = False
        while not validate:
            number = input('Enter new number here: ')
            validate = validate_number(number)
        
        contact[field] = number
    
    elif field == 'first_name':
        f_name = input('Enter new first name here: ')
        contact[field] = f_name

    elif field == 'last_name':
        l_name = input('Enter new last name here: ')
        contact[field] = l_name

    elif field == 'city':
        city = input('Enter new city here: ')
        contact[field] = city
    
    return 0