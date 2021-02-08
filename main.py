import sys

from bf_converters import (
    convert_to_compressed_form,
    convert_to_normal_form,
)


if __name__ == "__main__":
    input_bf = sys.stdin.read()
    if not input_bf:
        print("Input is empty!", file=sys.stderr)
        sys.exit(1)

    compressed = convert_to_compressed_form(input_bf)
    print(f"compressed: {compressed}")

    back_to_normal = convert_to_normal_form(compressed)
    print(f"back to normal: {back_to_normal}")
