from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_address import EmailAddress
    from .extension import Extension
    from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
    from .outlook_item import OutlookItem
    from .physical_address import PhysicalAddress
    from .profile_photo import ProfilePhoto
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

from .outlook_item import OutlookItem

@dataclass
class Contact(OutlookItem):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.contact"
    # The name of the contact's assistant.
    assistant_name: Optional[str] = None
    # The contact's birthday. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    birthday: Optional[datetime.datetime] = None
    # The contact's business address.
    business_address: Optional[PhysicalAddress] = None
    # The business home page of the contact.
    business_home_page: Optional[str] = None
    # The contact's business phone numbers.
    business_phones: Optional[List[str]] = None
    # The names of the contact's children.
    children: Optional[List[str]] = None
    # The name of the contact's company.
    company_name: Optional[str] = None
    # The contact's department.
    department: Optional[str] = None
    # The contact's display name. You can specify the display name in a create or update operation. Note that later updates to other properties may cause an automatically generated value to overwrite the displayName value you have specified. To preserve a pre-existing value, always include it as displayName in an update operation.
    display_name: Optional[str] = None
    # The contact's email addresses.
    email_addresses: Optional[List[EmailAddress]] = None
    # The collection of open extensions defined for the contact. Read-only. Nullable.
    extensions: Optional[List[Extension]] = None
    # The name the contact is filed under.
    file_as: Optional[str] = None
    # The contact's generation.
    generation: Optional[str] = None
    # The contact's given name.
    given_name: Optional[str] = None
    # The contact's home address.
    home_address: Optional[PhysicalAddress] = None
    # The contact's home phone numbers.
    home_phones: Optional[List[str]] = None
    # The imAddresses property
    im_addresses: Optional[List[str]] = None
    # The initials property
    initials: Optional[str] = None
    # The jobTitle property
    job_title: Optional[str] = None
    # The manager property
    manager: Optional[str] = None
    # The middleName property
    middle_name: Optional[str] = None
    # The mobilePhone property
    mobile_phone: Optional[str] = None
    # The collection of multi-value extended properties defined for the contact. Read-only. Nullable.
    multi_value_extended_properties: Optional[List[MultiValueLegacyExtendedProperty]] = None
    # The nickName property
    nick_name: Optional[str] = None
    # The officeLocation property
    office_location: Optional[str] = None
    # The otherAddress property
    other_address: Optional[PhysicalAddress] = None
    # The parentFolderId property
    parent_folder_id: Optional[str] = None
    # The personalNotes property
    personal_notes: Optional[str] = None
    # Optional contact picture. You can get or set a photo for a contact.
    photo: Optional[ProfilePhoto] = None
    # The profession property
    profession: Optional[str] = None
    # The collection of single-value extended properties defined for the contact. Read-only. Nullable.
    single_value_extended_properties: Optional[List[SingleValueLegacyExtendedProperty]] = None
    # The spouseName property
    spouse_name: Optional[str] = None
    # The surname property
    surname: Optional[str] = None
    # The title property
    title: Optional[str] = None
    # The yomiCompanyName property
    yomi_company_name: Optional[str] = None
    # The yomiGivenName property
    yomi_given_name: Optional[str] = None
    # The yomiSurname property
    yomi_surname: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Contact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Contact
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Contact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .email_address import EmailAddress
        from .extension import Extension
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .physical_address import PhysicalAddress
        from .profile_photo import ProfilePhoto
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        from .email_address import EmailAddress
        from .extension import Extension
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .physical_address import PhysicalAddress
        from .profile_photo import ProfilePhoto
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        fields: Dict[str, Callable[[Any], None]] = {
            "assistant_name": lambda n : setattr(self, 'assistant_name', n.get_str_value()),
            "birthday": lambda n : setattr(self, 'birthday', n.get_datetime_value()),
            "business_address": lambda n : setattr(self, 'business_address', n.get_object_value(PhysicalAddress)),
            "business_home_page": lambda n : setattr(self, 'business_home_page', n.get_str_value()),
            "business_phones": lambda n : setattr(self, 'business_phones', n.get_collection_of_primitive_values(str)),
            "children": lambda n : setattr(self, 'children', n.get_collection_of_primitive_values(str)),
            "company_name": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email_addresses": lambda n : setattr(self, 'email_addresses', n.get_collection_of_object_values(EmailAddress)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "file_as": lambda n : setattr(self, 'file_as', n.get_str_value()),
            "generation": lambda n : setattr(self, 'generation', n.get_str_value()),
            "given_name": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "home_address": lambda n : setattr(self, 'home_address', n.get_object_value(PhysicalAddress)),
            "home_phones": lambda n : setattr(self, 'home_phones', n.get_collection_of_primitive_values(str)),
            "im_addresses": lambda n : setattr(self, 'im_addresses', n.get_collection_of_primitive_values(str)),
            "initials": lambda n : setattr(self, 'initials', n.get_str_value()),
            "job_title": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "manager": lambda n : setattr(self, 'manager', n.get_str_value()),
            "middle_name": lambda n : setattr(self, 'middle_name', n.get_str_value()),
            "mobile_phone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "multi_value_extended_properties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(MultiValueLegacyExtendedProperty)),
            "nick_name": lambda n : setattr(self, 'nick_name', n.get_str_value()),
            "office_location": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "other_address": lambda n : setattr(self, 'other_address', n.get_object_value(PhysicalAddress)),
            "parent_folder_id": lambda n : setattr(self, 'parent_folder_id', n.get_str_value()),
            "personal_notes": lambda n : setattr(self, 'personal_notes', n.get_str_value()),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(ProfilePhoto)),
            "profession": lambda n : setattr(self, 'profession', n.get_str_value()),
            "single_value_extended_properties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(SingleValueLegacyExtendedProperty)),
            "spouse_name": lambda n : setattr(self, 'spouse_name', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "yomi_company_name": lambda n : setattr(self, 'yomi_company_name', n.get_str_value()),
            "yomi_given_name": lambda n : setattr(self, 'yomi_given_name', n.get_str_value()),
            "yomi_surname": lambda n : setattr(self, 'yomi_surname', n.get_str_value()),
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
        writer.write_str_value("assistant_name", self.assistant_name)
        writer.write_datetime_value("birthday", self.birthday)
        writer.write_object_value("business_address", self.business_address)
        writer.write_str_value("business_home_page", self.business_home_page)
        writer.write_collection_of_primitive_values("business_phones", self.business_phones)
        writer.write_collection_of_primitive_values("children", self.children)
        writer.write_str_value("company_name", self.company_name)
        writer.write_str_value("department", self.department)
        writer.write_str_value("display_name", self.display_name)
        writer.write_collection_of_object_values("email_addresses", self.email_addresses)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_str_value("file_as", self.file_as)
        writer.write_str_value("generation", self.generation)
        writer.write_str_value("given_name", self.given_name)
        writer.write_object_value("home_address", self.home_address)
        writer.write_collection_of_primitive_values("home_phones", self.home_phones)
        writer.write_collection_of_primitive_values("im_addresses", self.im_addresses)
        writer.write_str_value("initials", self.initials)
        writer.write_str_value("job_title", self.job_title)
        writer.write_str_value("manager", self.manager)
        writer.write_str_value("middle_name", self.middle_name)
        writer.write_str_value("mobile_phone", self.mobile_phone)
        writer.write_collection_of_object_values("multi_value_extended_properties", self.multi_value_extended_properties)
        writer.write_str_value("nick_name", self.nick_name)
        writer.write_str_value("office_location", self.office_location)
        writer.write_object_value("other_address", self.other_address)
        writer.write_str_value("parent_folder_id", self.parent_folder_id)
        writer.write_str_value("personal_notes", self.personal_notes)
        writer.write_object_value("photo", self.photo)
        writer.write_str_value("profession", self.profession)
        writer.write_collection_of_object_values("single_value_extended_properties", self.single_value_extended_properties)
        writer.write_str_value("spouse_name", self.spouse_name)
        writer.write_str_value("surname", self.surname)
        writer.write_str_value("title", self.title)
        writer.write_str_value("yomi_company_name", self.yomi_company_name)
        writer.write_str_value("yomi_given_name", self.yomi_given_name)
        writer.write_str_value("yomi_surname", self.yomi_surname)
    

