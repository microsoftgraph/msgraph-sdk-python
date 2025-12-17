from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alternative_security_id import AlternativeSecurityId
    from .directory_object import DirectoryObject
    from .extension import Extension

from .directory_object import DirectoryObject

@dataclass
class Device(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.device"
    # true if the account is enabled; otherwise, false. Required. Default is true.  Supports $filter (eq, ne, not, in). Only callers with at least the Cloud Device Administrator role can set this property.
    account_enabled: Optional[bool] = None
    # For internal use only. Not nullable. Supports $filter (eq, not, ge, le).
    alternative_security_ids: Optional[list[AlternativeSecurityId]] = None
    # The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter (eq, ne, not, ge, le, and eq on null values) and $orderby.
    approximate_last_sign_in_date_time: Optional[datetime.datetime] = None
    # The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    compliance_expiration_date_time: Optional[datetime.datetime] = None
    # User-defined property set by Intune to automatically add devices to groups and simplify managing devices.
    device_category: Optional[str] = None
    # Unique identifier set by Azure Device Registration Service at the time of registration. This alternate key can be used to reference the device object. Supports $filter (eq, ne, not, startsWith).
    device_id: Optional[str] = None
    # For internal use only. Set to null.
    device_metadata: Optional[str] = None
    # Ownership of the device. Intune sets this property. The possible values are: unknown, company, personal.
    device_ownership: Optional[str] = None
    # For internal use only.
    device_version: Optional[int] = None
    # The display name for the device. Maximum length is 256 characters. Required. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.
    display_name: Optional[str] = None
    # Enrollment profile applied to the device. For example, Apple Device Enrollment Profile, Device enrollment - Corporate device identifiers, or Windows Autopilot profile name. This property is set by Intune.
    enrollment_profile_name: Optional[str] = None
    # Enrollment type of the device. Intune sets this property. The possible values are: unknown, userEnrollment, deviceEnrollmentManager, appleBulkWithUser, appleBulkWithoutUser, windowsAzureADJoin, windowsBulkUserless, windowsAutoEnrollment, windowsBulkAzureDomainJoin, windowsCoManagement, windowsAzureADJoinUsingDeviceAuth,appleUserEnrollment, appleUserEnrollmentWithServiceAccount. NOTE: This property might return other values apart from those listed.
    enrollment_type: Optional[str] = None
    # The collection of open extensions defined for the device. Read-only. Nullable.
    extensions: Optional[list[Extension]] = None
    # true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
    is_compliant: Optional[bool] = None
    # true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
    is_managed: Optional[bool] = None
    # Indicates whether the device is a member of a restricted management administrative unit. If not set, the default value is null and the default behavior is false. Read-only.  To manage a device that's a member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Returned only on $select.
    is_management_restricted: Optional[bool] = None
    # true if the device is rooted or jail-broken. This property can only be updated by Intune.
    is_rooted: Optional[bool] = None
    # The management channel of the device. This property is set by Intune. The possible values are: eas, mdm, easMdm, intuneClient, easIntuneClient, configurationManagerClient, configurationManagerClientMdm, configurationManagerClientMdmEas, unknown, jamf, googleCloudDevicePolicyController.
    management_type: Optional[str] = None
    # Manufacturer of the device. Read-only.
    manufacturer: Optional[str] = None
    # Application identifier used to register device into MDM. Read-only. Supports $filter (eq, ne, not, startsWith).
    mdm_app_id: Optional[str] = None
    # Groups and administrative units that this device is a member of. Read-only. Nullable. Supports $expand.
    member_of: Optional[list[DirectoryObject]] = None
    # Model of the device. Read-only.
    model: Optional[str] = None
    # The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z Read-only. Supports $filter (eq, ne, not, ge, le, in).
    on_premises_last_sync_date_time: Optional[datetime.datetime] = None
    # The on-premises security identifier (SID) for the user who was synchronized from on-premises to the cloud. Read-only. Returned only on $select. Supports $filter (eq).
    on_premises_security_identifier: Optional[str] = None
    # true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
    on_premises_sync_enabled: Optional[bool] = None
    # The type of operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
    operating_system: Optional[str] = None
    # The version of the operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
    operating_system_version: Optional[str] = None
    # For internal use only. Not nullable. Supports $filter (eq, not, ge, le, startsWith,/$count eq 0, /$count ne 0).
    physical_ids: Optional[list[str]] = None
    # The profile type of the device. Possible values: RegisteredDevice (default), SecureVM, Printer, Shared, IoT.
    profile_type: Optional[str] = None
    # The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Read-only. Nullable. Supports $expand.
    registered_owners: Optional[list[DirectoryObject]] = None
    # Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable. Supports $expand.
    registered_users: Optional[list[DirectoryObject]] = None
    # Date and time of when the device was registered. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    registration_date_time: Optional[datetime.datetime] = None
    # List of labels applied to the device by the system. Supports $filter (/$count eq 0, /$count ne 0).
    system_labels: Optional[list[str]] = None
    # Groups and administrative units that the device is a member of. This operation is transitive. Supports $expand.
    transitive_member_of: Optional[list[DirectoryObject]] = None
    # Type of trust for the joined device. Read-only. Possible values:  Workplace (indicates bring your own personal devices), AzureAd (Cloud-only joined devices), ServerAd (on-premises domain joined devices joined to Microsoft Entra ID). For more information, see Introduction to device management in Microsoft Entra ID. Supports $filter (eq, ne, not, in).
    trust_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Device:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Device
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Device()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alternative_security_id import AlternativeSecurityId
        from .directory_object import DirectoryObject
        from .extension import Extension

        from .alternative_security_id import AlternativeSecurityId
        from .directory_object import DirectoryObject
        from .extension import Extension

        fields: dict[str, Callable[[Any], None]] = {
            "accountEnabled": lambda n : setattr(self, 'account_enabled', n.get_bool_value()),
            "alternativeSecurityIds": lambda n : setattr(self, 'alternative_security_ids', n.get_collection_of_object_values(AlternativeSecurityId)),
            "approximateLastSignInDateTime": lambda n : setattr(self, 'approximate_last_sign_in_date_time', n.get_datetime_value()),
            "complianceExpirationDateTime": lambda n : setattr(self, 'compliance_expiration_date_time', n.get_datetime_value()),
            "deviceCategory": lambda n : setattr(self, 'device_category', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceMetadata": lambda n : setattr(self, 'device_metadata', n.get_str_value()),
            "deviceOwnership": lambda n : setattr(self, 'device_ownership', n.get_str_value()),
            "deviceVersion": lambda n : setattr(self, 'device_version', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrollmentProfileName": lambda n : setattr(self, 'enrollment_profile_name', n.get_str_value()),
            "enrollmentType": lambda n : setattr(self, 'enrollment_type', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "isCompliant": lambda n : setattr(self, 'is_compliant', n.get_bool_value()),
            "isManaged": lambda n : setattr(self, 'is_managed', n.get_bool_value()),
            "isManagementRestricted": lambda n : setattr(self, 'is_management_restricted', n.get_bool_value()),
            "isRooted": lambda n : setattr(self, 'is_rooted', n.get_bool_value()),
            "managementType": lambda n : setattr(self, 'management_type', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "mdmAppId": lambda n : setattr(self, 'mdm_app_id', n.get_str_value()),
            "memberOf": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(DirectoryObject)),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "onPremisesLastSyncDateTime": lambda n : setattr(self, 'on_premises_last_sync_date_time', n.get_datetime_value()),
            "onPremisesSecurityIdentifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
            "onPremisesSyncEnabled": lambda n : setattr(self, 'on_premises_sync_enabled', n.get_bool_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "operatingSystemVersion": lambda n : setattr(self, 'operating_system_version', n.get_str_value()),
            "physicalIds": lambda n : setattr(self, 'physical_ids', n.get_collection_of_primitive_values(str)),
            "profileType": lambda n : setattr(self, 'profile_type', n.get_str_value()),
            "registeredOwners": lambda n : setattr(self, 'registered_owners', n.get_collection_of_object_values(DirectoryObject)),
            "registeredUsers": lambda n : setattr(self, 'registered_users', n.get_collection_of_object_values(DirectoryObject)),
            "registrationDateTime": lambda n : setattr(self, 'registration_date_time', n.get_datetime_value()),
            "systemLabels": lambda n : setattr(self, 'system_labels', n.get_collection_of_primitive_values(str)),
            "transitiveMemberOf": lambda n : setattr(self, 'transitive_member_of', n.get_collection_of_object_values(DirectoryObject)),
            "trustType": lambda n : setattr(self, 'trust_type', n.get_str_value()),
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
        writer.write_bool_value("accountEnabled", self.account_enabled)
        writer.write_collection_of_object_values("alternativeSecurityIds", self.alternative_security_ids)
        writer.write_datetime_value("approximateLastSignInDateTime", self.approximate_last_sign_in_date_time)
        writer.write_datetime_value("complianceExpirationDateTime", self.compliance_expiration_date_time)
        writer.write_str_value("deviceCategory", self.device_category)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceMetadata", self.device_metadata)
        writer.write_str_value("deviceOwnership", self.device_ownership)
        writer.write_int_value("deviceVersion", self.device_version)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("enrollmentProfileName", self.enrollment_profile_name)
        writer.write_str_value("enrollmentType", self.enrollment_type)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_bool_value("isCompliant", self.is_compliant)
        writer.write_bool_value("isManaged", self.is_managed)
        writer.write_bool_value("isManagementRestricted", self.is_management_restricted)
        writer.write_bool_value("isRooted", self.is_rooted)
        writer.write_str_value("managementType", self.management_type)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("mdmAppId", self.mdm_app_id)
        writer.write_collection_of_object_values("memberOf", self.member_of)
        writer.write_str_value("model", self.model)
        writer.write_datetime_value("onPremisesLastSyncDateTime", self.on_premises_last_sync_date_time)
        writer.write_str_value("onPremisesSecurityIdentifier", self.on_premises_security_identifier)
        writer.write_bool_value("onPremisesSyncEnabled", self.on_premises_sync_enabled)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_str_value("operatingSystemVersion", self.operating_system_version)
        writer.write_collection_of_primitive_values("physicalIds", self.physical_ids)
        writer.write_str_value("profileType", self.profile_type)
        writer.write_collection_of_object_values("registeredOwners", self.registered_owners)
        writer.write_collection_of_object_values("registeredUsers", self.registered_users)
        writer.write_datetime_value("registrationDateTime", self.registration_date_time)
        writer.write_collection_of_primitive_values("systemLabels", self.system_labels)
        writer.write_collection_of_object_values("transitiveMemberOf", self.transitive_member_of)
        writer.write_str_value("trustType", self.trust_type)
    

