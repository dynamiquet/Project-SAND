import sys

from ProductionCode.helper import *

def main():

    args = sys.argv[1:]
    
    # Checks if Command Line input is valid
    if (args[0] != "--disaster" or args[2] != "--county" or len(args) != 4):
        print(f"Usage: {sys.argv[0]} --disaster <kind of disaster(s)> --county <us_county>")
        exit(1)

    disaster = args[1]
    county = args[3]

    if (valid_county(county) == False):
        print("Not a valid county")
    # print(counter)

    #print(args)

    return 0

if __name__ == "__main__":
    main()