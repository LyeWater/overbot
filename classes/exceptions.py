from discord import app_commands


class OverBotException(Exception):
    """Base exception type for OverBot commands."""

    pass


class NoChoice(OverBotException):
    pass


class PaginationError(OverBotException):
    pass


class InvalidColor(OverBotException):
    def __init__(self) -> None:
        super().__init__(
            "You must enter an hex value (e.g. `#fff`) or an rgb value *comma separated* (e.g. 255, 255, 255)."
        )


class NoTriviaStats(OverBotException):
    def __init__(self) -> None:
        super().__init__("This member has no stats to show.")


class RequestError(OverBotException):
    pass


class NotFound(RequestError):
    def __init__(self) -> None:
        super().__init__("Player not found.")


class ValidationError(RequestError):
    def __init__(self) -> None:
        super().__init__("Validation error occured. Please try again.")


class InternalServerError(RequestError):
    def __init__(self) -> None:
        super().__init__(
            "The API is having internal server problems. Please be patient and try again later."
        )


class BlizzardServerError(RequestError):
    def __init__(self) -> None:
        super().__init__(
            "Blizzard is having internal server problems. Please be patient and try again later."
        )


class UnknownError(RequestError):
    def __init__(self) -> None:
        super().__init__("Something bad happened. Please be patient and try again.")


class TooManyAccounts(RequestError):
    def __init__(self, platform: str, username: str, players: int) -> None:
        match platform:
            case "pc":
                what = "BattleTag"
            case "console":
                what = "username"
        message = (
            f"**{players}** accounts found named `{username}`. Please "
            f"be more specific by entering your exact **{what}**."  # type: ignore # 'what' will always be bound to something
        )
        super().__init__(message)


class ProfileException(OverBotException):
    pass


class NoStats(ProfileException):
    def __init__(self, hero: str) -> None:
        if hero == "all-heroes":
            message = "This profile has no quick play nor competitive stats to display."
        else:
            message = (
                f"This profile has no quick play nor competitive stast for **{hero}** to display."
            )
        super().__init__(message)


class ProfileNotLinked(app_commands.CheckFailure):
    def __init__(self, *, is_author: bool) -> None:
        self.is_author = is_author


class ProfileLimitReached(app_commands.CheckFailure):
    def __init__(self, limit: int) -> None:
        self.limit = limit


class NotPremium(app_commands.CheckFailure):
    pass


class NotOwner(app_commands.CheckFailure):
    pass
