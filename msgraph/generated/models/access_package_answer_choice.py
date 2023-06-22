from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_localized_text

@dataclass
class AccessPackageAnswerChoice(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The actual value of the selected choice. This is typically a string value which is understandable by applications. Required.
    actual_value: Optional[str] = None
    # The text of the answer choice represented in a format for a specific locale.
    localizations: Optional[List[access_package_localized_text.AccessPackageLocalizedText]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The text property
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAnswerChoice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAnswerChoice
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAnswerChoice()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_localized_text

        from . import access_package_localized_text

        fields: Dict[str, Callable[[Any], None]] = {
            "actualValue": lambda n : setattr(self, 'actual_value', n.get_str_value()),
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(access_package_localized_text.AccessPackageLocalizedText)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_str_value("actualValue", self.actual_value)
        writer.write_collection_of_object_values("localizations", self.localizations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    

