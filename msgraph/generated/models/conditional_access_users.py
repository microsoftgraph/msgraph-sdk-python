from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_guests_or_external_users import ConditionalAccessGuestsOrExternalUsers

@dataclass
class ConditionalAccessUsers(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Group IDs excluded from scope of policy.
    exclude_groups: Optional[List[str]] = None
    # Internal guests or external users excluded from the policy scope. Optionally populated.
    exclude_guests_or_external_users: Optional[ConditionalAccessGuestsOrExternalUsers] = None
    # Role IDs excluded from scope of policy.
    exclude_roles: Optional[List[str]] = None
    # User IDs excluded from scope of policy and/or GuestsOrExternalUsers.
    exclude_users: Optional[List[str]] = None
    # Group IDs in scope of policy unless explicitly excluded.
    include_groups: Optional[List[str]] = None
    # Internal guests or external users included in the policy scope. Optionally populated.
    include_guests_or_external_users: Optional[ConditionalAccessGuestsOrExternalUsers] = None
    # Role IDs in scope of policy unless explicitly excluded.
    include_roles: Optional[List[str]] = None
    # User IDs in scope of policy unless explicitly excluded, None, All, or GuestsOrExternalUsers.
    include_users: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessUsers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessUsers
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessUsers()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_guests_or_external_users import ConditionalAccessGuestsOrExternalUsers

        from .conditional_access_guests_or_external_users import ConditionalAccessGuestsOrExternalUsers

        fields: Dict[str, Callable[[Any], None]] = {
            "excludeGroups": lambda n : setattr(self, 'exclude_groups', n.get_collection_of_primitive_values(str)),
            "excludeGuestsOrExternalUsers": lambda n : setattr(self, 'exclude_guests_or_external_users', n.get_object_value(ConditionalAccessGuestsOrExternalUsers)),
            "excludeRoles": lambda n : setattr(self, 'exclude_roles', n.get_collection_of_primitive_values(str)),
            "excludeUsers": lambda n : setattr(self, 'exclude_users', n.get_collection_of_primitive_values(str)),
            "includeGroups": lambda n : setattr(self, 'include_groups', n.get_collection_of_primitive_values(str)),
            "includeGuestsOrExternalUsers": lambda n : setattr(self, 'include_guests_or_external_users', n.get_object_value(ConditionalAccessGuestsOrExternalUsers)),
            "includeRoles": lambda n : setattr(self, 'include_roles', n.get_collection_of_primitive_values(str)),
            "includeUsers": lambda n : setattr(self, 'include_users', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("excludeGroups", self.exclude_groups)
        writer.write_object_value("excludeGuestsOrExternalUsers", self.exclude_guests_or_external_users)
        writer.write_collection_of_primitive_values("excludeRoles", self.exclude_roles)
        writer.write_collection_of_primitive_values("excludeUsers", self.exclude_users)
        writer.write_collection_of_primitive_values("includeGroups", self.include_groups)
        writer.write_object_value("includeGuestsOrExternalUsers", self.include_guests_or_external_users)
        writer.write_collection_of_primitive_values("includeRoles", self.include_roles)
        writer.write_collection_of_primitive_values("includeUsers", self.include_users)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

