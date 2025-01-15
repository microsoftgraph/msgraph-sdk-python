from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .administrative_unit import AdministrativeUnit
    from .education_class import EducationClass
    from .education_organization import EducationOrganization
    from .education_user import EducationUser
    from .identity_set import IdentitySet
    from .physical_address import PhysicalAddress

from .education_organization import EducationOrganization

@dataclass
class EducationSchool(EducationOrganization, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationSchool"
    # Address of the school.
    address: Optional[PhysicalAddress] = None
    # The underlying administrativeUnit for this school.
    administrative_unit: Optional[AdministrativeUnit] = None
    # Classes taught at the school. Nullable.
    classes: Optional[list[EducationClass]] = None
    # Entity who created the school.
    created_by: Optional[IdentitySet] = None
    # ID of school in syncing system.
    external_id: Optional[str] = None
    # ID of principal in syncing system.
    external_principal_id: Optional[str] = None
    # The fax property
    fax: Optional[str] = None
    # Highest grade taught.
    highest_grade: Optional[str] = None
    # Lowest grade taught.
    lowest_grade: Optional[str] = None
    # Phone number of school.
    phone: Optional[str] = None
    # Email address of the principal.
    principal_email: Optional[str] = None
    # Name of the principal.
    principal_name: Optional[str] = None
    # School Number.
    school_number: Optional[str] = None
    # Users in the school. Nullable.
    users: Optional[list[EducationUser]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationSchool:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationSchool
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationSchool()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .administrative_unit import AdministrativeUnit
        from .education_class import EducationClass
        from .education_organization import EducationOrganization
        from .education_user import EducationUser
        from .identity_set import IdentitySet
        from .physical_address import PhysicalAddress

        from .administrative_unit import AdministrativeUnit
        from .education_class import EducationClass
        from .education_organization import EducationOrganization
        from .education_user import EducationUser
        from .identity_set import IdentitySet
        from .physical_address import PhysicalAddress

        fields: dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(PhysicalAddress)),
            "administrativeUnit": lambda n : setattr(self, 'administrative_unit', n.get_object_value(AdministrativeUnit)),
            "classes": lambda n : setattr(self, 'classes', n.get_collection_of_object_values(EducationClass)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "externalPrincipalId": lambda n : setattr(self, 'external_principal_id', n.get_str_value()),
            "fax": lambda n : setattr(self, 'fax', n.get_str_value()),
            "highestGrade": lambda n : setattr(self, 'highest_grade', n.get_str_value()),
            "lowestGrade": lambda n : setattr(self, 'lowest_grade', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "principalEmail": lambda n : setattr(self, 'principal_email', n.get_str_value()),
            "principalName": lambda n : setattr(self, 'principal_name', n.get_str_value()),
            "schoolNumber": lambda n : setattr(self, 'school_number', n.get_str_value()),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(EducationUser)),
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
        writer.write_object_value("address", self.address)
        writer.write_object_value("administrativeUnit", self.administrative_unit)
        writer.write_collection_of_object_values("classes", self.classes)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("externalPrincipalId", self.external_principal_id)
        writer.write_str_value("fax", self.fax)
        writer.write_str_value("highestGrade", self.highest_grade)
        writer.write_str_value("lowestGrade", self.lowest_grade)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("principalEmail", self.principal_email)
        writer.write_str_value("principalName", self.principal_name)
        writer.write_str_value("schoolNumber", self.school_number)
        writer.write_collection_of_object_values("users", self.users)
    

