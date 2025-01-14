from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_resource_attribute import AccessPackageResourceAttribute
    from .access_package_resource_environment import AccessPackageResourceEnvironment
    from .access_package_resource_role import AccessPackageResourceRole
    from .access_package_resource_scope import AccessPackageResourceScope
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageResource(Entity, Parsable):
    # Contains information about the attributes to be collected from the requestor and sent to the resource application.
    attributes: Optional[list[AccessPackageResourceAttribute]] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # A description for the resource.
    description: Optional[str] = None
    # The display name of the resource, such as the application name, group name or site name.
    display_name: Optional[str] = None
    # Contains the environment information for the resource. This can be set using either the @odata.bind annotation or the environment's originId.Supports $expand.
    environment: Optional[AccessPackageResourceEnvironment] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier of the resource in the origin system. For a Microsoft Entra group, this is the identifier of the group.
    origin_id: Optional[str] = None
    # The type of the resource in the origin system, such as SharePointOnline, AadApplication or AadGroup.
    origin_system: Optional[str] = None
    # Read-only. Nullable. Supports $expand.
    roles: Optional[list[AccessPackageResourceRole]] = None
    # Read-only. Nullable. Supports $expand.
    scopes: Optional[list[AccessPackageResourceScope]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_resource_attribute import AccessPackageResourceAttribute
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .entity import Entity

        from .access_package_resource_attribute import AccessPackageResourceAttribute
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_collection_of_object_values(AccessPackageResourceAttribute)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "environment": lambda n : setattr(self, 'environment', n.get_object_value(AccessPackageResourceEnvironment)),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "originId": lambda n : setattr(self, 'origin_id', n.get_str_value()),
            "originSystem": lambda n : setattr(self, 'origin_system', n.get_str_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_object_values(AccessPackageResourceRole)),
            "scopes": lambda n : setattr(self, 'scopes', n.get_collection_of_object_values(AccessPackageResourceScope)),
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
        writer.write_collection_of_object_values("attributes", self.attributes)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("environment", self.environment)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_str_value("originId", self.origin_id)
        writer.write_str_value("originSystem", self.origin_system)
        writer.write_collection_of_object_values("roles", self.roles)
        writer.write_collection_of_object_values("scopes", self.scopes)
    

