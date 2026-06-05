from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ApplicationRiskScore(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Specifies the compliance risk score based on the application's alignment with regulatory standards and industry certifications such as HIPAA, CSA, and PCI-DSS.
    compliance: Optional[float] = None
    # Specifies the legal risk score based on data protection practices, privacy policy transparency, and jurisdictional compliance to regulations and policies such as DMCA and data retention policy.
    legal: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the provider risk score based on vendor credibility, operational maturity, and trustworthiness.
    provider: Optional[float] = None
    # Specifies the security risk score based on authentication strength, encryption, vulnerability management, and overall security hygiene.
    security: Optional[float] = None
    # Represents the composite risk score derived from all risk categories.
    total: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicationRiskScore:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationRiskScore
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicationRiskScore()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "compliance": lambda n : setattr(self, 'compliance', n.get_float_value()),
            "legal": lambda n : setattr(self, 'legal', n.get_float_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_float_value()),
            "security": lambda n : setattr(self, 'security', n.get_float_value()),
            "total": lambda n : setattr(self, 'total', n.get_float_value()),
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
        writer.write_float_value("compliance", self.compliance)
        writer.write_float_value("legal", self.legal)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("provider", self.provider)
        writer.write_float_value("security", self.security)
        writer.write_float_value("total", self.total)
        writer.write_additional_data_value(self.additional_data)
    

