from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .subject_set import SubjectSet

@dataclass
class AccessPackageAssignmentRequestorSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
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
    on_behalf_requestors: Optional[List[SubjectSet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentRequestorSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentRequestorSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentRequestorSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .subject_set import SubjectSet

        from .subject_set import SubjectSet

        fields: Dict[str, Callable[[Any], None]] = {
            "allow_custom_assignment_schedule": lambda n : setattr(self, 'allow_custom_assignment_schedule', n.get_bool_value()),
            "enable_on_behalf_requestors_to_add_access": lambda n : setattr(self, 'enable_on_behalf_requestors_to_add_access', n.get_bool_value()),
            "enable_on_behalf_requestors_to_remove_access": lambda n : setattr(self, 'enable_on_behalf_requestors_to_remove_access', n.get_bool_value()),
            "enable_on_behalf_requestors_to_update_access": lambda n : setattr(self, 'enable_on_behalf_requestors_to_update_access', n.get_bool_value()),
            "enable_targets_to_self_add_access": lambda n : setattr(self, 'enable_targets_to_self_add_access', n.get_bool_value()),
            "enable_targets_to_self_remove_access": lambda n : setattr(self, 'enable_targets_to_self_remove_access', n.get_bool_value()),
            "enable_targets_to_self_update_access": lambda n : setattr(self, 'enable_targets_to_self_update_access', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "on_behalf_requestors": lambda n : setattr(self, 'on_behalf_requestors', n.get_collection_of_object_values(SubjectSet)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("allow_custom_assignment_schedule", self.allow_custom_assignment_schedule)
        writer.write_bool_value("enable_on_behalf_requestors_to_add_access", self.enable_on_behalf_requestors_to_add_access)
        writer.write_bool_value("enable_on_behalf_requestors_to_remove_access", self.enable_on_behalf_requestors_to_remove_access)
        writer.write_bool_value("enable_on_behalf_requestors_to_update_access", self.enable_on_behalf_requestors_to_update_access)
        writer.write_bool_value("enable_targets_to_self_add_access", self.enable_targets_to_self_add_access)
        writer.write_bool_value("enable_targets_to_self_remove_access", self.enable_targets_to_self_remove_access)
        writer.write_bool_value("enable_targets_to_self_update_access", self.enable_targets_to_self_update_access)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("on_behalf_requestors", self.on_behalf_requestors)
        writer.write_additional_data_value(self.additional_data)
    

