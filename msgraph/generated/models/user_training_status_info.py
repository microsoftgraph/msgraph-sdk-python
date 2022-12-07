from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

training_status = lazy_import('msgraph.generated.models.training_status')

class UserTrainingStatusInfo(AdditionalDataHolder, Parsable):
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
    def assigned_date_time(self,) -> Optional[datetime]:
        """
        Gets the assignedDateTime property value. Date and time of assignment of the training to the user.
        Returns: Optional[datetime]
        """
        return self._assigned_date_time
    
    @assigned_date_time.setter
    def assigned_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the assignedDateTime property value. Date and time of assignment of the training to the user.
        Args:
            value: Value to set for the assignedDateTime property.
        """
        self._assigned_date_time = value
    
    @property
    def completion_date_time(self,) -> Optional[datetime]:
        """
        Gets the completionDateTime property value. Date and time of completion of the training by the user.
        Returns: Optional[datetime]
        """
        return self._completion_date_time
    
    @completion_date_time.setter
    def completion_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completionDateTime property value. Date and time of completion of the training by the user.
        Args:
            value: Value to set for the completionDateTime property.
        """
        self._completion_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userTrainingStatusInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Date and time of assignment of the training to the user.
        self._assigned_date_time: Optional[datetime] = None
        # Date and time of completion of the training by the user.
        self._completion_date_time: Optional[datetime] = None
        # Display name of the assigned training.
        self._display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The status of the training assigned to the user. Possible values are: unknown, assigned, inProgress, completed, overdue, unknownFutureValue.
        self._training_status: Optional[training_status.TrainingStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserTrainingStatusInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserTrainingStatusInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserTrainingStatusInfo()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the assigned training.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the assigned training.
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
            "assigned_date_time": lambda n : setattr(self, 'assigned_date_time', n.get_datetime_value()),
            "completion_date_time": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "training_status": lambda n : setattr(self, 'training_status', n.get_enum_value(training_status.TrainingStatus)),
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
        writer.write_datetime_value("assignedDateTime", self.assigned_date_time)
        writer.write_datetime_value("completionDateTime", self.completion_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("trainingStatus", self.training_status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def training_status(self,) -> Optional[training_status.TrainingStatus]:
        """
        Gets the trainingStatus property value. The status of the training assigned to the user. Possible values are: unknown, assigned, inProgress, completed, overdue, unknownFutureValue.
        Returns: Optional[training_status.TrainingStatus]
        """
        return self._training_status
    
    @training_status.setter
    def training_status(self,value: Optional[training_status.TrainingStatus] = None) -> None:
        """
        Sets the trainingStatus property value. The status of the training assigned to the user. Possible values are: unknown, assigned, inProgress, completed, overdue, unknownFutureValue.
        Args:
            value: Value to set for the trainingStatus property.
        """
        self._training_status = value
    

