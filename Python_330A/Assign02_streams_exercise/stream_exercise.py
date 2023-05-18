

class StreamProcessor(object):
    """
    Write a stream processor class that does the following:
        1. You initialize an instance with a stream of digits
          (AKA: file-like object, instance of StringIO), and
          store it as an instance variable.

          eg: f = io.StringIO("234761640930110349378289194")
              my_stream_processor = MyStreamProcessor(f)

        2. You call a `process` method of my_stream_processor.

          This method:

            1. Reads two digits at a time from the beginning of the stream
            2. Converts the two digits into a number, and adds that number
               to a running total.
            3. Once this number reaches 200 or more, the method returns how
               many two digit numbers it had to add together to reach its
               total.
            4. If `process` reaches the end of the stream BEFORE it has
               reached a sum of 200, then it will return how many two
               digit numbers it found before reaching the end of the
               stream.
            5. The method will add AT MOST 10 of these two digit numbers
               together: if it reaches the 10th two digit number and the
               sum has not yet reached 200, then the method will stop and
               return 10.

    For example, given a stream yielding "234761640930110349378289194", the
    process method will:

            1. Read two digits at a time from the stream: "23", "47", "61", etc.
            2. Convert these digits into a number: 23, 47, 61, etc., and  make a
               running total of these numbers: 23 + 47 equals 70. 70 + 61 equals
               131, etc.
            3. For this particular stream, the running total will exceed 200 after
               5 such additions: the `process` method should return 5.

    You can see the `tests.py` file for more examples of expected outcomes.
    """

    def __init__(self, stream):
        self._stream = stream

    def process(self):
      """
      TODO: Implement the `process` method, as described above.

      :return: int
      """

      count = 0  # How many two-digit numbers the `process` method has added
                  # together.
      total = 0  # The running total of sums.

      # TODO: WRITE CODE HERE:
      # Gets the value
      stream_string = self._stream.getvalue()

      # Checks if its odd, if so make it even.
      if len(stream_string) % 2 == 1:
         stream_string = stream_string.rstrip(stream_string[-1])

      # Splits string into chunks
      chunks = [stream_string[i:i+2] for i in range(0, len(stream_string), 2)]

      # Loops through and does the total/counts.
      for num in chunks:

         # Base Case
         if len(chunks) <= 1:
            return 0

         total += int(num)
         count += 1
         if total > 200:
            return count
         if count == 10:
            return count

      return count
