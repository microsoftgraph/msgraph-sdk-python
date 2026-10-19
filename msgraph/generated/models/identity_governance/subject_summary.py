from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SubjectSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The number of subjects with at least one failed task in a subject summary.
    failed_subjects: Optional[int] = None
    # The number of failed tasks for subjects in a subject summary.
    failed_tasks: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of subjects where all tasks succeeded in a subject summary.
    successful_subjects: Optional[int] = None
    # The total number of subjects in a subject summary.
    total_subjects: Optional[int] = None
    # The total tasks of subjects in a subject summary.
    total_tasks: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SubjectSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubjectSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SubjectSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "failedSubjects": lambda n : setattr(self, 'failed_subjects', n.get_int_value()),
            "failedTasks": lambda n : setattr(self, 'failed_tasks', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "successfulSubjects": lambda n : setattr(self, 'successful_subjects', n.get_int_value()),
            "totalSubjects": lambda n : setattr(self, 'total_subjects', n.get_int_value()),
            "totalTasks": lambda n : setattr(self, 'total_tasks', n.get_int_value()),
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
        writer.write_int_value("failedSubjects", self.failed_subjects)
        writer.write_int_value("failedTasks", self.failed_tasks)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("successfulSubjects", self.successful_subjects)
        writer.write_int_value("totalSubjects", self.total_subjects)
        writer.write_int_value("totalTasks", self.total_tasks)
        writer.write_additional_data_value(self.additional_data)
    

