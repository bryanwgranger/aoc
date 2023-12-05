import requests
import browser_cookie3
import datetime
import chevron
import os

def get_data(args):

    today = datetime.datetime.now().day
    if not args.day:
        day = today
    else:
        day = int(args.day)
    if day < 0 or day > 25 or day > int(today):
        exit("day is not valid")

    cur_year = datetime.datetime.now().year
    if not args.year:
        year = cur_year
    else:
        year = int(args.year)
    if year < 2016 or year > int(cur_year):
        exit("year is not valid")

    aoc_dir = f"./{year}"
    if not os.path.exists(aoc_dir):
        os.mkdir(aoc_dir)

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cj = browser_cookie3.firefox()

    r = requests.get(url=url,
                     cookies=cj)

    with open(os.path.join(aoc_dir, f"dec{day}_{year}.input"), "w") as infile:
        infile.write(r.text)

    with open("pytemplate.mustache", "r") as chevfile:
        chev_text = chevron.render(chevfile, data={"day": day,
                                       "year": year})
    file_path = os.path.join(aoc_dir, f"dec{day}_{year}.py")
    if not os.path.exists(file_path):
        with open(os.path.join(aoc_dir, f"dec{day}_{year}.py"), "w") as pyfile:
            pyfile.write(chev_text)
    else:
        print("warning: python file for this day has been detected. The existing file has not been overwritten.")

    print(f"Input for Dec {day}, {year} has been downloaded!")

if __name__ == "__main__":

    # setting the hyper parameters
    import argparse

    parser = argparse.ArgumentParser(description='Download AOC input data',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d', "--day", default=None, required=False)
    parser.add_argument('-y', "--year", default=None, required=False)

    args = parser.parse_args()

    get_data(args)