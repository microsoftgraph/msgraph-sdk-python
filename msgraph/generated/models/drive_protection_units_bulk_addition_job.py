from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .protection_units_bulk_job_base import ProtectionUnitsBulkJobBase

from .protection_units_bulk_job_base import ProtectionUnitsBulkJobBase

@dataclass
class DriveProtectionUnitsBulkAdditionJob(ProtectionUnitsBulkJobBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.driveProtectionUnitsBulkAdditionJob"
    # The list of OneDrive directoryObjectIds to add to the OneDrive protection policy.
    directory_object_ids: Optional[list[str]] = None
    # The list of email addresses to add to the OneDrive protection policy.
    drives: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DriveProtectionUnitsBulkAdditionJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DriveProtectionUnitsBulkAdditionJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DriveProtectionUnitsBulkAdditionJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .protection_units_bulk_job_base import ProtectionUnitsBulkJobBase

        from .protection_units_bulk_job_base import ProtectionUnitsBulkJobBase

        fields: dict[str, Callable[[Any], None]] = {
            "directoryObjectIds": lambda n : setattr(self, 'directory_object_ids', n.get_collection_of_primitive_values(str)),
            "drives": lambda n : setattr(self, 'drives', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("directoryObjectIds", self.directory_object_ids)
        writer.write_collection_of_primitive_values("drives", self.drives)
    

