from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.security.export_file_structure import ExportFileStructure
    from ........models.security.export_options import ExportOptions

@dataclass
class ExportPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The description property
    description: Optional[str] = None
    # The exportOptions property
    export_options: Optional[ExportOptions] = None
    # The exportStructure property
    export_structure: Optional[ExportFileStructure] = None
    # The outputName property
    output_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExportPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExportPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ........models.security.export_file_structure import ExportFileStructure
        from ........models.security.export_options import ExportOptions

        from ........models.security.export_file_structure import ExportFileStructure
        from ........models.security.export_options import ExportOptions

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "exportOptions": lambda n : setattr(self, 'export_options', n.get_collection_of_enum_values(ExportOptions)),
            "exportStructure": lambda n : setattr(self, 'export_structure', n.get_enum_value(ExportFileStructure)),
            "outputName": lambda n : setattr(self, 'output_name', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_enum_value("exportOptions", self.export_options)
        writer.write_enum_value("exportStructure", self.export_structure)
        writer.write_str_value("outputName", self.output_name)
        writer.write_additional_data_value(self.additional_data)
    

