from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
managed_app_flagged_reason = lazy_import('msgraph.generated.models.managed_app_flagged_reason')
managed_app_operation = lazy_import('msgraph.generated.models.managed_app_operation')
managed_app_policy = lazy_import('msgraph.generated.models.managed_app_policy')
mobile_app_identifier = lazy_import('msgraph.generated.models.mobile_app_identifier')

class ManagedAppRegistration(entity.Entity):
    """
    The ManagedAppEntity is the base entity type for all other entity types under app management workflow.
    """
    @property
    def app_identifier(self,) -> Optional[mobile_app_identifier.MobileAppIdentifier]:
        """
        Gets the appIdentifier property value. The app package Identifier
        Returns: Optional[mobile_app_identifier.MobileAppIdentifier]
        """
        return self._app_identifier
    
    @app_identifier.setter
    def app_identifier(self,value: Optional[mobile_app_identifier.MobileAppIdentifier] = None) -> None:
        """
        Sets the appIdentifier property value. The app package Identifier
        Args:
            value: Value to set for the appIdentifier property.
        """
        self._app_identifier = value
    
    @property
    def application_version(self,) -> Optional[str]:
        """
        Gets the applicationVersion property value. App version
        Returns: Optional[str]
        """
        return self._application_version
    
    @application_version.setter
    def application_version(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationVersion property value. App version
        Args:
            value: Value to set for the applicationVersion property.
        """
        self._application_version = value
    
    @property
    def applied_policies(self,) -> Optional[List[managed_app_policy.ManagedAppPolicy]]:
        """
        Gets the appliedPolicies property value. Zero or more policys already applied on the registered app when it last synchronized with managment service.
        Returns: Optional[List[managed_app_policy.ManagedAppPolicy]]
        """
        return self._applied_policies
    
    @applied_policies.setter
    def applied_policies(self,value: Optional[List[managed_app_policy.ManagedAppPolicy]] = None) -> None:
        """
        Sets the appliedPolicies property value. Zero or more policys already applied on the registered app when it last synchronized with managment service.
        Args:
            value: Value to set for the appliedPolicies property.
        """
        self._applied_policies = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managedAppRegistration and sets the default values.
        """
        super().__init__()
        # The app package Identifier
        self._app_identifier: Optional[mobile_app_identifier.MobileAppIdentifier] = None
        # App version
        self._application_version: Optional[str] = None
        # Zero or more policys already applied on the registered app when it last synchronized with managment service.
        self._applied_policies: Optional[List[managed_app_policy.ManagedAppPolicy]] = None
        # Date and time of creation
        self._created_date_time: Optional[datetime] = None
        # Host device name
        self._device_name: Optional[str] = None
        # App management SDK generated tag, which helps relate apps hosted on the same device. Not guaranteed to relate apps in all conditions.
        self._device_tag: Optional[str] = None
        # Host device type
        self._device_type: Optional[str] = None
        # Zero or more reasons an app registration is flagged. E.g. app running on rooted device
        self._flagged_reasons: Optional[List[managed_app_flagged_reason.ManagedAppFlaggedReason]] = None
        # Zero or more policies admin intended for the app as of now.
        self._intended_policies: Optional[List[managed_app_policy.ManagedAppPolicy]] = None
        # Date and time of last the app synced with management service.
        self._last_sync_date_time: Optional[datetime] = None
        # App management SDK version
        self._management_sdk_version: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Zero or more long running operations triggered on the app registration.
        self._operations: Optional[List[managed_app_operation.ManagedAppOperation]] = None
        # Operating System version
        self._platform_version: Optional[str] = None
        # The user Id to who this app registration belongs.
        self._user_id: Optional[str] = None
        # Version of the entity.
        self._version: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time of creation
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time of creation
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAppRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppRegistration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedAppRegistration()
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Host device name
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Host device name
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def device_tag(self,) -> Optional[str]:
        """
        Gets the deviceTag property value. App management SDK generated tag, which helps relate apps hosted on the same device. Not guaranteed to relate apps in all conditions.
        Returns: Optional[str]
        """
        return self._device_tag
    
    @device_tag.setter
    def device_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceTag property value. App management SDK generated tag, which helps relate apps hosted on the same device. Not guaranteed to relate apps in all conditions.
        Args:
            value: Value to set for the deviceTag property.
        """
        self._device_tag = value
    
    @property
    def device_type(self,) -> Optional[str]:
        """
        Gets the deviceType property value. Host device type
        Returns: Optional[str]
        """
        return self._device_type
    
    @device_type.setter
    def device_type(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceType property value. Host device type
        Args:
            value: Value to set for the deviceType property.
        """
        self._device_type = value
    
    @property
    def flagged_reasons(self,) -> Optional[List[managed_app_flagged_reason.ManagedAppFlaggedReason]]:
        """
        Gets the flaggedReasons property value. Zero or more reasons an app registration is flagged. E.g. app running on rooted device
        Returns: Optional[List[managed_app_flagged_reason.ManagedAppFlaggedReason]]
        """
        return self._flagged_reasons
    
    @flagged_reasons.setter
    def flagged_reasons(self,value: Optional[List[managed_app_flagged_reason.ManagedAppFlaggedReason]] = None) -> None:
        """
        Sets the flaggedReasons property value. Zero or more reasons an app registration is flagged. E.g. app running on rooted device
        Args:
            value: Value to set for the flaggedReasons property.
        """
        self._flagged_reasons = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_identifier": lambda n : setattr(self, 'app_identifier', n.get_object_value(mobile_app_identifier.MobileAppIdentifier)),
            "application_version": lambda n : setattr(self, 'application_version', n.get_str_value()),
            "applied_policies": lambda n : setattr(self, 'applied_policies', n.get_collection_of_object_values(managed_app_policy.ManagedAppPolicy)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "device_tag": lambda n : setattr(self, 'device_tag', n.get_str_value()),
            "device_type": lambda n : setattr(self, 'device_type', n.get_str_value()),
            "flagged_reasons": lambda n : setattr(self, 'flagged_reasons', n.get_collection_of_enum_values(managed_app_flagged_reason.ManagedAppFlaggedReason)),
            "intended_policies": lambda n : setattr(self, 'intended_policies', n.get_collection_of_object_values(managed_app_policy.ManagedAppPolicy)),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "management_sdk_version": lambda n : setattr(self, 'management_sdk_version', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(managed_app_operation.ManagedAppOperation)),
            "platform_version": lambda n : setattr(self, 'platform_version', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def intended_policies(self,) -> Optional[List[managed_app_policy.ManagedAppPolicy]]:
        """
        Gets the intendedPolicies property value. Zero or more policies admin intended for the app as of now.
        Returns: Optional[List[managed_app_policy.ManagedAppPolicy]]
        """
        return self._intended_policies
    
    @intended_policies.setter
    def intended_policies(self,value: Optional[List[managed_app_policy.ManagedAppPolicy]] = None) -> None:
        """
        Sets the intendedPolicies property value. Zero or more policies admin intended for the app as of now.
        Args:
            value: Value to set for the intendedPolicies property.
        """
        self._intended_policies = value
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. Date and time of last the app synced with management service.
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. Date and time of last the app synced with management service.
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    @property
    def management_sdk_version(self,) -> Optional[str]:
        """
        Gets the managementSdkVersion property value. App management SDK version
        Returns: Optional[str]
        """
        return self._management_sdk_version
    
    @management_sdk_version.setter
    def management_sdk_version(self,value: Optional[str] = None) -> None:
        """
        Sets the managementSdkVersion property value. App management SDK version
        Args:
            value: Value to set for the managementSdkVersion property.
        """
        self._management_sdk_version = value
    
    @property
    def operations(self,) -> Optional[List[managed_app_operation.ManagedAppOperation]]:
        """
        Gets the operations property value. Zero or more long running operations triggered on the app registration.
        Returns: Optional[List[managed_app_operation.ManagedAppOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[managed_app_operation.ManagedAppOperation]] = None) -> None:
        """
        Sets the operations property value. Zero or more long running operations triggered on the app registration.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def platform_version(self,) -> Optional[str]:
        """
        Gets the platformVersion property value. Operating System version
        Returns: Optional[str]
        """
        return self._platform_version
    
    @platform_version.setter
    def platform_version(self,value: Optional[str] = None) -> None:
        """
        Sets the platformVersion property value. Operating System version
        Args:
            value: Value to set for the platformVersion property.
        """
        self._platform_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("appIdentifier", self.app_identifier)
        writer.write_str_value("applicationVersion", self.application_version)
        writer.write_collection_of_object_values("appliedPolicies", self.applied_policies)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("deviceTag", self.device_tag)
        writer.write_str_value("deviceType", self.device_type)
        writer.write_enum_value("flaggedReasons", self.flagged_reasons)
        writer.write_collection_of_object_values("intendedPolicies", self.intended_policies)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("managementSdkVersion", self.management_sdk_version)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_str_value("platformVersion", self.platform_version)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("version", self.version)
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The user Id to who this app registration belongs.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The user Id to who this app registration belongs.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. Version of the entity.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. Version of the entity.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

