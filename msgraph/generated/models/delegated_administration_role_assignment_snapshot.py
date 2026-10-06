from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .role_template import RoleTemplate

@dataclass
class DelegatedAdministrationRoleAssignmentSnapshot(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The display name of the security group identified by groupId at the time the snapshot was created. Read-only.
    group_display_name: Optional[str] = None
    # The object ID of the role-assignable security group in the governing tenant that will be assigned the specified roles.
    group_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of role templates that define the Microsoft Entra roles to be assigned.
    role_templates: Optional[list[RoleTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DelegatedAdministrationRoleAssignmentSnapshot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdministrationRoleAssignmentSnapshot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DelegatedAdministrationRoleAssignmentSnapshot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .role_template import RoleTemplate

        from .role_template import RoleTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "groupDisplayName": lambda n : setattr(self, 'group_display_name', n.get_str_value()),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "roleTemplates": lambda n : setattr(self, 'role_templates', n.get_collection_of_object_values(RoleTemplate)),
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
        writer.write_str_value("groupDisplayName", self.group_display_name)
        writer.write_str_value("groupId", self.group_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("roleTemplates", self.role_templates)
        writer.write_additional_data_value(self.additional_data)
    

