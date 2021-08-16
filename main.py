import json
import pandas as pd

def main(args):

    with open(args.input) as f:
        data = json.load(f)
    print(data)

#===================================================================================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", metavar = "INPUT", type = str, default = "data/history/watch-history.json", help = "JSON file which contains google takeout data")

    args = parser.parse_args()
    main(args)
