import json
import pandas as pd

def get_artist_and_song(title):
    """ Separate ARTIST and TITLE from "Watched ARTIST - TITLE" strings """
    artist, song_name = title[8:], title[:8]
    return (artist, song_name)

#===================================================================================

def check_validity(title):
    if title[:7] != "Watched":
        return False

#===================================================================================

def main(args):

    # read json into pandas dataframe
    with open(args.input) as f:
        data = pd.read_json(args.input)
    #print(data)

    # only keep data entries which were from YouTube Music, not YouTube
    selected_data = data.loc[data["header"] == "YouTube Music"]

    for entry in selected_data["title"]:
        if not check_validity(entry):
            continue
        artist, song = get_artist_and_song(entry)
        #print(artist)
        #print(song)


#===================================================================================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", metavar = "INPUT", type = str, default = "data/history/watch-history.json", help = "JSON file which contains google takeout data")

    args = parser.parse_args()
    main(args)
