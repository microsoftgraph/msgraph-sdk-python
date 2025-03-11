from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .printer_discovery_settings import PrinterDiscoverySettings

@dataclass
class PrintSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Specifies whether document conversion is enabled for the tenant. If document conversion is enabled, Universal Print service converts documents into a format compatible with the printer (xps to pdf) when needed.
    document_conversion_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies settings that affect printer discovery when using Universal Print.
    printer_discovery_settings: Optional[PrinterDiscoverySettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrintSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrintSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrintSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .printer_discovery_settings import PrinterDiscoverySettings

        from .printer_discovery_settings import PrinterDiscoverySettings

        fields: dict[str, Callable[[Any], None]] = {
            "documentConversionEnabled": lambda n : setattr(self, 'document_conversion_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "printerDiscoverySettings": lambda n : setattr(self, 'printer_discovery_settings', n.get_object_value(PrinterDiscoverySettings)),
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
        writer.write_bool_value("documentConversionEnabled", self.document_conversion_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("printerDiscoverySettings", self.printer_discovery_settings)
        writer.write_additional_data_value(self.additional_data)
    

