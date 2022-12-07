from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

bitlocker = lazy_import('msgraph.generated.models.bitlocker')
entity = lazy_import('msgraph.generated.models.entity')
threat_assessment_request = lazy_import('msgraph.generated.models.threat_assessment_request')

class InformationProtection(entity.Entity):
    @property
    def bitlocker(self,) -> Optional[bitlocker.Bitlocker]:
        """
        Gets the bitlocker property value. The bitlocker property
        Returns: Optional[bitlocker.Bitlocker]
        """
        return self._bitlocker
    
    @bitlocker.setter
    def bitlocker(self,value: Optional[bitlocker.Bitlocker] = None) -> None:
        """
        Sets the bitlocker property value. The bitlocker property
        Args:
            value: Value to set for the bitlocker property.
        """
        self._bitlocker = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new InformationProtection and sets the default values.
        """
        super().__init__()
        # The bitlocker property
        self._bitlocker: Optional[bitlocker.Bitlocker] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The threatAssessmentRequests property
        self._threat_assessment_requests: Optional[List[threat_assessment_request.ThreatAssessmentRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InformationProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bitlocker": lambda n : setattr(self, 'bitlocker', n.get_object_value(bitlocker.Bitlocker)),
            "threat_assessment_requests": lambda n : setattr(self, 'threat_assessment_requests', n.get_collection_of_object_values(threat_assessment_request.ThreatAssessmentRequest)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("bitlocker", self.bitlocker)
        writer.write_collection_of_object_values("threatAssessmentRequests", self.threat_assessment_requests)
    
    @property
    def threat_assessment_requests(self,) -> Optional[List[threat_assessment_request.ThreatAssessmentRequest]]:
        """
        Gets the threatAssessmentRequests property value. The threatAssessmentRequests property
        Returns: Optional[List[threat_assessment_request.ThreatAssessmentRequest]]
        """
        return self._threat_assessment_requests
    
    @threat_assessment_requests.setter
    def threat_assessment_requests(self,value: Optional[List[threat_assessment_request.ThreatAssessmentRequest]] = None) -> None:
        """
        Sets the threatAssessmentRequests property value. The threatAssessmentRequests property
        Args:
            value: Value to set for the threatAssessmentRequests property.
        """
        self._threat_assessment_requests = value
    

