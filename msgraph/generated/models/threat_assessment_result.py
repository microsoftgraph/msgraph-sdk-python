from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
threat_assessment_result_type = lazy_import('msgraph.generated.models.threat_assessment_result_type')

class ThreatAssessmentResult(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new threatAssessmentResult and sets the default values.
        """
        super().__init__()
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # The result message for each threat assessment.
        self._message: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The threat assessment result type. Possible values are: checkPolicy, rescan.
        self._result_type: Optional[threat_assessment_result_type.ThreatAssessmentResultType] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ThreatAssessmentResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ThreatAssessmentResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ThreatAssessmentResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "result_type": lambda n : setattr(self, 'result_type', n.get_enum_value(threat_assessment_result_type.ThreatAssessmentResultType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. The result message for each threat assessment.
        Returns: Optional[str]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. The result message for each threat assessment.
        Args:
            value: Value to set for the message property.
        """
        self._message = value
    
    @property
    def result_type(self,) -> Optional[threat_assessment_result_type.ThreatAssessmentResultType]:
        """
        Gets the resultType property value. The threat assessment result type. Possible values are: checkPolicy, rescan.
        Returns: Optional[threat_assessment_result_type.ThreatAssessmentResultType]
        """
        return self._result_type
    
    @result_type.setter
    def result_type(self,value: Optional[threat_assessment_result_type.ThreatAssessmentResultType] = None) -> None:
        """
        Sets the resultType property value. The threat assessment result type. Possible values are: checkPolicy, rescan.
        Args:
            value: Value to set for the resultType property.
        """
        self._result_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("message", self.message)
        writer.write_enum_value("resultType", self.result_type)
    

