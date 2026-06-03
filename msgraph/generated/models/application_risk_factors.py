from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_risk_factor_general_info import ApplicationRiskFactorGeneralInfo
    from .application_risk_factor_legal_info import ApplicationRiskFactorLegalInfo
    from .application_risk_factor_security_info import ApplicationRiskFactorSecurityInfo
    from .application_security_compliance import ApplicationSecurityCompliance

@dataclass
class ApplicationRiskFactors(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Provides information about the application's adherence to security frameworks, certifications, and industry compliance standards.
    compliance: Optional[ApplicationSecurityCompliance] = None
    # Contains general business, operational, and data handling details that influence the application's risk assessment.
    general: Optional[ApplicationRiskFactorGeneralInfo] = None
    # Provides legal and regulatory compliance information, including data ownership, retention, and GDPR adherence.
    legal: Optional[ApplicationRiskFactorLegalInfo] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains information related to the application's security posture, such as encryption, authentication, and vulnerability management practices.
    security: Optional[ApplicationRiskFactorSecurityInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicationRiskFactors:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationRiskFactors
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicationRiskFactors()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_risk_factor_general_info import ApplicationRiskFactorGeneralInfo
        from .application_risk_factor_legal_info import ApplicationRiskFactorLegalInfo
        from .application_risk_factor_security_info import ApplicationRiskFactorSecurityInfo
        from .application_security_compliance import ApplicationSecurityCompliance

        from .application_risk_factor_general_info import ApplicationRiskFactorGeneralInfo
        from .application_risk_factor_legal_info import ApplicationRiskFactorLegalInfo
        from .application_risk_factor_security_info import ApplicationRiskFactorSecurityInfo
        from .application_security_compliance import ApplicationSecurityCompliance

        fields: dict[str, Callable[[Any], None]] = {
            "compliance": lambda n : setattr(self, 'compliance', n.get_object_value(ApplicationSecurityCompliance)),
            "general": lambda n : setattr(self, 'general', n.get_object_value(ApplicationRiskFactorGeneralInfo)),
            "legal": lambda n : setattr(self, 'legal', n.get_object_value(ApplicationRiskFactorLegalInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "security": lambda n : setattr(self, 'security', n.get_object_value(ApplicationRiskFactorSecurityInfo)),
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
        writer.write_object_value("compliance", self.compliance)
        writer.write_object_value("general", self.general)
        writer.write_object_value("legal", self.legal)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("security", self.security)
        writer.write_additional_data_value(self.additional_data)
    

