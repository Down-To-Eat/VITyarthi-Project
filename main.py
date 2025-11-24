import sys
from converter import convert_length, convert_temperature, convert_weight, convert_time, get_available_units
from history import ConversionHistory
from validator import get_valid_number, get_valid_choice, get_menu_choice, confirm_action, display_error, display_success
from logger import ApplicationLogger

def show_banner():
    print("\n======================================================================")
    print("UNIT CONVERTER PRO")
    print("======================================================================")
    print("Precision unit conversions with history tracking")
    print("Supports: Length, Temperature, Weight, Time")
    print("======================================================================")

def show_menu():
    print("\n----------------------------------------------------------------------")
    print("MAIN MENU")
    print("----------------------------------------------------------------------")
    print("1. Length Conversion (meter, km, mile, foot, inch, etc.)")
    print("2. Temperature Conversion (Celsius, Fahrenheit, Kelvin)")
    print("3. Weight Conversion (kg, gram, pound, ounce, etc.)")
    print("4. Time Conversion (second, minute, hour, day, etc.)")
    print("5. View Conversion History")
    print("6. View Usage Statistics")
    print("7. Export History to File")
    print("8. Clear History")
    print("9. View Application Logs")
    print("0. Exit")
    print("----------------------------------------------------------------------")

def do_conversion(cat, conv_func, hist, log):
    print("\n----------------------------------------------------------------------")
    print(cat.upper() + " CONVERSION")
    print("----------------------------------------------------------------------")
    units = get_available_units(cat)
    print("Available units: " + ', '.join(units))
    print()
    val = get_valid_number("Enter value to convert: ", allow_negative=True)
    if val == None:
        return
    from_unit = get_valid_choice("From unit: ", units, case_sensitive=False)
    if from_unit == None:
        return
    to_unit = get_valid_choice("To unit: ", units, case_sensitive=False)
    if to_unit == None:
        return
    try:
        ans = conv_func(val, from_unit, to_unit)
        print("\n======================================================================")
        print("CONVERSION RESULT")
        print("======================================================================")
        print(str(val) + " " + from_unit + " = " + str(ans) + " " + to_unit)
        print("======================================================================\n")
        hist.add_conversion(cat, val, from_unit, to_unit, ans)
        log.log_conversion(cat, val, from_unit, to_unit, ans)
        
    except ValueError as e:
        display_error(str(e))
        log.log_error_conversion(cat, str(e))
    except Exception as e:
        display_error("Unexpected error: " + str(e))
        log.log_error_conversion(cat, "Unexpected: " + str(e))

def main():
    hist = ConversionHistory(max_entries=50)
    log = ApplicationLogger(console_output=False)
    show_banner()
    log.log_user_action("Application started")
    print("\nWelcome! Let's convert some units.")
    while True:
        show_menu()
        choice = get_menu_choice(min_choice=0, max_choice=9)
        if choice == None:
            continue
        if choice == 1:
            log.log_user_action("Selected Length Conversion")
            do_conversion('length', convert_length, hist, log)
        
        elif choice == 2:
            log.log_user_action("Selected Temperature Conversion")
            do_conversion('temperature', convert_temperature, hist, log)
        
        elif choice == 3:
            log.log_user_action("Selected Weight Conversion")
            do_conversion('weight', convert_weight, hist, log)
        
        elif choice == 4:
            log.log_user_action("Selected Time Conversion")
            do_conversion('time', convert_time, hist, log)
        
        elif choice == 5:
            log.log_user_action("Viewed conversion history")
            hist.display_history(limit=15)
        
        elif choice == 6:
            log.log_user_action("Viewed usage statistics")
            hist.display_statistics()
        
        elif choice == 7:
            log.log_user_action("Exported history to file")
            hist.export_to_text('conversion_history_export.txt')
        
        elif choice == 8:
            if confirm_action("Clear all conversion history?"):
                hist.clear_history()
                log.log_user_action("Cleared conversion history")
            else:
                print("\nHistory clear cancelled.\n")
        
        elif choice == 9:
            log.log_user_action("Viewed application logs")
            print(log.get_log_summary())
        
        elif choice == 0:
            log.log_user_action("Exiting application")
            print("\n======================================================================")
            print("Thank you for using Unit Converter Pro!")
            print("======================================================================")
            stats = hist.get_statistics()
            if stats:
                print("\nSession Summary:")
                print("Total conversions performed: " + str(stats['total_conversions']))
                print("Most used category: " + stats['most_used'])
            print("\nYour conversion history has been saved.")
            print("Come back anytime for more conversions!\n")
            print("======================================================================\n")
            log.close_session()
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.\n")
        sys.exit(0)
    except Exception as e:
        print("\nCRITICAL ERROR: " + str(e) + "\n")
        sys.exit(1)
