import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, help="the base")
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()

zawartosc_pliku = json.load(args.f)


dupa(zawartosc_pliku['asd'])

# y = 3
# answer = args.x**y
# if args.verbosity >= 2:
#     print(f"Running '{__file__}'")
# if args.verbosity >= 1:
#     print(f"{args.x}^{args.y} == ", end="")
# print(answer)