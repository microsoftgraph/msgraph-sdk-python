from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_identity import EmailIdentity
    from .entity import Entity
    from .simulation_content_source import SimulationContentSource
    from .training_availability_status import TrainingAvailabilityStatus
    from .training_language_detail import TrainingLanguageDetail
    from .training_type import TrainingType

from .entity import Entity

@dataclass
class Training(Entity, Parsable):
    # Training availability status. The possible values are: unknown, notAvailable, available, archive, delete, unknownFutureValue.
    availability_status: Optional[TrainingAvailabilityStatus] = None
    # Identity of the user who created the training.
    created_by: Optional[EmailIdentity] = None
    # Date and time when the training was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The description for the training.
    description: Optional[str] = None
    # The display name for the training.
    display_name: Optional[str] = None
    # Training duration.
    duration_in_minutes: Optional[int] = None
    # Indicates whether the training has any evaluation.
    has_evaluation: Optional[bool] = None
    # Language specific details on a training.
    language_details: Optional[list[TrainingLanguageDetail]] = None
    # Identity of the user who last modified the training.
    last_modified_by: Optional[EmailIdentity] = None
    # Date and time when the training was last modified. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Training content source. The possible values are: unknown, global, tenant, unknownFutureValue.
    source: Optional[SimulationContentSource] = None
    # Supported locales for content for the associated training.
    supported_locales: Optional[list[str]] = None
    # Training tags.
    tags: Optional[list[str]] = None
    # The type of training. The possible values are: unknown, phishing, unknownFutureValue.
    type: Optional[TrainingType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Training:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Training
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Training()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_identity import EmailIdentity
        from .entity import Entity
        from .simulation_content_source import SimulationContentSource
        from .training_availability_status import TrainingAvailabilityStatus
        from .training_language_detail import TrainingLanguageDetail
        from .training_type import TrainingType

        from .email_identity import EmailIdentity
        from .entity import Entity
        from .simulation_content_source import SimulationContentSource
        from .training_availability_status import TrainingAvailabilityStatus
        from .training_language_detail import TrainingLanguageDetail
        from .training_type import TrainingType

        fields: dict[str, Callable[[Any], None]] = {
            "availabilityStatus": lambda n : setattr(self, 'availability_status', n.get_enum_value(TrainingAvailabilityStatus)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "durationInMinutes": lambda n : setattr(self, 'duration_in_minutes', n.get_int_value()),
            "hasEvaluation": lambda n : setattr(self, 'has_evaluation', n.get_bool_value()),
            "languageDetails": lambda n : setattr(self, 'language_details', n.get_collection_of_object_values(TrainingLanguageDetail)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(EmailIdentity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(SimulationContentSource)),
            "supportedLocales": lambda n : setattr(self, 'supported_locales', n.get_collection_of_primitive_values(str)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TrainingType)),
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
        writer.write_enum_value("availabilityStatus", self.availability_status)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("durationInMinutes", self.duration_in_minutes)
        writer.write_bool_value("hasEvaluation", self.has_evaluation)
        writer.write_collection_of_object_values("languageDetails", self.language_details)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("source", self.source)
        writer.write_collection_of_primitive_values("supportedLocales", self.supported_locales)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_enum_value("type", self.type)
    

