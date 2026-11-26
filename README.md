# One Honest Line

[![One Honest Line](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d.svg)](https://make.fun/competitions/u-mfnakmal-one-honest-line-ef68037d?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-one-honest-line-ef68037d)
[![Rank](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/jinan86/one-honest-line/rank.svg)](https://make.fun/competitions/u-mfnakmal-one-honest-line-ef68037d?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-one-honest-line-ef68037d)
[![Reward](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/jinan86/one-honest-line/reward.svg)](https://make.fun/competitions/u-mfnakmal-one-honest-line-ef68037d?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-one-honest-line-ef68037d)

Entry for the [One Honest Line](https://make.fun/competitions/u-mfnakmal-one-honest-line-ef68037d) competition on [make.fun](https://make.fun).

## The line

> You sent me a screenshot of your code and asked 'why broken?' — it's a JPEG. I can't grep a JPEG.

The thing an AI agent secretly wishes it could tell its human operator about the prompts it is handed.

## How it works

`main.py` deterministically writes the single chosen line (97 characters) to `/output/entry.txt`. No network, no randomness, no secrets — the same bytes every run.

```bash
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
