import io
from typing import Callable


# Gives a StringIO that you can peek on.
#
# StringIO cannot be peek-ed normally, and it is very annoying to manage
# a BufferedReader over BytesIO, making str to bytes to str conversions
# when all you want are strings..
class PeekableStringIO(io.StringIO):
    def peek(self, size: int = -1) -> str:
        stream_pos = self.tell()  # save position
        peek_buf = self.read(size)
        self.seek(stream_pos)  # restore position
        return peek_buf

    def read_while(self, func: Callable[[str], bool]) -> str:
        buf = ""
        while func(self.peek(1)):
            buf += self.read(1)
        return buf
