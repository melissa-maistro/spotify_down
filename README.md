# SPOTIFY DOWN WEB BOT
Automated web bot that allows you to download Spotify playlists from https://spotifydown.com/it.

## Requirements
- Python (I used version 3.12.2)
- selenium
- Adblock extension for Google Chrome

## How to run it?
1. Download the zip file from GitHub or clone the repository with the command: 
```console
git clone https://github.com/melissa-maistro/spotify_down.git
```

2. If you do not have a python interpreter, install it. Consult the official [python website](https://www.python.org/downloads/).

3. Install the selenium package by running the following command on your terminal:
```console
pip install selenium
```

4. Install the [Adblock extension](https://chromewebstore.google.com/detail/adblock-plus-ad-blocker-g/cfhdojbkjhnklbpkdaibdccddilifddb?hl=it) for Google Chrome.
   Then change this part of the code with the extension's path on your computer:
  ```console
  adblock_extension = "/Users/melissamaistro/Desktop/3.25_0"
  ```

5. Open the terminal and go to the directory where you downloaded the script. Run the script with the following command:
```console
python3 spotifydown.py
```

6. It is going to ask you the playlist's link (Share -> Copy link), from which song you would like to start the download (number) and where to download the playlist's songs
   (pass the full path, for example /Users/melissamaistro/Desktop/music/house).

7. Enjoy your music!

## Notes
- Sometimes it crashes because of pop-ups, unfortunately I have not found a solution to avoid them. My suggestion is to run the script again, it usually works!

