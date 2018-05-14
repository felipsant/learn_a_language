from app.app import run
import sys

if len(sys.argv) > 1:
    run(sys.argv[1])
else:
    run()