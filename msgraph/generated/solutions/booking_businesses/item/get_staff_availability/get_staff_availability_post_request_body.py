from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

date_time_time_zone = lazy_import('msgraph.generated.models.date_time_time_zone')

class GetStaffAvailabilityPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the getStaffAvailability method.
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
        Instantiates a new getStaffAvailabilityPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The endDateTime property
        self._end_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The staffIds property
        self._staff_ids: Optional[List[str]] = None
        # The startDateTime property
        self._start_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetStaffAvailabilityPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetStaffAvailabilityPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetStaffAvailabilityPostRequestBody()
    
    @property
    def end_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the endDateTime property value. The endDateTime property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the endDateTime property value. The endDateTime property
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "staff_ids": lambda n : setattr(self, 'staff_ids', n.get_collection_of_primitive_values(str)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("endDateTime", self.end_date_time)
        writer.write_collection_of_primitive_values("staffIds", self.staff_ids)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def staff_ids(self,) -> Optional[List[str]]:
        """
        Gets the staffIds property value. The staffIds property
        Returns: Optional[List[str]]
        """
        return self._staff_ids
    
    @staff_ids.setter
    def staff_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the staffIds property value. The staffIds property
        Args:
            value: Value to set for the staffIds property.
        """
        self._staff_ids = value
    
    @property
    def start_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the startDateTime property value. The startDateTime property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the startDateTime property value. The startDateTime property
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    

