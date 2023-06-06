from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_managed_app_protection, default_managed_app_protection, entity, ios_managed_app_protection, managed_app_policy, managed_app_registration, managed_app_status, managed_device_mobile_app_configuration, managed_e_book, mdm_windows_information_protection_policy, mobile_app, mobile_app_category, targeted_managed_app_configuration, vpp_token, windows_information_protection_policy

from . import entity

@dataclass
class DeviceAppManagement(entity.Entity):
    # Android managed app policies.
    android_managed_app_protections: Optional[List[android_managed_app_protection.AndroidManagedAppProtection]] = None
    # Default managed app policies.
    default_managed_app_protections: Optional[List[default_managed_app_protection.DefaultManagedAppProtection]] = None
    # iOS managed app policies.
    ios_managed_app_protections: Optional[List[ios_managed_app_protection.IosManagedAppProtection]] = None
    # Whether the account is enabled for syncing applications from the Microsoft Store for Business.
    is_enabled_for_microsoft_store_for_business: Optional[bool] = None
    # Managed app policies.
    managed_app_policies: Optional[List[managed_app_policy.ManagedAppPolicy]] = None
    # The managed app registrations.
    managed_app_registrations: Optional[List[managed_app_registration.ManagedAppRegistration]] = None
    # The managed app statuses.
    managed_app_statuses: Optional[List[managed_app_status.ManagedAppStatus]] = None
    # The Managed eBook.
    managed_e_books: Optional[List[managed_e_book.ManagedEBook]] = None
    # Windows information protection for apps running on devices which are MDM enrolled.
    mdm_windows_information_protection_policies: Optional[List[mdm_windows_information_protection_policy.MdmWindowsInformationProtectionPolicy]] = None
    # The locale information used to sync applications from the Microsoft Store for Business. Cultures that are specific to a country/region. The names of these cultures follow RFC 4646 (Windows Vista and later). The format is -<country/regioncode2>, where  is a lowercase two-letter code derived from ISO 639-1 and <country/regioncode2> is an uppercase two-letter code derived from ISO 3166. For example, en-US for English (United States) is a specific culture.
    microsoft_store_for_business_language: Optional[str] = None
    # The last time an application sync from the Microsoft Store for Business was completed.
    microsoft_store_for_business_last_completed_application_sync_time: Optional[datetime] = None
    # The last time the apps from the Microsoft Store for Business were synced successfully for the account.
    microsoft_store_for_business_last_successful_sync_date_time: Optional[datetime] = None
    # The mobile app categories.
    mobile_app_categories: Optional[List[mobile_app_category.MobileAppCategory]] = None
    # The Managed Device Mobile Application Configurations.
    mobile_app_configurations: Optional[List[managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration]] = None
    # The mobile apps.
    mobile_apps: Optional[List[mobile_app.MobileApp]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Targeted managed app configurations.
    targeted_managed_app_configurations: Optional[List[targeted_managed_app_configuration.TargetedManagedAppConfiguration]] = None
    # List of Vpp tokens for this organization.
    vpp_tokens: Optional[List[vpp_token.VppToken]] = None
    # Windows information protection for apps running on devices which are not MDM enrolled.
    windows_information_protection_policies: Optional[List[windows_information_protection_policy.WindowsInformationProtectionPolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAppManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAppManagement
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceAppManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_managed_app_protection, default_managed_app_protection, entity, ios_managed_app_protection, managed_app_policy, managed_app_registration, managed_app_status, managed_device_mobile_app_configuration, managed_e_book, mdm_windows_information_protection_policy, mobile_app, mobile_app_category, targeted_managed_app_configuration, vpp_token, windows_information_protection_policy

        fields: Dict[str, Callable[[Any], None]] = {
            "androidManagedAppProtections": lambda n : setattr(self, 'android_managed_app_protections', n.get_collection_of_object_values(android_managed_app_protection.AndroidManagedAppProtection)),
            "defaultManagedAppProtections": lambda n : setattr(self, 'default_managed_app_protections', n.get_collection_of_object_values(default_managed_app_protection.DefaultManagedAppProtection)),
            "iosManagedAppProtections": lambda n : setattr(self, 'ios_managed_app_protections', n.get_collection_of_object_values(ios_managed_app_protection.IosManagedAppProtection)),
            "isEnabledForMicrosoftStoreForBusiness": lambda n : setattr(self, 'is_enabled_for_microsoft_store_for_business', n.get_bool_value()),
            "managedAppPolicies": lambda n : setattr(self, 'managed_app_policies', n.get_collection_of_object_values(managed_app_policy.ManagedAppPolicy)),
            "managedAppRegistrations": lambda n : setattr(self, 'managed_app_registrations', n.get_collection_of_object_values(managed_app_registration.ManagedAppRegistration)),
            "managedAppStatuses": lambda n : setattr(self, 'managed_app_statuses', n.get_collection_of_object_values(managed_app_status.ManagedAppStatus)),
            "managedEBooks": lambda n : setattr(self, 'managed_e_books', n.get_collection_of_object_values(managed_e_book.ManagedEBook)),
            "mdmWindowsInformationProtectionPolicies": lambda n : setattr(self, 'mdm_windows_information_protection_policies', n.get_collection_of_object_values(mdm_windows_information_protection_policy.MdmWindowsInformationProtectionPolicy)),
            "microsoftStoreForBusinessLanguage": lambda n : setattr(self, 'microsoft_store_for_business_language', n.get_str_value()),
            "microsoftStoreForBusinessLastCompletedApplicationSyncTime": lambda n : setattr(self, 'microsoft_store_for_business_last_completed_application_sync_time', n.get_datetime_value()),
            "microsoftStoreForBusinessLastSuccessfulSyncDateTime": lambda n : setattr(self, 'microsoft_store_for_business_last_successful_sync_date_time', n.get_datetime_value()),
            "mobileApps": lambda n : setattr(self, 'mobile_apps', n.get_collection_of_object_values(mobile_app.MobileApp)),
            "mobileAppCategories": lambda n : setattr(self, 'mobile_app_categories', n.get_collection_of_object_values(mobile_app_category.MobileAppCategory)),
            "mobileAppConfigurations": lambda n : setattr(self, 'mobile_app_configurations', n.get_collection_of_object_values(managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration)),
            "targetedManagedAppConfigurations": lambda n : setattr(self, 'targeted_managed_app_configurations', n.get_collection_of_object_values(targeted_managed_app_configuration.TargetedManagedAppConfiguration)),
            "vppTokens": lambda n : setattr(self, 'vpp_tokens', n.get_collection_of_object_values(vpp_token.VppToken)),
            "windowsInformationProtectionPolicies": lambda n : setattr(self, 'windows_information_protection_policies', n.get_collection_of_object_values(windows_information_protection_policy.WindowsInformationProtectionPolicy)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("androidManagedAppProtections", self.android_managed_app_protections)
        writer.write_collection_of_object_values("defaultManagedAppProtections", self.default_managed_app_protections)
        writer.write_collection_of_object_values("iosManagedAppProtections", self.ios_managed_app_protections)
        writer.write_bool_value("isEnabledForMicrosoftStoreForBusiness", self.is_enabled_for_microsoft_store_for_business)
        writer.write_collection_of_object_values("managedAppPolicies", self.managed_app_policies)
        writer.write_collection_of_object_values("managedAppRegistrations", self.managed_app_registrations)
        writer.write_collection_of_object_values("managedAppStatuses", self.managed_app_statuses)
        writer.write_collection_of_object_values("managedEBooks", self.managed_e_books)
        writer.write_collection_of_object_values("mdmWindowsInformationProtectionPolicies", self.mdm_windows_information_protection_policies)
        writer.write_str_value("microsoftStoreForBusinessLanguage", self.microsoft_store_for_business_language)
        writer.write_datetime_value("microsoftStoreForBusinessLastCompletedApplicationSyncTime", self.microsoft_store_for_business_last_completed_application_sync_time)
        writer.write_datetime_value("microsoftStoreForBusinessLastSuccessfulSyncDateTime", self.microsoft_store_for_business_last_successful_sync_date_time)
        writer.write_collection_of_object_values("mobileApps", self.mobile_apps)
        writer.write_collection_of_object_values("mobileAppCategories", self.mobile_app_categories)
        writer.write_collection_of_object_values("mobileAppConfigurations", self.mobile_app_configurations)
        writer.write_collection_of_object_values("targetedManagedAppConfigurations", self.targeted_managed_app_configurations)
        writer.write_collection_of_object_values("vppTokens", self.vpp_tokens)
        writer.write_collection_of_object_values("windowsInformationProtectionPolicies", self.windows_information_protection_policies)
    

