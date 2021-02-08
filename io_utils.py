from io import StringIO
from typing import Callable, Iterator, Optional


# Gives a StringIO that you can peek on.
#
# StringIO cannot be peek-ed normally, and it is very annoying to manage
# a BufferedReader over BytesIO, making str to bytes to str conversions
# when all you want are strings..
class PeekableStringIO(StringIO):
    def peek(self, size: int = -1) -> str:
        stream_pos = self.tell()  # save position
        peek_buf = self.read(size)
        self.seek(stream_pos)  # restore position
        return peek_buf

    def skip_while(self, func: Callable[[str], bool]) -> int:
        nb_skipped_chars = 0
        for _ in self._do_while(func):
            nb_skipped_chars += 1
        return nb_skipped_chars

    def read_while(self, func: Callable[[str], bool]) -> str:
        buf = StringIO()
        for char in self._do_while(func):
            buf.write(char)
        return buf.getvalue()

    def _do_while(self, func: Callable[[str], bool]) -> Iterator[str]:
        def check_need_more(read_char: Optional[str]) -> bool:
            return func(read_char) if read_char else False

        while check_need_more(self.peek(1)):
            yield self.read(1)
