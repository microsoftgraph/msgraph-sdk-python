from __future__ import annotations
from datetime import datetime, timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import synchronization_schedule_state

class SynchronizationSchedule(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationSchedule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The expiration property
        self._expiration: Optional[datetime] = None
        # The interval property
        self._interval: Optional[timedelta] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The state property
        self._state: Optional[synchronization_schedule_state.SynchronizationScheduleState] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationSchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationSchedule()
    
    @property
    def expiration(self,) -> Optional[datetime]:
        """
        Gets the expiration property value. The expiration property
        Returns: Optional[datetime]
        """
        return self._expiration
    
    @expiration.setter
    def expiration(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expiration property value. The expiration property
        Args:
            value: Value to set for the expiration property.
        """
        self._expiration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import synchronization_schedule_state

        fields: Dict[str, Callable[[Any], None]] = {
            "expiration": lambda n : setattr(self, 'expiration', n.get_datetime_value()),
            "interval": lambda n : setattr(self, 'interval', n.get_timedelta_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(synchronization_schedule_state.SynchronizationScheduleState)),
        }
        return fields
    
    @property
    def interval(self,) -> Optional[timedelta]:
        """
        Gets the interval property value. The interval property
        Returns: Optional[timedelta]
        """
        return self._interval
    
    @interval.setter
    def interval(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the interval property value. The interval property
        Args:
            value: Value to set for the interval property.
        """
        self._interval = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("expiration", self.expiration)
        writer.write_timedelta_value("interval", self.interval)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[synchronization_schedule_state.SynchronizationScheduleState]:
        """
        Gets the state property value. The state property
        Returns: Optional[synchronization_schedule_state.SynchronizationScheduleState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[synchronization_schedule_state.SynchronizationScheduleState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

