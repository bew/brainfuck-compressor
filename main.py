import sys
from typing import Optional

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


class BrainfuckNormal2Short:
    def __init__(self):
        self.last_op: Optional[str] = None
        self.last_op_count = 0

    def convert(self, bf_code: str) -> str:
        bf_short_code = ""

        for op in bf_code:
            if not self.last_op:
                self._register_new_op(op)

            if self.last_op != op:
                bf_short_code += self._convert_to_bf_short()
                self._register_new_op(op)

            self.last_op_count += 1

        bf_short_code += self._convert_to_bf_short()
        return bf_short_code

    def _register_new_op(self, new_op: str):
        self.last_op = new_op
        self.last_op_count = 0

    def _convert_to_bf_short(self) -> str:
        try:
            return BF_TO_BF_SHORT[self.last_op] + str(self.last_op_count)
        except KeyError:
            return self.last_op * self.last_op_count


bf_code = input().strip()
if not bf_code:
    print("Input is empty!", file=sys.stderr)
    sys.exit(1)

bf_short_code = BrainfuckNormal2Short().convert(bf_code)

print(bf_short_code)
