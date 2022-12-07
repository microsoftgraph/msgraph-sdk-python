from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_gender = lazy_import('msgraph.generated.models.education_gender')

class EducationStudent(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def birth_date(self,) -> Optional[Date]:
        """
        Gets the birthDate property value. Birth date of the student.
        Returns: Optional[Date]
        """
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the birthDate property value. Birth date of the student.
        Args:
            value: Value to set for the birthDate property.
        """
        self._birth_date = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new educationStudent and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Birth date of the student.
        self._birth_date: Optional[Date] = None
        # ID of the student in the source system.
        self._external_id: Optional[str] = None
        # The possible values are: female, male, other, unknownFutureValue.
        self._gender: Optional[education_gender.EducationGender] = None
        # Current grade level of the student.
        self._grade: Optional[str] = None
        # Year the student is graduating from the school.
        self._graduation_year: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Student Number.
        self._student_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationStudent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationStudent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationStudent()
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. ID of the student in the source system.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. ID of the student in the source system.
        Args:
            value: Value to set for the externalId property.
        """
        self._external_id = value
    
    @property
    def gender(self,) -> Optional[education_gender.EducationGender]:
        """
        Gets the gender property value. The possible values are: female, male, other, unknownFutureValue.
        Returns: Optional[education_gender.EducationGender]
        """
        return self._gender
    
    @gender.setter
    def gender(self,value: Optional[education_gender.EducationGender] = None) -> None:
        """
        Sets the gender property value. The possible values are: female, male, other, unknownFutureValue.
        Args:
            value: Value to set for the gender property.
        """
        self._gender = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "birth_date": lambda n : setattr(self, 'birth_date', n.get_object_value(Date)),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "gender": lambda n : setattr(self, 'gender', n.get_enum_value(education_gender.EducationGender)),
            "grade": lambda n : setattr(self, 'grade', n.get_str_value()),
            "graduation_year": lambda n : setattr(self, 'graduation_year', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "student_number": lambda n : setattr(self, 'student_number', n.get_str_value()),
        }
        return fields
    
    @property
    def grade(self,) -> Optional[str]:
        """
        Gets the grade property value. Current grade level of the student.
        Returns: Optional[str]
        """
        return self._grade
    
    @grade.setter
    def grade(self,value: Optional[str] = None) -> None:
        """
        Sets the grade property value. Current grade level of the student.
        Args:
            value: Value to set for the grade property.
        """
        self._grade = value
    
    @property
    def graduation_year(self,) -> Optional[str]:
        """
        Gets the graduationYear property value. Year the student is graduating from the school.
        Returns: Optional[str]
        """
        return self._graduation_year
    
    @graduation_year.setter
    def graduation_year(self,value: Optional[str] = None) -> None:
        """
        Sets the graduationYear property value. Year the student is graduating from the school.
        Args:
            value: Value to set for the graduationYear property.
        """
        self._graduation_year = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("birthDate", self.birth_date)
        writer.write_str_value("externalId", self.external_id)
        writer.write_enum_value("gender", self.gender)
        writer.write_str_value("grade", self.grade)
        writer.write_str_value("graduationYear", self.graduation_year)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("studentNumber", self.student_number)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def student_number(self,) -> Optional[str]:
        """
        Gets the studentNumber property value. Student Number.
        Returns: Optional[str]
        """
        return self._student_number
    
    @student_number.setter
    def student_number(self,value: Optional[str] = None) -> None:
        """
        Sets the studentNumber property value. Student Number.
        Args:
            value: Value to set for the studentNumber property.
        """
        self._student_number = value
    

