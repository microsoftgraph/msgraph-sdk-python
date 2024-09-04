from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.base_delta_function_response import BaseDeltaFunctionResponse
    from .......models.mail_folder import MailFolder

from .......models.base_delta_function_response import BaseDeltaFunctionResponse

@dataclass
class DeltaGetResponse(BaseDeltaFunctionResponse):
    # The value property
    value: Optional[List[MailFolder]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeltaGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeltaGetResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeltaGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......models.base_delta_function_response import BaseDeltaFunctionResponse
        from .......models.mail_folder import MailFolder

        from .......models.base_delta_function_response import BaseDeltaFunctionResponse
        from .......models.mail_folder import MailFolder

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(MailFolder)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("value", self.value)
    

