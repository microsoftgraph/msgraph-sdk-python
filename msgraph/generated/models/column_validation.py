from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .display_name_localization import DisplayNameLocalization

@dataclass
class ColumnValidation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Default BCP 47 language tag for the description.
    default_language: Optional[str] = None
    # Localized messages that explain what is needed for this column's value to be considered valid. User will be prompted with this message if validation fails.
    descriptions: Optional[list[DisplayNameLocalization]] = None
    # The formula to validate column value. For examples, see Examples of common formulas in lists.
    formula: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ColumnValidation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ColumnValidation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ColumnValidation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .display_name_localization import DisplayNameLocalization

        from .display_name_localization import DisplayNameLocalization

        fields: dict[str, Callable[[Any], None]] = {
            "defaultLanguage": lambda n : setattr(self, 'default_language', n.get_str_value()),
            "descriptions": lambda n : setattr(self, 'descriptions', n.get_collection_of_object_values(DisplayNameLocalization)),
            "formula": lambda n : setattr(self, 'formula', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("defaultLanguage", self.default_language)
        writer.write_collection_of_object_values("descriptions", self.descriptions)
        writer.write_str_value("formula", self.formula)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

