from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_scope = lazy_import('msgraph.generated.models.app_scope')
directory_object = lazy_import('msgraph.generated.models.directory_object')
entity = lazy_import('msgraph.generated.models.entity')
unified_role_definition = lazy_import('msgraph.generated.models.unified_role_definition')

class UnifiedRoleScheduleBase(entity.Entity):
    @property
    def app_scope(self,) -> Optional[app_scope.AppScope]:
        """
        Gets the appScope property value. Read-only property with details of the app-specific scope when the role eligibility or assignment is scoped to an app. Nullable.
        Returns: Optional[app_scope.AppScope]
        """
        return self._app_scope
    
    @app_scope.setter
    def app_scope(self,value: Optional[app_scope.AppScope] = None) -> None:
        """
        Sets the appScope property value. Read-only property with details of the app-specific scope when the role eligibility or assignment is scoped to an app. Nullable.
        Args:
            value: Value to set for the appScope property.
        """
        self._app_scope = value
    
    @property
    def app_scope_id(self,) -> Optional[str]:
        """
        Gets the appScopeId property value. Identifier of the app-specific scope when the assignment or eligibility is scoped to an app. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units.
        Returns: Optional[str]
        """
        return self._app_scope_id
    
    @app_scope_id.setter
    def app_scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appScopeId property value. Identifier of the app-specific scope when the assignment or eligibility is scoped to an app. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units.
        Args:
            value: Value to set for the appScopeId property.
        """
        self._app_scope_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRoleScheduleBase and sets the default values.
        """
        super().__init__()
        # Read-only property with details of the app-specific scope when the role eligibility or assignment is scoped to an app. Nullable.
        self._app_scope: Optional[app_scope.AppScope] = None
        # Identifier of the app-specific scope when the assignment or eligibility is scoped to an app. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units.
        self._app_scope_id: Optional[str] = None
        # When the schedule was created.
        self._created_date_time: Optional[datetime] = None
        # Identifier of the object through which this schedule was created.
        self._created_using: Optional[str] = None
        # The directory object that is the scope of the role eligibility or assignment. Read-only.
        self._directory_scope: Optional[directory_object.DirectoryObject] = None
        # Identifier of the directory object representing the scope of the assignment or eligibility. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only.
        self._directory_scope_id: Optional[str] = None
        # When the schedule was last modified.
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The principal that's getting a role assignment or that's eligible for a role through the request.
        self._principal: Optional[directory_object.DirectoryObject] = None
        # Identifier of the principal that has been granted the role assignment or eligibility.
        self._principal_id: Optional[str] = None
        # Detailed information for the roleDefinition object that is referenced through the roleDefinitionId property.
        self._role_definition: Optional[unified_role_definition.UnifiedRoleDefinition] = None
        # Identifier of the unifiedRoleDefinition object that is being assigned to the principal or that a principal is eligible for.
        self._role_definition_id: Optional[str] = None
        # The status of the role assignment or eligibility request.
        self._status: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. When the schedule was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. When the schedule was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @property
    def created_using(self,) -> Optional[str]:
        """
        Gets the createdUsing property value. Identifier of the object through which this schedule was created.
        Returns: Optional[str]
        """
        return self._created_using
    
    @created_using.setter
    def created_using(self,value: Optional[str] = None) -> None:
        """
        Sets the createdUsing property value. Identifier of the object through which this schedule was created.
        Args:
            value: Value to set for the createdUsing property.
        """
        self._created_using = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleScheduleBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleScheduleBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleScheduleBase()
    
    @property
    def directory_scope(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the directoryScope property value. The directory object that is the scope of the role eligibility or assignment. Read-only.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._directory_scope
    
    @directory_scope.setter
    def directory_scope(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the directoryScope property value. The directory object that is the scope of the role eligibility or assignment. Read-only.
        Args:
            value: Value to set for the directoryScope property.
        """
        self._directory_scope = value
    
    @property
    def directory_scope_id(self,) -> Optional[str]:
        """
        Gets the directoryScopeId property value. Identifier of the directory object representing the scope of the assignment or eligibility. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only.
        Returns: Optional[str]
        """
        return self._directory_scope_id
    
    @directory_scope_id.setter
    def directory_scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the directoryScopeId property value. Identifier of the directory object representing the scope of the assignment or eligibility. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only.
        Args:
            value: Value to set for the directoryScopeId property.
        """
        self._directory_scope_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_scope": lambda n : setattr(self, 'app_scope', n.get_object_value(app_scope.AppScope)),
            "app_scope_id": lambda n : setattr(self, 'app_scope_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "created_using": lambda n : setattr(self, 'created_using', n.get_str_value()),
            "directory_scope": lambda n : setattr(self, 'directory_scope', n.get_object_value(directory_object.DirectoryObject)),
            "directory_scope_id": lambda n : setattr(self, 'directory_scope_id', n.get_str_value()),
            "modified_date_time": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(directory_object.DirectoryObject)),
            "principal_id": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "role_definition": lambda n : setattr(self, 'role_definition', n.get_object_value(unified_role_definition.UnifiedRoleDefinition)),
            "role_definition_id": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. When the schedule was last modified.
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. When the schedule was last modified.
        Args:
            value: Value to set for the modifiedDateTime property.
        """
        self._modified_date_time = value
    
    @property
    def principal(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the principal property value. The principal that's getting a role assignment or that's eligible for a role through the request.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._principal
    
    @principal.setter
    def principal(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the principal property value. The principal that's getting a role assignment or that's eligible for a role through the request.
        Args:
            value: Value to set for the principal property.
        """
        self._principal = value
    
    @property
    def principal_id(self,) -> Optional[str]:
        """
        Gets the principalId property value. Identifier of the principal that has been granted the role assignment or eligibility.
        Returns: Optional[str]
        """
        return self._principal_id
    
    @principal_id.setter
    def principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the principalId property value. Identifier of the principal that has been granted the role assignment or eligibility.
        Args:
            value: Value to set for the principalId property.
        """
        self._principal_id = value
    
    @property
    def role_definition(self,) -> Optional[unified_role_definition.UnifiedRoleDefinition]:
        """
        Gets the roleDefinition property value. Detailed information for the roleDefinition object that is referenced through the roleDefinitionId property.
        Returns: Optional[unified_role_definition.UnifiedRoleDefinition]
        """
        return self._role_definition
    
    @role_definition.setter
    def role_definition(self,value: Optional[unified_role_definition.UnifiedRoleDefinition] = None) -> None:
        """
        Sets the roleDefinition property value. Detailed information for the roleDefinition object that is referenced through the roleDefinitionId property.
        Args:
            value: Value to set for the roleDefinition property.
        """
        self._role_definition = value
    
    @property
    def role_definition_id(self,) -> Optional[str]:
        """
        Gets the roleDefinitionId property value. Identifier of the unifiedRoleDefinition object that is being assigned to the principal or that a principal is eligible for.
        Returns: Optional[str]
        """
        return self._role_definition_id
    
    @role_definition_id.setter
    def role_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleDefinitionId property value. Identifier of the unifiedRoleDefinition object that is being assigned to the principal or that a principal is eligible for.
        Args:
            value: Value to set for the roleDefinitionId property.
        """
        self._role_definition_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("appScope", self.app_scope)
        writer.write_str_value("appScopeId", self.app_scope_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("createdUsing", self.created_using)
        writer.write_object_value("directoryScope", self.directory_scope)
        writer.write_str_value("directoryScopeId", self.directory_scope_id)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_str_value("status", self.status)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status of the role assignment or eligibility request.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status of the role assignment or eligibility request.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

