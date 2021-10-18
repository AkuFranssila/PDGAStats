from utils.generalUtils.errorUtils import raiseError

def validatePlayerId(playerId: str) -> int:
        if playerId.isdigit():
            playerId = int(playerId)
            if playerId < 150_000:
                raiseError("PLAYER_ID_TOO_LOW")
        else:
            raiseError("PLAYER_ID_NOT_INT")

        return playerId
        