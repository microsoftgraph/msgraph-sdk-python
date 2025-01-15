from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class GroupLifecyclePolicy(Entity, Parsable):
    # List of email address to send notifications for groups without owners. Multiple email address can be defined by separating email address with a semicolon.
    alternate_notification_emails: Optional[str] = None
    # Number of days before a group expires and needs to be renewed. Once renewed, the group expiration is extended by the number of days defined.
    group_lifetime_in_days: Optional[int] = None
    # The group type for which the expiration policy applies. Possible values are All, Selected or None.
    managed_group_types: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupLifecyclePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupLifecyclePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupLifecyclePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "alternateNotificationEmails": lambda n : setattr(self, 'alternate_notification_emails', n.get_str_value()),
            "groupLifetimeInDays": lambda n : setattr(self, 'group_lifetime_in_days', n.get_int_value()),
            "managedGroupTypes": lambda n : setattr(self, 'managed_group_types', n.get_str_value()),
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
        writer.write_str_value("alternateNotificationEmails", self.alternate_notification_emails)
        writer.write_int_value("groupLifetimeInDays", self.group_lifetime_in_days)
        writer.write_str_value("managedGroupTypes", self.managed_group_types)
    

