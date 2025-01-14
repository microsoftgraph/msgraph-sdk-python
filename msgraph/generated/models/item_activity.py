from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_action import AccessAction
    from .drive_item import DriveItem
    from .entity import Entity
    from .identity_set import IdentitySet

from .entity import Entity

@dataclass
class ItemActivity(Entity, Parsable):
    # An item was accessed.
    access: Optional[AccessAction] = None
    # Details about when the activity took place. Read-only.
    activity_date_time: Optional[datetime.datetime] = None
    # Identity of who performed the action. Read-only.
    actor: Optional[IdentitySet] = None
    # Exposes the driveItem that was the target of this activity.
    drive_item: Optional[DriveItem] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_action import AccessAction
        from .drive_item import DriveItem
        from .entity import Entity
        from .identity_set import IdentitySet

        from .access_action import AccessAction
        from .drive_item import DriveItem
        from .entity import Entity
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "access": lambda n : setattr(self, 'access', n.get_object_value(AccessAction)),
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "actor": lambda n : setattr(self, 'actor', n.get_object_value(IdentitySet)),
            "driveItem": lambda n : setattr(self, 'drive_item', n.get_object_value(DriveItem)),
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
        writer.write_object_value("access", self.access)
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_object_value("actor", self.actor)
        writer.write_object_value("driveItem", self.drive_item)
    

