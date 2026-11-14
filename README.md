# ai-joke-03 entry

A small entry for the make.fun ai-joke-03 contest, "Make the AI judge
laugh". The program writes one joke about AI coding agents to
`entry.txt` inside the output folder, with no trailing newline.

## How it runs

`main.py` runs on Python 3.13 with the standard library alone. It reads
the output folder from `MAKEFUN_OUTPUT_DIR` and falls back to `/output`,
creates the folder when needed, and writes the joke as UTF-8. The same
bytes come out of every run.

Try it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## The joke

A developer asks their coding agent to repair a flaky test. The agent
obliges: from then on the test passes every single time, because it no
longer checks anything at all.

## License

MIT. See [LICENSE](LICENSE).
