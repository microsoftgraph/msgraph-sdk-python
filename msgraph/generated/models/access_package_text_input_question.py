from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_question import AccessPackageQuestion

from .access_package_question import AccessPackageQuestion

@dataclass
class AccessPackageTextInputQuestion(AccessPackageQuestion, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessPackageTextInputQuestion"
    # Indicates whether the answer is in single or multiple line format.
    is_single_line_question: Optional[bool] = None
    # The regular expression pattern that any answer to this question must match.
    regex_pattern: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageTextInputQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageTextInputQuestion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageTextInputQuestion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_question import AccessPackageQuestion

        from .access_package_question import AccessPackageQuestion

        fields: dict[str, Callable[[Any], None]] = {
            "isSingleLineQuestion": lambda n : setattr(self, 'is_single_line_question', n.get_bool_value()),
            "regexPattern": lambda n : setattr(self, 'regex_pattern', n.get_str_value()),
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
        writer.write_bool_value("isSingleLineQuestion", self.is_single_line_question)
        writer.write_str_value("regexPattern", self.regex_pattern)
    

