from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RunSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The number of failed workflow runs.
    failed_runs: Optional[int] = None
    # The number of failed tasks of a workflow.
    failed_tasks: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of successful workflow runs.
    successful_runs: Optional[int] = None
    # The total number of runs for a workflow.
    total_runs: Optional[int] = None
    # The total number of tasks processed by a workflow.
    total_tasks: Optional[int] = None
    # The total number of users processed by a workflow.
    total_users: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RunSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RunSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RunSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "failedRuns": lambda n : setattr(self, 'failed_runs', n.get_int_value()),
            "failedTasks": lambda n : setattr(self, 'failed_tasks', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "successfulRuns": lambda n : setattr(self, 'successful_runs', n.get_int_value()),
            "totalRuns": lambda n : setattr(self, 'total_runs', n.get_int_value()),
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
        writer.write_int_value("failedRuns", self.failed_runs)
        writer.write_int_value("failedTasks", self.failed_tasks)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("successfulRuns", self.successful_runs)
        writer.write_int_value("totalRuns", self.total_runs)
        writer.write_int_value("totalTasks", self.total_tasks)
        writer.write_int_value("totalUsers", self.total_users)
        writer.write_additional_data_value(self.additional_data)
    

