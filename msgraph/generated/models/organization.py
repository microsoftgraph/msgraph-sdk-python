from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assigned_plan import AssignedPlan
    from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
    from .directory_object import DirectoryObject
    from .extension import Extension
    from .mdm_authority import MdmAuthority
    from .organizational_branding import OrganizationalBranding
    from .partner_tenant_type import PartnerTenantType
    from .privacy_profile import PrivacyProfile
    from .provisioned_plan import ProvisionedPlan
    from .verified_domain import VerifiedDomain

from .directory_object import DirectoryObject

@dataclass
class Organization(DirectoryObject):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.organization"
    # The collection of service plans associated with the tenant. Not nullable.
    assigned_plans: Optional[List[AssignedPlan]] = None
    # Branding for the organization. Nullable.
    branding: Optional[OrganizationalBranding] = None
    # Telephone number for the organization. Although this is a string collection, only one number can be set for this property.
    business_phones: Optional[List[str]] = None
    # Navigation property to manage certificate-based authentication configuration. Only a single instance of certificateBasedAuthConfiguration can be created in the collection.
    certificate_based_auth_configuration: Optional[List[CertificateBasedAuthConfiguration]] = None
    # City name of the address for the organization.
    city: Optional[str] = None
    # Country/region name of the address for the organization.
    country: Optional[str] = None
    # Country or region abbreviation for the organization in ISO 3166-2 format.
    country_letter_code: Optional[str] = None
    # Timestamp of when the organization was created. The value cannot be modified and is automatically populated when the organization is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Two-letter ISO 3166 country code indicating the default service usage location of an organization.
    default_usage_location: Optional[str] = None
    # The display name for the tenant.
    display_name: Optional[str] = None
    # The collection of open extensions defined for the organization. Read-only. Nullable.
    extensions: Optional[List[Extension]] = None
    # Not nullable.
    marketing_notification_emails: Optional[List[str]] = None
    # Mobile device management authority.
    mobile_device_management_authority: Optional[MdmAuthority] = None
    # The time and date at which the tenant was last synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    on_premises_last_sync_date_time: Optional[datetime.datetime] = None
    # true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced. Nullable. null if this object has never been synced from an on-premises directory (default).
    on_premises_sync_enabled: Optional[bool] = None
    # The type of partnership this tenant has with Microsoft. The possible values are: microsoftSupport, syndicatePartner, breadthPartner, breadthPartnerDelegatedAdmin, resellerPartnerDelegatedAdmin, valueAddedResellerPartnerDelegatedAdmin, unknownFutureValue. Nullable. For more information about the possible types, see partnerTenantType values.
    partner_tenant_type: Optional[PartnerTenantType] = None
    # Postal code of the address for the organization.
    postal_code: Optional[str] = None
    # The preferred language for the organization. Should follow ISO 639-1 Code; for example, en.
    preferred_language: Optional[str] = None
    # The privacy profile of an organization.
    privacy_profile: Optional[PrivacyProfile] = None
    # Not nullable.
    provisioned_plans: Optional[List[ProvisionedPlan]] = None
    # Not nullable.
    security_compliance_notification_mails: Optional[List[str]] = None
    # Not nullable.
    security_compliance_notification_phones: Optional[List[str]] = None
    # State name of the address for the organization.
    state: Optional[str] = None
    # Street name of the address for organization.
    street: Optional[str] = None
    # Not nullable.
    technical_notification_mails: Optional[List[str]] = None
    # Not nullable. The tenant type option that was selected when the tenant was created. The possible values are:  AAD - An enterprise identity access management (IAM) service that serves business-to-employee and business-to-business (B2B) scenarios.  AAD B2C A customer identity access management (CIAM) service that serves business-to-consumer (B2C) scenarios.
    tenant_type: Optional[str] = None
    # The collection of domains associated with this tenant. Not nullable.
    verified_domains: Optional[List[VerifiedDomain]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Organization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Organization
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Organization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .assigned_plan import AssignedPlan
        from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
        from .directory_object import DirectoryObject
        from .extension import Extension
        from .mdm_authority import MdmAuthority
        from .organizational_branding import OrganizationalBranding
        from .partner_tenant_type import PartnerTenantType
        from .privacy_profile import PrivacyProfile
        from .provisioned_plan import ProvisionedPlan
        from .verified_domain import VerifiedDomain

        from .assigned_plan import AssignedPlan
        from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
        from .directory_object import DirectoryObject
        from .extension import Extension
        from .mdm_authority import MdmAuthority
        from .organizational_branding import OrganizationalBranding
        from .partner_tenant_type import PartnerTenantType
        from .privacy_profile import PrivacyProfile
        from .provisioned_plan import ProvisionedPlan
        from .verified_domain import VerifiedDomain

        fields: Dict[str, Callable[[Any], None]] = {
            "assigned_plans": lambda n : setattr(self, 'assigned_plans', n.get_collection_of_object_values(AssignedPlan)),
            "branding": lambda n : setattr(self, 'branding', n.get_object_value(OrganizationalBranding)),
            "business_phones": lambda n : setattr(self, 'business_phones', n.get_collection_of_primitive_values(str)),
            "certificate_based_auth_configuration": lambda n : setattr(self, 'certificate_based_auth_configuration', n.get_collection_of_object_values(CertificateBasedAuthConfiguration)),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "country_letter_code": lambda n : setattr(self, 'country_letter_code', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "default_usage_location": lambda n : setattr(self, 'default_usage_location', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "marketing_notification_emails": lambda n : setattr(self, 'marketing_notification_emails', n.get_collection_of_primitive_values(str)),
            "mobile_device_management_authority": lambda n : setattr(self, 'mobile_device_management_authority', n.get_enum_value(MdmAuthority)),
            "on_premises_last_sync_date_time": lambda n : setattr(self, 'on_premises_last_sync_date_time', n.get_datetime_value()),
            "on_premises_sync_enabled": lambda n : setattr(self, 'on_premises_sync_enabled', n.get_bool_value()),
            "partner_tenant_type": lambda n : setattr(self, 'partner_tenant_type', n.get_enum_value(PartnerTenantType)),
            "postal_code": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "preferred_language": lambda n : setattr(self, 'preferred_language', n.get_str_value()),
            "privacy_profile": lambda n : setattr(self, 'privacy_profile', n.get_object_value(PrivacyProfile)),
            "provisioned_plans": lambda n : setattr(self, 'provisioned_plans', n.get_collection_of_object_values(ProvisionedPlan)),
            "security_compliance_notification_mails": lambda n : setattr(self, 'security_compliance_notification_mails', n.get_collection_of_primitive_values(str)),
            "security_compliance_notification_phones": lambda n : setattr(self, 'security_compliance_notification_phones', n.get_collection_of_primitive_values(str)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "street": lambda n : setattr(self, 'street', n.get_str_value()),
            "technical_notification_mails": lambda n : setattr(self, 'technical_notification_mails', n.get_collection_of_primitive_values(str)),
            "tenant_type": lambda n : setattr(self, 'tenant_type', n.get_str_value()),
            "verified_domains": lambda n : setattr(self, 'verified_domains', n.get_collection_of_object_values(VerifiedDomain)),
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
        writer.write_collection_of_object_values("assigned_plans", self.assigned_plans)
        writer.write_object_value("branding", self.branding)
        writer.write_collection_of_primitive_values("business_phones", self.business_phones)
        writer.write_collection_of_object_values("certificate_based_auth_configuration", self.certificate_based_auth_configuration)
        writer.write_str_value("city", self.city)
        writer.write_str_value("country", self.country)
        writer.write_str_value("country_letter_code", self.country_letter_code)
        writer.write_datetime_value("created_date_time", self.created_date_time)
        writer.write_str_value("default_usage_location", self.default_usage_location)
        writer.write_str_value("display_name", self.display_name)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_collection_of_primitive_values("marketing_notification_emails", self.marketing_notification_emails)
        writer.write_enum_value("mobile_device_management_authority", self.mobile_device_management_authority)
        writer.write_datetime_value("on_premises_last_sync_date_time", self.on_premises_last_sync_date_time)
        writer.write_bool_value("on_premises_sync_enabled", self.on_premises_sync_enabled)
        writer.write_enum_value("partner_tenant_type", self.partner_tenant_type)
        writer.write_str_value("postal_code", self.postal_code)
        writer.write_str_value("preferred_language", self.preferred_language)
        writer.write_object_value("privacy_profile", self.privacy_profile)
        writer.write_collection_of_object_values("provisioned_plans", self.provisioned_plans)
        writer.write_collection_of_primitive_values("security_compliance_notification_mails", self.security_compliance_notification_mails)
        writer.write_collection_of_primitive_values("security_compliance_notification_phones", self.security_compliance_notification_phones)
        writer.write_str_value("state", self.state)
        writer.write_str_value("street", self.street)
        writer.write_collection_of_primitive_values("technical_notification_mails", self.technical_notification_mails)
        writer.write_str_value("tenant_type", self.tenant_type)
        writer.write_collection_of_object_values("verified_domains", self.verified_domains)
    

