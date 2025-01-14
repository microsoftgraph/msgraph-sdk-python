from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_answer import AccessPackageAnswer

from .access_package_answer import AccessPackageAnswer

@dataclass
class AccessPackageAnswerString(AccessPackageAnswer, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessPackageAnswerString"
    # The value stored on the requestor's user profile, if this answer is configured to be stored as a specific attribute.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAnswerString:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAnswerString
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAnswerString()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_answer import AccessPackageAnswer

        from .access_package_answer import AccessPackageAnswer

        fields: dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("value", self.value)
    

