from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import synchronization_job_subject

class SynchronizationJobApplicationParameters(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationJobApplicationParameters and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The ruleId property
        self._rule_id: Optional[str] = None
        # The subjects property
        self._subjects: Optional[List[synchronization_job_subject.SynchronizationJobSubject]] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationJobApplicationParameters:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationJobApplicationParameters
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationJobApplicationParameters()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import synchronization_job_subject

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ruleId": lambda n : setattr(self, 'rule_id', n.get_str_value()),
            "subjects": lambda n : setattr(self, 'subjects', n.get_collection_of_object_values(synchronization_job_subject.SynchronizationJobSubject)),
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
    def rule_id(self,) -> Optional[str]:
        """
        Gets the ruleId property value. The ruleId property
        Returns: Optional[str]
        """
        return self._rule_id
    
    @rule_id.setter
    def rule_id(self,value: Optional[str] = None) -> None:
        """
        Sets the ruleId property value. The ruleId property
        Args:
            value: Value to set for the rule_id property.
        """
        self._rule_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("ruleId", self.rule_id)
        writer.write_collection_of_object_values("subjects", self.subjects)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def subjects(self,) -> Optional[List[synchronization_job_subject.SynchronizationJobSubject]]:
        """
        Gets the subjects property value. The subjects property
        Returns: Optional[List[synchronization_job_subject.SynchronizationJobSubject]]
        """
        return self._subjects
    
    @subjects.setter
    def subjects(self,value: Optional[List[synchronization_job_subject.SynchronizationJobSubject]] = None) -> None:
        """
        Sets the subjects property value. The subjects property
        Args:
            value: Value to set for the subjects property.
        """
        self._subjects = value
    

