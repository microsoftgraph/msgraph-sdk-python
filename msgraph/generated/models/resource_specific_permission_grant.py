from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')

class ResourceSpecificPermissionGrant(directory_object.DirectoryObject):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def client_app_id(self,) -> Optional[str]:
        """
        Gets the clientAppId property value. ID of the service principal of the Azure AD app that has been granted access. Read-only.
        Returns: Optional[str]
        """
        return self._client_app_id
    
    @client_app_id.setter
    def client_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the clientAppId property value. ID of the service principal of the Azure AD app that has been granted access. Read-only.
        Args:
            value: Value to set for the clientAppId property.
        """
        self._client_app_id = value
    
    @property
    def client_id(self,) -> Optional[str]:
        """
        Gets the clientId property value. ID of the Azure AD app that has been granted access. Read-only.
        Returns: Optional[str]
        """
        return self._client_id
    
    @client_id.setter
    def client_id(self,value: Optional[str] = None) -> None:
        """
        Sets the clientId property value. ID of the Azure AD app that has been granted access. Read-only.
        Args:
            value: Value to set for the clientId property.
        """
        self._client_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new resourceSpecificPermissionGrant and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.resourceSpecificPermissionGrant"
        # ID of the service principal of the Azure AD app that has been granted access. Read-only.
        self._client_app_id: Optional[str] = None
        # ID of the Azure AD app that has been granted access. Read-only.
        self._client_id: Optional[str] = None
        # The name of the resource-specific permission. Read-only.
        self._permission: Optional[str] = None
        # The type of permission. Possible values are: Application, Delegated. Read-only.
        self._permission_type: Optional[str] = None
        # ID of the Azure AD app that is hosting the resource. Read-only.
        self._resource_app_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ResourceSpecificPermissionGrant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ResourceSpecificPermissionGrant
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ResourceSpecificPermissionGrant()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "client_app_id": lambda n : setattr(self, 'client_app_id', n.get_str_value()),
            "client_id": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "permission": lambda n : setattr(self, 'permission', n.get_str_value()),
            "permission_type": lambda n : setattr(self, 'permission_type', n.get_str_value()),
            "resource_app_id": lambda n : setattr(self, 'resource_app_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def permission(self,) -> Optional[str]:
        """
        Gets the permission property value. The name of the resource-specific permission. Read-only.
        Returns: Optional[str]
        """
        return self._permission
    
    @permission.setter
    def permission(self,value: Optional[str] = None) -> None:
        """
        Sets the permission property value. The name of the resource-specific permission. Read-only.
        Args:
            value: Value to set for the permission property.
        """
        self._permission = value
    
    @property
    def permission_type(self,) -> Optional[str]:
        """
        Gets the permissionType property value. The type of permission. Possible values are: Application, Delegated. Read-only.
        Returns: Optional[str]
        """
        return self._permission_type
    
    @permission_type.setter
    def permission_type(self,value: Optional[str] = None) -> None:
        """
        Sets the permissionType property value. The type of permission. Possible values are: Application, Delegated. Read-only.
        Args:
            value: Value to set for the permissionType property.
        """
        self._permission_type = value
    
    @property
    def resource_app_id(self,) -> Optional[str]:
        """
        Gets the resourceAppId property value. ID of the Azure AD app that is hosting the resource. Read-only.
        Returns: Optional[str]
        """
        return self._resource_app_id
    
    @resource_app_id.setter
    def resource_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceAppId property value. ID of the Azure AD app that is hosting the resource. Read-only.
        Args:
            value: Value to set for the resourceAppId property.
        """
        self._resource_app_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("clientAppId", self.client_app_id)
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("permission", self.permission)
        writer.write_str_value("permissionType", self.permission_type)
        writer.write_str_value("resourceAppId", self.resource_app_id)
    

