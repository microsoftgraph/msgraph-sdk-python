from enum import Enum

class IdentityUserFlowAttributeInputType(str, Enum):
    TextBox = "textBox",
    DateTimeDropdown = "dateTimeDropdown",
    RadioSingleSelect = "radioSingleSelect",
    DropdownSingleSelect = "dropdownSingleSelect",
    EmailBox = "emailBox",
    CheckboxMultiSelect = "checkboxMultiSelect",

