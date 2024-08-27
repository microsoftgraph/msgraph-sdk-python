from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class MacOSLobChildApp(AdditionalDataHolder, BackedModel, Parsable):
    """
    Contains properties of a macOS .app in the package
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The build number of the app.
    build_number: Optional[str] = None
    # The bundleId of the app.
    bundle_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The version number of the app.
    version_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSLobChildApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSLobChildApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSLobChildApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "buildNumber": lambda n : setattr(self, 'build_number', n.get_str_value()),
            "bundleId": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "versionNumber": lambda n : setattr(self, 'version_number', n.get_str_value()),
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
        writer.write_str_value("buildNumber", self.build_number)
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("versionNumber", self.version_number)
        writer.write_additional_data_value(self.additional_data)
    

