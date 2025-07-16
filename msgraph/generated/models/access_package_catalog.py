from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package import AccessPackage
    from .access_package_catalog_state import AccessPackageCatalogState
    from .access_package_catalog_type import AccessPackageCatalogType
    from .access_package_resource import AccessPackageResource
    from .access_package_resource_role import AccessPackageResourceRole
    from .access_package_resource_scope import AccessPackageResourceScope
    from .custom_callout_extension import CustomCalloutExtension
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageCatalog(Entity, Parsable):
    # The access packages in this catalog. Read-only. Nullable.
    access_packages: Optional[list[AccessPackage]] = None
    # Whether the catalog is created by a user or entitlement management. The possible values are: userManaged, serviceDefault, serviceManaged, unknownFutureValue.
    catalog_type: Optional[AccessPackageCatalogType] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The customWorkflowExtensions property
    custom_workflow_extensions: Optional[list[CustomCalloutExtension]] = None
    # The description of the access package catalog.
    description: Optional[str] = None
    # The display name of the access package catalog.
    display_name: Optional[str] = None
    # Whether the access packages in this catalog can be requested by users outside of the tenant.
    is_externally_visible: Optional[bool] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceRoles property
    resource_roles: Optional[list[AccessPackageResourceRole]] = None
    # The resourceScopes property
    resource_scopes: Optional[list[AccessPackageResourceScope]] = None
    # Access package resources in this catalog.
    resources: Optional[list[AccessPackageResource]] = None
    # Has the value published if the access packages are available for management. The possible values are: unpublished, published, unknownFutureValue.
    state: Optional[AccessPackageCatalogState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageCatalog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageCatalog
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageCatalog()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package import AccessPackage
        from .access_package_catalog_state import AccessPackageCatalogState
        from .access_package_catalog_type import AccessPackageCatalogType
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .custom_callout_extension import CustomCalloutExtension
        from .entity import Entity

        from .access_package import AccessPackage
        from .access_package_catalog_state import AccessPackageCatalogState
        from .access_package_catalog_type import AccessPackageCatalogType
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .custom_callout_extension import CustomCalloutExtension
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackages": lambda n : setattr(self, 'access_packages', n.get_collection_of_object_values(AccessPackage)),
            "catalogType": lambda n : setattr(self, 'catalog_type', n.get_enum_value(AccessPackageCatalogType)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customWorkflowExtensions": lambda n : setattr(self, 'custom_workflow_extensions', n.get_collection_of_object_values(CustomCalloutExtension)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isExternallyVisible": lambda n : setattr(self, 'is_externally_visible', n.get_bool_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "resourceRoles": lambda n : setattr(self, 'resource_roles', n.get_collection_of_object_values(AccessPackageResourceRole)),
            "resourceScopes": lambda n : setattr(self, 'resource_scopes', n.get_collection_of_object_values(AccessPackageResourceScope)),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(AccessPackageResource)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AccessPackageCatalogState)),
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
        writer.write_collection_of_object_values("accessPackages", self.access_packages)
        writer.write_enum_value("catalogType", self.catalog_type)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("customWorkflowExtensions", self.custom_workflow_extensions)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isExternallyVisible", self.is_externally_visible)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_collection_of_object_values("resourceRoles", self.resource_roles)
        writer.write_collection_of_object_values("resourceScopes", self.resource_scopes)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_enum_value("state", self.state)
    

