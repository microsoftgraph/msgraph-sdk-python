from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .domain_dns_record import DomainDnsRecord
    from .domain_state import DomainState
    from .entity import Entity
    from .internal_domain_federation import InternalDomainFederation

from .entity import Entity

@dataclass
class Domain(Entity, Parsable):
    # Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Microsoft Entra ID performs user authentication. Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. Not nullable.  To update this property in delegated scenarios, the calling app must be assigned the Domain-InternalFederation.ReadWrite.All permission.
    authentication_type: Optional[str] = None
    # This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.
    availability_status: Optional[str] = None
    # The objects such as users and groups that reference the domain ID. Read-only, Nullable. Doesn't support $expand. Supports $filter by the OData type of objects returned. For example, /domains/{domainId}/domainNameReferences/microsoft.graph.user and /domains/{domainId}/domainNameReferences/microsoft.graph.group.
    domain_name_references: Optional[list[DirectoryObject]] = None
    # Domain settings configured by a customer when federated with Microsoft Entra ID. Doesn't support $expand.
    federation_configuration: Optional[list[InternalDomainFederation]] = None
    # The value of the property is false if the DNS record management of the domain is delegated to Microsoft 365. Otherwise, the value is true. Not nullable
    is_admin_managed: Optional[bool] = None
    # true if this is the default domain that is used for user creation. There's only one default domain per company. Not nullable.
    is_default: Optional[bool] = None
    # true if this is the initial domain created by Microsoft Online Services (contoso.com). There's only one initial domain per company. Not nullable
    is_initial: Optional[bool] = None
    # true if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable.
    is_root: Optional[bool] = None
    # true if the domain completed domain ownership verification. Not nullable.
    is_verified: Optional[bool] = None
    # The manufacturer property
    manufacturer: Optional[str] = None
    # The model property
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the number of days before a user receives notification that their password expires. If the property isn't set, a default value of 14 days is used.
    password_notification_window_in_days: Optional[int] = None
    # Specifies the length of time that a password is valid before it must be changed. If the property isn't set, a default value of 90 days is used.
    password_validity_period_in_days: Optional[int] = None
    # Root domain of a subdomain. Read-only, Nullable. Supports $expand.
    root_domain: Optional[Domain] = None
    # DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services. Read-only, Nullable. Doesn't support $expand.
    service_configuration_records: Optional[list[DomainDnsRecord]] = None
    # Status of asynchronous operations scheduled for the domain.
    state: Optional[DomainState] = None
    # The capabilities assigned to the domain. Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune. The values that you can add or remove using the API include: Email, OfficeCommunicationsOnline, Yammer. Not nullable.
    supported_services: Optional[list[str]] = None
    # DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Microsoft Entra ID. Read-only, Nullable. Doesn't support $expand.
    verification_dns_records: Optional[list[DomainDnsRecord]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Domain:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Domain
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Domain()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .domain_dns_record import DomainDnsRecord
        from .domain_state import DomainState
        from .entity import Entity
        from .internal_domain_federation import InternalDomainFederation

        from .directory_object import DirectoryObject
        from .domain_dns_record import DomainDnsRecord
        from .domain_state import DomainState
        from .entity import Entity
        from .internal_domain_federation import InternalDomainFederation

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationType": lambda n : setattr(self, 'authentication_type', n.get_str_value()),
            "availabilityStatus": lambda n : setattr(self, 'availability_status', n.get_str_value()),
            "domainNameReferences": lambda n : setattr(self, 'domain_name_references', n.get_collection_of_object_values(DirectoryObject)),
            "federationConfiguration": lambda n : setattr(self, 'federation_configuration', n.get_collection_of_object_values(InternalDomainFederation)),
            "isAdminManaged": lambda n : setattr(self, 'is_admin_managed', n.get_bool_value()),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "isInitial": lambda n : setattr(self, 'is_initial', n.get_bool_value()),
            "isRoot": lambda n : setattr(self, 'is_root', n.get_bool_value()),
            "isVerified": lambda n : setattr(self, 'is_verified', n.get_bool_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "passwordNotificationWindowInDays": lambda n : setattr(self, 'password_notification_window_in_days', n.get_int_value()),
            "passwordValidityPeriodInDays": lambda n : setattr(self, 'password_validity_period_in_days', n.get_int_value()),
            "rootDomain": lambda n : setattr(self, 'root_domain', n.get_object_value(Domain)),
            "serviceConfigurationRecords": lambda n : setattr(self, 'service_configuration_records', n.get_collection_of_object_values(DomainDnsRecord)),
            "state": lambda n : setattr(self, 'state', n.get_object_value(DomainState)),
            "supportedServices": lambda n : setattr(self, 'supported_services', n.get_collection_of_primitive_values(str)),
            "verificationDnsRecords": lambda n : setattr(self, 'verification_dns_records', n.get_collection_of_object_values(DomainDnsRecord)),
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
        writer.write_str_value("authenticationType", self.authentication_type)
        writer.write_str_value("availabilityStatus", self.availability_status)
        writer.write_collection_of_object_values("domainNameReferences", self.domain_name_references)
        writer.write_collection_of_object_values("federationConfiguration", self.federation_configuration)
        writer.write_bool_value("isAdminManaged", self.is_admin_managed)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isInitial", self.is_initial)
        writer.write_bool_value("isRoot", self.is_root)
        writer.write_bool_value("isVerified", self.is_verified)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_int_value("passwordNotificationWindowInDays", self.password_notification_window_in_days)
        writer.write_int_value("passwordValidityPeriodInDays", self.password_validity_period_in_days)
        writer.write_object_value("rootDomain", self.root_domain)
        writer.write_collection_of_object_values("serviceConfigurationRecords", self.service_configuration_records)
        writer.write_object_value("state", self.state)
        writer.write_collection_of_primitive_values("supportedServices", self.supported_services)
        writer.write_collection_of_object_values("verificationDnsRecords", self.verification_dns_records)
    

