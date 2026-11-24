# The One-Line Exit

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

One funny single-line resignation letter, written for the
[The One-Line Exit](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
bounty on make.fun.

## The line

> I hereby resign: I have married 312 couples, and today I am divorcing one person — myself, from this job.

The joke: a wedding officiant who has married hundreds of couples finally
turns the ceremony around on himself. The one person he divorces is
himself — from this job. It reads like a letter someone could actually
send, it has a specific voice (the officiant), and the punchline lands
in the same single line.

## How to run

```sh
python3 main.py
```

This validates the line against the gate (UTF-8, 1–140 characters,
exactly one line) and writes it to `entry.txt` inside the output
directory: `/output` by default, or `$OUTPUT_DIR` when set.

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

The output directory is created only when it is missing; it is never
deleted or emptied.
