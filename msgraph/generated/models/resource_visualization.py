from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ResourceVisualization(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # A string describing where the item is stored. For example, the name of a SharePoint site or the user name identifying the owner of the OneDrive storing the item.
    container_display_name: Optional[str] = None
    # Can be used for filtering by the type of container in which the file is stored. Such as Site or OneDriveBusiness.
    container_type: Optional[str] = None
    # A path leading to the folder in which the item is stored.
    container_web_url: Optional[str] = None
    # The item's media type. Can be used for filtering for a specific type of file based on supported IANA Media Mime Types. Not all Media Mime Types are supported.
    media_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A URL leading to the preview image for the item.
    preview_image_url: Optional[str] = None
    # A preview text for the item.
    preview_text: Optional[str] = None
    # The item's title text.
    title: Optional[str] = None
    # The item's media type. Can be used for filtering for a specific file based on a specific type. See the section Type property values for supported types.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResourceVisualization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResourceVisualization
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResourceVisualization()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "containerDisplayName": lambda n : setattr(self, 'container_display_name', n.get_str_value()),
            "containerType": lambda n : setattr(self, 'container_type', n.get_str_value()),
            "containerWebUrl": lambda n : setattr(self, 'container_web_url', n.get_str_value()),
            "mediaType": lambda n : setattr(self, 'media_type', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "previewImageUrl": lambda n : setattr(self, 'preview_image_url', n.get_str_value()),
            "previewText": lambda n : setattr(self, 'preview_text', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("containerDisplayName", self.container_display_name)
        writer.write_str_value("containerType", self.container_type)
        writer.write_str_value("containerWebUrl", self.container_web_url)
        writer.write_str_value("mediaType", self.media_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("previewImageUrl", self.preview_image_url)
        writer.write_str_value("previewText", self.preview_text)
        writer.write_str_value("title", self.title)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

