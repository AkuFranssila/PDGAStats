from typing import Literal

error_messages = {
    "PLAYER_ID_TOO_LOW": "Player ID is too low to be valid. Check crawler for problems.",
    "PLAYER_ID_NOT_INT": "Player ID can not be converted to INT. Check crawler for problems.",
    "INCORRECT_TOURNAMENT_DATE": "Incorrect Tournament Crawl Options. Select all, test or latest.",
    "INCORRECT_S3_FOLDER_NAME": "Incorrect S3 Folder selected. Check mapping for correct naming."
}

error_messages_type = Literal[tuple(error_messages.keys())]