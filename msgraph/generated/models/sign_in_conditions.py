from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_flow import AuthenticationFlow
    from .conditional_access_client_app import ConditionalAccessClientApp
    from .conditional_access_device_platform import ConditionalAccessDevicePlatform
    from .device_info import DeviceInfo
    from .insider_risk_level import InsiderRiskLevel
    from .risk_level import RiskLevel

@dataclass
class SignInConditions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Type of authentication flow. The possible value is: deviceCodeFlow or authenticationTransfer. Default value is none.
    authentication_flow: Optional[AuthenticationFlow] = None
    # Client application type. The possible value is: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other, unknownFutureValue. Default value is all.
    client_app_type: Optional[ConditionalAccessClientApp] = None
    # Country from where the identity is authenticating.
    country: Optional[str] = None
    # Information about the device used for the sign-in.
    device_info: Optional[DeviceInfo] = None
    # Device platform. The possible value is: android, iOS, windows, windowsPhone, macOS, all, unknownFutureValue, linux. Default value is all.
    device_platform: Optional[ConditionalAccessDevicePlatform] = None
    # Insider risk associated with the authenticating user. The possible value is: none, minor, moderate, elevated, unknownFutureValue. Default value is none.
    insider_risk_level: Optional[InsiderRiskLevel] = None
    # Ip address of the authenticating identity.
    ip_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Risk associated with the service principal. The possible value is: low, medium, high, hidden, none, unknownFutureValue. Default value is none.
    service_principal_risk_level: Optional[RiskLevel] = None
    # Sign-in risk associated with the user. The possible value is: low, medium, high, hidden, none, unknownFutureValue. Default value is none.
    sign_in_risk_level: Optional[RiskLevel] = None
    # The authenticating user's risk level. The possible value is: low, medium, high, hidden, none, unknownFutureValue. Default value is none.
    user_risk_level: Optional[RiskLevel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SignInConditions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignInConditions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SignInConditions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_flow import AuthenticationFlow
        from .conditional_access_client_app import ConditionalAccessClientApp
        from .conditional_access_device_platform import ConditionalAccessDevicePlatform
        from .device_info import DeviceInfo
        from .insider_risk_level import InsiderRiskLevel
        from .risk_level import RiskLevel

        from .authentication_flow import AuthenticationFlow
        from .conditional_access_client_app import ConditionalAccessClientApp
        from .conditional_access_device_platform import ConditionalAccessDevicePlatform
        from .device_info import DeviceInfo
        from .insider_risk_level import InsiderRiskLevel
        from .risk_level import RiskLevel

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationFlow": lambda n : setattr(self, 'authentication_flow', n.get_object_value(AuthenticationFlow)),
            "clientAppType": lambda n : setattr(self, 'client_app_type', n.get_enum_value(ConditionalAccessClientApp)),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "deviceInfo": lambda n : setattr(self, 'device_info', n.get_object_value(DeviceInfo)),
            "devicePlatform": lambda n : setattr(self, 'device_platform', n.get_enum_value(ConditionalAccessDevicePlatform)),
            "insiderRiskLevel": lambda n : setattr(self, 'insider_risk_level', n.get_enum_value(InsiderRiskLevel)),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "servicePrincipalRiskLevel": lambda n : setattr(self, 'service_principal_risk_level', n.get_enum_value(RiskLevel)),
            "signInRiskLevel": lambda n : setattr(self, 'sign_in_risk_level', n.get_enum_value(RiskLevel)),
            "userRiskLevel": lambda n : setattr(self, 'user_risk_level', n.get_enum_value(RiskLevel)),
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
        writer.write_object_value("authenticationFlow", self.authentication_flow)
        writer.write_enum_value("clientAppType", self.client_app_type)
        writer.write_str_value("country", self.country)
        writer.write_object_value("deviceInfo", self.device_info)
        writer.write_enum_value("devicePlatform", self.device_platform)
        writer.write_enum_value("insiderRiskLevel", self.insider_risk_level)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("servicePrincipalRiskLevel", self.service_principal_risk_level)
        writer.write_enum_value("signInRiskLevel", self.sign_in_risk_level)
        writer.write_enum_value("userRiskLevel", self.user_risk_level)
        writer.write_additional_data_value(self.additional_data)
    

