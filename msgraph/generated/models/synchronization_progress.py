from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class SynchronizationProgress(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationProgress and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The completedUnits property
        self._completed_units: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The progressObservationDateTime property
        self._progress_observation_date_time: Optional[datetime] = None
        # The totalUnits property
        self._total_units: Optional[int] = None
        # The units property
        self._units: Optional[str] = None
    
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
    
    @property
    def completed_units(self,) -> Optional[int]:
        """
        Gets the completedUnits property value. The completedUnits property
        Returns: Optional[int]
        """
        return self._completed_units
    
    @completed_units.setter
    def completed_units(self,value: Optional[int] = None) -> None:
        """
        Sets the completedUnits property value. The completedUnits property
        Args:
            value: Value to set for the completed_units property.
        """
        self._completed_units = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationProgress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationProgress
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationProgress()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "completedUnits": lambda n : setattr(self, 'completed_units', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "progressObservationDateTime": lambda n : setattr(self, 'progress_observation_date_time', n.get_datetime_value()),
            "totalUnits": lambda n : setattr(self, 'total_units', n.get_int_value()),
            "units": lambda n : setattr(self, 'units', n.get_str_value()),
        }
        return fields
    
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
    
    @property
    def progress_observation_date_time(self,) -> Optional[datetime]:
        """
        Gets the progressObservationDateTime property value. The progressObservationDateTime property
        Returns: Optional[datetime]
        """
        return self._progress_observation_date_time
    
    @progress_observation_date_time.setter
    def progress_observation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the progressObservationDateTime property value. The progressObservationDateTime property
        Args:
            value: Value to set for the progress_observation_date_time property.
        """
        self._progress_observation_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("completedUnits", self.completed_units)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("progressObservationDateTime", self.progress_observation_date_time)
        writer.write_int_value("totalUnits", self.total_units)
        writer.write_str_value("units", self.units)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def total_units(self,) -> Optional[int]:
        """
        Gets the totalUnits property value. The totalUnits property
        Returns: Optional[int]
        """
        return self._total_units
    
    @total_units.setter
    def total_units(self,value: Optional[int] = None) -> None:
        """
        Sets the totalUnits property value. The totalUnits property
        Args:
            value: Value to set for the total_units property.
        """
        self._total_units = value
    
    @property
    def units(self,) -> Optional[str]:
        """
        Gets the units property value. The units property
        Returns: Optional[str]
        """
        return self._units
    
    @units.setter
    def units(self,value: Optional[str] = None) -> None:
        """
        Sets the units property value. The units property
        Args:
            value: Value to set for the units property.
        """
        self._units = value
    

