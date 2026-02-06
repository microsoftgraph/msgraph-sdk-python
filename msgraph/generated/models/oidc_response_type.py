from enum import Enum

class OidcResponseType(str, Enum):
    Code = "code",
    Id_token = "id_token",
    Token = "token",
    UnknownFutureValue = "unknownFutureValue",

