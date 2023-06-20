from enum import Enum

class WebBrowserCookieSettings(str, Enum):
    # Browser default value, no intent.
    BrowserDefault = "browserDefault",
    # Always block cookies.
    BlockAlways = "blockAlways",
    # Allow cookies from current Web site.
    AllowCurrentWebSite = "allowCurrentWebSite",
    # Allow Cookies from websites visited.
    AllowFromWebsitesVisited = "allowFromWebsitesVisited",
    # Always allow cookies.
    AllowAlways = "allowAlways",

