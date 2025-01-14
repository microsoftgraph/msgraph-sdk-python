from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .subject_set import SubjectSet

@dataclass
class AccessPackageAssignmentRequestorSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # False indicates that the requestor isn't permitted to include a schedule in their request.
    allow_custom_assignment_schedule: Optional[bool] = None
    # True allows on-behalf-of requestors to create a request to add access for another principal.
    enable_on_behalf_requestors_to_add_access: Optional[bool] = None
    # True allows on-behalf-of requestors to create a request to remove access for another principal.
    enable_on_behalf_requestors_to_remove_access: Optional[bool] = None
    # True allows on-behalf-of requestors to create a request to update access for another principal.
    enable_on_behalf_requestors_to_update_access: Optional[bool] = None
    # True allows requestors to create a request to add access for themselves.
    enable_targets_to_self_add_access: Optional[bool] = None
    # True allows requestors to create a request to remove their access.
    enable_targets_to_self_remove_access: Optional[bool] = None
    # True allows requestors to create a request to update their access.
    enable_targets_to_self_update_access: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The principals who can request on-behalf-of others.
    on_behalf_requestors: Optional[list[SubjectSet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAssignmentRequestorSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentRequestorSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentRequestorSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .subject_set import SubjectSet

        from .subject_set import SubjectSet

        fields: dict[str, Callable[[Any], None]] = {
            "allowCustomAssignmentSchedule": lambda n : setattr(self, 'allow_custom_assignment_schedule', n.get_bool_value()),
            "enableOnBehalfRequestorsToAddAccess": lambda n : setattr(self, 'enable_on_behalf_requestors_to_add_access', n.get_bool_value()),
            "enableOnBehalfRequestorsToRemoveAccess": lambda n : setattr(self, 'enable_on_behalf_requestors_to_remove_access', n.get_bool_value()),
            "enableOnBehalfRequestorsToUpdateAccess": lambda n : setattr(self, 'enable_on_behalf_requestors_to_update_access', n.get_bool_value()),
            "enableTargetsToSelfAddAccess": lambda n : setattr(self, 'enable_targets_to_self_add_access', n.get_bool_value()),
            "enableTargetsToSelfRemoveAccess": lambda n : setattr(self, 'enable_targets_to_self_remove_access', n.get_bool_value()),
            "enableTargetsToSelfUpdateAccess": lambda n : setattr(self, 'enable_targets_to_self_update_access', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "onBehalfRequestors": lambda n : setattr(self, 'on_behalf_requestors', n.get_collection_of_object_values(SubjectSet)),
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
        writer.write_bool_value("allowCustomAssignmentSchedule", self.allow_custom_assignment_schedule)
        writer.write_bool_value("enableOnBehalfRequestorsToAddAccess", self.enable_on_behalf_requestors_to_add_access)
        writer.write_bool_value("enableOnBehalfRequestorsToRemoveAccess", self.enable_on_behalf_requestors_to_remove_access)
        writer.write_bool_value("enableOnBehalfRequestorsToUpdateAccess", self.enable_on_behalf_requestors_to_update_access)
        writer.write_bool_value("enableTargetsToSelfAddAccess", self.enable_targets_to_self_add_access)
        writer.write_bool_value("enableTargetsToSelfRemoveAccess", self.enable_targets_to_self_remove_access)
        writer.write_bool_value("enableTargetsToSelfUpdateAccess", self.enable_targets_to_self_update_access)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("onBehalfRequestors", self.on_behalf_requestors)
        writer.write_additional_data_value(self.additional_data)
    

