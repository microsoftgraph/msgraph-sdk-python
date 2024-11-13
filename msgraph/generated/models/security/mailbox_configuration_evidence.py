from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .mailbox_configuration_type import MailboxConfigurationType

from .alert_evidence import AlertEvidence

@dataclass
class MailboxConfigurationEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.mailboxConfigurationEvidence"
    # The configurationId property
    configuration_id: Optional[str] = None
    # The configurationType property
    configuration_type: Optional[MailboxConfigurationType] = None
    # The displayName property
    display_name: Optional[str] = None
    # The externalDirectoryObjectId property
    external_directory_object_id: Optional[UUID] = None
    # The mailboxPrimaryAddress property
    mailbox_primary_address: Optional[str] = None
    # The upn property
    upn: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailboxConfigurationEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailboxConfigurationEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MailboxConfigurationEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .mailbox_configuration_type import MailboxConfigurationType

        from .alert_evidence import AlertEvidence
        from .mailbox_configuration_type import MailboxConfigurationType

        fields: Dict[str, Callable[[Any], None]] = {
            "configurationId": lambda n : setattr(self, 'configuration_id', n.get_str_value()),
            "configurationType": lambda n : setattr(self, 'configuration_type', n.get_enum_value(MailboxConfigurationType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalDirectoryObjectId": lambda n : setattr(self, 'external_directory_object_id', n.get_uuid_value()),
            "mailboxPrimaryAddress": lambda n : setattr(self, 'mailbox_primary_address', n.get_str_value()),
            "upn": lambda n : setattr(self, 'upn', n.get_str_value()),
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
        from .alert_evidence import AlertEvidence
        from .mailbox_configuration_type import MailboxConfigurationType

        writer.write_str_value("configurationId", self.configuration_id)
        writer.write_enum_value("configurationType", self.configuration_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_uuid_value("externalDirectoryObjectId", self.external_directory_object_id)
        writer.write_str_value("mailboxPrimaryAddress", self.mailbox_primary_address)
        writer.write_str_value("upn", self.upn)
    

