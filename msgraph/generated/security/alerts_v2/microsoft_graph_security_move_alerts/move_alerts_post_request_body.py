from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.security.correlation_reason import CorrelationReason

@dataclass
class MoveAlertsPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The alertComment property
    alert_comment: Optional[str] = None
    # The alertIds property
    alert_ids: Optional[list[str]] = None
    # The incidentId property
    incident_id: Optional[str] = None
    # The newCorrelationReasons property
    new_correlation_reasons: Optional[CorrelationReason] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MoveAlertsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MoveAlertsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MoveAlertsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ....models.security.correlation_reason import CorrelationReason

        from ....models.security.correlation_reason import CorrelationReason

        fields: dict[str, Callable[[Any], None]] = {
            "alertComment": lambda n : setattr(self, 'alert_comment', n.get_str_value()),
            "alertIds": lambda n : setattr(self, 'alert_ids', n.get_collection_of_primitive_values(str)),
            "incidentId": lambda n : setattr(self, 'incident_id', n.get_str_value()),
            "newCorrelationReasons": lambda n : setattr(self, 'new_correlation_reasons', n.get_collection_of_enum_values(CorrelationReason)),
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
        writer.write_str_value("alertComment", self.alert_comment)
        writer.write_collection_of_primitive_values("alertIds", self.alert_ids)
        writer.write_str_value("incidentId", self.incident_id)
        writer.write_enum_value("newCorrelationReasons", self.new_correlation_reasons)
        writer.write_additional_data_value(self.additional_data)
    

