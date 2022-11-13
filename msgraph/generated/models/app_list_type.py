from enum import Enum

class AppListType(Enum):
    # Default value, no intent.
    None_escaped = "none",
    # The list represents the apps that will be considered compliant (only apps on the list are compliant).
    AppsInListCompliant = "appsInListCompliant",
    # The list represents the apps that will be considered non compliant (all apps are compliant except apps on the list).
    AppsNotInListCompliant = "appsNotInListCompliant",

