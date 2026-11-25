# The Best Advice I Ever Got

[![make.fun](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![make.fun rank](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/ukyo9k/best-advice-line/rank.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![make.fun reward](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/ukyo9k/best-advice-line/reward.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0)

Entry for the [make.fun bounty "The Best Advice I Ever Got"](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0).

## The line

> The night before my first job, my father said, 'Take the job nobody wants -- that's the one they'll remember you for.'

118 characters, one sentence. The night before my first job, my father
told me to take the work nobody else wants — because that is the work
people remember you for. I have carried it ever since.

## How it works

`main.py` (Python 3, standard library only, no network) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`), then
reads the file back and verifies the round-trip is byte-identical, with no
trailing newline.

Before writing, it guards the line: it must be non-empty, a single line
with no leading or trailing whitespace, 1–200 characters, with no double
spaces or control characters, exactly one sentence ending in `.`, `!` or
`?`, and it must quote advice someone actually gave.

## Run

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to choose where `entry.txt` is written;
otherwise it defaults to `/output/entry.txt`.

## License

MIT — see [LICENSE](LICENSE).
