import sys

from ProductionCode.helper import *


def main():
    '''
    Accepts two Command Line inputs:
    Usage One: --disaster <name of disaster(s)> --county <name of US county, State abbreviation>
        Returns the hazard rating for the type of disaster(s) in the given county as recorded by FEMA's dataset

    Usage Two: --top5 <name of US county, State abbreviation>
        Returns the top five most hazardous disaster's in a given county
    '''

    args = sys.argv[1:]
    
    # Checks if Command Line input is valid
    if len(args) == 2:  # Check if it's the --top5 usage
        if args[0] != "--top5":
            print(f"Usage: {sys.argv[0]} --disaster <kind of disaster(s)> --county <us_county, state abbr.>")
            print(f"Alternative Usage: {sys.argv[0]} --top5 <us_county, state abbr.>")
            exit(1)
    elif len(args) == 4:  # Check if it's the --disaster usage
        if args[0] not in ["--disaster", "--disasters", "--top5"] or args[2] != "--county":
            print(f"Usage: {sys.argv[0]} --disaster <kind of disaster(s)> --county <us_county, state abbr.>")
            print(f"Alternative Usage: {sys.argv[0]} --top5 <us_county, state abbr.>")
            exit(1)
    else:
        # Invalid number of arguments
        print(f"Usage: {sys.argv[0]} --disaster <kind of disaster(s)> --county <us_county, state abbr.>")
        print(f"Alternative Usage: {sys.argv[0]} --top5 <us_county, state abbr.>")
        exit(1)
        

    # Running disaster(s) flag
    if (args[0] == "--disaster"):
        disaster = args[1]
        county = args[3]

        if (is_disaster(disaster) == False):
            print("At least one disaster is invalid. Please check spelling and try again")
            exit(1)

        if (is_us_county(county) == False):
            print("Not a valid county. Please check spelling and try again")
            exit(1)

        print(get_disaster_risk(disaster, county))

        
    
    # Running top5 flag
    if (args[0] == '--top5'):
        county = args[1]

        # Check validity of county
        if (is_us_county(county) == False):
            print("Not a valid county. Please check spelling and try again")
        else:
            print(get_top_five(county))
        
        return 0

if __name__ == "__main__":
    main()