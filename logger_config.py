from loguru import logger

log_file_path = "file.log"
log_format = "{time:YYYY-MM-DD HH:mm:ss} {level} {message}"

logger.add(
    log_file_path,
    format=log_format,
    level="INFO"
)

loguru_logger = logger
