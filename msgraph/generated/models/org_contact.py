from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .on_premises_provisioning_error import OnPremisesProvisioningError
    from .on_premises_sync_behavior import OnPremisesSyncBehavior
    from .phone import Phone
    from .physical_office_address import PhysicalOfficeAddress
    from .service_provisioning_error import ServiceProvisioningError

from .directory_object import DirectoryObject

@dataclass
class OrgContact(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.orgContact"
    # Postal addresses for this organizational contact. For now a contact can only have one physical address.
    addresses: Optional[list[PhysicalOfficeAddress]] = None
    # Name of the company that this organizational contact belongs to.  Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq for null values).
    company_name: Optional[str] = None
    # The name for the department in which the contact works.  Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq for null values).
    department: Optional[str] = None
    # The contact's direct reports. (The users and contacts that have their manager property set to this contact.)  Read-only. Nullable. Supports $expand.
    direct_reports: Optional[list[DirectoryObject]] = None
    # Display name for this organizational contact. Maximum length is 256 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq for null values), $search, and $orderby.
    display_name: Optional[str] = None
    # First name for this organizational contact. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq for null values).
    given_name: Optional[str] = None
    # Job title for this organizational contact. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq for null values).
    job_title: Optional[str] = None
    # The SMTP address for the contact, for example, 'jeff@contoso.com'. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq for null values).
    mail: Optional[str] = None
    # Email alias (portion of email address pre-pending the @ symbol) for this organizational contact. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq for null values).
    mail_nickname: Optional[str] = None
    # The user or contact that is this contact's manager. Read-only. Supports $expand and $filter (eq) by id.
    manager: Optional[DirectoryObject] = None
    # Groups that this contact is a member of. Read-only. Nullable. Supports $expand.
    member_of: Optional[list[DirectoryObject]] = None
    # Date and time when this organizational contact was last synchronized from on-premises AD. This date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, not, ge, le, in).
    on_premises_last_sync_date_time: Optional[datetime.datetime] = None
    # List of any synchronization provisioning errors for this organizational contact. Supports $filter (eq, not for category and propertyCausingError), /$count eq 0, /$count ne 0.
    on_premises_provisioning_errors: Optional[list[OnPremisesProvisioningError]] = None
    # The onPremisesSyncBehavior property
    on_premises_sync_behavior: Optional[OnPremisesSyncBehavior] = None
    # true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced and now mastered in Exchange; null if this object has never been synced from an on-premises directory (default).   Supports $filter (eq, ne, not, in, and eq for null values).
    on_premises_sync_enabled: Optional[bool] = None
    # List of phones for this organizational contact. Phone types can be mobile, business, and businessFax. Only one of each type can ever be present in the collection.
    phones: Optional[list[Phone]] = None
    # For example: 'SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com'. The any operator is required for filter expressions on multi-valued properties. Supports $filter (eq, not, ge, le, startsWith, /$count eq 0, /$count ne 0).
    proxy_addresses: Optional[list[str]] = None
    # Errors published by a federated service describing a non-transient, service-specific error regarding the properties or link from an organizational contact object .  Supports $filter (eq, not, for isResolved and serviceInstance).
    service_provisioning_errors: Optional[list[ServiceProvisioningError]] = None
    # Last name for this organizational contact. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq for null values).
    surname: Optional[str] = None
    # Groups that this contact is a member of, including groups that the contact is nested under. Read-only. Nullable.
    transitive_member_of: Optional[list[DirectoryObject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrgContact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrgContact
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrgContact()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .on_premises_provisioning_error import OnPremisesProvisioningError
        from .on_premises_sync_behavior import OnPremisesSyncBehavior
        from .phone import Phone
        from .physical_office_address import PhysicalOfficeAddress
        from .service_provisioning_error import ServiceProvisioningError

        from .directory_object import DirectoryObject
        from .on_premises_provisioning_error import OnPremisesProvisioningError
        from .on_premises_sync_behavior import OnPremisesSyncBehavior
        from .phone import Phone
        from .physical_office_address import PhysicalOfficeAddress
        from .service_provisioning_error import ServiceProvisioningError

        fields: dict[str, Callable[[Any], None]] = {
            "addresses": lambda n : setattr(self, 'addresses', n.get_collection_of_object_values(PhysicalOfficeAddress)),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "directReports": lambda n : setattr(self, 'direct_reports', n.get_collection_of_object_values(DirectoryObject)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "mail": lambda n : setattr(self, 'mail', n.get_str_value()),
            "mailNickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "manager": lambda n : setattr(self, 'manager', n.get_object_value(DirectoryObject)),
            "memberOf": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(DirectoryObject)),
            "onPremisesLastSyncDateTime": lambda n : setattr(self, 'on_premises_last_sync_date_time', n.get_datetime_value()),
            "onPremisesProvisioningErrors": lambda n : setattr(self, 'on_premises_provisioning_errors', n.get_collection_of_object_values(OnPremisesProvisioningError)),
            "onPremisesSyncBehavior": lambda n : setattr(self, 'on_premises_sync_behavior', n.get_object_value(OnPremisesSyncBehavior)),
            "onPremisesSyncEnabled": lambda n : setattr(self, 'on_premises_sync_enabled', n.get_bool_value()),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(Phone)),
            "proxyAddresses": lambda n : setattr(self, 'proxy_addresses', n.get_collection_of_primitive_values(str)),
            "serviceProvisioningErrors": lambda n : setattr(self, 'service_provisioning_errors', n.get_collection_of_object_values(ServiceProvisioningError)),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "transitiveMemberOf": lambda n : setattr(self, 'transitive_member_of', n.get_collection_of_object_values(DirectoryObject)),
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
        writer.write_collection_of_object_values("addresses", self.addresses)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("department", self.department)
        writer.write_collection_of_object_values("directReports", self.direct_reports)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("givenName", self.given_name)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_str_value("mail", self.mail)
        writer.write_str_value("mailNickname", self.mail_nickname)
        writer.write_object_value("manager", self.manager)
        writer.write_collection_of_object_values("memberOf", self.member_of)
        writer.write_datetime_value("onPremisesLastSyncDateTime", self.on_premises_last_sync_date_time)
        writer.write_collection_of_object_values("onPremisesProvisioningErrors", self.on_premises_provisioning_errors)
        writer.write_object_value("onPremisesSyncBehavior", self.on_premises_sync_behavior)
        writer.write_bool_value("onPremisesSyncEnabled", self.on_premises_sync_enabled)
        writer.write_collection_of_object_values("phones", self.phones)
        writer.write_collection_of_primitive_values("proxyAddresses", self.proxy_addresses)
        writer.write_collection_of_object_values("serviceProvisioningErrors", self.service_provisioning_errors)
        writer.write_str_value("surname", self.surname)
        writer.write_collection_of_object_values("transitiveMemberOf", self.transitive_member_of)
    

