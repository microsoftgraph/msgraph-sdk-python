from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .azure_resource_evidence import AzureResourceEvidence

from .alert_evidence import AlertEvidence

@dataclass
class SasTokenEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.sasTokenEvidence"
    # The allowedIpAddresses property
    allowed_ip_addresses: Optional[str] = None
    # The allowedResourceTypes property
    allowed_resource_types: Optional[list[str]] = None
    # The allowedServices property
    allowed_services: Optional[list[str]] = None
    # The expiryDateTime property
    expiry_date_time: Optional[datetime.datetime] = None
    # The permissions property
    permissions: Optional[list[str]] = None
    # The protocol property
    protocol: Optional[str] = None
    # The signatureHash property
    signature_hash: Optional[str] = None
    # The signedWith property
    signed_with: Optional[str] = None
    # The startDateTime property
    start_date_time: Optional[datetime.datetime] = None
    # The storageResource property
    storage_resource: Optional[AzureResourceEvidence] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SasTokenEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SasTokenEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SasTokenEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .azure_resource_evidence import AzureResourceEvidence

        from .alert_evidence import AlertEvidence
        from .azure_resource_evidence import AzureResourceEvidence

        fields: dict[str, Callable[[Any], None]] = {
            "allowedIpAddresses": lambda n : setattr(self, 'allowed_ip_addresses', n.get_str_value()),
            "allowedResourceTypes": lambda n : setattr(self, 'allowed_resource_types', n.get_collection_of_primitive_values(str)),
            "allowedServices": lambda n : setattr(self, 'allowed_services', n.get_collection_of_primitive_values(str)),
            "expiryDateTime": lambda n : setattr(self, 'expiry_date_time', n.get_datetime_value()),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_primitive_values(str)),
            "protocol": lambda n : setattr(self, 'protocol', n.get_str_value()),
            "signatureHash": lambda n : setattr(self, 'signature_hash', n.get_str_value()),
            "signedWith": lambda n : setattr(self, 'signed_with', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "storageResource": lambda n : setattr(self, 'storage_resource', n.get_object_value(AzureResourceEvidence)),
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
        writer.write_str_value("allowedIpAddresses", self.allowed_ip_addresses)
        writer.write_collection_of_primitive_values("allowedResourceTypes", self.allowed_resource_types)
        writer.write_collection_of_primitive_values("allowedServices", self.allowed_services)
        writer.write_datetime_value("expiryDateTime", self.expiry_date_time)
        writer.write_collection_of_primitive_values("permissions", self.permissions)
        writer.write_str_value("protocol", self.protocol)
        writer.write_str_value("signatureHash", self.signature_hash)
        writer.write_str_value("signedWith", self.signed_with)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_object_value("storageResource", self.storage_resource)
    

