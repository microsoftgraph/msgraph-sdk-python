from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_localized_text = lazy_import('msgraph.generated.models.access_package_localized_text')
entity = lazy_import('msgraph.generated.models.entity')

class AccessPackageQuestion(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageQuestion and sets the default values.
        """
        super().__init__()
        # Specifies whether the requestor is allowed to edit answers to questions for an assignment by posting an update to accessPackageAssignmentRequest.
        self._is_answer_editable: Optional[bool] = None
        # Whether the requestor is required to supply an answer or not.
        self._is_required: Optional[bool] = None
        # The text of the question represented in a format for a specific locale.
        self._localizations: Optional[List[access_package_localized_text.AccessPackageLocalizedText]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Relative position of this question when displaying a list of questions to the requestor.
        self._sequence: Optional[int] = None
        # The text of the question to show to the requestor.
        self._text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageQuestion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageQuestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "isAnswerEditable": lambda n : setattr(self, 'is_answer_editable', n.get_bool_value()),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(access_package_localized_text.AccessPackageLocalizedText)),
            "sequence": lambda n : setattr(self, 'sequence', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_answer_editable(self,) -> Optional[bool]:
        """
        Gets the isAnswerEditable property value. Specifies whether the requestor is allowed to edit answers to questions for an assignment by posting an update to accessPackageAssignmentRequest.
        Returns: Optional[bool]
        """
        return self._is_answer_editable
    
    @is_answer_editable.setter
    def is_answer_editable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAnswerEditable property value. Specifies whether the requestor is allowed to edit answers to questions for an assignment by posting an update to accessPackageAssignmentRequest.
        Args:
            value: Value to set for the is_answer_editable property.
        """
        self._is_answer_editable = value
    
    @property
    def is_required(self,) -> Optional[bool]:
        """
        Gets the isRequired property value. Whether the requestor is required to supply an answer or not.
        Returns: Optional[bool]
        """
        return self._is_required
    
    @is_required.setter
    def is_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRequired property value. Whether the requestor is required to supply an answer or not.
        Args:
            value: Value to set for the is_required property.
        """
        self._is_required = value
    
    @property
    def localizations(self,) -> Optional[List[access_package_localized_text.AccessPackageLocalizedText]]:
        """
        Gets the localizations property value. The text of the question represented in a format for a specific locale.
        Returns: Optional[List[access_package_localized_text.AccessPackageLocalizedText]]
        """
        return self._localizations
    
    @localizations.setter
    def localizations(self,value: Optional[List[access_package_localized_text.AccessPackageLocalizedText]] = None) -> None:
        """
        Sets the localizations property value. The text of the question represented in a format for a specific locale.
        Args:
            value: Value to set for the localizations property.
        """
        self._localizations = value
    
    @property
    def sequence(self,) -> Optional[int]:
        """
        Gets the sequence property value. Relative position of this question when displaying a list of questions to the requestor.
        Returns: Optional[int]
        """
        return self._sequence
    
    @sequence.setter
    def sequence(self,value: Optional[int] = None) -> None:
        """
        Sets the sequence property value. Relative position of this question when displaying a list of questions to the requestor.
        Args:
            value: Value to set for the sequence property.
        """
        self._sequence = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isAnswerEditable", self.is_answer_editable)
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_collection_of_object_values("localizations", self.localizations)
        writer.write_int_value("sequence", self.sequence)
        writer.write_str_value("text", self.text)
    
    @property
    def text(self,) -> Optional[str]:
        """
        Gets the text property value. The text of the question to show to the requestor.
        Returns: Optional[str]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[str] = None) -> None:
        """
        Sets the text property value. The text of the question to show to the requestor.
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    

