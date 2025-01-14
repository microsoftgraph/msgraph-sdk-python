from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .synchronization_job_restart_scope import SynchronizationJobRestartScope

@dataclass
class SynchronizationJobRestartCriteria(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Comma-separated combination of the following values: None, ConnectorDataStore, Escrows, Watermark, QuarantineState, Full, ForceDeletes. The property can also be empty.   None: Starts a paused or quarantined provisioning job. DO NOT USE. Use the Start synchronizationJob API instead.ConnectorDataStore - Clears the underlying cache for all users. DO NOT USE. Contact Microsoft Support for guidance.Escrows - Provisioning failures are marked as escrows and retried. Clearing escrows will stop the service from retrying failures.Watermark - Removing the watermark causes the service to reevaluate all the users again, rather than just processing changes.QuarantineState - Temporarily lifts the quarantine.Use Full if you want all of the options.ForceDeletes - Forces the system to delete the pending deleted users when using the accidental deletions prevention feature and the deletion threshold is exceeded. Leaving this property empty emulates the Restart provisioning option in the Microsoft Entra admin center. It is similar to setting the resetScope to include QuarantineState, Watermark, and Escrows. This option meets most customer needs.
    reset_scope: Optional[SynchronizationJobRestartScope] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SynchronizationJobRestartCriteria:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationJobRestartCriteria
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationJobRestartCriteria()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .synchronization_job_restart_scope import SynchronizationJobRestartScope

        from .synchronization_job_restart_scope import SynchronizationJobRestartScope

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resetScope": lambda n : setattr(self, 'reset_scope', n.get_collection_of_enum_values(SynchronizationJobRestartScope)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("resetScope", self.reset_scope)
        writer.write_additional_data_value(self.additional_data)
    

