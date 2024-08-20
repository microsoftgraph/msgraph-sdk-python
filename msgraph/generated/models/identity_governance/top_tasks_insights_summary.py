from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TopTasksInsightsSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Count of failed runs of the task.
    failed_tasks: Optional[int] = None
    # Count of failed users who were processed by the task.
    failed_users: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Count of successful runs of the task.
    successful_tasks: Optional[int] = None
    # Count of successful users processed by the task.
    successful_users: Optional[int] = None
    # The name of the task.
    task_definition_display_name: Optional[str] = None
    # The task ID.
    task_definition_id: Optional[str] = None
    # Count of total runs of the task.
    total_tasks: Optional[int] = None
    # Count of total users processed by the task.
    total_users: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TopTasksInsightsSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TopTasksInsightsSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TopTasksInsightsSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "failedTasks": lambda n : setattr(self, 'failed_tasks', n.get_int_value()),
            "failedUsers": lambda n : setattr(self, 'failed_users', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "successfulTasks": lambda n : setattr(self, 'successful_tasks', n.get_int_value()),
            "successfulUsers": lambda n : setattr(self, 'successful_users', n.get_int_value()),
            "taskDefinitionDisplayName": lambda n : setattr(self, 'task_definition_display_name', n.get_str_value()),
            "taskDefinitionId": lambda n : setattr(self, 'task_definition_id', n.get_str_value()),
            "totalTasks": lambda n : setattr(self, 'total_tasks', n.get_int_value()),
            "totalUsers": lambda n : setattr(self, 'total_users', n.get_int_value()),
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
        writer.write_int_value("failedTasks", self.failed_tasks)
        writer.write_int_value("failedUsers", self.failed_users)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("successfulTasks", self.successful_tasks)
        writer.write_int_value("successfulUsers", self.successful_users)
        writer.write_str_value("taskDefinitionDisplayName", self.task_definition_display_name)
        writer.write_str_value("taskDefinitionId", self.task_definition_id)
        writer.write_int_value("totalTasks", self.total_tasks)
        writer.write_int_value("totalUsers", self.total_users)
        writer.write_additional_data_value(self.additional_data)
    

