import sys
import re
import struct
import datetime

def convert_to_datetime(binary_value):
    binary_time = struct.unpack("<Q", bytes.fromhex(binary_value))[0]
    converted = datetime.datetime.fromtimestamp((binary_time - 116444736000000000) / 10000000)
    return converted

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ConvertTime.py [binary]")
        sys.exit(1)

    binary_value = sys.argv[1]
    if not re.match(r'^[0-9a-fA-F]{16}$', binary_value):
        print("Error: PLEASE type 16-character hexadecimal string.")
        sys.exit(1)

    try:
        converted = convert_to_datetime(binary_value)
        now = datetime.datetime.now()
        time_diff = converted - now
        if time_diff.total_seconds() > 0:
            print("ERROR: Timestamp is Illogical time")
            print("Time:", converted)
        else:
            print("SUCCESS!!")
            print("Time:", converted)
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)

