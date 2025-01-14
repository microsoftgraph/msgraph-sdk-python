from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delegated_admin_access_assignment_status import DelegatedAdminAccessAssignmentStatus
    from .delegated_admin_access_container import DelegatedAdminAccessContainer
    from .delegated_admin_access_details import DelegatedAdminAccessDetails
    from .entity import Entity

from .entity import Entity

@dataclass
class DelegatedAdminAccessAssignment(Entity, Parsable):
    # The accessContainer property
    access_container: Optional[DelegatedAdminAccessContainer] = None
    # The accessDetails property
    access_details: Optional[DelegatedAdminAccessDetails] = None
    # The date and time in ISO 8601 format and in UTC time when the access assignment was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time in ISO 8601 and in UTC time when this access assignment was last modified. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the access assignment. Read-only. The possible values are: pending, active, deleting, deleted, error, unknownFutureValue.
    status: Optional[DelegatedAdminAccessAssignmentStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DelegatedAdminAccessAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminAccessAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DelegatedAdminAccessAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delegated_admin_access_assignment_status import DelegatedAdminAccessAssignmentStatus
        from .delegated_admin_access_container import DelegatedAdminAccessContainer
        from .delegated_admin_access_details import DelegatedAdminAccessDetails
        from .entity import Entity

        from .delegated_admin_access_assignment_status import DelegatedAdminAccessAssignmentStatus
        from .delegated_admin_access_container import DelegatedAdminAccessContainer
        from .delegated_admin_access_details import DelegatedAdminAccessDetails
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "accessContainer": lambda n : setattr(self, 'access_container', n.get_object_value(DelegatedAdminAccessContainer)),
            "accessDetails": lambda n : setattr(self, 'access_details', n.get_object_value(DelegatedAdminAccessDetails)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DelegatedAdminAccessAssignmentStatus)),
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
        writer.write_object_value("accessContainer", self.access_container)
        writer.write_object_value("accessDetails", self.access_details)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("status", self.status)
    

