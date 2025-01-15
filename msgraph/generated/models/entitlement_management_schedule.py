from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .expiration_pattern import ExpirationPattern
    from .patterned_recurrence import PatternedRecurrence

@dataclass
class EntitlementManagementSchedule(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # When the access should expire.
    expiration: Optional[ExpirationPattern] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recurring access review pattern. Not used in access requests.
    recurrence: Optional[PatternedRecurrence] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EntitlementManagementSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EntitlementManagementSchedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EntitlementManagementSchedule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .expiration_pattern import ExpirationPattern
        from .patterned_recurrence import PatternedRecurrence

        from .expiration_pattern import ExpirationPattern
        from .patterned_recurrence import PatternedRecurrence

        fields: dict[str, Callable[[Any], None]] = {
            "expiration": lambda n : setattr(self, 'expiration', n.get_object_value(ExpirationPattern)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(PatternedRecurrence)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_object_value("expiration", self.expiration)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

