from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import average_comparative_score, control_score, entity, security_vendor_information

from . import entity

@dataclass
class SecureScore(entity.Entity):
    # Active user count of the given tenant.
    active_user_count: Optional[int] = None
    # Average score by different scopes (for example, average by industry, average by seating) and control category (Identity, Data, Device, Apps, Infrastructure) within the scope.
    average_comparative_scores: Optional[List[average_comparative_score.AverageComparativeScore]] = None
    # GUID string for tenant ID.
    azure_tenant_id: Optional[str] = None
    # Contains tenant scores for a set of controls.
    control_scores: Optional[List[control_score.ControlScore]] = None
    # The date when the entity is created.
    created_date_time: Optional[datetime] = None
    # Tenant current attained score on specified date.
    current_score: Optional[float] = None
    # Microsoft-provided services for the tenant (for example, Exchange online, Skype, Sharepoint).
    enabled_services: Optional[List[str]] = None
    # Licensed user count of the given tenant.
    licensed_user_count: Optional[int] = None
    # Tenant maximum possible score on specified date.
    max_score: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Complex type containing details about the security product/service vendor, provider, and subprovider (for example, vendor=Microsoft; provider=SecureScore). Required.
    vendor_information: Optional[security_vendor_information.SecurityVendorInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecureScore:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecureScore
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecureScore()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import average_comparative_score, control_score, entity, security_vendor_information

        fields: Dict[str, Callable[[Any], None]] = {
            "activeUserCount": lambda n : setattr(self, 'active_user_count', n.get_int_value()),
            "averageComparativeScores": lambda n : setattr(self, 'average_comparative_scores', n.get_collection_of_object_values(average_comparative_score.AverageComparativeScore)),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "controlScores": lambda n : setattr(self, 'control_scores', n.get_collection_of_object_values(control_score.ControlScore)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "currentScore": lambda n : setattr(self, 'current_score', n.get_float_value()),
            "enabledServices": lambda n : setattr(self, 'enabled_services', n.get_collection_of_primitive_values(str)),
            "licensedUserCount": lambda n : setattr(self, 'licensed_user_count', n.get_int_value()),
            "maxScore": lambda n : setattr(self, 'max_score', n.get_float_value()),
            "vendorInformation": lambda n : setattr(self, 'vendor_information', n.get_object_value(security_vendor_information.SecurityVendorInformation)),
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
        writer.write_int_value("activeUserCount", self.active_user_count)
        writer.write_collection_of_object_values("averageComparativeScores", self.average_comparative_scores)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_collection_of_object_values("controlScores", self.control_scores)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_float_value("currentScore", self.current_score)
        writer.write_collection_of_primitive_values("enabledServices", self.enabled_services)
        writer.write_int_value("licensedUserCount", self.licensed_user_count)
        writer.write_float_value("maxScore", self.max_score)
        writer.write_object_value("vendorInformation", self.vendor_information)
    

