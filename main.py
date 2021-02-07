import sys
from io_utils import PeekableStringIO


BF_NORMAL_TO_SHORT = {
    "+": "i",
    "-": "d",
    ">": "r",
    "<": "l",
}
BF_SHORT_TO_NORMAL = dict(zip(
    BF_NORMAL_TO_SHORT.values(),
    BF_NORMAL_TO_SHORT.keys(),
))


def convert_bf_normal_to_short(bf_normal: str) -> str:
    io = PeekableStringIO(bf_normal)
    bf_short = ""
    while io.peek(1):
        normal_operation = io.peek(1)
        group_of_same_operation = io.read_while(
            lambda char: char == normal_operation
        )
        duplicate_count = len(group_of_same_operation)
        try:
            short_operation = BF_NORMAL_TO_SHORT[normal_operation]
            bf_short += short_operation + str(duplicate_count)
        except KeyError:
            bf_short += normal_operation * duplicate_count
    return bf_short


def convert_bf_short_to_normal(bf_short: str) -> str:
    io = PeekableStringIO(bf_short)
    bf_normal = ""
    while io.peek(1):
        short_operation = io.read(1)
        if short_operation in BF_SHORT_TO_NORMAL:
            normal_operation = BF_SHORT_TO_NORMAL[short_operation]
            count = int(io.read(1))
        else:
            normal_operation = short_operation
            count = 1
        bf_normal += normal_operation * count
    return bf_normal


if __name__ == "__main__":
    bf_code = input().strip()
    if not bf_code:
        print("Input is empty!", file=sys.stderr)
        sys.exit(1)

    bf_short_code = convert_bf_normal_to_short(bf_code)
    print(f"Short bf: {bf_short_code}")

    bf_normal_code = convert_bf_short_to_normal(bf_short_code)
    print(f"Normal bf: {bf_normal_code}")
