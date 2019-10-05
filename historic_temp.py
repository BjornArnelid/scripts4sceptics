import os
import pandas
import matplotlib.pyplot as plt
import urllib.request
import zipfile

TEMP_FOLDER = "data/temperature/"

SMHI_STHLM_ZIP = "stockholm_daily_mean_temperature_1756_2018.zip"
SMHI_STHLM_TXT = "stockholm_daily_mean_temperature_1756_2018.txt"
SMHI_STOCKHOLM_URL = "https://www.smhi.se/polopoly_fs/1.2864!/" + SMHI_STHLM_ZIP


def collect_data():
    if not os.path.exists( TEMP_FOLDER + SMHI_STHLM_ZIP):
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
            zf.extractall(TEMP_FOLDER)
        print("Done!")


def load():
    columns = ((0,4), (5, 7), (8,10), (11,18), (19,26), (27,34), (35,37))
    df = pandas.read_fwf(TEMP_FOLDER + SMHI_STHLM_TXT, columns, header=None, skipinitialspace=True)
    df.columns =['Year', 'Month', 'Day', 'Original temp', 'Homogenized temp', 'Adjusted temp', 'Source']
    df['Date'] = pandas.to_datetime(df[['Year', 'Month', 'Day']])
    df.plot(x='Date', y='Adjusted temp', kind='line')
    plt.show()
