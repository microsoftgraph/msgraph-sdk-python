from enum import Enum

class WebApplicationFirewallProviderType(str, Enum):
    Akamai = "akamai",
    Cloudflare = "cloudflare",
    UnknownFutureValue = "unknownFutureValue",

