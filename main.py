import io
import sys
from typing import Callable

BF_TO_BF_SHORT = {
    "+": "i",
    "-": "d",
    ">": "r",
    "<": "l",
}
BF_SHORT_TO_BF = dict(zip(
    BF_TO_BF_SHORT.values(),
    BF_TO_BF_SHORT.keys(),
))


def io_peek_next_char(io: io.BufferedReader) -> str:
    buf = io.peek(1)
    if not buf:
        return ""
    return chr(buf[0])


def io_read_str_while(
    io: io.BufferedReader,
    func: Callable[[str], bool]
) -> str:
    buf = ""
    while func(io_peek_next_char(io)):
        buf += io.read(1).decode("utf-8")
    return buf


def convert_bf_normal_to_short(bf_normal: str) -> str:
    bf_normal_bytes = bytes(bf_normal, encoding="utf-8")
    io_stream = io.BufferedReader(io.BytesIO(bf_normal_bytes))  # type: ignore
    bf_short = ""
    while io_peek_next_char(io_stream):
        operation = io_peek_next_char(io_stream)
        group_of_same_operation = io_read_str_while(
            io_stream,
            lambda char: char == operation
        )
        duplicate_count = len(group_of_same_operation)
        try:
            bf_short += BF_TO_BF_SHORT[operation] + str(duplicate_count)
        except KeyError:
            bf_short += operation * duplicate_count
    return bf_short


bf_code = input().strip()
if not bf_code:
    print("Input is empty!", file=sys.stderr)
    sys.exit(1)

bf_short_code = convert_bf_normal_to_short(bf_code)

print(bf_short_code)
