from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .hashes import Hashes

@dataclass
class File(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Hashes of the file's binary content, if available. Read-only.
    hashes: Optional[Hashes] = None
    # The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.
    mime_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The processingMetadata property
    processing_metadata: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> File:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: File
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return File()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .hashes import Hashes

        from .hashes import Hashes

        fields: Dict[str, Callable[[Any], None]] = {
            "hashes": lambda n : setattr(self, 'hashes', n.get_object_value(Hashes)),
            "mimeType": lambda n : setattr(self, 'mime_type', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "processingMetadata": lambda n : setattr(self, 'processing_metadata', n.get_bool_value()),
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
        writer.write_object_value("hashes", self.hashes)
        writer.write_str_value("mimeType", self.mime_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("processingMetadata", self.processing_metadata)
        writer.write_additional_data_value(self.additional_data)
    

