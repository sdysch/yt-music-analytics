# YouTube music analytics
Because YouTube Music does not appear to have an API....

## Data
* Taken from [google takeouts](https://takeout.google.com/)
* Export playlists and history as JSON file
	* This exports both YouTube and YouTube Music history, but a header can separate them in the json file

## notes
* artist does not always appear to be saved? Sometimes it is under "subtitles", but not always?
```
  "header": "YouTube Music",
  "title": "Watched Red Hot Chili Peppers - By The Way [Official Music Video]",
  "subtitles": [{
    "name": "Red Hot Chili Peppers",
  }],
```
