from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_question = lazy_import('msgraph.generated.models.access_package_question')

class AccessPackageTextInputQuestion(access_package_question.AccessPackageQuestion):
    def __init__(self,) -> None:
        """
        Instantiates a new AccessPackageTextInputQuestion and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.accessPackageTextInputQuestion"
        # Indicates whether the answer will be in single or multiple line format.
        self._is_single_line_question: Optional[bool] = None
        # The regular expression pattern which any answer to this question must match.
        self._regex_pattern: Optional[str] = None
    
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
        fields = {
            "isSingleLineQuestion": lambda n : setattr(self, 'is_single_line_question', n.get_bool_value()),
            "regexPattern": lambda n : setattr(self, 'regex_pattern', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_single_line_question(self,) -> Optional[bool]:
        """
        Gets the isSingleLineQuestion property value. Indicates whether the answer will be in single or multiple line format.
        Returns: Optional[bool]
        """
        return self._is_single_line_question
    
    @is_single_line_question.setter
    def is_single_line_question(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSingleLineQuestion property value. Indicates whether the answer will be in single or multiple line format.
        Args:
            value: Value to set for the is_single_line_question property.
        """
        self._is_single_line_question = value
    
    @property
    def regex_pattern(self,) -> Optional[str]:
        """
        Gets the regexPattern property value. The regular expression pattern which any answer to this question must match.
        Returns: Optional[str]
        """
        return self._regex_pattern
    
    @regex_pattern.setter
    def regex_pattern(self,value: Optional[str] = None) -> None:
        """
        Sets the regexPattern property value. The regular expression pattern which any answer to this question must match.
        Args:
            value: Value to set for the regex_pattern property.
        """
        self._regex_pattern = value
    
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
    

