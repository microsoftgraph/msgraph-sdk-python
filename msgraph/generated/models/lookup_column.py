from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class LookupColumn(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates whether multiple values can be selected from the source.
    allow_multiple_values: Optional[bool] = None
    # Indicates whether values in the column should be able to exceed the standard limit of 255 characters.
    allow_unlimited_length: Optional[bool] = None
    # The name of the lookup source column.
    column_name: Optional[str] = None
    # The unique identifier of the lookup source list.
    list_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If specified, this column is a secondary lookup, pulling an additional field from the list item looked up by the primary lookup. Use the list item looked up by the primary as the source for the column named here.
    primary_lookup_column_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LookupColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LookupColumn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LookupColumn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "allowMultipleValues": lambda n : setattr(self, 'allow_multiple_values', n.get_bool_value()),
            "allowUnlimitedLength": lambda n : setattr(self, 'allow_unlimited_length', n.get_bool_value()),
            "columnName": lambda n : setattr(self, 'column_name', n.get_str_value()),
            "listId": lambda n : setattr(self, 'list_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primaryLookupColumnId": lambda n : setattr(self, 'primary_lookup_column_id', n.get_str_value()),
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
        writer.write_bool_value("allowMultipleValues", self.allow_multiple_values)
        writer.write_bool_value("allowUnlimitedLength", self.allow_unlimited_length)
        writer.write_str_value("columnName", self.column_name)
        writer.write_str_value("listId", self.list_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("primaryLookupColumnId", self.primary_lookup_column_id)
        writer.write_additional_data_value(self.additional_data)
    

