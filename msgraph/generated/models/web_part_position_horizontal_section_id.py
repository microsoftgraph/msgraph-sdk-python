from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .reference_numeric import ReferenceNumeric

@dataclass
class WebPartPosition_horizontalSectionId(BackedModel, ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes float, ReferenceNumeric, str
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Composed type representation for type float
    double: Optional[float] = None
    # Composed type representation for type ReferenceNumeric
    reference_numeric: Optional[ReferenceNumeric] = None
    # Composed type representation for type str
    string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebPartPosition_horizontalSectionId:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebPartPosition_horizontalSectionId
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("").get_str_value()
        except AttributeError:
            mapping_value = None
        result = WebPartPosition_horizontalSectionId()
        if reference_numeric_value := parse_node.get_enum_value(ReferenceNumeric):
            result.reference_numeric = reference_numeric_value
        elif double_value := parse_node.get_float_value():
            result.double = double_value
        elif string_value := parse_node.get_str_value():
            result.string = string_value
        return result
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .reference_numeric import ReferenceNumeric

        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.reference_numeric:
            writer.write_enum_value(None, self.reference_numeric)
        elif self.double:
            writer.write_float_value(None, self.double)
        elif self.string:
            writer.write_str_value(None, self.string)
    

