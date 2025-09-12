from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence

from .alert_evidence import AlertEvidence

@dataclass
class SecurityGroupEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.securityGroupEvidence"
    # The unique group identifier assigned by the on-premises Active Directory.
    active_directory_object_guid: Optional[UUID] = None
    # The name of the security group.
    display_name: Optional[str] = None
    # The distinguished name of the security group.
    distinguished_name: Optional[str] = None
    # The friendly name of the security group.
    friendly_name: Optional[str] = None
    # Unique identifier of the security group.
    security_group_id: Optional[str] = None
    # The security identifier of the group.
    sid: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityGroupEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityGroupEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityGroupEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence

        from .alert_evidence import AlertEvidence

        fields: dict[str, Callable[[Any], None]] = {
            "activeDirectoryObjectGuid": lambda n : setattr(self, 'active_directory_object_guid', n.get_uuid_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "distinguishedName": lambda n : setattr(self, 'distinguished_name', n.get_str_value()),
            "friendlyName": lambda n : setattr(self, 'friendly_name', n.get_str_value()),
            "securityGroupId": lambda n : setattr(self, 'security_group_id', n.get_str_value()),
            "sid": lambda n : setattr(self, 'sid', n.get_str_value()),
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
        writer.write_uuid_value("activeDirectoryObjectGuid", self.active_directory_object_guid)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("distinguishedName", self.distinguished_name)
        writer.write_str_value("friendlyName", self.friendly_name)
        writer.write_str_value("securityGroupId", self.security_group_id)
        writer.write_str_value("sid", self.sid)
    

