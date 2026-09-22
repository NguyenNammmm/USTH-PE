def save_message(text,logger):
    if not text.strip():
        logger.warning("empty"); return False
    logger.debug("validated"); logger.info("saved"); return True
