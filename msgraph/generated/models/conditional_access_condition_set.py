from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_applications, conditional_access_client_app, conditional_access_client_applications, conditional_access_devices, conditional_access_locations, conditional_access_platforms, conditional_access_users, risk_level

@dataclass
class ConditionalAccessConditionSet(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Applications and user actions included in and excluded from the policy. Required.
    applications: Optional[conditional_access_applications.ConditionalAccessApplications] = None
    # Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other. Required.
    client_app_types: Optional[List[conditional_access_client_app.ConditionalAccessClientApp]] = None
    # Client applications (service principals and workload identities) included in and excluded from the policy. Either users or clientApplications is required.
    client_applications: Optional[conditional_access_client_applications.ConditionalAccessClientApplications] = None
    # Devices in the policy.
    devices: Optional[conditional_access_devices.ConditionalAccessDevices] = None
    # Locations included in and excluded from the policy.
    locations: Optional[conditional_access_locations.ConditionalAccessLocations] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Platforms included in and excluded from the policy.
    platforms: Optional[conditional_access_platforms.ConditionalAccessPlatforms] = None
    # Service principal risk levels included in the policy. Possible values are: low, medium, high, none, unknownFutureValue.
    service_principal_risk_levels: Optional[List[risk_level.RiskLevel]] = None
    # Sign-in risk levels included in the policy. Possible values are: low, medium, high, hidden, none, unknownFutureValue. Required.
    sign_in_risk_levels: Optional[List[risk_level.RiskLevel]] = None
    # User risk levels included in the policy. Possible values are: low, medium, high, hidden, none, unknownFutureValue. Required.
    user_risk_levels: Optional[List[risk_level.RiskLevel]] = None
    # Users, groups, and roles included in and excluded from the policy. Either users or clientApplications is required.
    users: Optional[conditional_access_users.ConditionalAccessUsers] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessConditionSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessConditionSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessConditionSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conditional_access_applications, conditional_access_client_app, conditional_access_client_applications, conditional_access_devices, conditional_access_locations, conditional_access_platforms, conditional_access_users, risk_level

        fields: Dict[str, Callable[[Any], None]] = {
            "applications": lambda n : setattr(self, 'applications', n.get_object_value(conditional_access_applications.ConditionalAccessApplications)),
            "clientApplications": lambda n : setattr(self, 'client_applications', n.get_object_value(conditional_access_client_applications.ConditionalAccessClientApplications)),
            "clientAppTypes": lambda n : setattr(self, 'client_app_types', n.get_collection_of_enum_values(conditional_access_client_app.ConditionalAccessClientApp)),
            "devices": lambda n : setattr(self, 'devices', n.get_object_value(conditional_access_devices.ConditionalAccessDevices)),
            "locations": lambda n : setattr(self, 'locations', n.get_object_value(conditional_access_locations.ConditionalAccessLocations)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "platforms": lambda n : setattr(self, 'platforms', n.get_object_value(conditional_access_platforms.ConditionalAccessPlatforms)),
            "servicePrincipalRiskLevels": lambda n : setattr(self, 'service_principal_risk_levels', n.get_collection_of_enum_values(risk_level.RiskLevel)),
            "signInRiskLevels": lambda n : setattr(self, 'sign_in_risk_levels', n.get_collection_of_enum_values(risk_level.RiskLevel)),
            "users": lambda n : setattr(self, 'users', n.get_object_value(conditional_access_users.ConditionalAccessUsers)),
            "userRiskLevels": lambda n : setattr(self, 'user_risk_levels', n.get_collection_of_enum_values(risk_level.RiskLevel)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("applications", self.applications)
        writer.write_object_value("clientApplications", self.client_applications)
        writer.write_enum_value("clientAppTypes", self.client_app_types)
        writer.write_object_value("devices", self.devices)
        writer.write_object_value("locations", self.locations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("platforms", self.platforms)
        writer.write_enum_value("servicePrincipalRiskLevels", self.service_principal_risk_levels)
        writer.write_enum_value("signInRiskLevels", self.sign_in_risk_levels)
        writer.write_object_value("users", self.users)
        writer.write_enum_value("userRiskLevels", self.user_risk_levels)
        writer.write_additional_data_value(self.additional_data)
    

