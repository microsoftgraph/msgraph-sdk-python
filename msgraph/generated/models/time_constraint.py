from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

activity_domain = lazy_import('msgraph.generated.models.activity_domain')
time_slot = lazy_import('msgraph.generated.models.time_slot')

class TimeConstraint(AdditionalDataHolder, Parsable):
    @property
    def activity_domain(self,) -> Optional[activity_domain.ActivityDomain]:
        """
        Gets the activityDomain property value. The nature of the activity, optional. The possible values are: work, personal, unrestricted, or unknown.
        Returns: Optional[activity_domain.ActivityDomain]
        """
        return self._activity_domain
    
    @activity_domain.setter
    def activity_domain(self,value: Optional[activity_domain.ActivityDomain] = None) -> None:
        """
        Sets the activityDomain property value. The nature of the activity, optional. The possible values are: work, personal, unrestricted, or unknown.
        Args:
            value: Value to set for the activityDomain property.
        """
        self._activity_domain = value
    
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
        Instantiates a new timeConstraint and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The nature of the activity, optional. The possible values are: work, personal, unrestricted, or unknown.
        self._activity_domain: Optional[activity_domain.ActivityDomain] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The timeSlots property
        self._time_slots: Optional[List[time_slot.TimeSlot]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TimeConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TimeConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity_domain": lambda n : setattr(self, 'activity_domain', n.get_enum_value(activity_domain.ActivityDomain)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "time_slots": lambda n : setattr(self, 'time_slots', n.get_collection_of_object_values(time_slot.TimeSlot)),
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
        writer.write_enum_value("activityDomain", self.activity_domain)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("timeSlots", self.time_slots)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def time_slots(self,) -> Optional[List[time_slot.TimeSlot]]:
        """
        Gets the timeSlots property value. The timeSlots property
        Returns: Optional[List[time_slot.TimeSlot]]
        """
        return self._time_slots
    
    @time_slots.setter
    def time_slots(self,value: Optional[List[time_slot.TimeSlot]] = None) -> None:
        """
        Sets the timeSlots property value. The timeSlots property
        Args:
            value: Value to set for the timeSlots property.
        """
        self._time_slots = value
    

