from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

free_busy_error = lazy_import('msgraph.generated.models.free_busy_error')
schedule_item = lazy_import('msgraph.generated.models.schedule_item')
working_hours = lazy_import('msgraph.generated.models.working_hours')

class ScheduleInformation(AdditionalDataHolder, Parsable):
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
    def availability_view(self,) -> Optional[str]:
        """
        Gets the availabilityView property value. Represents a merged view of availability of all the items in scheduleItems. The view consists of time slots. Availability during each time slot is indicated with: 0= free, 1= tentative, 2= busy, 3= out of office, 4= working elsewhere.
        Returns: Optional[str]
        """
        return self._availability_view
    
    @availability_view.setter
    def availability_view(self,value: Optional[str] = None) -> None:
        """
        Sets the availabilityView property value. Represents a merged view of availability of all the items in scheduleItems. The view consists of time slots. Availability during each time slot is indicated with: 0= free, 1= tentative, 2= busy, 3= out of office, 4= working elsewhere.
        Args:
            value: Value to set for the availabilityView property.
        """
        self._availability_view = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new scheduleInformation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Represents a merged view of availability of all the items in scheduleItems. The view consists of time slots. Availability during each time slot is indicated with: 0= free, 1= tentative, 2= busy, 3= out of office, 4= working elsewhere.
        self._availability_view: Optional[str] = None
        # Error information from attempting to get the availability of the user, distribution list, or resource.
        self._error: Optional[free_busy_error.FreeBusyError] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # An SMTP address of the user, distribution list, or resource, identifying an instance of scheduleInformation.
        self._schedule_id: Optional[str] = None
        # Contains the items that describe the availability of the user or resource.
        self._schedule_items: Optional[List[schedule_item.ScheduleItem]] = None
        # The days of the week and hours in a specific time zone that the user works. These are set as part of the user's mailboxSettings.
        self._working_hours: Optional[working_hours.WorkingHours] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScheduleInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ScheduleInformation()
    
    @property
    def error(self,) -> Optional[free_busy_error.FreeBusyError]:
        """
        Gets the error property value. Error information from attempting to get the availability of the user, distribution list, or resource.
        Returns: Optional[free_busy_error.FreeBusyError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[free_busy_error.FreeBusyError] = None) -> None:
        """
        Sets the error property value. Error information from attempting to get the availability of the user, distribution list, or resource.
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "availability_view": lambda n : setattr(self, 'availability_view', n.get_str_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(free_busy_error.FreeBusyError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "schedule_id": lambda n : setattr(self, 'schedule_id', n.get_str_value()),
            "schedule_items": lambda n : setattr(self, 'schedule_items', n.get_collection_of_object_values(schedule_item.ScheduleItem)),
            "working_hours": lambda n : setattr(self, 'working_hours', n.get_object_value(working_hours.WorkingHours)),
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
    
    @property
    def schedule_id(self,) -> Optional[str]:
        """
        Gets the scheduleId property value. An SMTP address of the user, distribution list, or resource, identifying an instance of scheduleInformation.
        Returns: Optional[str]
        """
        return self._schedule_id
    
    @schedule_id.setter
    def schedule_id(self,value: Optional[str] = None) -> None:
        """
        Sets the scheduleId property value. An SMTP address of the user, distribution list, or resource, identifying an instance of scheduleInformation.
        Args:
            value: Value to set for the scheduleId property.
        """
        self._schedule_id = value
    
    @property
    def schedule_items(self,) -> Optional[List[schedule_item.ScheduleItem]]:
        """
        Gets the scheduleItems property value. Contains the items that describe the availability of the user or resource.
        Returns: Optional[List[schedule_item.ScheduleItem]]
        """
        return self._schedule_items
    
    @schedule_items.setter
    def schedule_items(self,value: Optional[List[schedule_item.ScheduleItem]] = None) -> None:
        """
        Sets the scheduleItems property value. Contains the items that describe the availability of the user or resource.
        Args:
            value: Value to set for the scheduleItems property.
        """
        self._schedule_items = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("availabilityView", self.availability_view)
        writer.write_object_value("error", self.error)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("scheduleId", self.schedule_id)
        writer.write_collection_of_object_values("scheduleItems", self.schedule_items)
        writer.write_object_value("workingHours", self.working_hours)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def working_hours(self,) -> Optional[working_hours.WorkingHours]:
        """
        Gets the workingHours property value. The days of the week and hours in a specific time zone that the user works. These are set as part of the user's mailboxSettings.
        Returns: Optional[working_hours.WorkingHours]
        """
        return self._working_hours
    
    @working_hours.setter
    def working_hours(self,value: Optional[working_hours.WorkingHours] = None) -> None:
        """
        Sets the workingHours property value. The days of the week and hours in a specific time zone that the user works. These are set as part of the user's mailboxSettings.
        Args:
            value: Value to set for the workingHours property.
        """
        self._working_hours = value
    

