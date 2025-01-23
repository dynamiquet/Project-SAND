import sys

from ProductionCode.helper import *

def main():

    args = sys.argv[1:]
    
    # Checks if Command Line input is valid
    if ((args[0] != "--disaster" and args[0] != "--disasters") or args[2] != "--county" or len(args) != 4):
        print(f"Usage: {sys.argv[0]} --disaster or --disasters <kind of disaster(s)> --county <us_county>")
        exit(1)

    disaster = args[1]
    county = args[3]

    # Testing purposes
    if (is_us_county(county) == False):
        print("Not a valid county")
    else:
        print("Valid county")

    if (is_disaster(disaster) == True):
        print("Valid disaster")
    else:
        print("Not a valid disaster")
    # print(counter)

    #print(args)

    return 0

if __name__ == "__main__":
    main()