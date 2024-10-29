from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .proxied_domain import ProxiedDomain

@dataclass
class WindowsInformationProtectionProxiedDomainCollection(AdditionalDataHolder, BackedModel, Parsable):
    """
    Windows Information Protection Proxied Domain Collection
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Display name
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of proxied domains
    proxied_domains: Optional[List[ProxiedDomain]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsInformationProtectionProxiedDomainCollection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionProxiedDomainCollection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsInformationProtectionProxiedDomainCollection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .proxied_domain import ProxiedDomain

        from .proxied_domain import ProxiedDomain

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "proxiedDomains": lambda n : setattr(self, 'proxied_domains', n.get_collection_of_object_values(ProxiedDomain)),
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
        from .proxied_domain import ProxiedDomain

        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("proxiedDomains", self.proxied_domains)
        writer.write_additional_data_value(self.additional_data)
    

