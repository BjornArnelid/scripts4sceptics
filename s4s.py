# Main Launcher script

import historic_temp


if __name__ == "__main__":
    temp = historic_temp.HistoricTemperatures()
    temp.collect_data()
    temp.load()
    temp.plot()
    temp.verify()

