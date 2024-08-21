from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .certification_control import CertificationControl

@dataclass
class ComplianceInformation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Collection of the certification controls associated with the certification.
    certification_controls: Optional[List[CertificationControl]] = None
    # The name of the compliance certification, for example, ISO 27018:2014, GDPR, FedRAMP, and NIST 800-171.
    certification_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComplianceInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComplianceInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ComplianceInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .certification_control import CertificationControl

        from .certification_control import CertificationControl

        fields: Dict[str, Callable[[Any], None]] = {
            "certificationControls": lambda n : setattr(self, 'certification_controls', n.get_collection_of_object_values(CertificationControl)),
            "certificationName": lambda n : setattr(self, 'certification_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("certificationControls", self.certification_controls)
        writer.write_str_value("certificationName", self.certification_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

