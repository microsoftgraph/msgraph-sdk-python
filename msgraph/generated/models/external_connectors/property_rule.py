from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..binary_operator import BinaryOperator
    from .rule_operation import RuleOperation

@dataclass
class PropertyRule(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The operation property
    operation: Optional[RuleOperation] = None
    # The property from the externalItem schema. Required.
    property_: Optional[str] = None
    # A collection with one or many strings. One or more specified strings are matched with the specified property using the specified operation. Required.
    values: Optional[list[str]] = None
    # The valuesJoinedBy property
    values_joined_by: Optional[BinaryOperator] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PropertyRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PropertyRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PropertyRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..binary_operator import BinaryOperator
        from .rule_operation import RuleOperation

        from ..binary_operator import BinaryOperator
        from .rule_operation import RuleOperation

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operation": lambda n : setattr(self, 'operation', n.get_enum_value(RuleOperation)),
            "property": lambda n : setattr(self, 'property_', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_collection_of_primitive_values(str)),
            "valuesJoinedBy": lambda n : setattr(self, 'values_joined_by', n.get_enum_value(BinaryOperator)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("operation", self.operation)
        writer.write_str_value("property", self.property_)
        writer.write_collection_of_primitive_values("values", self.values)
        writer.write_enum_value("valuesJoinedBy", self.values_joined_by)
        writer.write_additional_data_value(self.additional_data)
    

