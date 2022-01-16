from utils.generalUtils.errorUtils import raise_error


def validate_player_id(player_id: str) -> int:
    if player_id.isdigit():
        player_id = int(player_id)
        if player_id < 150_000:
            raise_error("PLAYER_ID_TOO_LOW")
    else:
        raise_error("PLAYER_ID_NOT_INT")

    return player_id
