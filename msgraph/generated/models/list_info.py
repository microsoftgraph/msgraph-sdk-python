from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ListInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # If true, indicates that content types are enabled for this list.
    content_types_enabled: Optional[bool] = None
    # If true, indicates that the list isn't normally visible in the SharePoint user experience.
    hidden: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # An enumerated value that represents the base list template used in creating the list. Possible values include documentLibrary, genericList, task, survey, announcements, contacts, and more.
    template: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "contentTypesEnabled": lambda n : setattr(self, 'content_types_enabled', n.get_bool_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "template": lambda n : setattr(self, 'template', n.get_str_value()),
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
        writer.write_bool_value("contentTypesEnabled", self.content_types_enabled)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("template", self.template)
        writer.write_additional_data_value(self.additional_data)
    

