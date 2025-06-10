from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.item_reference import ItemReference

@dataclass
class CopyPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The childrenOnly property
    children_only: Optional[bool] = None
    # The includeAllVersionHistory property
    include_all_version_history: Optional[bool] = None
    # The name property
    name: Optional[str] = None
    # The parentReference property
    parent_reference: Optional[ItemReference] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopyPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopyPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopyPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.item_reference import ItemReference

        from ......models.item_reference import ItemReference

        fields: dict[str, Callable[[Any], None]] = {
            "childrenOnly": lambda n : setattr(self, 'children_only', n.get_bool_value()),
            "includeAllVersionHistory": lambda n : setattr(self, 'include_all_version_history', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parentReference": lambda n : setattr(self, 'parent_reference', n.get_object_value(ItemReference)),
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
        writer.write_bool_value("childrenOnly", self.children_only)
        writer.write_bool_value("includeAllVersionHistory", self.include_all_version_history)
        writer.write_str_value("name", self.name)
        writer.write_object_value("parentReference", self.parent_reference)
        writer.write_additional_data_value(self.additional_data)
    

