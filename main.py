import argparse
import sys
from io import StringIO
from textwrap import dedent
from typing import List

from bf_converters import (
    convert_to_compressed_form,
    convert_to_normal_form,
    BF_NORMAL_ALLOWED_CHARS,
    BF_COMPRESSED_ALLOWED_CHARS,
)


def clean_input(input_code: str, allowed_chars: List[str]) -> str:
    io = StringIO(input_code)
    cleaned_input = StringIO()
    while char := io.read(1):
        if char in allowed_chars:
            cleaned_input.write(char)
        elif char == "#":
            # this is a comment, skip end of line
            io.readline()
        elif char in ("\n", "\r", " ", "\t"):
            # skip newlines and spaces
            pass
        else:
            allowed = "".join(allowed_chars)
            print(
                f"ERROR: invalid char '{char}' (ord: {ord(char)}),"
                f" allowed chars are '{allowed}'",
                file=sys.stderr
            )
            sys.exit(1)
    return cleaned_input.getvalue()


def parse_args():
    parser = argparse.ArgumentParser(description=dedent("""
        Convert stdin to the normal or compressed form of brainfuck,
        and print it to stdout.
    """))
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-d", "--decompress",
        action="store_true",
        default=False,
        help="Decompress compressed brainfuck code"
    )
    group.add_argument(
        "-c", "--compress",
        action="store_true",
        default=False,
        help="Compress normal brainfuck code"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        default=False,
        help="Be more verbose"
    )
    return parser.parse_args()


if __name__ == "__main__":
    input_bf = sys.stdin.read()
    if not input_bf:
        print("Input is empty!", file=sys.stderr)
        sys.exit(1)

    opts = parse_args()

    if opts.compress:
        cleaned_bf = clean_input(input_bf, BF_NORMAL_ALLOWED_CHARS)
        if opts.verbose:
            print("Cleaned code:")
            print(cleaned_bf)
        converted_bf = convert_to_compressed_form(cleaned_bf)
    else:
        cleaned_bf = clean_input(input_bf, BF_COMPRESSED_ALLOWED_CHARS)
        if opts.verbose:
            print("Cleaned code:")
            print(cleaned_bf)
        converted_bf = convert_to_normal_form(cleaned_bf)

    print(converted_bf)
