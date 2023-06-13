from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import display_name_localization

@dataclass
class ColumnValidation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Default BCP 47 language tag for the description.
    default_language: Optional[str] = None
    # Localized messages that explain what is needed for this column's value to be considered valid. User will be prompted with this message if validation fails.
    descriptions: Optional[List[display_name_localization.DisplayNameLocalization]] = None
    # The formula to validate column value. For examples, see Examples of common formulas in lists.
    formula: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ColumnValidation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ColumnValidation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ColumnValidation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import display_name_localization

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultLanguage": lambda n : setattr(self, 'default_language', n.get_str_value()),
            "descriptions": lambda n : setattr(self, 'descriptions', n.get_collection_of_object_values(display_name_localization.DisplayNameLocalization)),
            "formula": lambda n : setattr(self, 'formula', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("defaultLanguage", self.default_language)
        writer.write_collection_of_object_values("descriptions", self.descriptions)
        writer.write_str_value("formula", self.formula)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

