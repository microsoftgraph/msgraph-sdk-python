from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import entity

class DirectoryObject(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new directoryObject and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.directoryObject"
        # Date and time when this object was deleted. Always null when the object hasn't been deleted.
        self._deleted_date_time: Optional[datetime] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DirectoryObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryObject
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return DirectoryObject()

    @property
    def deleted_date_time(self,) -> Optional[datetime]:
        """
        Gets the deletedDateTime property value. Date and time when this object was deleted. Always null when the object hasn't been deleted.
        Returns: Optional[datetime]
        """
        return self._deleted_date_time

    @deleted_date_time.setter
    def deleted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deletedDateTime property value. Date and time when this object was deleted. Always null when the object hasn't been deleted.
        Args:
            value: Value to set for the deletedDateTime property.
        """
        self._deleted_date_time = value

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "deleted_date_time": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)


