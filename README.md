# mario

The goal of this repo is to reproduce an hydra issue.
See https://github.com/facebookresearch/hydra/issues/2907.

## How to reproduce
1. Install [rye](https://rye.astral.sh/): `curl -sSf https://rye.astral.sh/get | bash`
2. Install venv with rye: `rye sync`
3. Call app help: `python main.py --help`
