from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_details import EmailDetails
    from .entity import Entity
    from .target_owners import TargetOwners

from .entity import Entity

@dataclass
class OwnerlessGroupPolicy(Entity, Parsable):
    # The emailInfo property
    email_info: Optional[EmailDetails] = None
    # The enabledGroupIds property
    enabled_group_ids: Optional[list[str]] = None
    # The isEnabled property
    is_enabled: Optional[bool] = None
    # The maxMembersToNotify property
    max_members_to_notify: Optional[int] = None
    # The notificationDurationInWeeks property
    notification_duration_in_weeks: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyWebUrl property
    policy_web_url: Optional[str] = None
    # The targetOwners property
    target_owners: Optional[TargetOwners] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OwnerlessGroupPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OwnerlessGroupPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OwnerlessGroupPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_details import EmailDetails
        from .entity import Entity
        from .target_owners import TargetOwners

        from .email_details import EmailDetails
        from .entity import Entity
        from .target_owners import TargetOwners

        fields: dict[str, Callable[[Any], None]] = {
            "emailInfo": lambda n : setattr(self, 'email_info', n.get_object_value(EmailDetails)),
            "enabledGroupIds": lambda n : setattr(self, 'enabled_group_ids', n.get_collection_of_primitive_values(str)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "maxMembersToNotify": lambda n : setattr(self, 'max_members_to_notify', n.get_int_value()),
            "notificationDurationInWeeks": lambda n : setattr(self, 'notification_duration_in_weeks', n.get_int_value()),
            "policyWebUrl": lambda n : setattr(self, 'policy_web_url', n.get_str_value()),
            "targetOwners": lambda n : setattr(self, 'target_owners', n.get_object_value(TargetOwners)),
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
        writer.write_object_value("emailInfo", self.email_info)
        writer.write_collection_of_primitive_values("enabledGroupIds", self.enabled_group_ids)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_int_value("maxMembersToNotify", self.max_members_to_notify)
        writer.write_int_value("notificationDurationInWeeks", self.notification_duration_in_weeks)
        writer.write_str_value("policyWebUrl", self.policy_web_url)
        writer.write_object_value("targetOwners", self.target_owners)
    

