from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_action, drive_item, entity, identity_set

from . import entity

@dataclass
class ItemActivity(entity.Entity):
    # An item was accessed.
    access: Optional[access_action.AccessAction] = None
    # Details about when the activity took place. Read-only.
    activity_date_time: Optional[datetime] = None
    # Identity of who performed the action. Read-only.
    actor: Optional[identity_set.IdentitySet] = None
    # Exposes the driveItem that was the target of this activity.
    drive_item: Optional[drive_item.DriveItem] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemActivity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ItemActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_action, drive_item, entity, identity_set

        from . import access_action, drive_item, entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "access": lambda n : setattr(self, 'access', n.get_object_value(access_action.AccessAction)),
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "actor": lambda n : setattr(self, 'actor', n.get_object_value(identity_set.IdentitySet)),
            "driveItem": lambda n : setattr(self, 'drive_item', n.get_object_value(drive_item.DriveItem)),
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
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("access", self.access)
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_object_value("actor", self.actor)
        writer.write_object_value("driveItem", self.drive_item)
    

