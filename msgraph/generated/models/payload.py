from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_identity import EmailIdentity
    from .entity import Entity
    from .payload_brand import PayloadBrand
    from .payload_complexity import PayloadComplexity
    from .payload_delivery_platform import PayloadDeliveryPlatform
    from .payload_detail import PayloadDetail
    from .payload_industry import PayloadIndustry
    from .payload_theme import PayloadTheme
    from .simulation_attack_technique import SimulationAttackTechnique
    from .simulation_attack_type import SimulationAttackType
    from .simulation_content_source import SimulationContentSource
    from .simulation_content_status import SimulationContentStatus

from .entity import Entity

@dataclass
class Payload(Entity, Parsable):
    # The branch of a payload. The possible values are: unknown, other, americanExpress, capitalOne, dhl, docuSign, dropbox, facebook, firstAmerican, microsoft, netflix, scotiabank, sendGrid, stewartTitle, tesco, wellsFargo, syrinxCloud, adobe, teams, zoom, unknownFutureValue.
    brand: Optional[PayloadBrand] = None
    # The complexity of a payload. The possible values are: unknown, low, medium, high, unknownFutureValue.
    complexity: Optional[PayloadComplexity] = None
    # Identity of the user who created the attack simulation and training campaign payload.
    created_by: Optional[EmailIdentity] = None
    # Date and time when the attack simulation and training campaign payload. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Description of the attack simulation and training campaign payload.
    description: Optional[str] = None
    # Additional details about the payload.
    detail: Optional[PayloadDetail] = None
    # Display name of the attack simulation and training campaign payload. Supports $filter and $orderby.
    display_name: Optional[str] = None
    # Industry of a payload. The possible values are: unknown, other, banking, businessServices, consumerServices, education, energy, construction, consulting, financialServices, government, hospitality, insurance, legal, courierServices, IT, healthcare, manufacturing, retail, telecom, realEstate, unknownFutureValue.
    industry: Optional[PayloadIndustry] = None
    # Indicates whether the attack simulation and training campaign payload was created from an automation flow. Supports $filter and $orderby.
    is_automated: Optional[bool] = None
    # Indicates whether the payload is controversial.
    is_controversial: Optional[bool] = None
    # Indicates whether the payload is from any recent event.
    is_current_event: Optional[bool] = None
    # Payload language.
    language: Optional[str] = None
    # Identity of the user who most recently modified the attack simulation and training campaign payload.
    last_modified_by: Optional[EmailIdentity] = None
    # Date and time when the attack simulation and training campaign payload was last modified. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Free text tags for a payload.
    payload_tags: Optional[list[str]] = None
    # The payload delivery platform for a simulation. The possible values are: unknown, sms, email, teams, unknownFutureValue.
    platform: Optional[PayloadDeliveryPlatform] = None
    # Predicted probability for a payload to phish a targeted user.
    predicted_compromise_rate: Optional[float] = None
    # Attack type of the attack simulation and training campaign. Supports $filter and $orderby. The possible values are: unknown, social, cloud, endpoint, unknownFutureValue.
    simulation_attack_type: Optional[SimulationAttackType] = None
    # The source property
    source: Optional[SimulationContentSource] = None
    # Simulation content status. Supports $filter and $orderby. The possible values are: unknown, draft, ready, archive, delete, unknownFutureValue.
    status: Optional[SimulationContentStatus] = None
    # The social engineering technique used in the attack simulation and training campaign. Supports $filter and $orderby. The possible values are: unknown, credentialHarvesting, attachmentMalware, driveByUrl, linkInAttachment, linkToMalwareFile, unknownFutureValue, oAuthConsentGrant. Use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: oAuthConsentGrant. For more information on the types of social engineering attack techniques, see simulations.
    technique: Optional[SimulationAttackTechnique] = None
    # The theme of a payload. The possible values are: unknown, other, accountActivation, accountVerification, billing, cleanUpMail, controversial, documentReceived, expense, fax, financeReport, incomingMessages, invoice, itemReceived, loginAlert, mailReceived, password, payment, payroll, personalizedOffer, quarantine, remoteWork, reviewMessage, securityUpdate, serviceSuspended, signatureRequired, upgradeMailboxStorage, verifyMailbox, voicemail, advertisement, employeeEngagement, unknownFutureValue.
    theme: Optional[PayloadTheme] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Payload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Payload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Payload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_identity import EmailIdentity
        from .entity import Entity
        from .payload_brand import PayloadBrand
        from .payload_complexity import PayloadComplexity
        from .payload_delivery_platform import PayloadDeliveryPlatform
        from .payload_detail import PayloadDetail
        from .payload_industry import PayloadIndustry
        from .payload_theme import PayloadTheme
        from .simulation_attack_technique import SimulationAttackTechnique
        from .simulation_attack_type import SimulationAttackType
        from .simulation_content_source import SimulationContentSource
        from .simulation_content_status import SimulationContentStatus

        from .email_identity import EmailIdentity
        from .entity import Entity
        from .payload_brand import PayloadBrand
        from .payload_complexity import PayloadComplexity
        from .payload_delivery_platform import PayloadDeliveryPlatform
        from .payload_detail import PayloadDetail
        from .payload_industry import PayloadIndustry
        from .payload_theme import PayloadTheme
        from .simulation_attack_technique import SimulationAttackTechnique
        from .simulation_attack_type import SimulationAttackType
        from .simulation_content_source import SimulationContentSource
        from .simulation_content_status import SimulationContentStatus

        fields: dict[str, Callable[[Any], None]] = {
            "brand": lambda n : setattr(self, 'brand', n.get_enum_value(PayloadBrand)),
            "complexity": lambda n : setattr(self, 'complexity', n.get_enum_value(PayloadComplexity)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detail": lambda n : setattr(self, 'detail', n.get_object_value(PayloadDetail)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_enum_value(PayloadIndustry)),
            "isAutomated": lambda n : setattr(self, 'is_automated', n.get_bool_value()),
            "isControversial": lambda n : setattr(self, 'is_controversial', n.get_bool_value()),
            "isCurrentEvent": lambda n : setattr(self, 'is_current_event', n.get_bool_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(EmailIdentity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "payloadTags": lambda n : setattr(self, 'payload_tags', n.get_collection_of_primitive_values(str)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(PayloadDeliveryPlatform)),
            "predictedCompromiseRate": lambda n : setattr(self, 'predicted_compromise_rate', n.get_float_value()),
            "simulationAttackType": lambda n : setattr(self, 'simulation_attack_type', n.get_enum_value(SimulationAttackType)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(SimulationContentSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SimulationContentStatus)),
            "technique": lambda n : setattr(self, 'technique', n.get_enum_value(SimulationAttackTechnique)),
            "theme": lambda n : setattr(self, 'theme', n.get_enum_value(PayloadTheme)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("brand", self.brand)
        writer.write_enum_value("complexity", self.complexity)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_object_value("detail", self.detail)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("industry", self.industry)
        writer.write_bool_value("isAutomated", self.is_automated)
        writer.write_bool_value("isControversial", self.is_controversial)
        writer.write_bool_value("isCurrentEvent", self.is_current_event)
        writer.write_str_value("language", self.language)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("payloadTags", self.payload_tags)
        writer.write_enum_value("platform", self.platform)
        writer.write_float_value("predictedCompromiseRate", self.predicted_compromise_rate)
        writer.write_enum_value("simulationAttackType", self.simulation_attack_type)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("status", self.status)
        writer.write_enum_value("technique", self.technique)
        writer.write_enum_value("theme", self.theme)
    

