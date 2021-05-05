# Attempt at porting ERC Calculator to Python
# This showed me how bad I was at bitwise operations.
# seems to be working though

def get_reverse(x) -> int:
    reverse_second_part = 0

    for i in range(0, 32):
        temp = x >> (31 - i)
        temp &= 1
        temp = temp << i
        reverse_second_part |= temp

    return reverse_second_part


def get_full_binary(string: str, count: int) -> str:
    str2 = string
    while len(string) < count:
        str2 = "0" + string
    return str2


def start_decode(input_erc: str) -> str:
    if len(input_erc) != 16:
        return "Invalid number of characters."
    elif len(input_erc) == 16:
        # Splits the string into 8 character strings.
        first_part = input_erc[0:8]
        second_part = input_erc[8:16]

        # Treating the strings returned as HEX, converts them to an int.
        fp_int = int(first_part, 16)
        sp_int = int(second_part, 16)

        reverse_second_part = get_reverse(x=sp_int)

        xor = fp_int ^ reverse_second_part
        ret = (xor - 0xE010A11)

        # Formats the return as hex
        xd = hex(ret)

        last = get_full_binary(string=xd, count=8)
        return last
    else:
        return "error"


# test_erc = '66EECE00F2724BA5'
test_erc = input("Please enter your ERC: ")
# exp = 'B53B763E'
# print(f"Test ERC = {test_erc} expected answer is {exp}")

hex_return = str(start_decode(test_erc))
cleaned_return = hex_return.lstrip("0x").upper()

print(f"returned answer is: {cleaned_return}.")

