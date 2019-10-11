# Main Launcher script


import argparse
import historic_temp


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scripts 4 Sceptics. Verify things for yourself!')
    parser.add_argument('script', metavar='SCRIPT', type=str, help='script to verify',
                        choices=['historic_temp'])
    parser.add_argument('--verify', metavar='DATAPOINT', type=str, nargs='?',
                        help='produce a datapoint for verification')

    args = parser.parse_args()
    if args.script == 'historic_temp':
        temp = historic_temp.HistoricTemperatures()
        temp.collect_data()
        temp.load()
        if args.verify:
            temp.verify(args.verify)
        else:
            temp.plot()
            temp.verify()

