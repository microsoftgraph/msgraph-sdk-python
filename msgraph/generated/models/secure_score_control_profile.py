from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_information import ComplianceInformation
    from .entity import Entity
    from .secure_score_control_state_update import SecureScoreControlStateUpdate
    from .security_vendor_information import SecurityVendorInformation

from .entity import Entity

@dataclass
class SecureScoreControlProfile(Entity, Parsable):
    # Control action type (Config, Review, Behavior).
    action_type: Optional[str] = None
    # URL to where the control can be actioned.
    action_url: Optional[str] = None
    # GUID string for tenant ID.
    azure_tenant_id: Optional[str] = None
    # The collection of compliance information associated with secure score control. Not implemented. Currently returns null.
    compliance_information: Optional[list[ComplianceInformation]] = None
    # Control action category (Identity, Data, Device, Apps, Infrastructure).
    control_category: Optional[str] = None
    # Flag to indicate where the tenant has marked a control (ignored, thirdParty, reviewed) (supports update).
    control_state_updates: Optional[list[SecureScoreControlStateUpdate]] = None
    # Flag to indicate if a control is depreciated.
    deprecated: Optional[bool] = None
    # Resource cost of implemmentating control (low, moderate, high).
    implementation_cost: Optional[str] = None
    # Time at which the control profile entity was last modified. The Timestamp type represents date and time
    last_modified_date_time: Optional[datetime.datetime] = None
    # max attainable score for the control.
    max_score: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Microsoft's stack ranking of control.
    rank: Optional[int] = None
    # Description of what the control will help remediate.
    remediation: Optional[str] = None
    # Description of the impact on users of the remediation.
    remediation_impact: Optional[str] = None
    # Service that owns the control (Exchange, Sharepoint, Microsoft Entra ID).
    service: Optional[str] = None
    # List of threats the control mitigates (accountBreach, dataDeletion, dataExfiltration, dataSpillage, elevationOfPrivilege, maliciousInsider, passwordCracking, phishingOrWhaling, spoofing).
    threats: Optional[list[str]] = None
    # Control tier (Core, Defense in Depth, Advanced.)
    tier: Optional[str] = None
    # Title of the control.
    title: Optional[str] = None
    # User impact of implementing control (low, moderate, high).
    user_impact: Optional[str] = None
    # Complex type containing details about the security product/service vendor, provider, and subprovider (for example, vendor=Microsoft; provider=SecureScore). Required.
    vendor_information: Optional[SecurityVendorInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecureScoreControlProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecureScoreControlProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecureScoreControlProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_information import ComplianceInformation
        from .entity import Entity
        from .secure_score_control_state_update import SecureScoreControlStateUpdate
        from .security_vendor_information import SecurityVendorInformation

        from .compliance_information import ComplianceInformation
        from .entity import Entity
        from .secure_score_control_state_update import SecureScoreControlStateUpdate
        from .security_vendor_information import SecurityVendorInformation

        fields: dict[str, Callable[[Any], None]] = {
            "actionType": lambda n : setattr(self, 'action_type', n.get_str_value()),
            "actionUrl": lambda n : setattr(self, 'action_url', n.get_str_value()),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "complianceInformation": lambda n : setattr(self, 'compliance_information', n.get_collection_of_object_values(ComplianceInformation)),
            "controlCategory": lambda n : setattr(self, 'control_category', n.get_str_value()),
            "controlStateUpdates": lambda n : setattr(self, 'control_state_updates', n.get_collection_of_object_values(SecureScoreControlStateUpdate)),
            "deprecated": lambda n : setattr(self, 'deprecated', n.get_bool_value()),
            "implementationCost": lambda n : setattr(self, 'implementation_cost', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "maxScore": lambda n : setattr(self, 'max_score', n.get_float_value()),
            "rank": lambda n : setattr(self, 'rank', n.get_int_value()),
            "remediation": lambda n : setattr(self, 'remediation', n.get_str_value()),
            "remediationImpact": lambda n : setattr(self, 'remediation_impact', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "threats": lambda n : setattr(self, 'threats', n.get_collection_of_primitive_values(str)),
            "tier": lambda n : setattr(self, 'tier', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "userImpact": lambda n : setattr(self, 'user_impact', n.get_str_value()),
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
        writer.write_str_value("actionType", self.action_type)
        writer.write_str_value("actionUrl", self.action_url)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_collection_of_object_values("complianceInformation", self.compliance_information)
        writer.write_str_value("controlCategory", self.control_category)
        writer.write_collection_of_object_values("controlStateUpdates", self.control_state_updates)
        writer.write_bool_value("deprecated", self.deprecated)
        writer.write_str_value("implementationCost", self.implementation_cost)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_float_value("maxScore", self.max_score)
        writer.write_int_value("rank", self.rank)
        writer.write_str_value("remediation", self.remediation)
        writer.write_str_value("remediationImpact", self.remediation_impact)
        writer.write_str_value("service", self.service)
        writer.write_collection_of_primitive_values("threats", self.threats)
        writer.write_str_value("tier", self.tier)
        writer.write_str_value("title", self.title)
        writer.write_str_value("userImpact", self.user_impact)
        writer.write_object_value("vendorInformation", self.vendor_information)
    

