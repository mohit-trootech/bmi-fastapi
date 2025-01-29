from pathlib import Path
from dotenv import dotenv_values

config = dotenv_values(".env")
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = str(Path(__file__).parent.parent)
SERVICE_KEY = BASE_DIR + config.get("SERVICE_KEY")
