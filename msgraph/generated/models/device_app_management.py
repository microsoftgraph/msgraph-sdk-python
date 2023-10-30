from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_managed_app_protection import AndroidManagedAppProtection
    from .default_managed_app_protection import DefaultManagedAppProtection
    from .entity import Entity
    from .ios_managed_app_protection import IosManagedAppProtection
    from .managed_app_policy import ManagedAppPolicy
    from .managed_app_registration import ManagedAppRegistration
    from .managed_app_status import ManagedAppStatus
    from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
    from .managed_e_book import ManagedEBook
    from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
    from .mobile_app import MobileApp
    from .mobile_app_category import MobileAppCategory
    from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
    from .vpp_token import VppToken
    from .windows_information_protection_policy import WindowsInformationProtectionPolicy

from .entity import Entity

@dataclass
class DeviceAppManagement(Entity):
    """
    Singleton entity that acts as a container for all device app management functionality.
    """
    # Android managed app policies.
    android_managed_app_protections: Optional[List[AndroidManagedAppProtection]] = None
    # Default managed app policies.
    default_managed_app_protections: Optional[List[DefaultManagedAppProtection]] = None
    # iOS managed app policies.
    ios_managed_app_protections: Optional[List[IosManagedAppProtection]] = None
    # Whether the account is enabled for syncing applications from the Microsoft Store for Business.
    is_enabled_for_microsoft_store_for_business: Optional[bool] = None
    # Managed app policies.
    managed_app_policies: Optional[List[ManagedAppPolicy]] = None
    # The managed app registrations.
    managed_app_registrations: Optional[List[ManagedAppRegistration]] = None
    # The managed app statuses.
    managed_app_statuses: Optional[List[ManagedAppStatus]] = None
    # The Managed eBook.
    managed_e_books: Optional[List[ManagedEBook]] = None
    # Windows information protection for apps running on devices which are MDM enrolled.
    mdm_windows_information_protection_policies: Optional[List[MdmWindowsInformationProtectionPolicy]] = None
    # The locale information used to sync applications from the Microsoft Store for Business. Cultures that are specific to a country/region. The names of these cultures follow RFC 4646 (Windows Vista and later). The format is -<country/regioncode2>, where  is a lowercase two-letter code derived from ISO 639-1 and <country/regioncode2> is an uppercase two-letter code derived from ISO 3166. For example, en-US for English (United States) is a specific culture.
    microsoft_store_for_business_language: Optional[str] = None
    # The last time an application sync from the Microsoft Store for Business was completed.
    microsoft_store_for_business_last_completed_application_sync_time: Optional[datetime.datetime] = None
    # The last time the apps from the Microsoft Store for Business were synced successfully for the account.
    microsoft_store_for_business_last_successful_sync_date_time: Optional[datetime.datetime] = None
    # The mobile app categories.
    mobile_app_categories: Optional[List[MobileAppCategory]] = None
    # The Managed Device Mobile Application Configurations.
    mobile_app_configurations: Optional[List[ManagedDeviceMobileAppConfiguration]] = None
    # The mobile apps.
    mobile_apps: Optional[List[MobileApp]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Targeted managed app configurations.
    targeted_managed_app_configurations: Optional[List[TargetedManagedAppConfiguration]] = None
    # List of Vpp tokens for this organization.
    vpp_tokens: Optional[List[VppToken]] = None
    # Windows information protection for apps running on devices which are not MDM enrolled.
    windows_information_protection_policies: Optional[List[WindowsInformationProtectionPolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAppManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAppManagement
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceAppManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_managed_app_protection import AndroidManagedAppProtection
        from .default_managed_app_protection import DefaultManagedAppProtection
        from .entity import Entity
        from .ios_managed_app_protection import IosManagedAppProtection
        from .managed_app_policy import ManagedAppPolicy
        from .managed_app_registration import ManagedAppRegistration
        from .managed_app_status import ManagedAppStatus
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
        from .managed_e_book import ManagedEBook
        from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
        from .mobile_app import MobileApp
        from .mobile_app_category import MobileAppCategory
        from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
        from .vpp_token import VppToken
        from .windows_information_protection_policy import WindowsInformationProtectionPolicy

        from .android_managed_app_protection import AndroidManagedAppProtection
        from .default_managed_app_protection import DefaultManagedAppProtection
        from .entity import Entity
        from .ios_managed_app_protection import IosManagedAppProtection
        from .managed_app_policy import ManagedAppPolicy
        from .managed_app_registration import ManagedAppRegistration
        from .managed_app_status import ManagedAppStatus
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
        from .managed_e_book import ManagedEBook
        from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
        from .mobile_app import MobileApp
        from .mobile_app_category import MobileAppCategory
        from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
        from .vpp_token import VppToken
        from .windows_information_protection_policy import WindowsInformationProtectionPolicy

        fields: Dict[str, Callable[[Any], None]] = {
            "android_managed_app_protections": lambda n : setattr(self, 'android_managed_app_protections', n.get_collection_of_object_values(AndroidManagedAppProtection)),
            "default_managed_app_protections": lambda n : setattr(self, 'default_managed_app_protections', n.get_collection_of_object_values(DefaultManagedAppProtection)),
            "ios_managed_app_protections": lambda n : setattr(self, 'ios_managed_app_protections', n.get_collection_of_object_values(IosManagedAppProtection)),
            "is_enabled_for_microsoft_store_for_business": lambda n : setattr(self, 'is_enabled_for_microsoft_store_for_business', n.get_bool_value()),
            "managed_app_policies": lambda n : setattr(self, 'managed_app_policies', n.get_collection_of_object_values(ManagedAppPolicy)),
            "managed_app_registrations": lambda n : setattr(self, 'managed_app_registrations', n.get_collection_of_object_values(ManagedAppRegistration)),
            "managed_app_statuses": lambda n : setattr(self, 'managed_app_statuses', n.get_collection_of_object_values(ManagedAppStatus)),
            "managed_e_books": lambda n : setattr(self, 'managed_e_books', n.get_collection_of_object_values(ManagedEBook)),
            "mdm_windows_information_protection_policies": lambda n : setattr(self, 'mdm_windows_information_protection_policies', n.get_collection_of_object_values(MdmWindowsInformationProtectionPolicy)),
            "microsoft_store_for_business_language": lambda n : setattr(self, 'microsoft_store_for_business_language', n.get_str_value()),
            "microsoft_store_for_business_last_completed_application_sync_time": lambda n : setattr(self, 'microsoft_store_for_business_last_completed_application_sync_time', n.get_datetime_value()),
            "microsoft_store_for_business_last_successful_sync_date_time": lambda n : setattr(self, 'microsoft_store_for_business_last_successful_sync_date_time', n.get_datetime_value()),
            "mobile_app_categories": lambda n : setattr(self, 'mobile_app_categories', n.get_collection_of_object_values(MobileAppCategory)),
            "mobile_app_configurations": lambda n : setattr(self, 'mobile_app_configurations', n.get_collection_of_object_values(ManagedDeviceMobileAppConfiguration)),
            "mobile_apps": lambda n : setattr(self, 'mobile_apps', n.get_collection_of_object_values(MobileApp)),
            "targeted_managed_app_configurations": lambda n : setattr(self, 'targeted_managed_app_configurations', n.get_collection_of_object_values(TargetedManagedAppConfiguration)),
            "vpp_tokens": lambda n : setattr(self, 'vpp_tokens', n.get_collection_of_object_values(VppToken)),
            "windows_information_protection_policies": lambda n : setattr(self, 'windows_information_protection_policies', n.get_collection_of_object_values(WindowsInformationProtectionPolicy)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("android_managed_app_protections", self.android_managed_app_protections)
        writer.write_collection_of_object_values("default_managed_app_protections", self.default_managed_app_protections)
        writer.write_collection_of_object_values("ios_managed_app_protections", self.ios_managed_app_protections)
        writer.write_bool_value("is_enabled_for_microsoft_store_for_business", self.is_enabled_for_microsoft_store_for_business)
        writer.write_collection_of_object_values("managed_app_policies", self.managed_app_policies)
        writer.write_collection_of_object_values("managed_app_registrations", self.managed_app_registrations)
        writer.write_collection_of_object_values("managed_app_statuses", self.managed_app_statuses)
        writer.write_collection_of_object_values("managed_e_books", self.managed_e_books)
        writer.write_collection_of_object_values("mdm_windows_information_protection_policies", self.mdm_windows_information_protection_policies)
        writer.write_str_value("microsoft_store_for_business_language", self.microsoft_store_for_business_language)
        writer.write_datetime_value("microsoft_store_for_business_last_completed_application_sync_time", self.microsoft_store_for_business_last_completed_application_sync_time)
        writer.write_datetime_value("microsoft_store_for_business_last_successful_sync_date_time", self.microsoft_store_for_business_last_successful_sync_date_time)
        writer.write_collection_of_object_values("mobile_app_categories", self.mobile_app_categories)
        writer.write_collection_of_object_values("mobile_app_configurations", self.mobile_app_configurations)
        writer.write_collection_of_object_values("mobile_apps", self.mobile_apps)
        writer.write_collection_of_object_values("targeted_managed_app_configurations", self.targeted_managed_app_configurations)
        writer.write_collection_of_object_values("vpp_tokens", self.vpp_tokens)
        writer.write_collection_of_object_values("windows_information_protection_policies", self.windows_information_protection_policies)
    

