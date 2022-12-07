from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

administrative_unit = lazy_import('msgraph.generated.models.administrative_unit')
education_class = lazy_import('msgraph.generated.models.education_class')
education_organization = lazy_import('msgraph.generated.models.education_organization')
education_user = lazy_import('msgraph.generated.models.education_user')
identity_set = lazy_import('msgraph.generated.models.identity_set')
physical_address = lazy_import('msgraph.generated.models.physical_address')

class EducationSchool(education_organization.EducationOrganization):
    @property
    def address(self,) -> Optional[physical_address.PhysicalAddress]:
        """
        Gets the address property value. Address of the school.
        Returns: Optional[physical_address.PhysicalAddress]
        """
        return self._address
    
    @address.setter
    def address(self,value: Optional[physical_address.PhysicalAddress] = None) -> None:
        """
        Sets the address property value. Address of the school.
        Args:
            value: Value to set for the address property.
        """
        self._address = value
    
    @property
    def administrative_unit(self,) -> Optional[administrative_unit.AdministrativeUnit]:
        """
        Gets the administrativeUnit property value. The underlying administrativeUnit for this school.
        Returns: Optional[administrative_unit.AdministrativeUnit]
        """
        return self._administrative_unit
    
    @administrative_unit.setter
    def administrative_unit(self,value: Optional[administrative_unit.AdministrativeUnit] = None) -> None:
        """
        Sets the administrativeUnit property value. The underlying administrativeUnit for this school.
        Args:
            value: Value to set for the administrativeUnit property.
        """
        self._administrative_unit = value
    
    @property
    def classes(self,) -> Optional[List[education_class.EducationClass]]:
        """
        Gets the classes property value. Classes taught at the school. Nullable.
        Returns: Optional[List[education_class.EducationClass]]
        """
        return self._classes
    
    @classes.setter
    def classes(self,value: Optional[List[education_class.EducationClass]] = None) -> None:
        """
        Sets the classes property value. Classes taught at the school. Nullable.
        Args:
            value: Value to set for the classes property.
        """
        self._classes = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EducationSchool and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationSchool"
        # Address of the school.
        self._address: Optional[physical_address.PhysicalAddress] = None
        # The underlying administrativeUnit for this school.
        self._administrative_unit: Optional[administrative_unit.AdministrativeUnit] = None
        # Classes taught at the school. Nullable.
        self._classes: Optional[List[education_class.EducationClass]] = None
        # Entity who created the school.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # ID of school in syncing system.
        self._external_id: Optional[str] = None
        # ID of principal in syncing system.
        self._external_principal_id: Optional[str] = None
        # The fax property
        self._fax: Optional[str] = None
        # Highest grade taught.
        self._highest_grade: Optional[str] = None
        # Lowest grade taught.
        self._lowest_grade: Optional[str] = None
        # Phone number of school.
        self._phone: Optional[str] = None
        # Email address of the principal.
        self._principal_email: Optional[str] = None
        # Name of the principal.
        self._principal_name: Optional[str] = None
        # School Number.
        self._school_number: Optional[str] = None
        # Users in the school. Nullable.
        self._users: Optional[List[education_user.EducationUser]] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. Entity who created the school.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. Entity who created the school.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSchool:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSchool
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationSchool()
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. ID of school in syncing system.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. ID of school in syncing system.
        Args:
            value: Value to set for the externalId property.
        """
        self._external_id = value
    
    @property
    def external_principal_id(self,) -> Optional[str]:
        """
        Gets the externalPrincipalId property value. ID of principal in syncing system.
        Returns: Optional[str]
        """
        return self._external_principal_id
    
    @external_principal_id.setter
    def external_principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalPrincipalId property value. ID of principal in syncing system.
        Args:
            value: Value to set for the externalPrincipalId property.
        """
        self._external_principal_id = value
    
    @property
    def fax(self,) -> Optional[str]:
        """
        Gets the fax property value. The fax property
        Returns: Optional[str]
        """
        return self._fax
    
    @fax.setter
    def fax(self,value: Optional[str] = None) -> None:
        """
        Sets the fax property value. The fax property
        Args:
            value: Value to set for the fax property.
        """
        self._fax = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(physical_address.PhysicalAddress)),
            "administrative_unit": lambda n : setattr(self, 'administrative_unit', n.get_object_value(administrative_unit.AdministrativeUnit)),
            "classes": lambda n : setattr(self, 'classes', n.get_collection_of_object_values(education_class.EducationClass)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "external_principal_id": lambda n : setattr(self, 'external_principal_id', n.get_str_value()),
            "fax": lambda n : setattr(self, 'fax', n.get_str_value()),
            "highest_grade": lambda n : setattr(self, 'highest_grade', n.get_str_value()),
            "lowest_grade": lambda n : setattr(self, 'lowest_grade', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "principal_email": lambda n : setattr(self, 'principal_email', n.get_str_value()),
            "principal_name": lambda n : setattr(self, 'principal_name', n.get_str_value()),
            "school_number": lambda n : setattr(self, 'school_number', n.get_str_value()),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(education_user.EducationUser)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def highest_grade(self,) -> Optional[str]:
        """
        Gets the highestGrade property value. Highest grade taught.
        Returns: Optional[str]
        """
        return self._highest_grade
    
    @highest_grade.setter
    def highest_grade(self,value: Optional[str] = None) -> None:
        """
        Sets the highestGrade property value. Highest grade taught.
        Args:
            value: Value to set for the highestGrade property.
        """
        self._highest_grade = value
    
    @property
    def lowest_grade(self,) -> Optional[str]:
        """
        Gets the lowestGrade property value. Lowest grade taught.
        Returns: Optional[str]
        """
        return self._lowest_grade
    
    @lowest_grade.setter
    def lowest_grade(self,value: Optional[str] = None) -> None:
        """
        Sets the lowestGrade property value. Lowest grade taught.
        Args:
            value: Value to set for the lowestGrade property.
        """
        self._lowest_grade = value
    
    @property
    def phone(self,) -> Optional[str]:
        """
        Gets the phone property value. Phone number of school.
        Returns: Optional[str]
        """
        return self._phone
    
    @phone.setter
    def phone(self,value: Optional[str] = None) -> None:
        """
        Sets the phone property value. Phone number of school.
        Args:
            value: Value to set for the phone property.
        """
        self._phone = value
    
    @property
    def principal_email(self,) -> Optional[str]:
        """
        Gets the principalEmail property value. Email address of the principal.
        Returns: Optional[str]
        """
        return self._principal_email
    
    @principal_email.setter
    def principal_email(self,value: Optional[str] = None) -> None:
        """
        Sets the principalEmail property value. Email address of the principal.
        Args:
            value: Value to set for the principalEmail property.
        """
        self._principal_email = value
    
    @property
    def principal_name(self,) -> Optional[str]:
        """
        Gets the principalName property value. Name of the principal.
        Returns: Optional[str]
        """
        return self._principal_name
    
    @principal_name.setter
    def principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the principalName property value. Name of the principal.
        Args:
            value: Value to set for the principalName property.
        """
        self._principal_name = value
    
    @property
    def school_number(self,) -> Optional[str]:
        """
        Gets the schoolNumber property value. School Number.
        Returns: Optional[str]
        """
        return self._school_number
    
    @school_number.setter
    def school_number(self,value: Optional[str] = None) -> None:
        """
        Sets the schoolNumber property value. School Number.
        Args:
            value: Value to set for the schoolNumber property.
        """
        self._school_number = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def users(self,) -> Optional[List[education_user.EducationUser]]:
        """
        Gets the users property value. Users in the school. Nullable.
        Returns: Optional[List[education_user.EducationUser]]
        """
        return self._users
    
    @users.setter
    def users(self,value: Optional[List[education_user.EducationUser]] = None) -> None:
        """
        Sets the users property value. Users in the school. Nullable.
        Args:
            value: Value to set for the users property.
        """
        self._users = value
    

