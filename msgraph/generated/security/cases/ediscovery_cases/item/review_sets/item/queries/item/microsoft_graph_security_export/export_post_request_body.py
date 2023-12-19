from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .export_post_request_body_export_options import ExportPostRequestBody_exportOptions
    from .export_post_request_body_export_structure import ExportPostRequestBody_exportStructure

@dataclass
class ExportPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The description property
    description: Optional[str] = None
    # The exportOptions property
    export_options: Optional[ExportPostRequestBody_exportOptions] = None
    # The exportStructure property
    export_structure: Optional[ExportPostRequestBody_exportStructure] = None
    # The outputName property
    output_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExportPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ExportPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .export_post_request_body_export_options import ExportPostRequestBody_exportOptions
        from .export_post_request_body_export_structure import ExportPostRequestBody_exportStructure

        from .export_post_request_body_export_options import ExportPostRequestBody_exportOptions
        from .export_post_request_body_export_structure import ExportPostRequestBody_exportStructure

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "exportOptions": lambda n : setattr(self, 'export_options', n.get_enum_value(ExportPostRequestBody_exportOptions)),
            "exportStructure": lambda n : setattr(self, 'export_structure', n.get_enum_value(ExportPostRequestBody_exportStructure)),
            "outputName": lambda n : setattr(self, 'output_name', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("description", self.description)
        writer.write_enum_value("exportOptions", self.export_options)
        writer.write_enum_value("exportStructure", self.export_structure)
        writer.write_str_value("outputName", self.output_name)
        writer.write_additional_data_value(self.additional_data)
    

