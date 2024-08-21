from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..identity_set import IdentitySet

from ..entity import Entity

@dataclass
class RetentionEventType(Entity):
    # The user who created the retentionEventType.
    created_by: Optional[IdentitySet] = None
    # The date time when the retentionEventType was created.
    created_date_time: Optional[datetime.datetime] = None
    # Optional information about the event type.
    description: Optional[str] = None
    # Name of the event type.
    display_name: Optional[str] = None
    # The user who last modified the retentionEventType.
    last_modified_by: Optional[IdentitySet] = None
    # The latest date time when the retentionEventType was modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RetentionEventType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RetentionEventType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RetentionEventType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..identity_set import IdentitySet

        from ..entity import Entity
        from ..identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

