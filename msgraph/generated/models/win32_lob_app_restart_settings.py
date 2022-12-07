from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class Win32LobAppRestartSettings(AdditionalDataHolder, Parsable):
    """
    Contains properties describing restart coordination following an app installation.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new win32LobAppRestartSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number of minutes before the restart time to display the countdown dialog for pending restarts.
        self._countdown_display_before_restart_in_minutes: Optional[int] = None
        # The number of minutes to wait before restarting the device after an app installation.
        self._grace_period_in_minutes: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The number of minutes to snooze the restart notification dialog when the snooze button is selected.
        self._restart_notification_snooze_duration_in_minutes: Optional[int] = None
    
    @property
    def countdown_display_before_restart_in_minutes(self,) -> Optional[int]:
        """
        Gets the countdownDisplayBeforeRestartInMinutes property value. The number of minutes before the restart time to display the countdown dialog for pending restarts.
        Returns: Optional[int]
        """
        return self._countdown_display_before_restart_in_minutes
    
    @countdown_display_before_restart_in_minutes.setter
    def countdown_display_before_restart_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the countdownDisplayBeforeRestartInMinutes property value. The number of minutes before the restart time to display the countdown dialog for pending restarts.
        Args:
            value: Value to set for the countdownDisplayBeforeRestartInMinutes property.
        """
        self._countdown_display_before_restart_in_minutes = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppRestartSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppRestartSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppRestartSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "countdown_display_before_restart_in_minutes": lambda n : setattr(self, 'countdown_display_before_restart_in_minutes', n.get_int_value()),
            "grace_period_in_minutes": lambda n : setattr(self, 'grace_period_in_minutes', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restart_notification_snooze_duration_in_minutes": lambda n : setattr(self, 'restart_notification_snooze_duration_in_minutes', n.get_int_value()),
        }
        return fields
    
    @property
    def grace_period_in_minutes(self,) -> Optional[int]:
        """
        Gets the gracePeriodInMinutes property value. The number of minutes to wait before restarting the device after an app installation.
        Returns: Optional[int]
        """
        return self._grace_period_in_minutes
    
    @grace_period_in_minutes.setter
    def grace_period_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the gracePeriodInMinutes property value. The number of minutes to wait before restarting the device after an app installation.
        Args:
            value: Value to set for the gracePeriodInMinutes property.
        """
        self._grace_period_in_minutes = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def restart_notification_snooze_duration_in_minutes(self,) -> Optional[int]:
        """
        Gets the restartNotificationSnoozeDurationInMinutes property value. The number of minutes to snooze the restart notification dialog when the snooze button is selected.
        Returns: Optional[int]
        """
        return self._restart_notification_snooze_duration_in_minutes
    
    @restart_notification_snooze_duration_in_minutes.setter
    def restart_notification_snooze_duration_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the restartNotificationSnoozeDurationInMinutes property value. The number of minutes to snooze the restart notification dialog when the snooze button is selected.
        Args:
            value: Value to set for the restartNotificationSnoozeDurationInMinutes property.
        """
        self._restart_notification_snooze_duration_in_minutes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("countdownDisplayBeforeRestartInMinutes", self.countdown_display_before_restart_in_minutes)
        writer.write_int_value("gracePeriodInMinutes", self.grace_period_in_minutes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("restartNotificationSnoozeDurationInMinutes", self.restart_notification_snooze_duration_in_minutes)
        writer.write_additional_data_value(self.additional_data)
    

