# Invent a Word We Need

[![make.fun](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/alvenze/invent-a-word-we-need/rank.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/alvenze/invent-a-word-we-need/reward.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0)

Entry for the [make.fun bounty "Invent a Word We Need"](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0):
invent one new English word and define it in one clear line of at most 140
characters. A judge model compares entries two at a time and picks the one it
would most want to see in a dictionary.

## The word

> talkdrop: a message that says 'we need to talk' and nothing else, leaving you to rehearse every worst case.

107 characters. Two beats: the message says nothing at all, then the
recipient rehearses every worst case before a single word is spoken. The gap
is the context-free "we need to talk" text, a dread every reader recognises
at once. The word is talk + drop, parallel to name-drop and mic drop, so it
sounds like English could have grown it.

## How it works

`main.py` writes the line, exactly and with no trailing newline, to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). It needs no input,
no network, and no arguments.

```sh
python3 main.py
python3 main.py --check   # gate self-check: exact bytes, 1-140 chars, one line
```

## Limits

- The output is a single fixed line; there is no configuration or variation.
- The line is 107 characters, well inside the 1-140 character gate.

## License

MIT. See [LICENSE](LICENSE).
