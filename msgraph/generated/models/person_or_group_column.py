from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PersonOrGroupColumn(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates whether multiple values can be selected from the source.
    allow_multiple_selection: Optional[bool] = None
    # Whether to allow selection of people only, or people and groups. Must be one of peopleAndGroups or peopleOnly.
    choose_from_type: Optional[str] = None
    # How to display the information about the person or group chosen. See below.
    display_as: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PersonOrGroupColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PersonOrGroupColumn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PersonOrGroupColumn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowMultipleSelection": lambda n : setattr(self, 'allow_multiple_selection', n.get_bool_value()),
            "chooseFromType": lambda n : setattr(self, 'choose_from_type', n.get_str_value()),
            "displayAs": lambda n : setattr(self, 'display_as', n.get_str_value()),
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
        writer.write_bool_value("allowMultipleSelection", self.allow_multiple_selection)
        writer.write_str_value("chooseFromType", self.choose_from_type)
        writer.write_str_value("displayAs", self.display_as)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

