from enum import Enum

class AuthenticationAttributeCollectionInputType(str, Enum):
    Text = "text",
    RadioSingleSelect = "radioSingleSelect",
    CheckboxMultiSelect = "checkboxMultiSelect",
    Boolean = "boolean",
    UnknownFutureValue = "unknownFutureValue",

