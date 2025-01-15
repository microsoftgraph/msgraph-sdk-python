from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WebPartPosition(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates the identifier of the column where the web part is located.
    column_id: Optional[float] = None
    # Indicates the horizontal section where the web part is located.
    horizontal_section_id: Optional[float] = None
    # Indicates whether the web part is located in the vertical section.
    is_in_vertical_section: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Index of the current web part. Represents the order of the web part in this column or section.
    web_part_index: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebPartPosition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebPartPosition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebPartPosition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "columnId": lambda n : setattr(self, 'column_id', n.get_float_value()),
            "horizontalSectionId": lambda n : setattr(self, 'horizontal_section_id', n.get_float_value()),
            "isInVerticalSection": lambda n : setattr(self, 'is_in_vertical_section', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "webPartIndex": lambda n : setattr(self, 'web_part_index', n.get_float_value()),
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
        writer.write_float_value("columnId", self.column_id)
        writer.write_float_value("horizontalSectionId", self.horizontal_section_id)
        writer.write_bool_value("isInVerticalSection", self.is_in_vertical_section)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("webPartIndex", self.web_part_index)
        writer.write_additional_data_value(self.additional_data)
    

