from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')
domain_dns_record = lazy_import('msgraph.generated.models.domain_dns_record')
domain_state = lazy_import('msgraph.generated.models.domain_state')
entity = lazy_import('msgraph.generated.models.entity')
internal_domain_federation = lazy_import('msgraph.generated.models.internal_domain_federation')

class Domain(entity.Entity):
    @property
    def authentication_type(self,) -> Optional[str]:
        """
        Gets the authenticationType property value. Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Azure AD performs user authentication. Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. This property is read-only and is not nullable.
        Returns: Optional[str]
        """
        return self._authentication_type
    
    @authentication_type.setter
    def authentication_type(self,value: Optional[str] = None) -> None:
        """
        Sets the authenticationType property value. Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Azure AD performs user authentication. Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. This property is read-only and is not nullable.
        Args:
            value: Value to set for the authenticationType property.
        """
        self._authentication_type = value
    
    @property
    def availability_status(self,) -> Optional[str]:
        """
        Gets the availabilityStatus property value. This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.
        Returns: Optional[str]
        """
        return self._availability_status
    
    @availability_status.setter
    def availability_status(self,value: Optional[str] = None) -> None:
        """
        Sets the availabilityStatus property value. This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.
        Args:
            value: Value to set for the availabilityStatus property.
        """
        self._availability_status = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Domain and sets the default values.
        """
        super().__init__()
        # Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Azure AD performs user authentication. Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. This property is read-only and is not nullable.
        self._authentication_type: Optional[str] = None
        # This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.
        self._availability_status: Optional[str] = None
        # The objects such as users and groups that reference the domain ID. Read-only, Nullable. Supports $expand and $filter by the OData type of objects returned. For example /domains/{domainId}/domainNameReferences/microsoft.graph.user and /domains/{domainId}/domainNameReferences/microsoft.graph.group.
        self._domain_name_references: Optional[List[directory_object.DirectoryObject]] = None
        # Domain settings configured by a customer when federated with Azure AD. Supports $expand.
        self._federation_configuration: Optional[List[internal_domain_federation.InternalDomainFederation]] = None
        # The value of the property is false if the DNS record management of the domain has been delegated to Microsoft 365. Otherwise, the value is true. Not nullable
        self._is_admin_managed: Optional[bool] = None
        # true if this is the default domain that is used for user creation. There is only one default domain per company. Not nullable
        self._is_default: Optional[bool] = None
        # true if this is the initial domain created by Microsoft Online Services (companyname.onmicrosoft.com). There is only one initial domain per company. Not nullable
        self._is_initial: Optional[bool] = None
        # true if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable
        self._is_root: Optional[bool] = None
        # true if the domain has completed domain ownership verification. Not nullable
        self._is_verified: Optional[bool] = None
        # The manufacturer property
        self._manufacturer: Optional[str] = None
        # The model property
        self._model: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Specifies the number of days before a user receives notification that their password will expire. If the property is not set, a default value of 14 days will be used.
        self._password_notification_window_in_days: Optional[int] = None
        # Specifies the length of time that a password is valid before it must be changed. If the property is not set, a default value of 90 days will be used.
        self._password_validity_period_in_days: Optional[int] = None
        # DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services. Read-only, Nullable. Supports $expand.
        self._service_configuration_records: Optional[List[domain_dns_record.DomainDnsRecord]] = None
        # Status of asynchronous operations scheduled for the domain.
        self._state: Optional[domain_state.DomainState] = None
        # The capabilities assigned to the domain. Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune. The values which you can add/remove using Graph API include: Email, OfficeCommunicationsOnline, Yammer. Not nullable.
        self._supported_services: Optional[List[str]] = None
        # DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Azure AD. Read-only, Nullable. Supports $expand.
        self._verification_dns_records: Optional[List[domain_dns_record.DomainDnsRecord]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Domain:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Domain
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Domain()
    
    @property
    def domain_name_references(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the domainNameReferences property value. The objects such as users and groups that reference the domain ID. Read-only, Nullable. Supports $expand and $filter by the OData type of objects returned. For example /domains/{domainId}/domainNameReferences/microsoft.graph.user and /domains/{domainId}/domainNameReferences/microsoft.graph.group.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._domain_name_references
    
    @domain_name_references.setter
    def domain_name_references(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the domainNameReferences property value. The objects such as users and groups that reference the domain ID. Read-only, Nullable. Supports $expand and $filter by the OData type of objects returned. For example /domains/{domainId}/domainNameReferences/microsoft.graph.user and /domains/{domainId}/domainNameReferences/microsoft.graph.group.
        Args:
            value: Value to set for the domainNameReferences property.
        """
        self._domain_name_references = value
    
    @property
    def federation_configuration(self,) -> Optional[List[internal_domain_federation.InternalDomainFederation]]:
        """
        Gets the federationConfiguration property value. Domain settings configured by a customer when federated with Azure AD. Supports $expand.
        Returns: Optional[List[internal_domain_federation.InternalDomainFederation]]
        """
        return self._federation_configuration
    
    @federation_configuration.setter
    def federation_configuration(self,value: Optional[List[internal_domain_federation.InternalDomainFederation]] = None) -> None:
        """
        Sets the federationConfiguration property value. Domain settings configured by a customer when federated with Azure AD. Supports $expand.
        Args:
            value: Value to set for the federationConfiguration property.
        """
        self._federation_configuration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_type": lambda n : setattr(self, 'authentication_type', n.get_str_value()),
            "availability_status": lambda n : setattr(self, 'availability_status', n.get_str_value()),
            "domain_name_references": lambda n : setattr(self, 'domain_name_references', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "federation_configuration": lambda n : setattr(self, 'federation_configuration', n.get_collection_of_object_values(internal_domain_federation.InternalDomainFederation)),
            "is_admin_managed": lambda n : setattr(self, 'is_admin_managed', n.get_bool_value()),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "is_initial": lambda n : setattr(self, 'is_initial', n.get_bool_value()),
            "is_root": lambda n : setattr(self, 'is_root', n.get_bool_value()),
            "is_verified": lambda n : setattr(self, 'is_verified', n.get_bool_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "password_notification_window_in_days": lambda n : setattr(self, 'password_notification_window_in_days', n.get_int_value()),
            "password_validity_period_in_days": lambda n : setattr(self, 'password_validity_period_in_days', n.get_int_value()),
            "service_configuration_records": lambda n : setattr(self, 'service_configuration_records', n.get_collection_of_object_values(domain_dns_record.DomainDnsRecord)),
            "state": lambda n : setattr(self, 'state', n.get_object_value(domain_state.DomainState)),
            "supported_services": lambda n : setattr(self, 'supported_services', n.get_collection_of_primitive_values(str)),
            "verification_dns_records": lambda n : setattr(self, 'verification_dns_records', n.get_collection_of_object_values(domain_dns_record.DomainDnsRecord)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_admin_managed(self,) -> Optional[bool]:
        """
        Gets the isAdminManaged property value. The value of the property is false if the DNS record management of the domain has been delegated to Microsoft 365. Otherwise, the value is true. Not nullable
        Returns: Optional[bool]
        """
        return self._is_admin_managed
    
    @is_admin_managed.setter
    def is_admin_managed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAdminManaged property value. The value of the property is false if the DNS record management of the domain has been delegated to Microsoft 365. Otherwise, the value is true. Not nullable
        Args:
            value: Value to set for the isAdminManaged property.
        """
        self._is_admin_managed = value
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. true if this is the default domain that is used for user creation. There is only one default domain per company. Not nullable
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. true if this is the default domain that is used for user creation. There is only one default domain per company. Not nullable
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def is_initial(self,) -> Optional[bool]:
        """
        Gets the isInitial property value. true if this is the initial domain created by Microsoft Online Services (companyname.onmicrosoft.com). There is only one initial domain per company. Not nullable
        Returns: Optional[bool]
        """
        return self._is_initial
    
    @is_initial.setter
    def is_initial(self,value: Optional[bool] = None) -> None:
        """
        Sets the isInitial property value. true if this is the initial domain created by Microsoft Online Services (companyname.onmicrosoft.com). There is only one initial domain per company. Not nullable
        Args:
            value: Value to set for the isInitial property.
        """
        self._is_initial = value
    
    @property
    def is_root(self,) -> Optional[bool]:
        """
        Gets the isRoot property value. true if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable
        Returns: Optional[bool]
        """
        return self._is_root
    
    @is_root.setter
    def is_root(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRoot property value. true if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable
        Args:
            value: Value to set for the isRoot property.
        """
        self._is_root = value
    
    @property
    def is_verified(self,) -> Optional[bool]:
        """
        Gets the isVerified property value. true if the domain has completed domain ownership verification. Not nullable
        Returns: Optional[bool]
        """
        return self._is_verified
    
    @is_verified.setter
    def is_verified(self,value: Optional[bool] = None) -> None:
        """
        Sets the isVerified property value. true if the domain has completed domain ownership verification. Not nullable
        Args:
            value: Value to set for the isVerified property.
        """
        self._is_verified = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. The manufacturer property
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. The manufacturer property
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. The model property
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. The model property
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def password_notification_window_in_days(self,) -> Optional[int]:
        """
        Gets the passwordNotificationWindowInDays property value. Specifies the number of days before a user receives notification that their password will expire. If the property is not set, a default value of 14 days will be used.
        Returns: Optional[int]
        """
        return self._password_notification_window_in_days
    
    @password_notification_window_in_days.setter
    def password_notification_window_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordNotificationWindowInDays property value. Specifies the number of days before a user receives notification that their password will expire. If the property is not set, a default value of 14 days will be used.
        Args:
            value: Value to set for the passwordNotificationWindowInDays property.
        """
        self._password_notification_window_in_days = value
    
    @property
    def password_validity_period_in_days(self,) -> Optional[int]:
        """
        Gets the passwordValidityPeriodInDays property value. Specifies the length of time that a password is valid before it must be changed. If the property is not set, a default value of 90 days will be used.
        Returns: Optional[int]
        """
        return self._password_validity_period_in_days
    
    @password_validity_period_in_days.setter
    def password_validity_period_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordValidityPeriodInDays property value. Specifies the length of time that a password is valid before it must be changed. If the property is not set, a default value of 90 days will be used.
        Args:
            value: Value to set for the passwordValidityPeriodInDays property.
        """
        self._password_validity_period_in_days = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
        writer.write_collection_of_object_values("serviceConfigurationRecords", self.service_configuration_records)
        writer.write_object_value("state", self.state)
        writer.write_collection_of_primitive_values("supportedServices", self.supported_services)
        writer.write_collection_of_object_values("verificationDnsRecords", self.verification_dns_records)
    
    @property
    def service_configuration_records(self,) -> Optional[List[domain_dns_record.DomainDnsRecord]]:
        """
        Gets the serviceConfigurationRecords property value. DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services. Read-only, Nullable. Supports $expand.
        Returns: Optional[List[domain_dns_record.DomainDnsRecord]]
        """
        return self._service_configuration_records
    
    @service_configuration_records.setter
    def service_configuration_records(self,value: Optional[List[domain_dns_record.DomainDnsRecord]] = None) -> None:
        """
        Sets the serviceConfigurationRecords property value. DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services. Read-only, Nullable. Supports $expand.
        Args:
            value: Value to set for the serviceConfigurationRecords property.
        """
        self._service_configuration_records = value
    
    @property
    def state(self,) -> Optional[domain_state.DomainState]:
        """
        Gets the state property value. Status of asynchronous operations scheduled for the domain.
        Returns: Optional[domain_state.DomainState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[domain_state.DomainState] = None) -> None:
        """
        Sets the state property value. Status of asynchronous operations scheduled for the domain.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def supported_services(self,) -> Optional[List[str]]:
        """
        Gets the supportedServices property value. The capabilities assigned to the domain. Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune. The values which you can add/remove using Graph API include: Email, OfficeCommunicationsOnline, Yammer. Not nullable.
        Returns: Optional[List[str]]
        """
        return self._supported_services
    
    @supported_services.setter
    def supported_services(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the supportedServices property value. The capabilities assigned to the domain. Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune. The values which you can add/remove using Graph API include: Email, OfficeCommunicationsOnline, Yammer. Not nullable.
        Args:
            value: Value to set for the supportedServices property.
        """
        self._supported_services = value
    
    @property
    def verification_dns_records(self,) -> Optional[List[domain_dns_record.DomainDnsRecord]]:
        """
        Gets the verificationDnsRecords property value. DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Azure AD. Read-only, Nullable. Supports $expand.
        Returns: Optional[List[domain_dns_record.DomainDnsRecord]]
        """
        return self._verification_dns_records
    
    @verification_dns_records.setter
    def verification_dns_records(self,value: Optional[List[domain_dns_record.DomainDnsRecord]] = None) -> None:
        """
        Sets the verificationDnsRecords property value. DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Azure AD. Read-only, Nullable. Supports $expand.
        Args:
            value: Value to set for the verificationDnsRecords property.
        """
        self._verification_dns_records = value
    

