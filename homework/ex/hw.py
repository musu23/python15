attempts = 0
while True:
    try:
        age = int(input('Age: '))
    except ValueError:
        attempts += 1
        if attempts == 3:
            print('You entered an invalid value too many times. Please try again later...')
            break
        print('Invalid value. Try again.')
        continue

    if age >= 18:
        print('You are grown')
    else:
        print('You are a child!')
    break


