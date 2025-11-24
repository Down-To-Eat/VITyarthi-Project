def get_valid_number(prompt, allow_negative=True, min_val=None, max_val=None):
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("Error: Please enter a value.\n")
                continue
            num = float(value)
            if not allow_negative and num < 0:
                print("Error: Negative values not allowed.\n")
                continue
            if min_val is not None and num < min_val:
                print(f" Error: Value must be at least {min_val}.\n")
                continue
            if max_val is not None and num > max_val:
                print(f"Error: Value must not exceed {max_val}.\n")
                continue
            return num
        except ValueError:
            print("Error: Please enter a valid number.\n")
        except KeyboardInterrupt:
            print("\n\nInput cancelled.\n")
            return None

def get_valid_choice(prompt, valid_options, case_sensitive=False):
    while True:
        try:
            choice = input(prompt).strip()
            
            if not choice:
                print("Error: Please enter a choice.\n")
                continue
            if not case_sensitive:
                choice_compare = choice.lower()
                valid_compare = [opt.lower() for opt in valid_options]
                
                if choice_compare in valid_compare:
                    idx = valid_compare.index(choice_compare)
                    return valid_options[idx]
            else:
                if choice in valid_options:
                    return choice
            
            print(f"Error: Invalid choice. Options: {', '.join(valid_options)}\n")
        
        except KeyboardInterrupt:
            print("\n\nInput cancelled.\n")
            return None

def get_menu_choice(min_choice=1, max_choice=10):
    while True:
        try:
            choice = input(f"\nEnter your choice ({min_choice}-{max_choice}): ").strip()
            
            if not choice:
                print("Error: Please enter a choice number.\n")
                continue
            
            num = int(choice)
            
            if min_choice <= num <= max_choice:
                return num
            else:
                print(f"Error: Please enter a number between {min_choice} and {max_choice}.\n")
        
        except ValueError:
            print("Error: Please enter a valid number.\n")
        except KeyboardInterrupt:
            print("\n\nInput cancelled.\n")
            return None

def confirm_action(prompt="Are you sure?"):
    while True:
        response = input(f"{prompt} (yes/no): ").strip().lower()
        
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please answer 'yes' or 'no'.\n")

def display_error(message):
    print(f"\nERROR: {message}\n")

def display_success(message):
    print(f"\nSUCCESS: {message}\n")

def display_warning(message):
    print(f"\nWARNING: {message}\n")
