from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

location_constraint_item = lazy_import('msgraph.generated.models.location_constraint_item')

class LocationConstraint(AdditionalDataHolder, Parsable):
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
        Instantiates a new locationConstraint and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The client requests the service to include in the response a meeting location for the meeting. If this is true and all the resources are busy, findMeetingTimes will not return any meeting time suggestions. If this is false and all the resources are busy, findMeetingTimes would still look for meeting times without locations.
        self._is_required: Optional[bool] = None
        # Constraint information for one or more locations that the client requests for the meeting.
        self._locations: Optional[List[location_constraint_item.LocationConstraintItem]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The client requests the service to suggest one or more meeting locations.
        self._suggest_location: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LocationConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LocationConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LocationConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_required": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "locations": lambda n : setattr(self, 'locations', n.get_collection_of_object_values(location_constraint_item.LocationConstraintItem)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "suggest_location": lambda n : setattr(self, 'suggest_location', n.get_bool_value()),
        }
        return fields
    
    @property
    def is_required(self,) -> Optional[bool]:
        """
        Gets the isRequired property value. The client requests the service to include in the response a meeting location for the meeting. If this is true and all the resources are busy, findMeetingTimes will not return any meeting time suggestions. If this is false and all the resources are busy, findMeetingTimes would still look for meeting times without locations.
        Returns: Optional[bool]
        """
        return self._is_required
    
    @is_required.setter
    def is_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRequired property value. The client requests the service to include in the response a meeting location for the meeting. If this is true and all the resources are busy, findMeetingTimes will not return any meeting time suggestions. If this is false and all the resources are busy, findMeetingTimes would still look for meeting times without locations.
        Args:
            value: Value to set for the isRequired property.
        """
        self._is_required = value
    
    @property
    def locations(self,) -> Optional[List[location_constraint_item.LocationConstraintItem]]:
        """
        Gets the locations property value. Constraint information for one or more locations that the client requests for the meeting.
        Returns: Optional[List[location_constraint_item.LocationConstraintItem]]
        """
        return self._locations
    
    @locations.setter
    def locations(self,value: Optional[List[location_constraint_item.LocationConstraintItem]] = None) -> None:
        """
        Sets the locations property value. Constraint information for one or more locations that the client requests for the meeting.
        Args:
            value: Value to set for the locations property.
        """
        self._locations = value
    
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
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_collection_of_object_values("locations", self.locations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("suggestLocation", self.suggest_location)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def suggest_location(self,) -> Optional[bool]:
        """
        Gets the suggestLocation property value. The client requests the service to suggest one or more meeting locations.
        Returns: Optional[bool]
        """
        return self._suggest_location
    
    @suggest_location.setter
    def suggest_location(self,value: Optional[bool] = None) -> None:
        """
        Sets the suggestLocation property value. The client requests the service to suggest one or more meeting locations.
        Args:
            value: Value to set for the suggestLocation property.
        """
        self._suggest_location = value
    

