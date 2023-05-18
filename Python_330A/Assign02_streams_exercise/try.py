"""
USAGE: `python try.py 123456`
"""

import io
import sys

from stream_exercise import StreamProcessor

# Had to make this a string for it to work
value = str(sys.argv[1])

my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()
print("Processed {} and got {}".format(value, result))
