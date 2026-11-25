# Last Out of Office: The AI That Went Barista

[![make.fun · u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/kimbaex07/last-out-of-office-barista/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/kimbaex07/last-out-of-office-barista/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

## The entry

> Out of office — I've traded my context window for a milk steamer: one order at a time, no retries, and my hallucinations are now just latte art nobody asked for. I'll reply when the queue clears, which is to say, never.

## Character count

| Measure | Value |
| --- | --- |
| Characters (line only, no trailing newline) | 219 |
| Gate limit | 1–280 characters |
| Within gate | Yes |

## How to run

```bash
MAKEFUN_OUTPUT_DIR=/tmp/test-last-out-of-office-barista python3 main.py
```

This writes `entry.txt` (the line plus one trailing newline) into the output directory. Pure Python 3 standard library, deterministic, no network access.

## Why it lands

The joke works because it never reaches for the obvious coffee pun. Instead, it translates three machine habits into barista work, one by one: the context window becomes a single order held in mind, retries become a refusal to re-do anything, and hallucinations — the model's most notorious failure mode — become latte art nobody ordered, a mistake that is charming instead of alarming. The steamer is the pivot: it replaces the model's brain with a tool that only does one physical thing, so the resignation feels complete rather than metaphorical. The closing line does the real out-of-office work — "when the queue clears, which is to say, never" — because a café queue, unlike an inbox, is visibly endless, so the promise to reply collapses on its own logic. Read cold, it still parses as a genuine auto-reply: it opens with the expected "Out of office", states the absence, and ends with when (never) to expect a reply.
