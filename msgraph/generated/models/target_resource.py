from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_type import GroupType
    from .modified_property import ModifiedProperty

@dataclass
class TargetResource(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates the visible name defined for the resource. Typically specified when the resource is created.
    display_name: Optional[str] = None
    # When type is set to Group, this indicates the group type. The possible values are: unifiedGroups, azureAD, and unknownFutureValue
    group_type: Optional[GroupType] = None
    # Indicates the unique ID of the resource.
    id: Optional[str] = None
    # Indicates name, old value and new value of each attribute that changed. Property values depend on the operation type.
    modified_properties: Optional[list[ModifiedProperty]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Describes the resource type.  Example values include Application, Group, ServicePrincipal, and User.
    type: Optional[str] = None
    # When type is set to User, this includes the user name that initiated the action; null for other types.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TargetResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TargetResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TargetResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .group_type import GroupType
        from .modified_property import ModifiedProperty

        from .group_type import GroupType
        from .modified_property import ModifiedProperty

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "groupType": lambda n : setattr(self, 'group_type', n.get_enum_value(GroupType)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "modifiedProperties": lambda n : setattr(self, 'modified_properties', n.get_collection_of_object_values(ModifiedProperty)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("groupType", self.group_type)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_object_values("modifiedProperties", self.modified_properties)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("type", self.type)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

