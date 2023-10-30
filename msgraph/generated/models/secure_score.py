from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .average_comparative_score import AverageComparativeScore
    from .control_score import ControlScore
    from .entity import Entity
    from .security_vendor_information import SecurityVendorInformation

from .entity import Entity

@dataclass
class SecureScore(Entity):
    # Active user count of the given tenant.
    active_user_count: Optional[int] = None
    # Average score by different scopes (for example, average by industry, average by seating) and control category (Identity, Data, Device, Apps, Infrastructure) within the scope.
    average_comparative_scores: Optional[List[AverageComparativeScore]] = None
    # GUID string for tenant ID.
    azure_tenant_id: Optional[str] = None
    # Contains tenant scores for a set of controls.
    control_scores: Optional[List[ControlScore]] = None
    # The date when the entity is created.
    created_date_time: Optional[datetime.datetime] = None
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
    vendor_information: Optional[SecurityVendorInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecureScore:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecureScore
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SecureScore()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .average_comparative_score import AverageComparativeScore
        from .control_score import ControlScore
        from .entity import Entity
        from .security_vendor_information import SecurityVendorInformation

        from .average_comparative_score import AverageComparativeScore
        from .control_score import ControlScore
        from .entity import Entity
        from .security_vendor_information import SecurityVendorInformation

        fields: Dict[str, Callable[[Any], None]] = {
            "active_user_count": lambda n : setattr(self, 'active_user_count', n.get_int_value()),
            "average_comparative_scores": lambda n : setattr(self, 'average_comparative_scores', n.get_collection_of_object_values(AverageComparativeScore)),
            "azure_tenant_id": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "control_scores": lambda n : setattr(self, 'control_scores', n.get_collection_of_object_values(ControlScore)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "current_score": lambda n : setattr(self, 'current_score', n.get_float_value()),
            "enabled_services": lambda n : setattr(self, 'enabled_services', n.get_collection_of_primitive_values(str)),
            "licensed_user_count": lambda n : setattr(self, 'licensed_user_count', n.get_int_value()),
            "max_score": lambda n : setattr(self, 'max_score', n.get_float_value()),
            "vendor_information": lambda n : setattr(self, 'vendor_information', n.get_object_value(SecurityVendorInformation)),
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
        writer.write_int_value("active_user_count", self.active_user_count)
        writer.write_collection_of_object_values("average_comparative_scores", self.average_comparative_scores)
        writer.write_str_value("azure_tenant_id", self.azure_tenant_id)
        writer.write_collection_of_object_values("control_scores", self.control_scores)
        writer.write_datetime_value("created_date_time", self.created_date_time)
        writer.write_float_value("current_score", self.current_score)
        writer.write_collection_of_primitive_values("enabled_services", self.enabled_services)
        writer.write_int_value("licensed_user_count", self.licensed_user_count)
        writer.write_float_value("max_score", self.max_score)
        writer.write_object_value("vendor_information", self.vendor_information)
    

