from typing import Literal

errorMessages = {
    "PLAYER_ID_TOO_LOW": "Player ID is too low to be valid. Check crawler for problems.",
    "PLAYER_ID_NOT_INT": "Player ID can not be converted to INT. Check crawler for problems.",
    "INCORRECT_TOURNAMENT_DATE": "Incorrect Tournament Crawl Options. Select all, test or latest."
}

errorMessagesType = Literal[tuple(errorMessages.keys())]