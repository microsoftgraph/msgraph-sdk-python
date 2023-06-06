from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_question

from . import access_package_question

@dataclass
class AccessPackageTextInputQuestion(access_package_question.AccessPackageQuestion):
    odata_type = "#microsoft.graph.accessPackageTextInputQuestion"
    # Indicates whether the answer will be in single or multiple line format.
    is_single_line_question: Optional[bool] = None
    # The regular expression pattern which any answer to this question must match.
    regex_pattern: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageTextInputQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageTextInputQuestion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageTextInputQuestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_question

        fields: Dict[str, Callable[[Any], None]] = {
            "isSingleLineQuestion": lambda n : setattr(self, 'is_single_line_question', n.get_bool_value()),
            "regexPattern": lambda n : setattr(self, 'regex_pattern', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isSingleLineQuestion", self.is_single_line_question)
        writer.write_str_value("regexPattern", self.regex_pattern)
    

