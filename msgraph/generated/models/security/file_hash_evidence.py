from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .file_hash_algorithm import FileHashAlgorithm

from .alert_evidence import AlertEvidence

@dataclass
class FileHashEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.fileHashEvidence"
    # The algorithm property
    algorithm: Optional[FileHashAlgorithm] = None
    # The value property
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileHashEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileHashEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileHashEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .file_hash_algorithm import FileHashAlgorithm

        from .alert_evidence import AlertEvidence
        from .file_hash_algorithm import FileHashAlgorithm

        fields: Dict[str, Callable[[Any], None]] = {
            "algorithm": lambda n : setattr(self, 'algorithm', n.get_enum_value(FileHashAlgorithm)),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_enum_value("algorithm", self.algorithm)
        writer.write_str_value("value", self.value)
    

