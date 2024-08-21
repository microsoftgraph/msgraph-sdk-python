from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ImageInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Optional; parameter used to indicate the server is able to render image dynamically in response to parameterization. For example – a high contrast image
    add_image_query: Optional[bool] = None
    # Optional; alt-text accessible content for the image
    alternate_text: Optional[str] = None
    # The alternativeText property
    alternative_text: Optional[str] = None
    # Optional; URI that points to an icon which represents the application used to generate the activity
    icon_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImageInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImageInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ImageInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "addImageQuery": lambda n : setattr(self, 'add_image_query', n.get_bool_value()),
            "alternateText": lambda n : setattr(self, 'alternate_text', n.get_str_value()),
            "alternativeText": lambda n : setattr(self, 'alternative_text', n.get_str_value()),
            "iconUrl": lambda n : setattr(self, 'icon_url', n.get_str_value()),
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
        writer.write_bool_value("addImageQuery", self.add_image_query)
        writer.write_str_value("alternateText", self.alternate_text)
        writer.write_str_value("alternativeText", self.alternative_text)
        writer.write_str_value("iconUrl", self.icon_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

