from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .permission_type import PermissionType

from .entity import Entity

@dataclass
class PermissionGrantConditionSet(Entity, Parsable):
    # A list of appId values for the client applications to match with, or a list with the single value all to match any client application. Default is the single value all.
    client_application_ids: Optional[list[str]] = None
    # A list of Microsoft Partner Network (MPN) IDs for verified publishers of the client application, or a list with the single value all to match with client apps from any publisher. Default is the single value all.
    client_application_publisher_ids: Optional[list[str]] = None
    # A list of Microsoft Entra tenant IDs in which the client application is registered, or a list with the single value all to match with client apps registered in any tenant. Default is the single value all.
    client_application_tenant_ids: Optional[list[str]] = None
    # Set to true to only match on client applications with a verified publisher. Set to false to match on any client app, even if it doesn't have a verified publisher. Default is false.
    client_applications_from_verified_publisher_only: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The permission classification for the permission being granted, or all to match with any permission classification (including permissions that aren't classified). Default is all.
    permission_classification: Optional[str] = None
    # The permission type of the permission being granted. Possible values: application for application permissions (for example app roles), or delegated for delegated permissions. The value delegatedUserConsentable indicates delegated permissions that haven't been configured by the API publisher to require admin consent—this value may be used in built-in permission grant policies, but can't be used in custom permission grant policies. Required.
    permission_type: Optional[PermissionType] = None
    # The list of id values for the specific permissions to match with, or a list with the single value all to match with any permission. The id of delegated permissions can be found in the oauth2PermissionScopes property of the API's servicePrincipal object. The id of application permissions can be found in the appRoles property of the API's servicePrincipal object. The id of resource-specific application permissions can be found in the resourceSpecificApplicationPermissions property of the API's servicePrincipal object. Default is the single value all.
    permissions: Optional[list[str]] = None
    # The appId of the resource application (for example the API) for which a permission is being granted, or any to match with any resource application or API. Default is any.
    resource_application: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PermissionGrantConditionSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionGrantConditionSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PermissionGrantConditionSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .permission_type import PermissionType

        from .entity import Entity
        from .permission_type import PermissionType

        fields: dict[str, Callable[[Any], None]] = {
            "clientApplicationIds": lambda n : setattr(self, 'client_application_ids', n.get_collection_of_primitive_values(str)),
            "clientApplicationPublisherIds": lambda n : setattr(self, 'client_application_publisher_ids', n.get_collection_of_primitive_values(str)),
            "clientApplicationTenantIds": lambda n : setattr(self, 'client_application_tenant_ids', n.get_collection_of_primitive_values(str)),
            "clientApplicationsFromVerifiedPublisherOnly": lambda n : setattr(self, 'client_applications_from_verified_publisher_only', n.get_bool_value()),
            "permissionClassification": lambda n : setattr(self, 'permission_classification', n.get_str_value()),
            "permissionType": lambda n : setattr(self, 'permission_type', n.get_enum_value(PermissionType)),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_primitive_values(str)),
            "resourceApplication": lambda n : setattr(self, 'resource_application', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("clientApplicationIds", self.client_application_ids)
        writer.write_collection_of_primitive_values("clientApplicationPublisherIds", self.client_application_publisher_ids)
        writer.write_collection_of_primitive_values("clientApplicationTenantIds", self.client_application_tenant_ids)
        writer.write_bool_value("clientApplicationsFromVerifiedPublisherOnly", self.client_applications_from_verified_publisher_only)
        writer.write_str_value("permissionClassification", self.permission_classification)
        writer.write_enum_value("permissionType", self.permission_type)
        writer.write_collection_of_primitive_values("permissions", self.permissions)
        writer.write_str_value("resourceApplication", self.resource_application)
    

