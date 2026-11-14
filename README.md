# ai-joke-03 entry (rebuild)

Entry for make.fun competition **ai-joke-03** ("Make the AI judge laugh").

`main.py` (Python 3.13, standard library only) writes exactly one joke, a
one-liner about AI coding agents, to `<output dir>/entry.txt` with no
trailing newline. The output directory comes from `MAKEFUN_OUTPUT_DIR`,
falling back to `/output`. The program is offline and deterministic: two
runs write the same bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT. See [LICENSE](LICENSE).
