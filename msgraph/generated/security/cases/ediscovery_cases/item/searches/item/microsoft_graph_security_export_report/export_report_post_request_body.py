from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.security.additional_options import AdditionalOptions
    from ........models.security.export_criteria import ExportCriteria
    from ........models.security.export_location import ExportLocation

@dataclass
class ExportReportPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The additionalOptions property
    additional_options: Optional[AdditionalOptions] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The exportCriteria property
    export_criteria: Optional[ExportCriteria] = None
    # The exportLocation property
    export_location: Optional[ExportLocation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExportReportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExportReportPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExportReportPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.security.additional_options import AdditionalOptions
        from ........models.security.export_criteria import ExportCriteria
        from ........models.security.export_location import ExportLocation

        from ........models.security.additional_options import AdditionalOptions
        from ........models.security.export_criteria import ExportCriteria
        from ........models.security.export_location import ExportLocation

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalOptions": lambda n : setattr(self, 'additional_options', n.get_collection_of_enum_values(AdditionalOptions)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "exportCriteria": lambda n : setattr(self, 'export_criteria', n.get_collection_of_enum_values(ExportCriteria)),
            "exportLocation": lambda n : setattr(self, 'export_location', n.get_collection_of_enum_values(ExportLocation)),
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
        from ........models.security.additional_options import AdditionalOptions
        from ........models.security.export_criteria import ExportCriteria
        from ........models.security.export_location import ExportLocation

        writer.write_enum_value("additionalOptions", self.additional_options)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("exportCriteria", self.export_criteria)
        writer.write_enum_value("exportLocation", self.export_location)
        writer.write_additional_data_value(self.additional_data)
    

