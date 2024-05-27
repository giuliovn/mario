import hydra

from omegaconf import OmegaConf


@hydra.main(
    version_base=None,
    config_path=".",
    config_name="conf",
)
def main(_cfg):
    print(f"Config:\n{OmegaConf.to_yaml(_cfg, resolve=True)}")


if __name__ == "__main__":
    main()
