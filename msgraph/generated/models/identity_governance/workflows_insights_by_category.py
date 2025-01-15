from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WorkflowsInsightsByCategory(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Failed 'Joiner' workflows processed in a tenant.
    failed_joiner_runs: Optional[int] = None
    # Failed 'Leaver' workflows processed in a tenant.
    failed_leaver_runs: Optional[int] = None
    # Failed 'Mover' workflows processed in a tenant.
    failed_mover_runs: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Successful 'Joiner' workflows processed in a tenant.
    successful_joiner_runs: Optional[int] = None
    # Successful 'Leaver' workflows processed in a tenant.
    successful_leaver_runs: Optional[int] = None
    # Successful 'Mover' workflows processed in a tenant.
    successful_mover_runs: Optional[int] = None
    # Total 'Joiner' workflows processed in a tenant.
    total_joiner_runs: Optional[int] = None
    # Total 'Leaver' workflows processed in a tenant.
    total_leaver_runs: Optional[int] = None
    # Total 'Mover' workflows processed in a tenant.
    total_mover_runs: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkflowsInsightsByCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkflowsInsightsByCategory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkflowsInsightsByCategory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "failedJoinerRuns": lambda n : setattr(self, 'failed_joiner_runs', n.get_int_value()),
            "failedLeaverRuns": lambda n : setattr(self, 'failed_leaver_runs', n.get_int_value()),
            "failedMoverRuns": lambda n : setattr(self, 'failed_mover_runs', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "successfulJoinerRuns": lambda n : setattr(self, 'successful_joiner_runs', n.get_int_value()),
            "successfulLeaverRuns": lambda n : setattr(self, 'successful_leaver_runs', n.get_int_value()),
            "successfulMoverRuns": lambda n : setattr(self, 'successful_mover_runs', n.get_int_value()),
            "totalJoinerRuns": lambda n : setattr(self, 'total_joiner_runs', n.get_int_value()),
            "totalLeaverRuns": lambda n : setattr(self, 'total_leaver_runs', n.get_int_value()),
            "totalMoverRuns": lambda n : setattr(self, 'total_mover_runs', n.get_int_value()),
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
        writer.write_int_value("failedJoinerRuns", self.failed_joiner_runs)
        writer.write_int_value("failedLeaverRuns", self.failed_leaver_runs)
        writer.write_int_value("failedMoverRuns", self.failed_mover_runs)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("successfulJoinerRuns", self.successful_joiner_runs)
        writer.write_int_value("successfulLeaverRuns", self.successful_leaver_runs)
        writer.write_int_value("successfulMoverRuns", self.successful_mover_runs)
        writer.write_int_value("totalJoinerRuns", self.total_joiner_runs)
        writer.write_int_value("totalLeaverRuns", self.total_leaver_runs)
        writer.write_int_value("totalMoverRuns", self.total_mover_runs)
        writer.write_additional_data_value(self.additional_data)
    

