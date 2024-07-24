from enum import Enum, EnumMeta

class EnumDirectValueMeta(EnumMeta):
    """
    Metaclass for Enum that allows direct access to an Enum's value as a class attribute.
    """
    def __getattribute__(cls, name):
        """
        Override attribute access to allow direct access to Enum's value.
        
        Args:
        cls (EnumDirectValueMeta): The Enum class.
        name (str): The name of the attribute being accessed.
        
        Returns:
        Any: The value of the attribute if it's an Enum member, otherwise returns the attribute as is.
        """
        value = super().__getattribute__(name)
        if isinstance(value, cls):
            value = value.value
        return value

import pickle
import os

def save_obj(filename, obj, overwrite=True):
    """
    Save an object to a file using pickle.
    
    Args:
    filename (str): Name of the file to save the object to.
    obj (Any): The object to save.
    overwrite (bool): If False, the function will append a number to the filename if a file with the same name exists.
    """
    if not overwrite:
        file_number = 1
        
        # Split the file name and extension
        file_name, file_extension = os.path.splitext(filename)
        
        # Check if the file already exists
        while os.path.exists(filename):
            # Append the auto-increment number before the extension
            filename = f"{file_name}_{file_number}{file_extension}"
            file_number += 1
    
    with open(filename, "wb") as file:
        pickle.dump(obj, file)
    
def load_obj(filename):
    """
    Load an object from a file using pickle.
    
    Args:
    filename (str): Name of the file to load the object from.
    
    Returns:
    Any: The loaded object.
    """
    with open(filename, "rb") as file:
        obj = pickle.load(file)
    return obj

class PrettyPrint:
    """
    Helper class for terminal output styling.
    """
    # Text colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    GREY = '\033[90m'
    BLACK = '\033[90m'

    # Text styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

    @staticmethod
    def apply_styles(*styles):
        """Combines multiple styles into a single string."""
        return ''.join(styles)

    @staticmethod
    def pprint(msg: str, color: str = CYAN, *styles: str):
        """
        Pretty prints the message with specified color and styles.

        Args:
            msg (str): Message to print.
            color (str, optional): Color for the text. Defaults to CYAN.
            styles (str): Additional text styles (e.g., PrettyPrint.BOLD, PrettyPrint.UNDERLINE).
        """
        styled_msg = PrettyPrint.apply_styles(color, *styles)
        print(styled_msg + msg + PrettyPrint.RESET)

########################
##  BINARY OPERATIONS ##
########################
class DataType(Enum, metaclass=EnumDirectValueMeta):
    """
    Enumeration for data types, allowing direct access to the Enum values.
    """
    UBNR =  0
    BNR  =  1
    DIS  =  2

def resolution(MSB, LSB, max, type: DataType = DataType.BNR):
    """
    Calculate the resolution of a binary number.
    
    Args:
    MSB (int): Most significant bit position.
    LSB (int): Least significant bit position.
    max (int): Maximum value represented by the number.
    type (DataType): Data type, either BNR (binary) or UBNR (unsigned binary).
    
    Returns:
    float: The resolution.
    
    Raises:
    TypeError: If the type is not recognized.
    """
    n = MSB - LSB + 1
    if type == DataType.BNR:
        r = max / (2 ** (n - 1))
    elif type == DataType.UBNR:
        r = max / (2 ** n)
    else:
        raise TypeError("Type not recognized")
    return r

def bin2int(binary: str):
    """
    Convert a binary string to an integer.
    
    Args:
    binary (str): Binary string to convert.
    
    Returns:
    int: The integer value.
    """
    num = 0
    for i, bit in enumerate(binary[::-1]):
        num += int(bit) * 2 ** i
    return num

def bin2int(bin: str, complement=False, verbose=False):
    """
    Convert a binary string to an integer, with optional two's complement conversion.
    
    Args:
    bin (str): Binary string to convert.
    complement (bool): If True, treat the binary string as a two's complement number.
    verbose (bool): If True, print detailed conversion steps.
    
    Returns:
    int: The integer value.
    """
    n = len(bin)
    res = 0
    for i in range(n - int(complement)):
        bit = int(bin[n - 1 - i])
        val = int(bit) * 2 ** i
        if verbose:
            print(f"{bit} * 2^{i} = {val}")
        res += val
    
    if complement:
        bit = -int(bin[0])
        val = bit * 2 ** (n - 1)
        if verbose:
            print(f"{bit} * 2^{n - 1} = {val}")
        res += val
    
    return res

def int2bin(num):
    """
    Convert an integer to a binary string.
    
    Args:
    num (int): Integer to convert.
    
    Returns:
    str: The binary string representation of the integer.
    """
    return bin(num)[2:]

def bit_combos(n, verbose=False):
    """
    Generate and optionally print all possible combinations of n bits.
    
    Parameters:
    n (int): Number of bits.
    verbose (bool): If True, print all combinations. Default is False.
    
    Returns:
    str: A string containing all possible combinations of n bits, each on a new line.
    """
    # Calculate the total number of combinations (2^n)
    num_combinations = 2 ** n
    
    # Initialize an empty string to store combinations
    combinations = str()
    
    # Iterate over all combinations
    for i in range(num_combinations):
        # Convert the index to a binary string of length n
        binary_str = format(i, f'0{n}b')
        # Append the binary string to the combinations string with a newline
        combinations += binary_str + "\n"
    
    # If verbose is True, print the combinations
    if verbose:
        print(combinations)
    
    # Return the combinations string
    return combinations

