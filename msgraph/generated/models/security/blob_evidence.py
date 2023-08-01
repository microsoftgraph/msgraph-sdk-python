from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .blob_container_evidence import BlobContainerEvidence
    from .file_hash import FileHash

from .alert_evidence import AlertEvidence

@dataclass
class BlobEvidence(AlertEvidence):
    odata_type = "#microsoft.graph.security.blobEvidence"
    # The blobContainer property
    blob_container: Optional[BlobContainerEvidence] = None
    # The etag property
    etag: Optional[str] = None
    # The fileHashes property
    file_hashes: Optional[List[FileHash]] = None
    # The name property
    name: Optional[str] = None
    # The url property
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BlobEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BlobEvidence
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BlobEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .blob_container_evidence import BlobContainerEvidence
        from .file_hash import FileHash

        from .alert_evidence import AlertEvidence
        from .blob_container_evidence import BlobContainerEvidence
        from .file_hash import FileHash

        fields: Dict[str, Callable[[Any], None]] = {
            "blobContainer": lambda n : setattr(self, 'blob_container', n.get_object_value(BlobContainerEvidence)),
            "etag": lambda n : setattr(self, 'etag', n.get_str_value()),
            "fileHashes": lambda n : setattr(self, 'file_hashes', n.get_collection_of_object_values(FileHash)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("blobContainer", self.blob_container)
        writer.write_str_value("etag", self.etag)
        writer.write_collection_of_object_values("fileHashes", self.file_hashes)
        writer.write_str_value("name", self.name)
        writer.write_str_value("url", self.url)
    

