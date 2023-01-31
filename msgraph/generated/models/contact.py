from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

email_address = lazy_import('msgraph.generated.models.email_address')
extension = lazy_import('msgraph.generated.models.extension')
multi_value_legacy_extended_property = lazy_import('msgraph.generated.models.multi_value_legacy_extended_property')
outlook_item = lazy_import('msgraph.generated.models.outlook_item')
physical_address = lazy_import('msgraph.generated.models.physical_address')
profile_photo = lazy_import('msgraph.generated.models.profile_photo')
single_value_legacy_extended_property = lazy_import('msgraph.generated.models.single_value_legacy_extended_property')

class Contact(outlook_item.OutlookItem):
    @property
    def assistant_name(self,) -> Optional[str]:
        """
        Gets the assistantName property value. The name of the contact's assistant.
        Returns: Optional[str]
        """
        return self._assistant_name
    
    @assistant_name.setter
    def assistant_name(self,value: Optional[str] = None) -> None:
        """
        Sets the assistantName property value. The name of the contact's assistant.
        Args:
            value: Value to set for the assistantName property.
        """
        self._assistant_name = value
    
    @property
    def birthday(self,) -> Optional[datetime]:
        """
        Gets the birthday property value. The contact's birthday. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._birthday
    
    @birthday.setter
    def birthday(self,value: Optional[datetime] = None) -> None:
        """
        Sets the birthday property value. The contact's birthday. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the birthday property.
        """
        self._birthday = value
    
    @property
    def business_address(self,) -> Optional[physical_address.PhysicalAddress]:
        """
        Gets the businessAddress property value. The contact's business address.
        Returns: Optional[physical_address.PhysicalAddress]
        """
        return self._business_address
    
    @business_address.setter
    def business_address(self,value: Optional[physical_address.PhysicalAddress] = None) -> None:
        """
        Sets the businessAddress property value. The contact's business address.
        Args:
            value: Value to set for the businessAddress property.
        """
        self._business_address = value
    
    @property
    def business_home_page(self,) -> Optional[str]:
        """
        Gets the businessHomePage property value. The business home page of the contact.
        Returns: Optional[str]
        """
        return self._business_home_page
    
    @business_home_page.setter
    def business_home_page(self,value: Optional[str] = None) -> None:
        """
        Sets the businessHomePage property value. The business home page of the contact.
        Args:
            value: Value to set for the businessHomePage property.
        """
        self._business_home_page = value
    
    @property
    def business_phones(self,) -> Optional[List[str]]:
        """
        Gets the businessPhones property value. The contact's business phone numbers.
        Returns: Optional[List[str]]
        """
        return self._business_phones
    
    @business_phones.setter
    def business_phones(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the businessPhones property value. The contact's business phone numbers.
        Args:
            value: Value to set for the businessPhones property.
        """
        self._business_phones = value
    
    @property
    def children(self,) -> Optional[List[str]]:
        """
        Gets the children property value. The names of the contact's children.
        Returns: Optional[List[str]]
        """
        return self._children
    
    @children.setter
    def children(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the children property value. The names of the contact's children.
        Args:
            value: Value to set for the children property.
        """
        self._children = value
    
    @property
    def company_name(self,) -> Optional[str]:
        """
        Gets the companyName property value. The name of the contact's company.
        Returns: Optional[str]
        """
        return self._company_name
    
    @company_name.setter
    def company_name(self,value: Optional[str] = None) -> None:
        """
        Sets the companyName property value. The name of the contact's company.
        Args:
            value: Value to set for the companyName property.
        """
        self._company_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Contact and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.contact"
        # The name of the contact's assistant.
        self._assistant_name: Optional[str] = None
        # The contact's birthday. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._birthday: Optional[datetime] = None
        # The contact's business address.
        self._business_address: Optional[physical_address.PhysicalAddress] = None
        # The business home page of the contact.
        self._business_home_page: Optional[str] = None
        # The contact's business phone numbers.
        self._business_phones: Optional[List[str]] = None
        # The names of the contact's children.
        self._children: Optional[List[str]] = None
        # The name of the contact's company.
        self._company_name: Optional[str] = None
        # The contact's department.
        self._department: Optional[str] = None
        # The contact's display name. You can specify the display name in a create or update operation. Note that later updates to other properties may cause an automatically generated value to overwrite the displayName value you have specified. To preserve a pre-existing value, always include it as displayName in an update operation.
        self._display_name: Optional[str] = None
        # The contact's email addresses.
        self._email_addresses: Optional[List[email_address.EmailAddress]] = None
        # The collection of open extensions defined for the contact. Read-only. Nullable.
        self._extensions: Optional[List[extension.Extension]] = None
        # The name the contact is filed under.
        self._file_as: Optional[str] = None
        # The contact's generation.
        self._generation: Optional[str] = None
        # The contact's given name.
        self._given_name: Optional[str] = None
        # The contact's home address.
        self._home_address: Optional[physical_address.PhysicalAddress] = None
        # The contact's home phone numbers.
        self._home_phones: Optional[List[str]] = None
        self._im_addresses: Optional[List[str]] = None
        self._initials: Optional[str] = None
        self._job_title: Optional[str] = None
        self._manager: Optional[str] = None
        self._middle_name: Optional[str] = None
        self._mobile_phone: Optional[str] = None
        # The collection of multi-value extended properties defined for the contact. Read-only. Nullable.
        self._multi_value_extended_properties: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None
        self._nick_name: Optional[str] = None
        self._office_location: Optional[str] = None
        self._other_address: Optional[physical_address.PhysicalAddress] = None
        self._parent_folder_id: Optional[str] = None
        self._personal_notes: Optional[str] = None
        # Optional contact picture. You can get or set a photo for a contact.
        self._photo: Optional[profile_photo.ProfilePhoto] = None
        self._profession: Optional[str] = None
        # The collection of single-value extended properties defined for the contact. Read-only. Nullable.
        self._single_value_extended_properties: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None
        self._spouse_name: Optional[str] = None
        self._surname: Optional[str] = None
        self._title: Optional[str] = None
        self._yomi_company_name: Optional[str] = None
        self._yomi_given_name: Optional[str] = None
        self._yomi_surname: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Contact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Contact
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Contact()
    
    @property
    def department(self,) -> Optional[str]:
        """
        Gets the department property value. The contact's department.
        Returns: Optional[str]
        """
        return self._department
    
    @department.setter
    def department(self,value: Optional[str] = None) -> None:
        """
        Sets the department property value. The contact's department.
        Args:
            value: Value to set for the department property.
        """
        self._department = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The contact's display name. You can specify the display name in a create or update operation. Note that later updates to other properties may cause an automatically generated value to overwrite the displayName value you have specified. To preserve a pre-existing value, always include it as displayName in an update operation.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The contact's display name. You can specify the display name in a create or update operation. Note that later updates to other properties may cause an automatically generated value to overwrite the displayName value you have specified. To preserve a pre-existing value, always include it as displayName in an update operation.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def email_addresses(self,) -> Optional[List[email_address.EmailAddress]]:
        """
        Gets the emailAddresses property value. The contact's email addresses.
        Returns: Optional[List[email_address.EmailAddress]]
        """
        return self._email_addresses
    
    @email_addresses.setter
    def email_addresses(self,value: Optional[List[email_address.EmailAddress]] = None) -> None:
        """
        Sets the emailAddresses property value. The contact's email addresses.
        Args:
            value: Value to set for the emailAddresses property.
        """
        self._email_addresses = value
    
    @property
    def extensions(self,) -> Optional[List[extension.Extension]]:
        """
        Gets the extensions property value. The collection of open extensions defined for the contact. Read-only. Nullable.
        Returns: Optional[List[extension.Extension]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[extension.Extension]] = None) -> None:
        """
        Sets the extensions property value. The collection of open extensions defined for the contact. Read-only. Nullable.
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    @property
    def file_as(self,) -> Optional[str]:
        """
        Gets the fileAs property value. The name the contact is filed under.
        Returns: Optional[str]
        """
        return self._file_as
    
    @file_as.setter
    def file_as(self,value: Optional[str] = None) -> None:
        """
        Sets the fileAs property value. The name the contact is filed under.
        Args:
            value: Value to set for the fileAs property.
        """
        self._file_as = value
    
    @property
    def generation(self,) -> Optional[str]:
        """
        Gets the generation property value. The contact's generation.
        Returns: Optional[str]
        """
        return self._generation
    
    @generation.setter
    def generation(self,value: Optional[str] = None) -> None:
        """
        Sets the generation property value. The contact's generation.
        Args:
            value: Value to set for the generation property.
        """
        self._generation = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assistantName": lambda n : setattr(self, 'assistant_name', n.get_str_value()),
            "birthday": lambda n : setattr(self, 'birthday', n.get_datetime_value()),
            "businessAddress": lambda n : setattr(self, 'business_address', n.get_object_value(physical_address.PhysicalAddress)),
            "businessHomePage": lambda n : setattr(self, 'business_home_page', n.get_str_value()),
            "businessPhones": lambda n : setattr(self, 'business_phones', n.get_collection_of_primitive_values(str)),
            "children": lambda n : setattr(self, 'children', n.get_collection_of_primitive_values(str)),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "emailAddresses": lambda n : setattr(self, 'email_addresses', n.get_collection_of_object_values(email_address.EmailAddress)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "fileAs": lambda n : setattr(self, 'file_as', n.get_str_value()),
            "generation": lambda n : setattr(self, 'generation', n.get_str_value()),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "homeAddress": lambda n : setattr(self, 'home_address', n.get_object_value(physical_address.PhysicalAddress)),
            "homePhones": lambda n : setattr(self, 'home_phones', n.get_collection_of_primitive_values(str)),
            "imAddresses": lambda n : setattr(self, 'im_addresses', n.get_collection_of_primitive_values(str)),
            "initials": lambda n : setattr(self, 'initials', n.get_str_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "manager": lambda n : setattr(self, 'manager', n.get_str_value()),
            "middleName": lambda n : setattr(self, 'middle_name', n.get_str_value()),
            "mobilePhone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "multiValueExtendedProperties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty)),
            "nickName": lambda n : setattr(self, 'nick_name', n.get_str_value()),
            "officeLocation": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "otherAddress": lambda n : setattr(self, 'other_address', n.get_object_value(physical_address.PhysicalAddress)),
            "parentFolderId": lambda n : setattr(self, 'parent_folder_id', n.get_str_value()),
            "personalNotes": lambda n : setattr(self, 'personal_notes', n.get_str_value()),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(profile_photo.ProfilePhoto)),
            "profession": lambda n : setattr(self, 'profession', n.get_str_value()),
            "singleValueExtendedProperties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(single_value_legacy_extended_property.SingleValueLegacyExtendedProperty)),
            "spouseName": lambda n : setattr(self, 'spouse_name', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "yomiCompanyName": lambda n : setattr(self, 'yomi_company_name', n.get_str_value()),
            "yomiGivenName": lambda n : setattr(self, 'yomi_given_name', n.get_str_value()),
            "yomiSurname": lambda n : setattr(self, 'yomi_surname', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def given_name(self,) -> Optional[str]:
        """
        Gets the givenName property value. The contact's given name.
        Returns: Optional[str]
        """
        return self._given_name
    
    @given_name.setter
    def given_name(self,value: Optional[str] = None) -> None:
        """
        Sets the givenName property value. The contact's given name.
        Args:
            value: Value to set for the givenName property.
        """
        self._given_name = value
    
    @property
    def home_address(self,) -> Optional[physical_address.PhysicalAddress]:
        """
        Gets the homeAddress property value. The contact's home address.
        Returns: Optional[physical_address.PhysicalAddress]
        """
        return self._home_address
    
    @home_address.setter
    def home_address(self,value: Optional[physical_address.PhysicalAddress] = None) -> None:
        """
        Sets the homeAddress property value. The contact's home address.
        Args:
            value: Value to set for the homeAddress property.
        """
        self._home_address = value
    
    @property
    def home_phones(self,) -> Optional[List[str]]:
        """
        Gets the homePhones property value. The contact's home phone numbers.
        Returns: Optional[List[str]]
        """
        return self._home_phones
    
    @home_phones.setter
    def home_phones(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the homePhones property value. The contact's home phone numbers.
        Args:
            value: Value to set for the homePhones property.
        """
        self._home_phones = value
    
    @property
    def im_addresses(self,) -> Optional[List[str]]:
        """
        Gets the imAddresses property value. 
        Returns: Optional[List[str]]
        """
        return self._im_addresses
    
    @im_addresses.setter
    def im_addresses(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the imAddresses property value. 
        Args:
            value: Value to set for the imAddresses property.
        """
        self._im_addresses = value
    
    @property
    def initials(self,) -> Optional[str]:
        """
        Gets the initials property value. 
        Returns: Optional[str]
        """
        return self._initials
    
    @initials.setter
    def initials(self,value: Optional[str] = None) -> None:
        """
        Sets the initials property value. 
        Args:
            value: Value to set for the initials property.
        """
        self._initials = value
    
    @property
    def job_title(self,) -> Optional[str]:
        """
        Gets the jobTitle property value. 
        Returns: Optional[str]
        """
        return self._job_title
    
    @job_title.setter
    def job_title(self,value: Optional[str] = None) -> None:
        """
        Sets the jobTitle property value. 
        Args:
            value: Value to set for the jobTitle property.
        """
        self._job_title = value
    
    @property
    def manager(self,) -> Optional[str]:
        """
        Gets the manager property value. 
        Returns: Optional[str]
        """
        return self._manager
    
    @manager.setter
    def manager(self,value: Optional[str] = None) -> None:
        """
        Sets the manager property value. 
        Args:
            value: Value to set for the manager property.
        """
        self._manager = value
    
    @property
    def middle_name(self,) -> Optional[str]:
        """
        Gets the middleName property value. 
        Returns: Optional[str]
        """
        return self._middle_name
    
    @middle_name.setter
    def middle_name(self,value: Optional[str] = None) -> None:
        """
        Sets the middleName property value. 
        Args:
            value: Value to set for the middleName property.
        """
        self._middle_name = value
    
    @property
    def mobile_phone(self,) -> Optional[str]:
        """
        Gets the mobilePhone property value. 
        Returns: Optional[str]
        """
        return self._mobile_phone
    
    @mobile_phone.setter
    def mobile_phone(self,value: Optional[str] = None) -> None:
        """
        Sets the mobilePhone property value. 
        Args:
            value: Value to set for the mobilePhone property.
        """
        self._mobile_phone = value
    
    @property
    def multi_value_extended_properties(self,) -> Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]:
        """
        Gets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the contact. Read-only. Nullable.
        Returns: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]
        """
        return self._multi_value_extended_properties
    
    @multi_value_extended_properties.setter
    def multi_value_extended_properties(self,value: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the contact. Read-only. Nullable.
        Args:
            value: Value to set for the multiValueExtendedProperties property.
        """
        self._multi_value_extended_properties = value
    
    @property
    def nick_name(self,) -> Optional[str]:
        """
        Gets the nickName property value. 
        Returns: Optional[str]
        """
        return self._nick_name
    
    @nick_name.setter
    def nick_name(self,value: Optional[str] = None) -> None:
        """
        Sets the nickName property value. 
        Args:
            value: Value to set for the nickName property.
        """
        self._nick_name = value
    
    @property
    def office_location(self,) -> Optional[str]:
        """
        Gets the officeLocation property value. 
        Returns: Optional[str]
        """
        return self._office_location
    
    @office_location.setter
    def office_location(self,value: Optional[str] = None) -> None:
        """
        Sets the officeLocation property value. 
        Args:
            value: Value to set for the officeLocation property.
        """
        self._office_location = value
    
    @property
    def other_address(self,) -> Optional[physical_address.PhysicalAddress]:
        """
        Gets the otherAddress property value. 
        Returns: Optional[physical_address.PhysicalAddress]
        """
        return self._other_address
    
    @other_address.setter
    def other_address(self,value: Optional[physical_address.PhysicalAddress] = None) -> None:
        """
        Sets the otherAddress property value. 
        Args:
            value: Value to set for the otherAddress property.
        """
        self._other_address = value
    
    @property
    def parent_folder_id(self,) -> Optional[str]:
        """
        Gets the parentFolderId property value. 
        Returns: Optional[str]
        """
        return self._parent_folder_id
    
    @parent_folder_id.setter
    def parent_folder_id(self,value: Optional[str] = None) -> None:
        """
        Sets the parentFolderId property value. 
        Args:
            value: Value to set for the parentFolderId property.
        """
        self._parent_folder_id = value
    
    @property
    def personal_notes(self,) -> Optional[str]:
        """
        Gets the personalNotes property value. 
        Returns: Optional[str]
        """
        return self._personal_notes
    
    @personal_notes.setter
    def personal_notes(self,value: Optional[str] = None) -> None:
        """
        Sets the personalNotes property value. 
        Args:
            value: Value to set for the personalNotes property.
        """
        self._personal_notes = value
    
    @property
    def photo(self,) -> Optional[profile_photo.ProfilePhoto]:
        """
        Gets the photo property value. Optional contact picture. You can get or set a photo for a contact.
        Returns: Optional[profile_photo.ProfilePhoto]
        """
        return self._photo
    
    @photo.setter
    def photo(self,value: Optional[profile_photo.ProfilePhoto] = None) -> None:
        """
        Sets the photo property value. Optional contact picture. You can get or set a photo for a contact.
        Args:
            value: Value to set for the photo property.
        """
        self._photo = value
    
    @property
    def profession(self,) -> Optional[str]:
        """
        Gets the profession property value. 
        Returns: Optional[str]
        """
        return self._profession
    
    @profession.setter
    def profession(self,value: Optional[str] = None) -> None:
        """
        Sets the profession property value. 
        Args:
            value: Value to set for the profession property.
        """
        self._profession = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("assistantName", self.assistant_name)
        writer.write_datetime_value("birthday", self.birthday)
        writer.write_object_value("businessAddress", self.business_address)
        writer.write_str_value("businessHomePage", self.business_home_page)
        writer.write_collection_of_primitive_values("businessPhones", self.business_phones)
        writer.write_collection_of_primitive_values("children", self.children)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("department", self.department)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("emailAddresses", self.email_addresses)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_str_value("fileAs", self.file_as)
        writer.write_str_value("generation", self.generation)
        writer.write_str_value("givenName", self.given_name)
        writer.write_object_value("homeAddress", self.home_address)
        writer.write_collection_of_primitive_values("homePhones", self.home_phones)
        writer.write_collection_of_primitive_values("imAddresses", self.im_addresses)
        writer.write_str_value("initials", self.initials)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_str_value("manager", self.manager)
        writer.write_str_value("middleName", self.middle_name)
        writer.write_str_value("mobilePhone", self.mobile_phone)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_str_value("nickName", self.nick_name)
        writer.write_str_value("officeLocation", self.office_location)
        writer.write_object_value("otherAddress", self.other_address)
        writer.write_str_value("parentFolderId", self.parent_folder_id)
        writer.write_str_value("personalNotes", self.personal_notes)
        writer.write_object_value("photo", self.photo)
        writer.write_str_value("profession", self.profession)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
        writer.write_str_value("spouseName", self.spouse_name)
        writer.write_str_value("surname", self.surname)
        writer.write_str_value("title", self.title)
        writer.write_str_value("yomiCompanyName", self.yomi_company_name)
        writer.write_str_value("yomiGivenName", self.yomi_given_name)
        writer.write_str_value("yomiSurname", self.yomi_surname)
    
    @property
    def single_value_extended_properties(self,) -> Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]:
        """
        Gets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the contact. Read-only. Nullable.
        Returns: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]
        """
        return self._single_value_extended_properties
    
    @single_value_extended_properties.setter
    def single_value_extended_properties(self,value: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the contact. Read-only. Nullable.
        Args:
            value: Value to set for the singleValueExtendedProperties property.
        """
        self._single_value_extended_properties = value
    
    @property
    def spouse_name(self,) -> Optional[str]:
        """
        Gets the spouseName property value. 
        Returns: Optional[str]
        """
        return self._spouse_name
    
    @spouse_name.setter
    def spouse_name(self,value: Optional[str] = None) -> None:
        """
        Sets the spouseName property value. 
        Args:
            value: Value to set for the spouseName property.
        """
        self._spouse_name = value
    
    @property
    def surname(self,) -> Optional[str]:
        """
        Gets the surname property value. 
        Returns: Optional[str]
        """
        return self._surname
    
    @surname.setter
    def surname(self,value: Optional[str] = None) -> None:
        """
        Sets the surname property value. 
        Args:
            value: Value to set for the surname property.
        """
        self._surname = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. 
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. 
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    
    @property
    def yomi_company_name(self,) -> Optional[str]:
        """
        Gets the yomiCompanyName property value. 
        Returns: Optional[str]
        """
        return self._yomi_company_name
    
    @yomi_company_name.setter
    def yomi_company_name(self,value: Optional[str] = None) -> None:
        """
        Sets the yomiCompanyName property value. 
        Args:
            value: Value to set for the yomiCompanyName property.
        """
        self._yomi_company_name = value
    
    @property
    def yomi_given_name(self,) -> Optional[str]:
        """
        Gets the yomiGivenName property value. 
        Returns: Optional[str]
        """
        return self._yomi_given_name
    
    @yomi_given_name.setter
    def yomi_given_name(self,value: Optional[str] = None) -> None:
        """
        Sets the yomiGivenName property value. 
        Args:
            value: Value to set for the yomiGivenName property.
        """
        self._yomi_given_name = value
    
    @property
    def yomi_surname(self,) -> Optional[str]:
        """
        Gets the yomiSurname property value. 
        Returns: Optional[str]
        """
        return self._yomi_surname
    
    @yomi_surname.setter
    def yomi_surname(self,value: Optional[str] = None) -> None:
        """
        Sets the yomiSurname property value. 
        Args:
            value: Value to set for the yomiSurname property.
        """
        self._yomi_surname = value
    

