from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .average_comparative_score import AverageComparativeScore
    from .control_score import ControlScore
    from .entity import Entity
    from .security_vendor_information import SecurityVendorInformation

from .entity import Entity

@dataclass
class SecureScore(Entity, Parsable):
    # Active user count of the given tenant.
    active_user_count: Optional[int] = None
    # Average score by different scopes (for example, average by industry, average by seating) and control category (Identity, Data, Device, Apps, Infrastructure) within the scope.
    average_comparative_scores: Optional[list[AverageComparativeScore]] = None
    # GUID string for tenant ID.
    azure_tenant_id: Optional[str] = None
    # Contains tenant scores for a set of controls.
    control_scores: Optional[list[ControlScore]] = None
    # When the report was created.
    created_date_time: Optional[datetime.datetime] = None
    # Tenant current attained score on specified date.
    current_score: Optional[float] = None
    # Microsoft-provided services for the tenant (for example, Exchange online, Skype, Sharepoint).
    enabled_services: Optional[list[str]] = None
    # Licensed user count of the given tenant.
    licensed_user_count: Optional[int] = None
    # Tenant maximum possible score on specified date.
    max_score: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Complex type containing details about the security product/service vendor, provider, and subprovider (for example, vendor=Microsoft; provider=SecureScore). Required.
    vendor_information: Optional[SecurityVendorInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecureScore:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecureScore
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecureScore()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .average_comparative_score import AverageComparativeScore
        from .control_score import ControlScore
        from .entity import Entity
        from .security_vendor_information import SecurityVendorInformation

        from .average_comparative_score import AverageComparativeScore
        from .control_score import ControlScore
        from .entity import Entity
        from .security_vendor_information import SecurityVendorInformation

        fields: dict[str, Callable[[Any], None]] = {
            "activeUserCount": lambda n : setattr(self, 'active_user_count', n.get_int_value()),
            "averageComparativeScores": lambda n : setattr(self, 'average_comparative_scores', n.get_collection_of_object_values(AverageComparativeScore)),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "controlScores": lambda n : setattr(self, 'control_scores', n.get_collection_of_object_values(ControlScore)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "currentScore": lambda n : setattr(self, 'current_score', n.get_float_value()),
            "enabledServices": lambda n : setattr(self, 'enabled_services', n.get_collection_of_primitive_values(str)),
            "licensedUserCount": lambda n : setattr(self, 'licensed_user_count', n.get_int_value()),
            "maxScore": lambda n : setattr(self, 'max_score', n.get_float_value()),
            "vendorInformation": lambda n : setattr(self, 'vendor_information', n.get_object_value(SecurityVendorInformation)),
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
    

