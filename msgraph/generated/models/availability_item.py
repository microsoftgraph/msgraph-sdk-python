from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

bookings_availability_status = lazy_import('msgraph.generated.models.bookings_availability_status')
date_time_time_zone = lazy_import('msgraph.generated.models.date_time_time_zone')

class AvailabilityItem(AdditionalDataHolder, Parsable):
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
        Instantiates a new availabilityItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The endDateTime property
        self._end_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates the service ID in case of 1:n appointments. If the appointment is of type 1:n, this field will be present, otherwise, null.
        self._service_id: Optional[str] = None
        # The startDateTime property
        self._start_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The status of the staff member. Possible values are: available, busy, slotsAvailable, outOfOffice, unknownFutureValue.
        self._status: Optional[bookings_availability_status.BookingsAvailabilityStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AvailabilityItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AvailabilityItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AvailabilityItem()
    
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
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "service_id": lambda n : setattr(self, 'service_id', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(bookings_availability_status.BookingsAvailabilityStatus)),
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
            value: Value to set for the OdataType property.
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
        writer.write_object_value("endDateTime", self.end_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("serviceId", self.service_id)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service_id(self,) -> Optional[str]:
        """
        Gets the serviceId property value. Indicates the service ID in case of 1:n appointments. If the appointment is of type 1:n, this field will be present, otherwise, null.
        Returns: Optional[str]
        """
        return self._service_id
    
    @service_id.setter
    def service_id(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceId property value. Indicates the service ID in case of 1:n appointments. If the appointment is of type 1:n, this field will be present, otherwise, null.
        Args:
            value: Value to set for the serviceId property.
        """
        self._service_id = value
    
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
    
    @property
    def status(self,) -> Optional[bookings_availability_status.BookingsAvailabilityStatus]:
        """
        Gets the status property value. The status of the staff member. Possible values are: available, busy, slotsAvailable, outOfOffice, unknownFutureValue.
        Returns: Optional[bookings_availability_status.BookingsAvailabilityStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[bookings_availability_status.BookingsAvailabilityStatus] = None) -> None:
        """
        Sets the status property value. The status of the staff member. Possible values are: available, busy, slotsAvailable, outOfOffice, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

