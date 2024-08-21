from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .vm_cloud_provider import VmCloudProvider

@dataclass
class VmMetadata(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The cloudProvider property
    cloud_provider: Optional[VmCloudProvider] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier of the Azure resource.
    resource_id: Optional[str] = None
    # Unique identifier of the Azure subscription the customer tenant belongs to.
    subscription_id: Optional[str] = None
    # Unique identifier of the virtual machine instance.
    vm_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VmMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VmMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VmMetadata()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .vm_cloud_provider import VmCloudProvider

        from .vm_cloud_provider import VmCloudProvider

        fields: Dict[str, Callable[[Any], None]] = {
            "cloudProvider": lambda n : setattr(self, 'cloud_provider', n.get_enum_value(VmCloudProvider)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "subscriptionId": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
            "vmId": lambda n : setattr(self, 'vm_id', n.get_str_value()),
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
        writer.write_enum_value("cloudProvider", self.cloud_provider)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_str_value("vmId", self.vm_id)
        writer.write_additional_data_value(self.additional_data)
    

