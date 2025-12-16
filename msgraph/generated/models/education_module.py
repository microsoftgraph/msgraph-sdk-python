from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_module_resource import EducationModuleResource
    from .education_module_status import EducationModuleStatus
    from .entity import Entity
    from .identity_set import IdentitySet

from .entity import Entity

@dataclass
class EducationModule(Entity, Parsable):
    # The display name of the user that created the module.
    created_by: Optional[IdentitySet] = None
    # Date time the module was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime.datetime] = None
    # Description of the module.
    description: Optional[str] = None
    # Name of the module.
    display_name: Optional[str] = None
    # Indicates whether the module is pinned or not.
    is_pinned: Optional[bool] = None
    # The last user that modified the module.
    last_modified_by: Optional[IdentitySet] = None
    # Date time the module was last modified. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Learning objects that are associated with this module. Only teachers can modify this list. Nullable.
    resources: Optional[list[EducationModuleResource]] = None
    # Folder URL where all the file resources for this module are stored.
    resources_folder_url: Optional[str] = None
    # Status of the module. You can't use a PATCH operation to update this value. The possible values are: draft and published.
    status: Optional[EducationModuleStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationModule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationModule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationModule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_module_resource import EducationModuleResource
        from .education_module_status import EducationModuleStatus
        from .entity import Entity
        from .identity_set import IdentitySet

        from .education_module_resource import EducationModuleResource
        from .education_module_status import EducationModuleStatus
        from .entity import Entity
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isPinned": lambda n : setattr(self, 'is_pinned', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(EducationModuleResource)),
            "resourcesFolderUrl": lambda n : setattr(self, 'resources_folder_url', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(EducationModuleStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isPinned", self.is_pinned)
        writer.write_collection_of_object_values("resources", self.resources)
    

