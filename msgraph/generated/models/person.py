from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .location import Location
    from .person_type import PersonType
    from .phone import Phone
    from .scored_email_address import ScoredEmailAddress
    from .website import Website

from .entity import Entity

@dataclass
class Person(Entity, Parsable):
    # The person's birthday.
    birthday: Optional[str] = None
    # The name of the person's company.
    company_name: Optional[str] = None
    # The person's department.
    department: Optional[str] = None
    # The person's display name.
    display_name: Optional[str] = None
    # The person's given name.
    given_name: Optional[str] = None
    # The instant message voice over IP (VOIP) session initiation protocol (SIP) address for the user. Read-only.
    im_address: Optional[str] = None
    # True if the user has flagged this person as a favorite.
    is_favorite: Optional[bool] = None
    # The person's job title.
    job_title: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The location of the person's office.
    office_location: Optional[str] = None
    # Free-form notes that the user has taken about this person.
    person_notes: Optional[str] = None
    # The type of person.
    person_type: Optional[PersonType] = None
    # The person's phone numbers.
    phones: Optional[list[Phone]] = None
    # The person's addresses.
    postal_addresses: Optional[list[Location]] = None
    # The person's profession.
    profession: Optional[str] = None
    # The person's email addresses.
    scored_email_addresses: Optional[list[ScoredEmailAddress]] = None
    # The person's surname.
    surname: Optional[str] = None
    # The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.
    user_principal_name: Optional[str] = None
    # The person's websites.
    websites: Optional[list[Website]] = None
    # The phonetic Japanese name of the person's company.
    yomi_company: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Person:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Person
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Person()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .location import Location
        from .person_type import PersonType
        from .phone import Phone
        from .scored_email_address import ScoredEmailAddress
        from .website import Website

        from .entity import Entity
        from .location import Location
        from .person_type import PersonType
        from .phone import Phone
        from .scored_email_address import ScoredEmailAddress
        from .website import Website

        fields: dict[str, Callable[[Any], None]] = {
            "birthday": lambda n : setattr(self, 'birthday', n.get_str_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "imAddress": lambda n : setattr(self, 'im_address', n.get_str_value()),
            "isFavorite": lambda n : setattr(self, 'is_favorite', n.get_bool_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "officeLocation": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "personNotes": lambda n : setattr(self, 'person_notes', n.get_str_value()),
            "personType": lambda n : setattr(self, 'person_type', n.get_object_value(PersonType)),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(Phone)),
            "postalAddresses": lambda n : setattr(self, 'postal_addresses', n.get_collection_of_object_values(Location)),
            "profession": lambda n : setattr(self, 'profession', n.get_str_value()),
            "scoredEmailAddresses": lambda n : setattr(self, 'scored_email_addresses', n.get_collection_of_object_values(ScoredEmailAddress)),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "websites": lambda n : setattr(self, 'websites', n.get_collection_of_object_values(Website)),
            "yomiCompany": lambda n : setattr(self, 'yomi_company', n.get_str_value()),
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
    

