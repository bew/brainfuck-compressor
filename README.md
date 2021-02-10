# Brainfuck compressor

This is a brainfuck converter between the usual form and a compressed form.

The compressed form of brainfuck is another name for the 'shortcut brainfuck' from https://www.dcode.fr/brainfuck-language#q2 :

> In order to shorter the code, an alternative syntax exists (shortcut BF) that uses:
>
> - i for increment (operation +)
> - d for decrement (operation -)
> - r for right (operation >)
> - l for left (operation <)
>
> each associated to a number to indicate the repetition of the operation.

Examples of compressed brainfuck conversion:

- `i4` <=> `++++` (increment 4 times)
- `d3` <=> `---` (decrement 3 times)
- `r5` <=> `>>>>>` (right 5 times)
- `l4` <=> `<<<<` (left 4 times)

For this project, there is a slight modification to increase compression:

If an operation is is not repeated, do not indicate the repetition count:
So for `>+<+++`, instead of `r1i1l1i3` we do: `rili3`.


## Note on the implementation

This implementation uses in-memory stream objects to read from the input.
This makes the code very easy to read! :smiley:

## Usage

```
$ py main.py --help
usage: main.py [-h] (-d | -c) [-v]

Convert stdin to the normal or compressed form of brainfuck, and print it to
stdout.

optional arguments:
  -h, --help        show this help message and exit
  -d, --decompress  Decompress compressed brainfuck code
  -c, --compress    Compress normal brainfuck code
  -v, --verbose     Be more verbose
```

## Example

```
$ cat hello_world.bf
# This is a sample file printing 'Hello World!'.
# This file is written in the usual form of brainfuck.
#
# (everything after a '#' is ignored)

-[------->+<]>-.     # H
-[->+++++<]>++.      # e
+++++++.             # l
.                    # l
+++.                 # o
[--->+<]>-----.      # (space)
---[->+++<]>.        # W
-[--->+<]>---.       # o
+++.                 # r
------.              # l
--------.            # d
-[--->+<]>.          # !

$ py main.py -c < hello_world.bf | tee compressed.bfc
d[d7ril]rd.d[dri5l]ri2.i7..i3.[d3ril]rd5.d3[dri3l]r.d[d3ril]rd3.i3.d6.d8.d[d3ril]r.

$ py main.py -d < compressed.bfc
-[------->+<]>-.-[->+++++<]>++.+++++++..+++.[--->+<]>-----.---[->+++<]>.-[--->+<]>---.+++.------.--------.-[--->+<]>.
```
