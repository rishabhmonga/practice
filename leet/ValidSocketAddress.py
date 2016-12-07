"""
This is the file with your answer, do not rename or move it.
Write your code in it, and save it before submitting your answer.
"""

def is_valid_socket(address):
    """Determine if the provided string is a valid socket address.
    This function declaration must be kept unmodified.

    Args:
        address: A string with a socket address, eg,
            '127.12.23.43:5000', to be checked for validity.
    Returns:
        A boolean indicating whether the provided string is a valid
        socket address.
    """
    # write your implementation here

    # validating input to be a string and not empty
    if address is None or not isinstance(address, basestring) or address == "":
        return False
    # splitting the address into host and port
    s = address.split(':')
    # checking if host and port both exist
    if len(s) != 2:
        return False
    host = s[0].split('.')
    port = s[1]

    # validations for port address
    if not port.isdigit():
        return False
    i = int(port)
    if i < 0 or i > 65535:
        return False

    # validations for host address
    # checking all parts of the host address are present and are integers
    if len(host) != 4:
        return False
    for addr_part in host:
        if not addr_part.isdigit():
            return False
        i = int(addr_part)
        if i < 0 or i > 255:
            return False
    return True


# This tests your code with the examples given in the question,
# and is provided only for your convenience.
if __name__ == '__main__':
    for address in ["127.12.23.43:5000",
                   "127.A:-12"]:
        print(is_valid_socket(address))


