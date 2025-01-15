from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .resource_action import ResourceAction

@dataclass
class RolePermission(AdditionalDataHolder, BackedModel, Parsable):
    """
    Contains the set of ResourceActions determining the allowed and not allowed permissions for each role.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Resource Actions each containing a set of allowed and not allowed permissions.
    resource_actions: Optional[list[ResourceAction]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RolePermission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RolePermission
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RolePermission()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .resource_action import ResourceAction

        from .resource_action import ResourceAction

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceActions": lambda n : setattr(self, 'resource_actions', n.get_collection_of_object_values(ResourceAction)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("resourceActions", self.resource_actions)
        writer.write_additional_data_value(self.additional_data)
    

