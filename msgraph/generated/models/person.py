from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
location = lazy_import('msgraph.generated.models.location')
person_type = lazy_import('msgraph.generated.models.person_type')
phone = lazy_import('msgraph.generated.models.phone')
scored_email_address = lazy_import('msgraph.generated.models.scored_email_address')
website = lazy_import('msgraph.generated.models.website')

class Person(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def birthday(self,) -> Optional[str]:
        """
        Gets the birthday property value. The person's birthday.
        Returns: Optional[str]
        """
        return self._birthday
    
    @birthday.setter
    def birthday(self,value: Optional[str] = None) -> None:
        """
        Sets the birthday property value. The person's birthday.
        Args:
            value: Value to set for the birthday property.
        """
        self._birthday = value
    
    @property
    def company_name(self,) -> Optional[str]:
        """
        Gets the companyName property value. The name of the person's company.
        Returns: Optional[str]
        """
        return self._company_name
    
    @company_name.setter
    def company_name(self,value: Optional[str] = None) -> None:
        """
        Sets the companyName property value. The name of the person's company.
        Args:
            value: Value to set for the companyName property.
        """
        self._company_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new person and sets the default values.
        """
        super().__init__()
        # The person's birthday.
        self._birthday: Optional[str] = None
        # The name of the person's company.
        self._company_name: Optional[str] = None
        # The person's department.
        self._department: Optional[str] = None
        # The person's display name.
        self._display_name: Optional[str] = None
        # The person's given name.
        self._given_name: Optional[str] = None
        # The instant message voice over IP (VOIP) session initiation protocol (SIP) address for the user. Read-only.
        self._im_address: Optional[str] = None
        # true if the user has flagged this person as a favorite.
        self._is_favorite: Optional[bool] = None
        # The person's job title.
        self._job_title: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The location of the person's office.
        self._office_location: Optional[str] = None
        # Free-form notes that the user has taken about this person.
        self._person_notes: Optional[str] = None
        # The type of person.
        self._person_type: Optional[person_type.PersonType] = None
        # The person's phone numbers.
        self._phones: Optional[List[phone.Phone]] = None
        # The person's addresses.
        self._postal_addresses: Optional[List[location.Location]] = None
        # The person's profession.
        self._profession: Optional[str] = None
        # The person's email addresses.
        self._scored_email_addresses: Optional[List[scored_email_address.ScoredEmailAddress]] = None
        # The person's surname.
        self._surname: Optional[str] = None
        # The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.
        self._user_principal_name: Optional[str] = None
        # The person's websites.
        self._websites: Optional[List[website.Website]] = None
        # The phonetic Japanese name of the person's company.
        self._yomi_company: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Person:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Person
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Person()
    
    @property
    def department(self,) -> Optional[str]:
        """
        Gets the department property value. The person's department.
        Returns: Optional[str]
        """
        return self._department
    
    @department.setter
    def department(self,value: Optional[str] = None) -> None:
        """
        Sets the department property value. The person's department.
        Args:
            value: Value to set for the department property.
        """
        self._department = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The person's display name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The person's display name.
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
            "birthday": lambda n : setattr(self, 'birthday', n.get_str_value()),
            "company_name": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "given_name": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "im_address": lambda n : setattr(self, 'im_address', n.get_str_value()),
            "is_favorite": lambda n : setattr(self, 'is_favorite', n.get_bool_value()),
            "job_title": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "office_location": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "person_notes": lambda n : setattr(self, 'person_notes', n.get_str_value()),
            "person_type": lambda n : setattr(self, 'person_type', n.get_object_value(person_type.PersonType)),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(phone.Phone)),
            "postal_addresses": lambda n : setattr(self, 'postal_addresses', n.get_collection_of_object_values(location.Location)),
            "profession": lambda n : setattr(self, 'profession', n.get_str_value()),
            "scored_email_addresses": lambda n : setattr(self, 'scored_email_addresses', n.get_collection_of_object_values(scored_email_address.ScoredEmailAddress)),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "websites": lambda n : setattr(self, 'websites', n.get_collection_of_object_values(website.Website)),
            "yomi_company": lambda n : setattr(self, 'yomi_company', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def given_name(self,) -> Optional[str]:
        """
        Gets the givenName property value. The person's given name.
        Returns: Optional[str]
        """
        return self._given_name
    
    @given_name.setter
    def given_name(self,value: Optional[str] = None) -> None:
        """
        Sets the givenName property value. The person's given name.
        Args:
            value: Value to set for the givenName property.
        """
        self._given_name = value
    
    @property
    def im_address(self,) -> Optional[str]:
        """
        Gets the imAddress property value. The instant message voice over IP (VOIP) session initiation protocol (SIP) address for the user. Read-only.
        Returns: Optional[str]
        """
        return self._im_address
    
    @im_address.setter
    def im_address(self,value: Optional[str] = None) -> None:
        """
        Sets the imAddress property value. The instant message voice over IP (VOIP) session initiation protocol (SIP) address for the user. Read-only.
        Args:
            value: Value to set for the imAddress property.
        """
        self._im_address = value
    
    @property
    def is_favorite(self,) -> Optional[bool]:
        """
        Gets the isFavorite property value. true if the user has flagged this person as a favorite.
        Returns: Optional[bool]
        """
        return self._is_favorite
    
    @is_favorite.setter
    def is_favorite(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFavorite property value. true if the user has flagged this person as a favorite.
        Args:
            value: Value to set for the isFavorite property.
        """
        self._is_favorite = value
    
    @property
    def job_title(self,) -> Optional[str]:
        """
        Gets the jobTitle property value. The person's job title.
        Returns: Optional[str]
        """
        return self._job_title
    
    @job_title.setter
    def job_title(self,value: Optional[str] = None) -> None:
        """
        Sets the jobTitle property value. The person's job title.
        Args:
            value: Value to set for the jobTitle property.
        """
        self._job_title = value
    
    @property
    def office_location(self,) -> Optional[str]:
        """
        Gets the officeLocation property value. The location of the person's office.
        Returns: Optional[str]
        """
        return self._office_location
    
    @office_location.setter
    def office_location(self,value: Optional[str] = None) -> None:
        """
        Sets the officeLocation property value. The location of the person's office.
        Args:
            value: Value to set for the officeLocation property.
        """
        self._office_location = value
    
    @property
    def person_notes(self,) -> Optional[str]:
        """
        Gets the personNotes property value. Free-form notes that the user has taken about this person.
        Returns: Optional[str]
        """
        return self._person_notes
    
    @person_notes.setter
    def person_notes(self,value: Optional[str] = None) -> None:
        """
        Sets the personNotes property value. Free-form notes that the user has taken about this person.
        Args:
            value: Value to set for the personNotes property.
        """
        self._person_notes = value
    
    @property
    def person_type(self,) -> Optional[person_type.PersonType]:
        """
        Gets the personType property value. The type of person.
        Returns: Optional[person_type.PersonType]
        """
        return self._person_type
    
    @person_type.setter
    def person_type(self,value: Optional[person_type.PersonType] = None) -> None:
        """
        Sets the personType property value. The type of person.
        Args:
            value: Value to set for the personType property.
        """
        self._person_type = value
    
    @property
    def phones(self,) -> Optional[List[phone.Phone]]:
        """
        Gets the phones property value. The person's phone numbers.
        Returns: Optional[List[phone.Phone]]
        """
        return self._phones
    
    @phones.setter
    def phones(self,value: Optional[List[phone.Phone]] = None) -> None:
        """
        Sets the phones property value. The person's phone numbers.
        Args:
            value: Value to set for the phones property.
        """
        self._phones = value
    
    @property
    def postal_addresses(self,) -> Optional[List[location.Location]]:
        """
        Gets the postalAddresses property value. The person's addresses.
        Returns: Optional[List[location.Location]]
        """
        return self._postal_addresses
    
    @postal_addresses.setter
    def postal_addresses(self,value: Optional[List[location.Location]] = None) -> None:
        """
        Sets the postalAddresses property value. The person's addresses.
        Args:
            value: Value to set for the postalAddresses property.
        """
        self._postal_addresses = value
    
    @property
    def profession(self,) -> Optional[str]:
        """
        Gets the profession property value. The person's profession.
        Returns: Optional[str]
        """
        return self._profession
    
    @profession.setter
    def profession(self,value: Optional[str] = None) -> None:
        """
        Sets the profession property value. The person's profession.
        Args:
            value: Value to set for the profession property.
        """
        self._profession = value
    
    @property
    def scored_email_addresses(self,) -> Optional[List[scored_email_address.ScoredEmailAddress]]:
        """
        Gets the scoredEmailAddresses property value. The person's email addresses.
        Returns: Optional[List[scored_email_address.ScoredEmailAddress]]
        """
        return self._scored_email_addresses
    
    @scored_email_addresses.setter
    def scored_email_addresses(self,value: Optional[List[scored_email_address.ScoredEmailAddress]] = None) -> None:
        """
        Sets the scoredEmailAddresses property value. The person's email addresses.
        Args:
            value: Value to set for the scoredEmailAddresses property.
        """
        self._scored_email_addresses = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("birthday", self.birthday)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("department", self.department)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("givenName", self.given_name)
        writer.write_str_value("imAddress", self.im_address)
        writer.write_bool_value("isFavorite", self.is_favorite)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_str_value("officeLocation", self.office_location)
        writer.write_str_value("personNotes", self.person_notes)
        writer.write_object_value("personType", self.person_type)
        writer.write_collection_of_object_values("phones", self.phones)
        writer.write_collection_of_object_values("postalAddresses", self.postal_addresses)
        writer.write_str_value("profession", self.profession)
        writer.write_collection_of_object_values("scoredEmailAddresses", self.scored_email_addresses)
        writer.write_str_value("surname", self.surname)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_collection_of_object_values("websites", self.websites)
        writer.write_str_value("yomiCompany", self.yomi_company)
    
    @property
    def surname(self,) -> Optional[str]:
        """
        Gets the surname property value. The person's surname.
        Returns: Optional[str]
        """
        return self._surname
    
    @surname.setter
    def surname(self,value: Optional[str] = None) -> None:
        """
        Sets the surname property value. The person's surname.
        Args:
            value: Value to set for the surname property.
        """
        self._surname = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    
    @property
    def websites(self,) -> Optional[List[website.Website]]:
        """
        Gets the websites property value. The person's websites.
        Returns: Optional[List[website.Website]]
        """
        return self._websites
    
    @websites.setter
    def websites(self,value: Optional[List[website.Website]] = None) -> None:
        """
        Sets the websites property value. The person's websites.
        Args:
            value: Value to set for the websites property.
        """
        self._websites = value
    
    @property
    def yomi_company(self,) -> Optional[str]:
        """
        Gets the yomiCompany property value. The phonetic Japanese name of the person's company.
        Returns: Optional[str]
        """
        return self._yomi_company
    
    @yomi_company.setter
    def yomi_company(self,value: Optional[str] = None) -> None:
        """
        Sets the yomiCompany property value. The phonetic Japanese name of the person's company.
        Args:
            value: Value to set for the yomiCompany property.
        """
        self._yomi_company = value
    

