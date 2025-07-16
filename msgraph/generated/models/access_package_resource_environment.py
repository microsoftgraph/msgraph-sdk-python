from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_resource import AccessPackageResource
    from .connection_info import ConnectionInfo
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageResourceEnvironment(Entity, Parsable):
    # Connection information of an environment used to connect to a resource.
    connection_info: Optional[ConnectionInfo] = None
    # The date and time that this object was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The description of this object.
    description: Optional[str] = None
    # The display name of this object.
    display_name: Optional[str] = None
    # Determines whether this is default environment or not. It is set to true for all static origin systems, such as Microsoft Entra groups and Microsoft Entra Applications.
    is_default_environment: Optional[bool] = None
    # The date and time that this object was last modified. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier of this environment in the origin system.
    origin_id: Optional[str] = None
    # The type of the resource in the origin system, that is, SharePointOnline. Requires $filter (eq).
    origin_system: Optional[str] = None
    # Read-only. Required.
    resources: Optional[list[AccessPackageResource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageResourceEnvironment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceEnvironment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResourceEnvironment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_resource import AccessPackageResource
        from .connection_info import ConnectionInfo
        from .entity import Entity

        from .access_package_resource import AccessPackageResource
        from .connection_info import ConnectionInfo
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "connectionInfo": lambda n : setattr(self, 'connection_info', n.get_object_value(ConnectionInfo)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isDefaultEnvironment": lambda n : setattr(self, 'is_default_environment', n.get_bool_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "originId": lambda n : setattr(self, 'origin_id', n.get_str_value()),
            "originSystem": lambda n : setattr(self, 'origin_system', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(AccessPackageResource)),
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
        writer.write_object_value("connectionInfo", self.connection_info)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isDefaultEnvironment", self.is_default_environment)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_str_value("originId", self.origin_id)
        writer.write_str_value("originSystem", self.origin_system)
        writer.write_collection_of_object_values("resources", self.resources)
    

