from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class FolderView(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The method by which the folder should be sorted.
    sort_by: Optional[str] = None
    # If true, indicates that items should be sorted in descending order. Otherwise, items should be sorted ascending.
    sort_order: Optional[str] = None
    # The type of view that should be used to represent the folder.
    view_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FolderView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FolderView
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FolderView()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sortBy": lambda n : setattr(self, 'sort_by', n.get_str_value()),
            "sortOrder": lambda n : setattr(self, 'sort_order', n.get_str_value()),
            "viewType": lambda n : setattr(self, 'view_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sortBy", self.sort_by)
        writer.write_str_value("sortOrder", self.sort_order)
        writer.write_str_value("viewType", self.view_type)
        writer.write_additional_data_value(self.additional_data)
    

