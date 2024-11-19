from pathlib import Path

from WDL.CLI import runner as wdl_run

SCRIPT_DIR = Path(__file__).parent
WDL_PATH = SCRIPT_DIR / "wdl/hello.wdl"
INPUTS = [
    SCRIPT_DIR / "inputs/1.json",
    SCRIPT_DIR / "inputs/2.json",
]


def main(wdl_path: Path, inputs: list[Path]):
    for input in inputs:
        out = wdl_run(
            str(wdl_path),
            input_file=str(input),
            run_dir="outputs",
            stdout_file=None,
            stderr_file=None,
            cfg=str(SCRIPT_DIR / "cfg/miniwdl.cfg"),
            no_cache=False,
            verbose=True,
            debug=True,
            no_color=False
        )
    return out


if __name__ == "__main__":
    main(WDL_PATH, INPUTS)
