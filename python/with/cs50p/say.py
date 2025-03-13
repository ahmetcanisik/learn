import cowsay
import sys

if len(sys.argv) < 2:
    sys.exit("to few arguments")

cowsay.trex(f"Hello {sys.argv[1]}")