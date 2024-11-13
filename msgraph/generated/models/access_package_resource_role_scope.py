from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_resource_role import AccessPackageResourceRole
    from .access_package_resource_scope import AccessPackageResourceScope
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageResourceRoleScope(Entity, Parsable):
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The role property
    role: Optional[AccessPackageResourceRole] = None
    # The scope property
    scope: Optional[AccessPackageResourceScope] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageResourceRoleScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceRoleScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResourceRoleScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .entity import Entity

        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "role": lambda n : setattr(self, 'role', n.get_object_value(AccessPackageResourceRole)),
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(AccessPackageResourceScope)),
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
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .entity import Entity

        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("role", self.role)
        writer.write_object_value("scope", self.scope)
    

