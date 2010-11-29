import sys

import mpq
from sc2.parsers import replays

def main():
    if len(sys.argv) != 2:
        print "Usage: %s FILENAME" % (sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1]
    print "Opening: %s" % filename
    parser = replays.ReplayParser(filename)
    print parser.info


if __name__ == "__main__":
    main()
