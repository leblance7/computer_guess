while True:
    input_value = input('Do you want me or you to guess')
    if input_value in ['You','you']:
        import computer_guess.py
    elif input_value in ['Me', 'me']:
        import human_guess.py
        
