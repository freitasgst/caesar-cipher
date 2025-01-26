

def convert_message_to_dec(plain_text) -> list[int]:
    message_in_dec = [ord(letra) for letra in plain_text]
    return message_in_dec


def rotate_message(message_in_dec, n) -> list[int]:
    rotated_message = [num + n for num in message_in_dec]
    return rotated_message


def convert_message_to_str(rotated_message) -> str:
    message_in_str = [chr(num) for num in rotated_message]
    message_in_str = "".join(message_in_str)
    return message_in_str


def main():  # pragma: no cover
    rotation_n = int(input("Rotation (key): "))
    plain_text = input("Type message: ")

    plain_message_in_dec = convert_message_to_dec(plain_text)
    rotated_message_in_dec = rotate_message(plain_message_in_dec, rotation_n)
    encripted_message = convert_message_to_str(rotated_message_in_dec)

    print("The message is: ", encripted_message)


if __name__ == "__main__":  # pragma: no cover
    main()
