from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .case_operation import CaseOperation
    from .report_file_metadata import ReportFileMetadata

from .case_operation import CaseOperation

@dataclass
class EdiscoveryHoldPolicySyncOperation(CaseOperation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains the properties for report file metadata, including downloadUrl, fileName, and size.
    report_file_metadata: Optional[list[ReportFileMetadata]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdiscoveryHoldPolicySyncOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryHoldPolicySyncOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryHoldPolicySyncOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .case_operation import CaseOperation
        from .report_file_metadata import ReportFileMetadata

        from .case_operation import CaseOperation
        from .report_file_metadata import ReportFileMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "reportFileMetadata": lambda n : setattr(self, 'report_file_metadata', n.get_collection_of_object_values(ReportFileMetadata)),
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
        writer.write_collection_of_object_values("reportFileMetadata", self.report_file_metadata)
    

