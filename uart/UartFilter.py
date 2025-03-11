class UartFilter():
    def filter_message(message: str) -> str:
        return UartFilter.__remove_eol(message)

    def __remove_eol(message: str) -> str:
        return message[2:-3]
