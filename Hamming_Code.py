def read_bits():
    data = input()
    data_list = list(data) # Make a list from the string input.
    return data_list


def set_parity_type():
    print("1: Even")
    print("2: Odd")
    option = int(input())
    if option == 1:
        return "even"
    elif option == 2:
        return "odd"
    else:
        print("Wrong option")
        exit(1)


def power_of_two(num): 
    rem = 0
    while num != 1 and rem == 0:
        rem = num % 2       # To check if the number is power of two we devided with two.
        num /= 2
    if num == 1 and rem == 0:   # If it lands at one it is.
        return 1                # If it does not produce devision remaining then it is.
    else:
        return 0


def generate_parity_bits(data_array):
    message = ["P1", "P2"]  # Initialize message list.
    index = 3   # Keep track of which P (parity) is next. 
    flag = 0    # We use the flag to not skip any number when we place the P.
    for array_index in range(len(data_array)):
        if power_of_two(array_index + 3) and flag == 0:
            message.append("P" + str(index))
            index += 1
            message.append(data_array[array_index])
            array_index -= 1    # Go back one not to skip data bits.
            flag = 1    # We make flag 1 to skip double checking for power of two an just add data bit.
        else:
            message.append(data_array[array_index])     # Add data bit.
            flag = 0    # Reset flag.
    return message


def calculate_parity_bits(message, parity_type):
    new_message = []
    for index in range(len(message)):
        if message[index][0] == "P":
            start = 0
            step = int(message[index][1])
            flag = 0
            for i in range(start, len(message), step):
                if message[i][0] != "P" and flag == 0:
                    temp = int(message[i])      # Initialize first value for XOR.
                    flag = 1                    # We must do this because in XOR initializing as 0 can affect the result.
                elif message[i][0] != "P" and flag == 1:
                    temp ^= int(message[i])     # Calculate XOR 

            if parity_type == "even":
                new_message.append(int(temp))   # Add result
            elif parity_type == "odd":
                new_message.append(int(not temp)) # Add the result after NOT gate.
        else:
            new_message.append(int(message[index]))

    return new_message


def main():
    # Read binary bits of message.
    data_array = read_bits() 
    # Add the parity bits to the message.
    message = generate_parity_bits(data_array) 
    # Print the message with the parity bits.
    print(message) 
    # Set even or odd parity.
    parity_type = set_parity_type()  
    # Calculate parity bits and add the to according positions on the message.
    send_message = calculate_parity_bits(message, parity_type) 
    # Print the message to send.
    print(send_message)

""" Start of the program. """
if __name__ == "__main__":
    main()
