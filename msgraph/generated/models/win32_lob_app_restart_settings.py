from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Win32LobAppRestartSettings(AdditionalDataHolder, BackedModel, Parsable):
    """
    Contains properties describing restart coordination following an app installation.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The number of minutes before the restart time to display the countdown dialog for pending restarts.
    countdown_display_before_restart_in_minutes: Optional[int] = None
    # The number of minutes to wait before restarting the device after an app installation.
    grace_period_in_minutes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of minutes to snooze the restart notification dialog when the snooze button is selected.
    restart_notification_snooze_duration_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppRestartSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppRestartSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppRestartSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "countdownDisplayBeforeRestartInMinutes": lambda n : setattr(self, 'countdown_display_before_restart_in_minutes', n.get_int_value()),
            "gracePeriodInMinutes": lambda n : setattr(self, 'grace_period_in_minutes', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restartNotificationSnoozeDurationInMinutes": lambda n : setattr(self, 'restart_notification_snooze_duration_in_minutes', n.get_int_value()),
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
        writer.write_int_value("countdownDisplayBeforeRestartInMinutes", self.countdown_display_before_restart_in_minutes)
        writer.write_int_value("gracePeriodInMinutes", self.grace_period_in_minutes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("restartNotificationSnoozeDurationInMinutes", self.restart_notification_snooze_duration_in_minutes)
        writer.write_additional_data_value(self.additional_data)
    

