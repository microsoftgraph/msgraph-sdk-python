from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bitlocker import Bitlocker
    from .threat_assessment_request import ThreatAssessmentRequest

@dataclass
class InformationProtection(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The bitlocker property
    bitlocker: Optional[Bitlocker] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The threatAssessmentRequests property
    threat_assessment_requests: Optional[List[ThreatAssessmentRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InformationProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InformationProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .bitlocker import Bitlocker
        from .threat_assessment_request import ThreatAssessmentRequest

        from .bitlocker import Bitlocker
        from .threat_assessment_request import ThreatAssessmentRequest

        fields: Dict[str, Callable[[Any], None]] = {
            "bitlocker": lambda n : setattr(self, 'bitlocker', n.get_object_value(Bitlocker)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "threatAssessmentRequests": lambda n : setattr(self, 'threat_assessment_requests', n.get_collection_of_object_values(ThreatAssessmentRequest)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from .bitlocker import Bitlocker
        from .threat_assessment_request import ThreatAssessmentRequest

        writer.write_object_value("bitlocker", self.bitlocker)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("threatAssessmentRequests", self.threat_assessment_requests)
        writer.write_additional_data_value(self.additional_data)
    

