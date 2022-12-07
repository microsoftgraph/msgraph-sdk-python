from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

training_status = lazy_import('msgraph.generated.models.training_status')
user_training_content_event_info = lazy_import('msgraph.generated.models.user_training_content_event_info')

class UserTrainingEventInfo(AdditionalDataHolder, Parsable):
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
        Instantiates a new userTrainingEventInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Display name of the training.
        self._display_name: Optional[str] = None
        # Latest status of the training assigned to the user. Possible values are: unknown, assigned, inProgress, completed, overdue, unknownFutureValue.
        self._latest_training_status: Optional[training_status.TrainingStatus] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Event details of the training when it was assigned to the user.
        self._training_assigned_properties: Optional[user_training_content_event_info.UserTrainingContentEventInfo] = None
        # Event details of the training when it was completed by the user.
        self._training_completed_properties: Optional[user_training_content_event_info.UserTrainingContentEventInfo] = None
        # Event details of the training when it was updated/in-progress by the user.
        self._training_updated_properties: Optional[user_training_content_event_info.UserTrainingContentEventInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserTrainingEventInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserTrainingEventInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserTrainingEventInfo()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the training.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the training.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "latest_training_status": lambda n : setattr(self, 'latest_training_status', n.get_enum_value(training_status.TrainingStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "training_assigned_properties": lambda n : setattr(self, 'training_assigned_properties', n.get_object_value(user_training_content_event_info.UserTrainingContentEventInfo)),
            "training_completed_properties": lambda n : setattr(self, 'training_completed_properties', n.get_object_value(user_training_content_event_info.UserTrainingContentEventInfo)),
            "training_updated_properties": lambda n : setattr(self, 'training_updated_properties', n.get_object_value(user_training_content_event_info.UserTrainingContentEventInfo)),
        }
        return fields
    
    @property
    def latest_training_status(self,) -> Optional[training_status.TrainingStatus]:
        """
        Gets the latestTrainingStatus property value. Latest status of the training assigned to the user. Possible values are: unknown, assigned, inProgress, completed, overdue, unknownFutureValue.
        Returns: Optional[training_status.TrainingStatus]
        """
        return self._latest_training_status
    
    @latest_training_status.setter
    def latest_training_status(self,value: Optional[training_status.TrainingStatus] = None) -> None:
        """
        Sets the latestTrainingStatus property value. Latest status of the training assigned to the user. Possible values are: unknown, assigned, inProgress, completed, overdue, unknownFutureValue.
        Args:
            value: Value to set for the latestTrainingStatus property.
        """
        self._latest_training_status = value
    
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("latestTrainingStatus", self.latest_training_status)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("trainingAssignedProperties", self.training_assigned_properties)
        writer.write_object_value("trainingCompletedProperties", self.training_completed_properties)
        writer.write_object_value("trainingUpdatedProperties", self.training_updated_properties)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def training_assigned_properties(self,) -> Optional[user_training_content_event_info.UserTrainingContentEventInfo]:
        """
        Gets the trainingAssignedProperties property value. Event details of the training when it was assigned to the user.
        Returns: Optional[user_training_content_event_info.UserTrainingContentEventInfo]
        """
        return self._training_assigned_properties
    
    @training_assigned_properties.setter
    def training_assigned_properties(self,value: Optional[user_training_content_event_info.UserTrainingContentEventInfo] = None) -> None:
        """
        Sets the trainingAssignedProperties property value. Event details of the training when it was assigned to the user.
        Args:
            value: Value to set for the trainingAssignedProperties property.
        """
        self._training_assigned_properties = value
    
    @property
    def training_completed_properties(self,) -> Optional[user_training_content_event_info.UserTrainingContentEventInfo]:
        """
        Gets the trainingCompletedProperties property value. Event details of the training when it was completed by the user.
        Returns: Optional[user_training_content_event_info.UserTrainingContentEventInfo]
        """
        return self._training_completed_properties
    
    @training_completed_properties.setter
    def training_completed_properties(self,value: Optional[user_training_content_event_info.UserTrainingContentEventInfo] = None) -> None:
        """
        Sets the trainingCompletedProperties property value. Event details of the training when it was completed by the user.
        Args:
            value: Value to set for the trainingCompletedProperties property.
        """
        self._training_completed_properties = value
    
    @property
    def training_updated_properties(self,) -> Optional[user_training_content_event_info.UserTrainingContentEventInfo]:
        """
        Gets the trainingUpdatedProperties property value. Event details of the training when it was updated/in-progress by the user.
        Returns: Optional[user_training_content_event_info.UserTrainingContentEventInfo]
        """
        return self._training_updated_properties
    
    @training_updated_properties.setter
    def training_updated_properties(self,value: Optional[user_training_content_event_info.UserTrainingContentEventInfo] = None) -> None:
        """
        Sets the trainingUpdatedProperties property value. Event details of the training when it was updated/in-progress by the user.
        Args:
            value: Value to set for the trainingUpdatedProperties property.
        """
        self._training_updated_properties = value
    

