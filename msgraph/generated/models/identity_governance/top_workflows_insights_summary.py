from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lifecycle_workflow_category import LifecycleWorkflowCategory

@dataclass
class TopWorkflowsInsightsSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Count of failed runs for workflow.
    failed_runs: Optional[int] = None
    # Count of failed users who were processed.
    failed_users: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Count of successful runs of the workflow.
    successful_runs: Optional[int] = None
    # Count of successful users processed by the workflow.
    successful_users: Optional[int] = None
    # Count of total runs of workflow.
    total_runs: Optional[int] = None
    # Total number of users processed by the workflow.
    total_users: Optional[int] = None
    # The workflowCategory property
    workflow_category: Optional[LifecycleWorkflowCategory] = None
    # The name of the workflow.
    workflow_display_name: Optional[str] = None
    # The workflow ID.
    workflow_id: Optional[str] = None
    # The version of the workflow that was a top workflow ran.
    workflow_version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TopWorkflowsInsightsSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TopWorkflowsInsightsSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TopWorkflowsInsightsSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .lifecycle_workflow_category import LifecycleWorkflowCategory

        from .lifecycle_workflow_category import LifecycleWorkflowCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "failedRuns": lambda n : setattr(self, 'failed_runs', n.get_int_value()),
            "failedUsers": lambda n : setattr(self, 'failed_users', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "successfulRuns": lambda n : setattr(self, 'successful_runs', n.get_int_value()),
            "successfulUsers": lambda n : setattr(self, 'successful_users', n.get_int_value()),
            "totalRuns": lambda n : setattr(self, 'total_runs', n.get_int_value()),
            "totalUsers": lambda n : setattr(self, 'total_users', n.get_int_value()),
            "workflowCategory": lambda n : setattr(self, 'workflow_category', n.get_enum_value(LifecycleWorkflowCategory)),
            "workflowDisplayName": lambda n : setattr(self, 'workflow_display_name', n.get_str_value()),
            "workflowId": lambda n : setattr(self, 'workflow_id', n.get_str_value()),
            "workflowVersion": lambda n : setattr(self, 'workflow_version', n.get_int_value()),
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
        writer.write_int_value("failedUsers", self.failed_users)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("successfulRuns", self.successful_runs)
        writer.write_int_value("successfulUsers", self.successful_users)
        writer.write_int_value("totalRuns", self.total_runs)
        writer.write_int_value("totalUsers", self.total_users)
        writer.write_enum_value("workflowCategory", self.workflow_category)
        writer.write_str_value("workflowDisplayName", self.workflow_display_name)
        writer.write_str_value("workflowId", self.workflow_id)
        writer.write_int_value("workflowVersion", self.workflow_version)
        writer.write_additional_data_value(self.additional_data)
    

