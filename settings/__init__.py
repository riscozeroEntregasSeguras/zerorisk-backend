import os
import logging

from .base import *

ENV_VAR = "ENVIRONMENT_VAR"
PRODUCTION = "PRODUCTION"
DEVELOPMENT = "DEVELOPMENT"

if os.getenv(ENV_VAR) == PRODUCTION:
    from .production import *
else:
    logging.warning("No valid value set for environment variable '{}'. "
                    "Assuming value '{}'".format(ENV_VAR, DEVELOPMENT))
    from .development import *
