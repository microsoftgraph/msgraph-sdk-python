from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')

class AppRoleAssignment(directory_object.DirectoryObject):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def app_role_id(self,) -> Optional[str]:
        """
        Gets the appRoleId property value. The identifier (id) for the app role which is assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application has not declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create.
        Returns: Optional[str]
        """
        return self._app_role_id
    
    @app_role_id.setter
    def app_role_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appRoleId property value. The identifier (id) for the app role which is assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application has not declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create.
        Args:
            value: Value to set for the appRoleId property.
        """
        self._app_role_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new appRoleAssignment and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.appRoleAssignment"
        # The identifier (id) for the app role which is assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application has not declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create.
        self._app_role_id: Optional[str] = None
        # The time when the app role assignment was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The display name of the user, group, or service principal that was granted the app role assignment. Read-only. Supports $filter (eq and startswith).
        self._principal_display_name: Optional[str] = None
        # The unique identifier (id) for the user, security group, or service principal being granted the app role. Security groups with dynamic memberships are supported. Required on create.
        self._principal_id: Optional[str] = None
        # The type of the assigned principal. This can either be User, Group, or ServicePrincipal. Read-only.
        self._principal_type: Optional[str] = None
        # The display name of the resource app's service principal to which the assignment is made.
        self._resource_display_name: Optional[str] = None
        # The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).
        self._resource_id: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The time when the app role assignment was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The time when the app role assignment was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppRoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppRoleAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppRoleAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_role_id": lambda n : setattr(self, 'app_role_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "principal_display_name": lambda n : setattr(self, 'principal_display_name', n.get_str_value()),
            "principal_id": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "principal_type": lambda n : setattr(self, 'principal_type', n.get_str_value()),
            "resource_display_name": lambda n : setattr(self, 'resource_display_name', n.get_str_value()),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def principal_display_name(self,) -> Optional[str]:
        """
        Gets the principalDisplayName property value. The display name of the user, group, or service principal that was granted the app role assignment. Read-only. Supports $filter (eq and startswith).
        Returns: Optional[str]
        """
        return self._principal_display_name
    
    @principal_display_name.setter
    def principal_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the principalDisplayName property value. The display name of the user, group, or service principal that was granted the app role assignment. Read-only. Supports $filter (eq and startswith).
        Args:
            value: Value to set for the principalDisplayName property.
        """
        self._principal_display_name = value
    
    @property
    def principal_id(self,) -> Optional[str]:
        """
        Gets the principalId property value. The unique identifier (id) for the user, security group, or service principal being granted the app role. Security groups with dynamic memberships are supported. Required on create.
        Returns: Optional[str]
        """
        return self._principal_id
    
    @principal_id.setter
    def principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the principalId property value. The unique identifier (id) for the user, security group, or service principal being granted the app role. Security groups with dynamic memberships are supported. Required on create.
        Args:
            value: Value to set for the principalId property.
        """
        self._principal_id = value
    
    @property
    def principal_type(self,) -> Optional[str]:
        """
        Gets the principalType property value. The type of the assigned principal. This can either be User, Group, or ServicePrincipal. Read-only.
        Returns: Optional[str]
        """
        return self._principal_type
    
    @principal_type.setter
    def principal_type(self,value: Optional[str] = None) -> None:
        """
        Sets the principalType property value. The type of the assigned principal. This can either be User, Group, or ServicePrincipal. Read-only.
        Args:
            value: Value to set for the principalType property.
        """
        self._principal_type = value
    
    @property
    def resource_display_name(self,) -> Optional[str]:
        """
        Gets the resourceDisplayName property value. The display name of the resource app's service principal to which the assignment is made.
        Returns: Optional[str]
        """
        return self._resource_display_name
    
    @resource_display_name.setter
    def resource_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceDisplayName property value. The display name of the resource app's service principal to which the assignment is made.
        Args:
            value: Value to set for the resourceDisplayName property.
        """
        self._resource_display_name = value
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).
        Args:
            value: Value to set for the resourceId property.
        """
        self._resource_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appRoleId", self.app_role_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("principalDisplayName", self.principal_display_name)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_str_value("principalType", self.principal_type)
        writer.write_str_value("resourceDisplayName", self.resource_display_name)
        writer.write_str_value("resourceId", self.resource_id)
    

