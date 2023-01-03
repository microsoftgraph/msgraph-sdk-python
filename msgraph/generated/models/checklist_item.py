from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ChecklistItem(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def checked_date_time(self,) -> Optional[datetime]:
        """
        Gets the checkedDateTime property value. The date and time when the checklistItem was finished.
        Returns: Optional[datetime]
        """
        return self._checked_date_time
    
    @checked_date_time.setter
    def checked_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the checkedDateTime property value. The date and time when the checklistItem was finished.
        Args:
            value: Value to set for the checkedDateTime property.
        """
        self._checked_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new checklistItem and sets the default values.
        """
        super().__init__()
        # The date and time when the checklistItem was finished.
        self._checked_date_time: Optional[datetime] = None
        # The date and time when the checklistItem was created.
        self._created_date_time: Optional[datetime] = None
        # Field indicating the title of checklistItem.
        self._display_name: Optional[str] = None
        # State indicating whether the item is checked off or not.
        self._is_checked: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the checklistItem was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the checklistItem was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChecklistItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChecklistItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChecklistItem()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Field indicating the title of checklistItem.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Field indicating the title of checklistItem.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "checked_date_time": lambda n : setattr(self, 'checked_date_time', n.get_datetime_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_checked": lambda n : setattr(self, 'is_checked', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_checked(self,) -> Optional[bool]:
        """
        Gets the isChecked property value. State indicating whether the item is checked off or not.
        Returns: Optional[bool]
        """
        return self._is_checked
    
    @is_checked.setter
    def is_checked(self,value: Optional[bool] = None) -> None:
        """
        Sets the isChecked property value. State indicating whether the item is checked off or not.
        Args:
            value: Value to set for the isChecked property.
        """
        self._is_checked = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("checkedDateTime", self.checked_date_time)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isChecked", self.is_checked)
    

