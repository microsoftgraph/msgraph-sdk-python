from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class HlookupPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The lookupValue property
    lookup_value: Optional[json.Json] = None
    # The rangeLookup property
    range_lookup: Optional[json.Json] = None
    # The rowIndexNum property
    row_index_num: Optional[json.Json] = None
    # The tableArray property
    table_array: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HlookupPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HlookupPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HlookupPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "lookupValue": lambda n : setattr(self, 'lookup_value', n.get_object_value(json.Json)),
            "rangeLookup": lambda n : setattr(self, 'range_lookup', n.get_object_value(json.Json)),
            "rowIndexNum": lambda n : setattr(self, 'row_index_num', n.get_object_value(json.Json)),
            "tableArray": lambda n : setattr(self, 'table_array', n.get_object_value(json.Json)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("lookupValue", self.lookup_value)
        writer.write_object_value("rangeLookup", self.range_lookup)
        writer.write_object_value("rowIndexNum", self.row_index_num)
        writer.write_object_value("tableArray", self.table_array)
        writer.write_additional_data_value(self.additional_data)
    

