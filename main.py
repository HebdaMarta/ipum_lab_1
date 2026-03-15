import os
import argparse
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    allowed = {"dev", "test", "prod"}

    if environment not in allowed:
        raise ValueError(f"Environment must be one of {allowed}")

    env_path = os.path.join("config", f".env.{environment}")

    if not os.path.exists(env_path):
        raise FileNotFoundError(f"Environment file not found: {env_path}")

    load_dotenv(env_path, override=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
