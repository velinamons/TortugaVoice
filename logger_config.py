import sys
from loguru import logger

logger.remove()

log_file_path = "file.log"
log_format = "{time:YYYY-MM-DD HH:mm:ss} {level} {message}"

logger.add(
    sys.stderr,
    format=log_format,
    level="DEBUG"
)

logger.add(
    log_file_path,
    format=log_format,
    level="DEBUG"
)
