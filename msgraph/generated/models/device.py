from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alternative_security_id = lazy_import('msgraph.generated.models.alternative_security_id')
directory_object = lazy_import('msgraph.generated.models.directory_object')
extension = lazy_import('msgraph.generated.models.extension')

class Device(directory_object.DirectoryObject):
    @property
    def account_enabled(self,) -> Optional[bool]:
        """
        Gets the accountEnabled property value. true if the account is enabled; otherwise, false. Required. Default is true.  Supports $filter (eq, ne, not, in). Only callers in Global Administrator and Cloud Device Administrator roles can set this property.
        Returns: Optional[bool]
        """
        return self._account_enabled
    
    @account_enabled.setter
    def account_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the accountEnabled property value. true if the account is enabled; otherwise, false. Required. Default is true.  Supports $filter (eq, ne, not, in). Only callers in Global Administrator and Cloud Device Administrator roles can set this property.
        Args:
            value: Value to set for the accountEnabled property.
        """
        self._account_enabled = value
    
    @property
    def alternative_security_ids(self,) -> Optional[List[alternative_security_id.AlternativeSecurityId]]:
        """
        Gets the alternativeSecurityIds property value. For internal use only. Not nullable. Supports $filter (eq, not, ge, le).
        Returns: Optional[List[alternative_security_id.AlternativeSecurityId]]
        """
        return self._alternative_security_ids
    
    @alternative_security_ids.setter
    def alternative_security_ids(self,value: Optional[List[alternative_security_id.AlternativeSecurityId]] = None) -> None:
        """
        Sets the alternativeSecurityIds property value. For internal use only. Not nullable. Supports $filter (eq, not, ge, le).
        Args:
            value: Value to set for the alternativeSecurityIds property.
        """
        self._alternative_security_ids = value
    
    @property
    def approximate_last_sign_in_date_time(self,) -> Optional[datetime]:
        """
        Gets the approximateLastSignInDateTime property value. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter (eq, ne, not, ge, le, and eq on null values) and $orderBy.
        Returns: Optional[datetime]
        """
        return self._approximate_last_sign_in_date_time
    
    @approximate_last_sign_in_date_time.setter
    def approximate_last_sign_in_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the approximateLastSignInDateTime property value. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter (eq, ne, not, ge, le, and eq on null values) and $orderBy.
        Args:
            value: Value to set for the approximateLastSignInDateTime property.
        """
        self._approximate_last_sign_in_date_time = value
    
    @property
    def compliance_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the complianceExpirationDateTime property value. The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._compliance_expiration_date_time
    
    @compliance_expiration_date_time.setter
    def compliance_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the complianceExpirationDateTime property value. The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the complianceExpirationDateTime property.
        """
        self._compliance_expiration_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new device and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.device"
        # true if the account is enabled; otherwise, false. Required. Default is true.  Supports $filter (eq, ne, not, in). Only callers in Global Administrator and Cloud Device Administrator roles can set this property.
        self._account_enabled: Optional[bool] = None
        # For internal use only. Not nullable. Supports $filter (eq, not, ge, le).
        self._alternative_security_ids: Optional[List[alternative_security_id.AlternativeSecurityId]] = None
        # The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter (eq, ne, not, ge, le, and eq on null values) and $orderBy.
        self._approximate_last_sign_in_date_time: Optional[datetime] = None
        # The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._compliance_expiration_date_time: Optional[datetime] = None
        # Unique identifier set by Azure Device Registration Service at the time of registration. Supports $filter (eq, ne, not, startsWith).
        self._device_id: Optional[str] = None
        # For internal use only. Set to null.
        self._device_metadata: Optional[str] = None
        # For internal use only.
        self._device_version: Optional[int] = None
        # The display name for the device. Required. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        self._display_name: Optional[str] = None
        # The collection of open extensions defined for the device. Read-only. Nullable.
        self._extensions: Optional[List[extension.Extension]] = None
        # true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
        self._is_compliant: Optional[bool] = None
        # true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
        self._is_managed: Optional[bool] = None
        # Application identifier used to register device into MDM. Read-only. Supports $filter (eq, ne, not, startsWith).
        self._mdm_app_id: Optional[str] = None
        # Groups and administrative units that this device is a member of. Read-only. Nullable. Supports $expand.
        self._member_of: Optional[List[directory_object.DirectoryObject]] = None
        # The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z Read-only. Supports $filter (eq, ne, not, ge, le, in).
        self._on_premises_last_sync_date_time: Optional[datetime] = None
        # true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
        self._on_premises_sync_enabled: Optional[bool] = None
        # The type of operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
        self._operating_system: Optional[str] = None
        # The version of the operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
        self._operating_system_version: Optional[str] = None
        # For internal use only. Not nullable. Supports $filter (eq, not, ge, le, startsWith,/$count eq 0, /$count ne 0).
        self._physical_ids: Optional[List[str]] = None
        # The profile type of the device. Possible values: RegisteredDevice (default), SecureVM, Printer, Shared, IoT.
        self._profile_type: Optional[str] = None
        # The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable. Supports $expand.
        self._registered_owners: Optional[List[directory_object.DirectoryObject]] = None
        # Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable. Supports $expand.
        self._registered_users: Optional[List[directory_object.DirectoryObject]] = None
        # List of labels applied to the device by the system. Supports $filter (/$count eq 0, /$count ne 0).
        self._system_labels: Optional[List[str]] = None
        # Groups and administrative units that the device is a member of. This operation is transitive. Supports $expand.
        self._transitive_member_of: Optional[List[directory_object.DirectoryObject]] = None
        # Type of trust for the joined device. Read-only. Possible values:  Workplace (indicates bring your own personal devices), AzureAd (Cloud only joined devices), ServerAd (on-premises domain joined devices joined to Azure AD). For more details, see Introduction to device management in Azure Active Directory
        self._trust_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Device:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Device
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Device()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. Unique identifier set by Azure Device Registration Service at the time of registration. Supports $filter (eq, ne, not, startsWith).
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. Unique identifier set by Azure Device Registration Service at the time of registration. Supports $filter (eq, ne, not, startsWith).
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_metadata(self,) -> Optional[str]:
        """
        Gets the deviceMetadata property value. For internal use only. Set to null.
        Returns: Optional[str]
        """
        return self._device_metadata
    
    @device_metadata.setter
    def device_metadata(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceMetadata property value. For internal use only. Set to null.
        Args:
            value: Value to set for the deviceMetadata property.
        """
        self._device_metadata = value
    
    @property
    def device_version(self,) -> Optional[int]:
        """
        Gets the deviceVersion property value. For internal use only.
        Returns: Optional[int]
        """
        return self._device_version
    
    @device_version.setter
    def device_version(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceVersion property value. For internal use only.
        Args:
            value: Value to set for the deviceVersion property.
        """
        self._device_version = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the device. Required. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the device. Required. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def extensions(self,) -> Optional[List[extension.Extension]]:
        """
        Gets the extensions property value. The collection of open extensions defined for the device. Read-only. Nullable.
        Returns: Optional[List[extension.Extension]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[extension.Extension]] = None) -> None:
        """
        Sets the extensions property value. The collection of open extensions defined for the device. Read-only. Nullable.
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_enabled": lambda n : setattr(self, 'account_enabled', n.get_bool_value()),
            "alternative_security_ids": lambda n : setattr(self, 'alternative_security_ids', n.get_collection_of_object_values(alternative_security_id.AlternativeSecurityId)),
            "approximate_last_sign_in_date_time": lambda n : setattr(self, 'approximate_last_sign_in_date_time', n.get_datetime_value()),
            "compliance_expiration_date_time": lambda n : setattr(self, 'compliance_expiration_date_time', n.get_datetime_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_metadata": lambda n : setattr(self, 'device_metadata', n.get_str_value()),
            "device_version": lambda n : setattr(self, 'device_version', n.get_int_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "is_compliant": lambda n : setattr(self, 'is_compliant', n.get_bool_value()),
            "is_managed": lambda n : setattr(self, 'is_managed', n.get_bool_value()),
            "mdm_app_id": lambda n : setattr(self, 'mdm_app_id', n.get_str_value()),
            "member_of": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "on_premises_last_sync_date_time": lambda n : setattr(self, 'on_premises_last_sync_date_time', n.get_datetime_value()),
            "on_premises_sync_enabled": lambda n : setattr(self, 'on_premises_sync_enabled', n.get_bool_value()),
            "operating_system": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "operating_system_version": lambda n : setattr(self, 'operating_system_version', n.get_str_value()),
            "physical_ids": lambda n : setattr(self, 'physical_ids', n.get_collection_of_primitive_values(str)),
            "profile_type": lambda n : setattr(self, 'profile_type', n.get_str_value()),
            "registered_owners": lambda n : setattr(self, 'registered_owners', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "registered_users": lambda n : setattr(self, 'registered_users', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "system_labels": lambda n : setattr(self, 'system_labels', n.get_collection_of_primitive_values(str)),
            "transitive_member_of": lambda n : setattr(self, 'transitive_member_of', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "trust_type": lambda n : setattr(self, 'trust_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_compliant(self,) -> Optional[bool]:
        """
        Gets the isCompliant property value. true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
        Returns: Optional[bool]
        """
        return self._is_compliant
    
    @is_compliant.setter
    def is_compliant(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCompliant property value. true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
        Args:
            value: Value to set for the isCompliant property.
        """
        self._is_compliant = value
    
    @property
    def is_managed(self,) -> Optional[bool]:
        """
        Gets the isManaged property value. true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
        Returns: Optional[bool]
        """
        return self._is_managed
    
    @is_managed.setter
    def is_managed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isManaged property value. true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
        Args:
            value: Value to set for the isManaged property.
        """
        self._is_managed = value
    
    @property
    def mdm_app_id(self,) -> Optional[str]:
        """
        Gets the mdmAppId property value. Application identifier used to register device into MDM. Read-only. Supports $filter (eq, ne, not, startsWith).
        Returns: Optional[str]
        """
        return self._mdm_app_id
    
    @mdm_app_id.setter
    def mdm_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the mdmAppId property value. Application identifier used to register device into MDM. Read-only. Supports $filter (eq, ne, not, startsWith).
        Args:
            value: Value to set for the mdmAppId property.
        """
        self._mdm_app_id = value
    
    @property
    def member_of(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the memberOf property value. Groups and administrative units that this device is a member of. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._member_of
    
    @member_of.setter
    def member_of(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the memberOf property value. Groups and administrative units that this device is a member of. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the memberOf property.
        """
        self._member_of = value
    
    @property
    def on_premises_last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the onPremisesLastSyncDateTime property value. The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z Read-only. Supports $filter (eq, ne, not, ge, le, in).
        Returns: Optional[datetime]
        """
        return self._on_premises_last_sync_date_time
    
    @on_premises_last_sync_date_time.setter
    def on_premises_last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the onPremisesLastSyncDateTime property value. The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z Read-only. Supports $filter (eq, ne, not, ge, le, in).
        Args:
            value: Value to set for the onPremisesLastSyncDateTime property.
        """
        self._on_premises_last_sync_date_time = value
    
    @property
    def on_premises_sync_enabled(self,) -> Optional[bool]:
        """
        Gets the onPremisesSyncEnabled property value. true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
        Returns: Optional[bool]
        """
        return self._on_premises_sync_enabled
    
    @on_premises_sync_enabled.setter
    def on_premises_sync_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the onPremisesSyncEnabled property value. true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
        Args:
            value: Value to set for the onPremisesSyncEnabled property.
        """
        self._on_premises_sync_enabled = value
    
    @property
    def operating_system(self,) -> Optional[str]:
        """
        Gets the operatingSystem property value. The type of operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._operating_system
    
    @operating_system.setter
    def operating_system(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystem property value. The type of operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
        Args:
            value: Value to set for the operatingSystem property.
        """
        self._operating_system = value
    
    @property
    def operating_system_version(self,) -> Optional[str]:
        """
        Gets the operatingSystemVersion property value. The version of the operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._operating_system_version
    
    @operating_system_version.setter
    def operating_system_version(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystemVersion property value. The version of the operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
        Args:
            value: Value to set for the operatingSystemVersion property.
        """
        self._operating_system_version = value
    
    @property
    def physical_ids(self,) -> Optional[List[str]]:
        """
        Gets the physicalIds property value. For internal use only. Not nullable. Supports $filter (eq, not, ge, le, startsWith,/$count eq 0, /$count ne 0).
        Returns: Optional[List[str]]
        """
        return self._physical_ids
    
    @physical_ids.setter
    def physical_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the physicalIds property value. For internal use only. Not nullable. Supports $filter (eq, not, ge, le, startsWith,/$count eq 0, /$count ne 0).
        Args:
            value: Value to set for the physicalIds property.
        """
        self._physical_ids = value
    
    @property
    def profile_type(self,) -> Optional[str]:
        """
        Gets the profileType property value. The profile type of the device. Possible values: RegisteredDevice (default), SecureVM, Printer, Shared, IoT.
        Returns: Optional[str]
        """
        return self._profile_type
    
    @profile_type.setter
    def profile_type(self,value: Optional[str] = None) -> None:
        """
        Sets the profileType property value. The profile type of the device. Possible values: RegisteredDevice (default), SecureVM, Printer, Shared, IoT.
        Args:
            value: Value to set for the profileType property.
        """
        self._profile_type = value
    
    @property
    def registered_owners(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the registeredOwners property value. The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._registered_owners
    
    @registered_owners.setter
    def registered_owners(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the registeredOwners property value. The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the registeredOwners property.
        """
        self._registered_owners = value
    
    @property
    def registered_users(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the registeredUsers property value. Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._registered_users
    
    @registered_users.setter
    def registered_users(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the registeredUsers property value. Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the registeredUsers property.
        """
        self._registered_users = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("accountEnabled", self.account_enabled)
        writer.write_collection_of_object_values("alternativeSecurityIds", self.alternative_security_ids)
        writer.write_datetime_value("approximateLastSignInDateTime", self.approximate_last_sign_in_date_time)
        writer.write_datetime_value("complianceExpirationDateTime", self.compliance_expiration_date_time)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceMetadata", self.device_metadata)
        writer.write_int_value("deviceVersion", self.device_version)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_bool_value("isCompliant", self.is_compliant)
        writer.write_bool_value("isManaged", self.is_managed)
        writer.write_str_value("mdmAppId", self.mdm_app_id)
        writer.write_collection_of_object_values("memberOf", self.member_of)
        writer.write_datetime_value("onPremisesLastSyncDateTime", self.on_premises_last_sync_date_time)
        writer.write_bool_value("onPremisesSyncEnabled", self.on_premises_sync_enabled)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_str_value("operatingSystemVersion", self.operating_system_version)
        writer.write_collection_of_primitive_values("physicalIds", self.physical_ids)
        writer.write_str_value("profileType", self.profile_type)
        writer.write_collection_of_object_values("registeredOwners", self.registered_owners)
        writer.write_collection_of_object_values("registeredUsers", self.registered_users)
        writer.write_collection_of_primitive_values("systemLabels", self.system_labels)
        writer.write_collection_of_object_values("transitiveMemberOf", self.transitive_member_of)
        writer.write_str_value("trustType", self.trust_type)
    
    @property
    def system_labels(self,) -> Optional[List[str]]:
        """
        Gets the systemLabels property value. List of labels applied to the device by the system. Supports $filter (/$count eq 0, /$count ne 0).
        Returns: Optional[List[str]]
        """
        return self._system_labels
    
    @system_labels.setter
    def system_labels(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the systemLabels property value. List of labels applied to the device by the system. Supports $filter (/$count eq 0, /$count ne 0).
        Args:
            value: Value to set for the systemLabels property.
        """
        self._system_labels = value
    
    @property
    def transitive_member_of(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the transitiveMemberOf property value. Groups and administrative units that the device is a member of. This operation is transitive. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._transitive_member_of
    
    @transitive_member_of.setter
    def transitive_member_of(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the transitiveMemberOf property value. Groups and administrative units that the device is a member of. This operation is transitive. Supports $expand.
        Args:
            value: Value to set for the transitiveMemberOf property.
        """
        self._transitive_member_of = value
    
    @property
    def trust_type(self,) -> Optional[str]:
        """
        Gets the trustType property value. Type of trust for the joined device. Read-only. Possible values:  Workplace (indicates bring your own personal devices), AzureAd (Cloud only joined devices), ServerAd (on-premises domain joined devices joined to Azure AD). For more details, see Introduction to device management in Azure Active Directory
        Returns: Optional[str]
        """
        return self._trust_type
    
    @trust_type.setter
    def trust_type(self,value: Optional[str] = None) -> None:
        """
        Sets the trustType property value. Type of trust for the joined device. Read-only. Possible values:  Workplace (indicates bring your own personal devices), AzureAd (Cloud only joined devices), ServerAd (on-premises domain joined devices joined to Azure AD). For more details, see Introduction to device management in Azure Active Directory
        Args:
            value: Value to set for the trustType property.
        """
        self._trust_type = value
    

