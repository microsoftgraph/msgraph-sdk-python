from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')
on_premises_provisioning_error = lazy_import('msgraph.generated.models.on_premises_provisioning_error')
phone = lazy_import('msgraph.generated.models.phone')
physical_office_address = lazy_import('msgraph.generated.models.physical_office_address')

class OrgContact(directory_object.DirectoryObject):
    @property
    def addresses(self,) -> Optional[List[physical_office_address.PhysicalOfficeAddress]]:
        """
        Gets the addresses property value. The addresses property
        Returns: Optional[List[physical_office_address.PhysicalOfficeAddress]]
        """
        return self._addresses
    
    @addresses.setter
    def addresses(self,value: Optional[List[physical_office_address.PhysicalOfficeAddress]] = None) -> None:
        """
        Sets the addresses property value. The addresses property
        Args:
            value: Value to set for the addresses property.
        """
        self._addresses = value
    
    @property
    def company_name(self,) -> Optional[str]:
        """
        Gets the companyName property value. The companyName property
        Returns: Optional[str]
        """
        return self._company_name
    
    @company_name.setter
    def company_name(self,value: Optional[str] = None) -> None:
        """
        Sets the companyName property value. The companyName property
        Args:
            value: Value to set for the companyName property.
        """
        self._company_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new OrgContact and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.orgContact"
        # The addresses property
        self._addresses: Optional[List[physical_office_address.PhysicalOfficeAddress]] = None
        # The companyName property
        self._company_name: Optional[str] = None
        # The department property
        self._department: Optional[str] = None
        # The directReports property
        self._direct_reports: Optional[List[directory_object.DirectoryObject]] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The givenName property
        self._given_name: Optional[str] = None
        # The jobTitle property
        self._job_title: Optional[str] = None
        # The mail property
        self._mail: Optional[str] = None
        # The mailNickname property
        self._mail_nickname: Optional[str] = None
        # The manager property
        self._manager: Optional[directory_object.DirectoryObject] = None
        # The memberOf property
        self._member_of: Optional[List[directory_object.DirectoryObject]] = None
        # The onPremisesLastSyncDateTime property
        self._on_premises_last_sync_date_time: Optional[datetime] = None
        # The onPremisesProvisioningErrors property
        self._on_premises_provisioning_errors: Optional[List[on_premises_provisioning_error.OnPremisesProvisioningError]] = None
        # The onPremisesSyncEnabled property
        self._on_premises_sync_enabled: Optional[bool] = None
        # The phones property
        self._phones: Optional[List[phone.Phone]] = None
        # The proxyAddresses property
        self._proxy_addresses: Optional[List[str]] = None
        # The surname property
        self._surname: Optional[str] = None
        # The transitiveMemberOf property
        self._transitive_member_of: Optional[List[directory_object.DirectoryObject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OrgContact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OrgContact
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OrgContact()
    
    @property
    def department(self,) -> Optional[str]:
        """
        Gets the department property value. The department property
        Returns: Optional[str]
        """
        return self._department
    
    @department.setter
    def department(self,value: Optional[str] = None) -> None:
        """
        Sets the department property value. The department property
        Args:
            value: Value to set for the department property.
        """
        self._department = value
    
    @property
    def direct_reports(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the directReports property value. The directReports property
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._direct_reports
    
    @direct_reports.setter
    def direct_reports(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the directReports property value. The directReports property
        Args:
            value: Value to set for the directReports property.
        """
        self._direct_reports = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "addresses": lambda n : setattr(self, 'addresses', n.get_collection_of_object_values(physical_office_address.PhysicalOfficeAddress)),
            "company_name": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "direct_reports": lambda n : setattr(self, 'direct_reports', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "given_name": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "job_title": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "mail": lambda n : setattr(self, 'mail', n.get_str_value()),
            "mail_nickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "manager": lambda n : setattr(self, 'manager', n.get_object_value(directory_object.DirectoryObject)),
            "member_of": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "on_premises_last_sync_date_time": lambda n : setattr(self, 'on_premises_last_sync_date_time', n.get_datetime_value()),
            "on_premises_provisioning_errors": lambda n : setattr(self, 'on_premises_provisioning_errors', n.get_collection_of_object_values(on_premises_provisioning_error.OnPremisesProvisioningError)),
            "on_premises_sync_enabled": lambda n : setattr(self, 'on_premises_sync_enabled', n.get_bool_value()),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(phone.Phone)),
            "proxy_addresses": lambda n : setattr(self, 'proxy_addresses', n.get_collection_of_primitive_values(str)),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "transitive_member_of": lambda n : setattr(self, 'transitive_member_of', n.get_collection_of_object_values(directory_object.DirectoryObject)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def given_name(self,) -> Optional[str]:
        """
        Gets the givenName property value. The givenName property
        Returns: Optional[str]
        """
        return self._given_name
    
    @given_name.setter
    def given_name(self,value: Optional[str] = None) -> None:
        """
        Sets the givenName property value. The givenName property
        Args:
            value: Value to set for the givenName property.
        """
        self._given_name = value
    
    @property
    def job_title(self,) -> Optional[str]:
        """
        Gets the jobTitle property value. The jobTitle property
        Returns: Optional[str]
        """
        return self._job_title
    
    @job_title.setter
    def job_title(self,value: Optional[str] = None) -> None:
        """
        Sets the jobTitle property value. The jobTitle property
        Args:
            value: Value to set for the jobTitle property.
        """
        self._job_title = value
    
    @property
    def mail(self,) -> Optional[str]:
        """
        Gets the mail property value. The mail property
        Returns: Optional[str]
        """
        return self._mail
    
    @mail.setter
    def mail(self,value: Optional[str] = None) -> None:
        """
        Sets the mail property value. The mail property
        Args:
            value: Value to set for the mail property.
        """
        self._mail = value
    
    @property
    def mail_nickname(self,) -> Optional[str]:
        """
        Gets the mailNickname property value. The mailNickname property
        Returns: Optional[str]
        """
        return self._mail_nickname
    
    @mail_nickname.setter
    def mail_nickname(self,value: Optional[str] = None) -> None:
        """
        Sets the mailNickname property value. The mailNickname property
        Args:
            value: Value to set for the mailNickname property.
        """
        self._mail_nickname = value
    
    @property
    def manager(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the manager property value. The manager property
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._manager
    
    @manager.setter
    def manager(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the manager property value. The manager property
        Args:
            value: Value to set for the manager property.
        """
        self._manager = value
    
    @property
    def member_of(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the memberOf property value. The memberOf property
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._member_of
    
    @member_of.setter
    def member_of(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the memberOf property value. The memberOf property
        Args:
            value: Value to set for the memberOf property.
        """
        self._member_of = value
    
    @property
    def on_premises_last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the onPremisesLastSyncDateTime property value. The onPremisesLastSyncDateTime property
        Returns: Optional[datetime]
        """
        return self._on_premises_last_sync_date_time
    
    @on_premises_last_sync_date_time.setter
    def on_premises_last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the onPremisesLastSyncDateTime property value. The onPremisesLastSyncDateTime property
        Args:
            value: Value to set for the onPremisesLastSyncDateTime property.
        """
        self._on_premises_last_sync_date_time = value
    
    @property
    def on_premises_provisioning_errors(self,) -> Optional[List[on_premises_provisioning_error.OnPremisesProvisioningError]]:
        """
        Gets the onPremisesProvisioningErrors property value. The onPremisesProvisioningErrors property
        Returns: Optional[List[on_premises_provisioning_error.OnPremisesProvisioningError]]
        """
        return self._on_premises_provisioning_errors
    
    @on_premises_provisioning_errors.setter
    def on_premises_provisioning_errors(self,value: Optional[List[on_premises_provisioning_error.OnPremisesProvisioningError]] = None) -> None:
        """
        Sets the onPremisesProvisioningErrors property value. The onPremisesProvisioningErrors property
        Args:
            value: Value to set for the onPremisesProvisioningErrors property.
        """
        self._on_premises_provisioning_errors = value
    
    @property
    def on_premises_sync_enabled(self,) -> Optional[bool]:
        """
        Gets the onPremisesSyncEnabled property value. The onPremisesSyncEnabled property
        Returns: Optional[bool]
        """
        return self._on_premises_sync_enabled
    
    @on_premises_sync_enabled.setter
    def on_premises_sync_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the onPremisesSyncEnabled property value. The onPremisesSyncEnabled property
        Args:
            value: Value to set for the onPremisesSyncEnabled property.
        """
        self._on_premises_sync_enabled = value
    
    @property
    def phones(self,) -> Optional[List[phone.Phone]]:
        """
        Gets the phones property value. The phones property
        Returns: Optional[List[phone.Phone]]
        """
        return self._phones
    
    @phones.setter
    def phones(self,value: Optional[List[phone.Phone]] = None) -> None:
        """
        Sets the phones property value. The phones property
        Args:
            value: Value to set for the phones property.
        """
        self._phones = value
    
    @property
    def proxy_addresses(self,) -> Optional[List[str]]:
        """
        Gets the proxyAddresses property value. The proxyAddresses property
        Returns: Optional[List[str]]
        """
        return self._proxy_addresses
    
    @proxy_addresses.setter
    def proxy_addresses(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the proxyAddresses property value. The proxyAddresses property
        Args:
            value: Value to set for the proxyAddresses property.
        """
        self._proxy_addresses = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
        writer.write_bool_value("onPremisesSyncEnabled", self.on_premises_sync_enabled)
        writer.write_collection_of_object_values("phones", self.phones)
        writer.write_collection_of_primitive_values("proxyAddresses", self.proxy_addresses)
        writer.write_str_value("surname", self.surname)
        writer.write_collection_of_object_values("transitiveMemberOf", self.transitive_member_of)
    
    @property
    def surname(self,) -> Optional[str]:
        """
        Gets the surname property value. The surname property
        Returns: Optional[str]
        """
        return self._surname
    
    @surname.setter
    def surname(self,value: Optional[str] = None) -> None:
        """
        Sets the surname property value. The surname property
        Args:
            value: Value to set for the surname property.
        """
        self._surname = value
    
    @property
    def transitive_member_of(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the transitiveMemberOf property value. The transitiveMemberOf property
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._transitive_member_of
    
    @transitive_member_of.setter
    def transitive_member_of(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the transitiveMemberOf property value. The transitiveMemberOf property
        Args:
            value: Value to set for the transitiveMemberOf property.
        """
        self._transitive_member_of = value
    

