from .base import *
DEBUG = True if os.getenv("DEBUG", "True").lower() in {"1", "true", "yes"} else False
