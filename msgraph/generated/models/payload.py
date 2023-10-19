from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

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
class Payload(Entity):
    # The brand property
    brand: Optional[PayloadBrand] = None
    # The complexity property
    complexity: Optional[PayloadComplexity] = None
    # The createdBy property
    created_by: Optional[EmailIdentity] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The description property
    description: Optional[str] = None
    # The detail property
    detail: Optional[PayloadDetail] = None
    # The displayName property
    display_name: Optional[str] = None
    # The industry property
    industry: Optional[PayloadIndustry] = None
    # The isAutomated property
    is_automated: Optional[bool] = None
    # The isControversial property
    is_controversial: Optional[bool] = None
    # The isCurrentEvent property
    is_current_event: Optional[bool] = None
    # The language property
    language: Optional[str] = None
    # The lastModifiedBy property
    last_modified_by: Optional[EmailIdentity] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The payloadTags property
    payload_tags: Optional[List[str]] = None
    # The platform property
    platform: Optional[PayloadDeliveryPlatform] = None
    # The predictedCompromiseRate property
    predicted_compromise_rate: Optional[float] = None
    # The simulationAttackType property
    simulation_attack_type: Optional[SimulationAttackType] = None
    # The source property
    source: Optional[SimulationContentSource] = None
    # The status property
    status: Optional[SimulationContentStatus] = None
    # The technique property
    technique: Optional[SimulationAttackTechnique] = None
    # The theme property
    theme: Optional[PayloadTheme] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Payload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Payload
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Payload()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
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

        fields: Dict[str, Callable[[Any], None]] = {
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
        if not writer:
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
    

