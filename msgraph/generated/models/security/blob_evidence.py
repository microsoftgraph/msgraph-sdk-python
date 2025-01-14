from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .blob_container_evidence import BlobContainerEvidence
    from .file_hash import FileHash

from .alert_evidence import AlertEvidence

@dataclass
class BlobEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.blobEvidence"
    # The container which the blob belongs to.
    blob_container: Optional[BlobContainerEvidence] = None
    # The Etag associated with this blob.
    etag: Optional[str] = None
    # The file hashes associated with this blob.
    file_hashes: Optional[list[FileHash]] = None
    # The name of the blob.
    name: Optional[str] = None
    # The full URL representation of the blob.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BlobEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BlobEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BlobEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .blob_container_evidence import BlobContainerEvidence
        from .file_hash import FileHash

        from .alert_evidence import AlertEvidence
        from .blob_container_evidence import BlobContainerEvidence
        from .file_hash import FileHash

        fields: dict[str, Callable[[Any], None]] = {
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("blobContainer", self.blob_container)
        writer.write_str_value("etag", self.etag)
        writer.write_collection_of_object_values("fileHashes", self.file_hashes)
        writer.write_str_value("name", self.name)
        writer.write_str_value("url", self.url)
    

