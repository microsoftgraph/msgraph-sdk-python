from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SecurityVendorInformation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
    provider: Optional[str] = None
    # Version of the provider or subprovider, if it exists, that generated the alert. Required
    provider_version: Optional[str] = None
    # Specific subprovider (under aggregating provider); for example, WindowsDefenderATP.SmartScreen.
    sub_provider: Optional[str] = None
    # Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
    vendor: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityVendorInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityVendorInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityVendorInformation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "providerVersion": lambda n : setattr(self, 'provider_version', n.get_str_value()),
            "subProvider": lambda n : setattr(self, 'sub_provider', n.get_str_value()),
            "vendor": lambda n : setattr(self, 'vendor', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("providerVersion", self.provider_version)
        writer.write_str_value("subProvider", self.sub_provider)
        writer.write_str_value("vendor", self.vendor)
        writer.write_additional_data_value(self.additional_data)
    

