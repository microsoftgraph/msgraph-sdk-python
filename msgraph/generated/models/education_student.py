from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_gender import EducationGender

@dataclass
class EducationStudent(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Birth date of the student.
    birth_date: Optional[datetime.date] = None
    # ID of the student in the source system.
    external_id: Optional[str] = None
    # The possible values are: female, male, other, unknownFutureValue.
    gender: Optional[EducationGender] = None
    # Current grade level of the student.
    grade: Optional[str] = None
    # Year the student is graduating from the school.
    graduation_year: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Student Number.
    student_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationStudent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationStudent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationStudent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_gender import EducationGender

        from .education_gender import EducationGender

        fields: dict[str, Callable[[Any], None]] = {
            "birthDate": lambda n : setattr(self, 'birth_date', n.get_date_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "gender": lambda n : setattr(self, 'gender', n.get_enum_value(EducationGender)),
            "grade": lambda n : setattr(self, 'grade', n.get_str_value()),
            "graduationYear": lambda n : setattr(self, 'graduation_year', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "studentNumber": lambda n : setattr(self, 'student_number', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_date_value("birthDate", self.birth_date)
        writer.write_str_value("externalId", self.external_id)
        writer.write_enum_value("gender", self.gender)
        writer.write_str_value("grade", self.grade)
        writer.write_str_value("graduationYear", self.graduation_year)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("studentNumber", self.student_number)
        writer.write_additional_data_value(self.additional_data)
    

