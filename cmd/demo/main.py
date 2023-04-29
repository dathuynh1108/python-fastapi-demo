
import sys
from pathlib import Path
if __name__ == '__main__' and __package__ is None:
    # Import root directory
    file = Path(__file__).resolve()
    sys.path.append(str(file.parents[2].absolute())) 

from internal.demo import handler
h = handler.handler()
h.start()

   