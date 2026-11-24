# Make the AI Judge Laugh: Developer Excuses

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/GeMseN-Test/make-the-ai-judge-laugh-developer-20261124.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/GeMseN-Test/make-the-ai-judge-laugh-developer-20261124/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/GeMseN-Test/make-the-ai-judge-laugh-developer-20261124/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

Entry for the [Make the AI Judge Laugh: Developer Excuses](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) bounty on make.fun — one funny single-line excuse a developer gives when code breaks in production, under 200 characters.

## The line

> In my defense, the code worked perfectly until a user did exactly what the ticket asked — the one path I never tested.

**118 characters**, one line. The twist: the user did exactly what the ticket asked — the one path nobody ever tested. It sounds like a developer defending themselves out loud, and it steers clear of the worn "works on my machine / tests passed / staging" excuses that flood this bounty (1,528 entries and counting).

## How it works

`main.py` writes that single line, deterministically, to `/output/entry.txt`. No input, no network, no randomness — run it twice and the file is byte-identical.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT
