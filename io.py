import sys

def printf(args: str, *forms):
    args_list = list(args)
    form_idx = 0  # Keep track of which form argument to use
    
    i = 0
    while i < len(args_list):
        if args_list[i] == "%" and i + 1 < len(args_list):
            if args_list[i + 1] == "s":
                try:
                    # Replace %s with the corresponding string argument
                    args_list[i] = str(forms[form_idx])
                    form_idx += 1
                    args_list[i + 1] = ""
                except IndexError:
                    sys.stdout.write("Not enough arguments provided for %s\n")
                    return
            elif args_list[i + 1] == "d":
                try:
                    # Replace %d with the corresponding integer argument
                    args_list[i] = str(int(forms[form_idx]))
                    form_idx += 1
                    args_list[i + 1] = ""
                except (ValueError, IndexError):
                    sys.stdout.write("Invalid or missing argument for %d\n")
                    return
        i += 1

    args = ''.join(args_list)
    sys.stdout.write(args + '\n')

# Test cases
printf("hel%dlo", 4)
printf("Name: %s, Age: %d", "Alice", 30)
