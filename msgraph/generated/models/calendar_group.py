from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import calendar, entity

from . import entity

class CalendarGroup(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new calendarGroup and sets the default values.
        """
        super().__init__()
        # The calendars in the calendar group. Navigation property. Read-only. Nullable.
        self._calendars: Optional[List[calendar.Calendar]] = None
        # Identifies the version of the calendar group. Every time the calendar group is changed, ChangeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
        self._change_key: Optional[str] = None
        # The class identifier. Read-only.
        self._class_id: Optional[UUID] = None
        # The group name.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def calendars(self,) -> Optional[List[calendar.Calendar]]:
        """
        Gets the calendars property value. The calendars in the calendar group. Navigation property. Read-only. Nullable.
        Returns: Optional[List[calendar.Calendar]]
        """
        return self._calendars
    
    @calendars.setter
    def calendars(self,value: Optional[List[calendar.Calendar]] = None) -> None:
        """
        Sets the calendars property value. The calendars in the calendar group. Navigation property. Read-only. Nullable.
        Args:
            value: Value to set for the calendars property.
        """
        self._calendars = value
    
    @property
    def change_key(self,) -> Optional[str]:
        """
        Gets the changeKey property value. Identifies the version of the calendar group. Every time the calendar group is changed, ChangeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
        Returns: Optional[str]
        """
        return self._change_key
    
    @change_key.setter
    def change_key(self,value: Optional[str] = None) -> None:
        """
        Sets the changeKey property value. Identifies the version of the calendar group. Every time the calendar group is changed, ChangeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
        Args:
            value: Value to set for the change_key property.
        """
        self._change_key = value
    
    @property
    def class_id(self,) -> Optional[UUID]:
        """
        Gets the classId property value. The class identifier. Read-only.
        Returns: Optional[UUID]
        """
        return self._class_id
    
    @class_id.setter
    def class_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the classId property value. The class identifier. Read-only.
        Args:
            value: Value to set for the class_id property.
        """
        self._class_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CalendarGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CalendarGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CalendarGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import calendar, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "calendars": lambda n : setattr(self, 'calendars', n.get_collection_of_object_values(calendar.Calendar)),
            "changeKey": lambda n : setattr(self, 'change_key', n.get_str_value()),
            "classId": lambda n : setattr(self, 'class_id', n.get_uuid_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The group name.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The group name.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("calendars", self.calendars)
        writer.write_str_value("changeKey", self.change_key)
        writer.write_uuid_value("classId", self.class_id)
        writer.write_str_value("name", self.name)
    

