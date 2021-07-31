
def main():
    number = input('Enter your phone number here: ')
    message = phone_validator(number)
    if message == 'lenght':
        print('Your number should consist of exactly 10 digits')
    elif message == 'digits':
        print('Your number should consist of only numerical chars')
    elif message == 'valid':
        print('Your number is valid!')
    else:
        print('Something went wrong! Contact developer')



def phone_validator(phone_number: str) -> str:
    """Return tuple(bool and message) if the phone number consist of 10 digits
    Message specifies the what's wrong with the number provided"""
    if len(phone_number) < 10:
        return f'lenght'
    elif not phone_number.isdigit():
        return 'digits'
    else:
        return 'valid'


if __name__ == '__main__':
    main()