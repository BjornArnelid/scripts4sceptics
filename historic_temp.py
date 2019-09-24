import urllib.request
import zipfile
import os


TEMP_FOLDER = "data/temperature/"

SMHI_STHLM_ZIP = "stockholm_daily_mean_temperature_1756_2018.zip"
SMHI_STHLM_TXT = "stockholm_daily_mean_temperature_1756_2018.txt"
SMHI_STOCKHOLM_URL = "https://www.smhi.se/polopoly_fs/1.2864!/" + SMHI_STHLM_ZIP




def run():
    if not os.path.exists( TEMP_FOLDER + '/temperature_stockholm.zip'):
        print("Fetching temperature data from %s..." % SMHI_STOCKHOLM_URL)
        weather_data = urllib.request.urlopen(SMHI_STOCKHOLM_URL)
        weather_download = weather_data.read()
        with open(TEMP_FOLDER + SMHI_STHLM_ZIP, 'wb') as f:
            f.write(weather_download)
        print("Done!")
    else:
        print("Using locally stored data")
    if not os.path.exists(TEMP_FOLDER + SMHI_STHLM_TXT):
        print("Extracting temperature data from " + SMHI_STHLM_ZIP)
        with zipfile.ZipFile(TEMP_FOLDER + SMHI_STHLM_ZIP, 'r') as zf:
            with zf.open(TEMP_FOLDER + SMHI_STHLM_TXT) as tf:
                pass
    # unpack if needed
