from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .server_processed_content import ServerProcessedContent

@dataclass
class WebPartData(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Data version of the web part. The value is defined by the web part developer. Different dataVersions usually refers to a different property structure.
    data_version: Optional[str] = None
    # Description of the web part.
    description: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains collections of data that can be processed by server side services like search index and link fixup.
    server_processed_content: Optional[ServerProcessedContent] = None
    # Title of the web part.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebPartData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebPartData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebPartData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .server_processed_content import ServerProcessedContent

        from .server_processed_content import ServerProcessedContent

        fields: dict[str, Callable[[Any], None]] = {
            "dataVersion": lambda n : setattr(self, 'data_version', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serverProcessedContent": lambda n : setattr(self, 'server_processed_content', n.get_object_value(ServerProcessedContent)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("dataVersion", self.data_version)
        writer.write_str_value("description", self.description)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("serverProcessedContent", self.server_processed_content)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

