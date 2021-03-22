"""Console script for investopedia_simulator_api."""
import argparse
import sys


def main():
    """Console script for investopedia_simulator_api."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "investopedia_simulator_api.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
