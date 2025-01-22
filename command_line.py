import sys

def main():

    args = sys.argv[1:]

    # if len(args) != 4:
    #     print(f"Usage: {sys.argv[0]} --disaster <kind of disaster(s)> --county <us_county>")
    
    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} --disaster <kind of disaster(s)> --county <us_county>")
    
    
        

    # counter = 0
    # for arg in args:
    #     counter = counter + 1
    #     print(arg)

    # print(counter)

    #print(args)

    return 0

if __name__ == "__main__":
    main()