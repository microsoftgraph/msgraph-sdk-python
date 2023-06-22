from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delegated_admin_access_assignment_status, delegated_admin_access_container, delegated_admin_access_details, entity

from . import entity

@dataclass
class DelegatedAdminAccessAssignment(entity.Entity):
    # The accessContainer property
    access_container: Optional[delegated_admin_access_container.DelegatedAdminAccessContainer] = None
    # The accessDetails property
    access_details: Optional[delegated_admin_access_details.DelegatedAdminAccessDetails] = None
    # The date and time in ISO 8601 format and in UTC time when the access assignment was created. Read-only.
    created_date_time: Optional[datetime] = None
    # The date and time in ISO 8601 and in UTC time when this access assignment was last modified. Read-only.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the access assignment. Read-only. The possible values are: pending, active, deleting, deleted, error, unknownFutureValue.
    status: Optional[delegated_admin_access_assignment_status.DelegatedAdminAccessAssignmentStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DelegatedAdminAccessAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminAccessAssignment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DelegatedAdminAccessAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import delegated_admin_access_assignment_status, delegated_admin_access_container, delegated_admin_access_details, entity

        from . import delegated_admin_access_assignment_status, delegated_admin_access_container, delegated_admin_access_details, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessContainer": lambda n : setattr(self, 'access_container', n.get_object_value(delegated_admin_access_container.DelegatedAdminAccessContainer)),
            "accessDetails": lambda n : setattr(self, 'access_details', n.get_object_value(delegated_admin_access_details.DelegatedAdminAccessDetails)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(delegated_admin_access_assignment_status.DelegatedAdminAccessAssignmentStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("accessContainer", self.access_container)
        writer.write_object_value("accessDetails", self.access_details)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("status", self.status)
    

