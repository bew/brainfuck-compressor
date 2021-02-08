from io import StringIO

from io_utils import PeekableStringIO


BF_NORMAL_ALLOWED_CHARS = [char for char in "+-><[],."]
BF_COMPRESSED_ALLOWED_CHARS = [char for char in "idrl[],.0123456789"]

BF_NORMAL_TO_COMPRESSED = {
    "+": "i",
    "-": "d",
    ">": "r",
    "<": "l",
}
BF_COMPRESSED_TO_NORMAL = dict(zip(
    BF_NORMAL_TO_COMPRESSED.values(),
    BF_NORMAL_TO_COMPRESSED.keys(),
))


def convert_to_compressed_form(bf_normal: str) -> str:
    io = PeekableStringIO(bf_normal)
    bf_compressed = StringIO()
    while normal_operation := io.peek(1):
        duplicate_count = io.skip_while(
            lambda char: char == normal_operation
        )
        try:
            compressed_operation = BF_NORMAL_TO_COMPRESSED[normal_operation]
            if duplicate_count > 1:
                bf_compressed.write(compressed_operation + str(duplicate_count))
            else:
                bf_compressed.write(compressed_operation)
        except KeyError:
            bf_compressed.write(normal_operation * duplicate_count)
    return bf_compressed.getvalue()


def convert_to_normal_form(bf_compressed: str) -> str:
    io = PeekableStringIO(bf_compressed)
    bf_normal = StringIO()
    while compressed_operation := io.read(1):
        if compressed_operation in BF_COMPRESSED_TO_NORMAL:
            normal_operation = BF_COMPRESSED_TO_NORMAL[compressed_operation]
            count = int(io.read_while(lambda c: c.isdigit()) or "1")
        else:
            normal_operation = compressed_operation
            count = 1
        bf_normal.write(normal_operation * count)
    return bf_normal.getvalue()
