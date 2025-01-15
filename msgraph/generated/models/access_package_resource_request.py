from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_catalog import AccessPackageCatalog
    from .access_package_request_state import AccessPackageRequestState
    from .access_package_request_type import AccessPackageRequestType
    from .access_package_resource import AccessPackageResource
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageResourceRequest(Entity, Parsable):
    # The catalog property
    catalog: Optional[AccessPackageCatalog] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of the request. Use adminAdd to add a resource, if the caller is an administrator or resource owner, adminUpdate to update a resource, or adminRemove to remove a resource.
    request_type: Optional[AccessPackageRequestType] = None
    # The resource property
    resource: Optional[AccessPackageResource] = None
    # The outcome of whether the service was able to add the resource to the catalog. The value is delivered if the resource was added or removed, and deliveryFailed if it couldn't be added or removed. Read-only.
    state: Optional[AccessPackageRequestState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageResourceRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResourceRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_request_state import AccessPackageRequestState
        from .access_package_request_type import AccessPackageRequestType
        from .access_package_resource import AccessPackageResource
        from .entity import Entity

        from .access_package_catalog import AccessPackageCatalog
        from .access_package_request_state import AccessPackageRequestState
        from .access_package_request_type import AccessPackageRequestType
        from .access_package_resource import AccessPackageResource
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "catalog": lambda n : setattr(self, 'catalog', n.get_object_value(AccessPackageCatalog)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "requestType": lambda n : setattr(self, 'request_type', n.get_enum_value(AccessPackageRequestType)),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(AccessPackageResource)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AccessPackageRequestState)),
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
        writer.write_object_value("catalog", self.catalog)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("requestType", self.request_type)
        writer.write_object_value("resource", self.resource)
        writer.write_enum_value("state", self.state)
    

