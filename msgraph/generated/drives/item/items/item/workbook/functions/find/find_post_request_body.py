from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class FindPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The findText property
    find_text: Optional[json.Json] = None
    # The startNum property
    start_num: Optional[json.Json] = None
    # The withinText property
    within_text: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FindPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FindPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FindPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "findText": lambda n : setattr(self, 'find_text', n.get_object_value(json.Json)),
            "startNum": lambda n : setattr(self, 'start_num', n.get_object_value(json.Json)),
            "withinText": lambda n : setattr(self, 'within_text', n.get_object_value(json.Json)),
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
        writer.write_object_value("findText", self.find_text)
        writer.write_object_value("startNum", self.start_num)
        writer.write_object_value("withinText", self.within_text)
        writer.write_additional_data_value(self.additional_data)
    

