from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
permission_type = lazy_import('msgraph.generated.models.permission_type')

class PermissionGrantConditionSet(entity.Entity):
    """
    Provides operations to manage the collection of application entities.
    """
    @property
    def client_application_ids(self,) -> Optional[List[str]]:
        """
        Gets the clientApplicationIds property value. A list of appId values for the client applications to match with, or a list with the single value all to match any client application. Default is the single value all.
        Returns: Optional[List[str]]
        """
        return self._client_application_ids
    
    @client_application_ids.setter
    def client_application_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the clientApplicationIds property value. A list of appId values for the client applications to match with, or a list with the single value all to match any client application. Default is the single value all.
        Args:
            value: Value to set for the clientApplicationIds property.
        """
        self._client_application_ids = value
    
    @property
    def client_application_publisher_ids(self,) -> Optional[List[str]]:
        """
        Gets the clientApplicationPublisherIds property value. A list of Microsoft Partner Network (MPN) IDs for verified publishers of the client application, or a list with the single value all to match with client apps from any publisher. Default is the single value all.
        Returns: Optional[List[str]]
        """
        return self._client_application_publisher_ids
    
    @client_application_publisher_ids.setter
    def client_application_publisher_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the clientApplicationPublisherIds property value. A list of Microsoft Partner Network (MPN) IDs for verified publishers of the client application, or a list with the single value all to match with client apps from any publisher. Default is the single value all.
        Args:
            value: Value to set for the clientApplicationPublisherIds property.
        """
        self._client_application_publisher_ids = value
    
    @property
    def client_applications_from_verified_publisher_only(self,) -> Optional[bool]:
        """
        Gets the clientApplicationsFromVerifiedPublisherOnly property value. Set to true to only match on client applications with a verified publisher. Set to false to match on any client app, even if it does not have a verified publisher. Default is false.
        Returns: Optional[bool]
        """
        return self._client_applications_from_verified_publisher_only
    
    @client_applications_from_verified_publisher_only.setter
    def client_applications_from_verified_publisher_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the clientApplicationsFromVerifiedPublisherOnly property value. Set to true to only match on client applications with a verified publisher. Set to false to match on any client app, even if it does not have a verified publisher. Default is false.
        Args:
            value: Value to set for the clientApplicationsFromVerifiedPublisherOnly property.
        """
        self._client_applications_from_verified_publisher_only = value
    
    @property
    def client_application_tenant_ids(self,) -> Optional[List[str]]:
        """
        Gets the clientApplicationTenantIds property value. A list of Azure Active Directory tenant IDs in which the client application is registered, or a list with the single value all to match with client apps registered in any tenant. Default is the single value all.
        Returns: Optional[List[str]]
        """
        return self._client_application_tenant_ids
    
    @client_application_tenant_ids.setter
    def client_application_tenant_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the clientApplicationTenantIds property value. A list of Azure Active Directory tenant IDs in which the client application is registered, or a list with the single value all to match with client apps registered in any tenant. Default is the single value all.
        Args:
            value: Value to set for the clientApplicationTenantIds property.
        """
        self._client_application_tenant_ids = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new permissionGrantConditionSet and sets the default values.
        """
        super().__init__()
        # A list of appId values for the client applications to match with, or a list with the single value all to match any client application. Default is the single value all.
        self._client_application_ids: Optional[List[str]] = None
        # A list of Microsoft Partner Network (MPN) IDs for verified publishers of the client application, or a list with the single value all to match with client apps from any publisher. Default is the single value all.
        self._client_application_publisher_ids: Optional[List[str]] = None
        # Set to true to only match on client applications with a verified publisher. Set to false to match on any client app, even if it does not have a verified publisher. Default is false.
        self._client_applications_from_verified_publisher_only: Optional[bool] = None
        # A list of Azure Active Directory tenant IDs in which the client application is registered, or a list with the single value all to match with client apps registered in any tenant. Default is the single value all.
        self._client_application_tenant_ids: Optional[List[str]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The permission classification for the permission being granted, or all to match with any permission classification (including permissions which are not classified). Default is all.
        self._permission_classification: Optional[str] = None
        # The list of id values for the specific permissions to match with, or a list with the single value all to match with any permission. The id of delegated permissions can be found in the oauth2PermissionScopes property of the API's **servicePrincipal** object. The id of application permissions can be found in the appRoles property of the API's **servicePrincipal** object. The id of resource-specific application permissions can be found in the resourceSpecificApplicationPermissions property of the API's **servicePrincipal** object. Default is the single value all.
        self._permissions: Optional[List[str]] = None
        # The permission type of the permission being granted. Possible values: application for application permissions (e.g. app roles), or delegated for delegated permissions. The value delegatedUserConsentable indicates delegated permissions which have not been configured by the API publisher to require admin consent—this value may be used in built-in permission grant policies, but cannot be used in custom permission grant policies. Required.
        self._permission_type: Optional[permission_type.PermissionType] = None
        # The appId of the resource application (e.g. the API) for which a permission is being granted, or any to match with any resource application or API. Default is any.
        self._resource_application: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PermissionGrantConditionSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PermissionGrantConditionSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PermissionGrantConditionSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "client_application_ids": lambda n : setattr(self, 'client_application_ids', n.get_collection_of_primitive_values(str)),
            "client_application_publisher_ids": lambda n : setattr(self, 'client_application_publisher_ids', n.get_collection_of_primitive_values(str)),
            "client_applications_from_verified_publisher_only": lambda n : setattr(self, 'client_applications_from_verified_publisher_only', n.get_bool_value()),
            "client_application_tenant_ids": lambda n : setattr(self, 'client_application_tenant_ids', n.get_collection_of_primitive_values(str)),
            "permission_classification": lambda n : setattr(self, 'permission_classification', n.get_str_value()),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_primitive_values(str)),
            "permission_type": lambda n : setattr(self, 'permission_type', n.get_enum_value(permission_type.PermissionType)),
            "resource_application": lambda n : setattr(self, 'resource_application', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def permission_classification(self,) -> Optional[str]:
        """
        Gets the permissionClassification property value. The permission classification for the permission being granted, or all to match with any permission classification (including permissions which are not classified). Default is all.
        Returns: Optional[str]
        """
        return self._permission_classification
    
    @permission_classification.setter
    def permission_classification(self,value: Optional[str] = None) -> None:
        """
        Sets the permissionClassification property value. The permission classification for the permission being granted, or all to match with any permission classification (including permissions which are not classified). Default is all.
        Args:
            value: Value to set for the permissionClassification property.
        """
        self._permission_classification = value
    
    @property
    def permissions(self,) -> Optional[List[str]]:
        """
        Gets the permissions property value. The list of id values for the specific permissions to match with, or a list with the single value all to match with any permission. The id of delegated permissions can be found in the oauth2PermissionScopes property of the API's **servicePrincipal** object. The id of application permissions can be found in the appRoles property of the API's **servicePrincipal** object. The id of resource-specific application permissions can be found in the resourceSpecificApplicationPermissions property of the API's **servicePrincipal** object. Default is the single value all.
        Returns: Optional[List[str]]
        """
        return self._permissions
    
    @permissions.setter
    def permissions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the permissions property value. The list of id values for the specific permissions to match with, or a list with the single value all to match with any permission. The id of delegated permissions can be found in the oauth2PermissionScopes property of the API's **servicePrincipal** object. The id of application permissions can be found in the appRoles property of the API's **servicePrincipal** object. The id of resource-specific application permissions can be found in the resourceSpecificApplicationPermissions property of the API's **servicePrincipal** object. Default is the single value all.
        Args:
            value: Value to set for the permissions property.
        """
        self._permissions = value
    
    @property
    def permission_type(self,) -> Optional[permission_type.PermissionType]:
        """
        Gets the permissionType property value. The permission type of the permission being granted. Possible values: application for application permissions (e.g. app roles), or delegated for delegated permissions. The value delegatedUserConsentable indicates delegated permissions which have not been configured by the API publisher to require admin consent—this value may be used in built-in permission grant policies, but cannot be used in custom permission grant policies. Required.
        Returns: Optional[permission_type.PermissionType]
        """
        return self._permission_type
    
    @permission_type.setter
    def permission_type(self,value: Optional[permission_type.PermissionType] = None) -> None:
        """
        Sets the permissionType property value. The permission type of the permission being granted. Possible values: application for application permissions (e.g. app roles), or delegated for delegated permissions. The value delegatedUserConsentable indicates delegated permissions which have not been configured by the API publisher to require admin consent—this value may be used in built-in permission grant policies, but cannot be used in custom permission grant policies. Required.
        Args:
            value: Value to set for the permissionType property.
        """
        self._permission_type = value
    
    @property
    def resource_application(self,) -> Optional[str]:
        """
        Gets the resourceApplication property value. The appId of the resource application (e.g. the API) for which a permission is being granted, or any to match with any resource application or API. Default is any.
        Returns: Optional[str]
        """
        return self._resource_application
    
    @resource_application.setter
    def resource_application(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceApplication property value. The appId of the resource application (e.g. the API) for which a permission is being granted, or any to match with any resource application or API. Default is any.
        Args:
            value: Value to set for the resourceApplication property.
        """
        self._resource_application = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("clientApplicationIds", self.client_application_ids)
        writer.write_collection_of_primitive_values("clientApplicationPublisherIds", self.client_application_publisher_ids)
        writer.write_bool_value("clientApplicationsFromVerifiedPublisherOnly", self.client_applications_from_verified_publisher_only)
        writer.write_collection_of_primitive_values("clientApplicationTenantIds", self.client_application_tenant_ids)
        writer.write_str_value("permissionClassification", self.permission_classification)
        writer.write_collection_of_primitive_values("permissions", self.permissions)
        writer.write_enum_value("permissionType", self.permission_type)
        writer.write_str_value("resourceApplication", self.resource_application)
    

