from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CrossTenantAccessPolicyInboundTrust(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Specifies whether compliant devices from external Microsoft Entra organizations are trusted.
    is_compliant_device_accepted: Optional[bool] = None
    # Specifies whether Microsoft Entra hybrid joined devices from external Microsoft Entra organizations are trusted.
    is_hybrid_azure_a_d_joined_device_accepted: Optional[bool] = None
    # Specifies whether MFA from external Microsoft Entra organizations is trusted.
    is_mfa_accepted: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CrossTenantAccessPolicyInboundTrust:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyInboundTrust
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantAccessPolicyInboundTrust()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isCompliantDeviceAccepted": lambda n : setattr(self, 'is_compliant_device_accepted', n.get_bool_value()),
            "isHybridAzureADJoinedDeviceAccepted": lambda n : setattr(self, 'is_hybrid_azure_a_d_joined_device_accepted', n.get_bool_value()),
            "isMfaAccepted": lambda n : setattr(self, 'is_mfa_accepted', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("isCompliantDeviceAccepted", self.is_compliant_device_accepted)
        writer.write_bool_value("isHybridAzureADJoinedDeviceAccepted", self.is_hybrid_azure_a_d_joined_device_accepted)
        writer.write_bool_value("isMfaAccepted", self.is_mfa_accepted)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

