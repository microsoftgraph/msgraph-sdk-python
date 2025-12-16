from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .applied_conditional_access_policy import AppliedConditionalAccessPolicy
    from .conditional_access_status import ConditionalAccessStatus
    from .device_detail import DeviceDetail
    from .entity import Entity
    from .risk_detail import RiskDetail
    from .risk_event_type import RiskEventType
    from .risk_level import RiskLevel
    from .risk_state import RiskState
    from .sign_in_location import SignInLocation
    from .sign_in_status import SignInStatus

from .entity import Entity

@dataclass
class SignIn(Entity, Parsable):
    # App name displayed in the Microsoft Entra admin center.  Supports $filter (eq, startsWith).
    app_display_name: Optional[str] = None
    # Unique GUID that represents the app ID in the Microsoft Entra ID.  Supports $filter (eq).
    app_id: Optional[str] = None
    # Provides a list of conditional access policies that the corresponding sign-in activity triggers. Apps need more Conditional Access-related privileges to read the details of this property. For more information, see Permissions for viewing applied conditional access (CA) policies in sign-ins.
    applied_conditional_access_policies: Optional[list[AppliedConditionalAccessPolicy]] = None
    # Identifies the client used for the sign-in activity. Modern authentication clients include Browser, modern clients. Legacy authentication clients include Exchange ActiveSync, IMAP, MAPI, SMTP, POP, and other clients.  Supports $filter (eq).
    client_app_used: Optional[str] = None
    # Reports status of an activated conditional access policy. The possible values are: success, failure, notApplied, and unknownFutureValue.  Supports $filter (eq).
    conditional_access_status: Optional[ConditionalAccessStatus] = None
    # The request ID sent from the client when the sign-in is initiated. Used to troubleshoot sign-in activity.  Supports $filter (eq).
    correlation_id: Optional[str] = None
    # Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as 2014-01-01T00:00:00Z.  Supports $orderby, $filter (eq, le, and ge).
    created_date_time: Optional[datetime.datetime] = None
    # Device information from where the sign-in occurred; includes device ID, operating system, and browser.  Supports $filter (eq, startsWith) on browser and operatingSytem properties.
    device_detail: Optional[DeviceDetail] = None
    # IP address of the client used to sign in.  Supports $filter (eq, startsWith).
    ip_address: Optional[str] = None
    # Indicates whether a sign-in is interactive.
    is_interactive: Optional[bool] = None
    # Provides the city, state, and country code where the sign-in originated.  Supports $filter (eq, startsWith) on city, state, and countryOrRegion properties.
    location: Optional[SignInLocation] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the resource the user signed into.  Supports $filter (eq).
    resource_display_name: Optional[str] = None
    # ID of the resource that the user signed into.  Supports $filter (eq).
    resource_id: Optional[str] = None
    # The reason behind a specific state of a risky user, sign-in, or a risk event. The value none means that Microsoft Entra risk detection did not flag the user or the sign-in as a risky event so far.  Supports $filter (eq). Note: Details for this property are only available for Microsoft Entra ID P2 customers. All other customers are returned hidden.
    risk_detail: Optional[RiskDetail] = None
    # The riskEventTypes property
    risk_event_types: Optional[list[RiskEventType]] = None
    # The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence, generic, or unknownFutureValue.  Supports $filter (eq, startsWith).
    risk_event_types_v2: Optional[list[str]] = None
    # Aggregated risk level. The possible values are: none, low, medium, high, hidden, and unknownFutureValue. The value hidden means the user or sign-in wasn't enabled for Microsoft Entra ID Protection.  Supports $filter (eq).  Note: Details for this property are only available for Microsoft Entra ID P2 customers. All other customers are returned hidden.
    risk_level_aggregated: Optional[RiskLevel] = None
    # Risk level during sign-in. The possible values are: none, low, medium, high, hidden, and unknownFutureValue. The value hidden means the user or sign-in wasn't enabled for Microsoft Entra ID Protection.  Supports $filter (eq). Note: Details for this property are only available for Microsoft Entra ID P2 customers. All other customers are returned hidden.
    risk_level_during_sign_in: Optional[RiskLevel] = None
    # Reports status of the risky user, sign-in, or a risk event. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.  Supports $filter (eq).
    risk_state: Optional[RiskState] = None
    # Sign-in status. Includes the error code and description of the error (if a sign-in failure occurs).  Supports $filter (eq) on errorCode property.
    status: Optional[SignInStatus] = None
    # Display name of the user that initiated the sign-in.  Supports $filter (eq, startsWith).
    user_display_name: Optional[str] = None
    # ID of the user that initiated the sign-in.  Supports $filter (eq).
    user_id: Optional[str] = None
    # User principal name of the user that initiated the sign-in. This value is always in lowercase. For guest users whose values in the user object typically contain #EXT# before the domain part, this property stores the value in both lowercase and the 'true' format. For example, while the user object stores AdeleVance_fabrikam.com#EXT#@contoso.com, the sign-in logs store adelevance@fabrikam.com. Supports $filter (eq, startsWith).
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SignIn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignIn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SignIn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .applied_conditional_access_policy import AppliedConditionalAccessPolicy
        from .conditional_access_status import ConditionalAccessStatus
        from .device_detail import DeviceDetail
        from .entity import Entity
        from .risk_detail import RiskDetail
        from .risk_event_type import RiskEventType
        from .risk_level import RiskLevel
        from .risk_state import RiskState
        from .sign_in_location import SignInLocation
        from .sign_in_status import SignInStatus

        from .applied_conditional_access_policy import AppliedConditionalAccessPolicy
        from .conditional_access_status import ConditionalAccessStatus
        from .device_detail import DeviceDetail
        from .entity import Entity
        from .risk_detail import RiskDetail
        from .risk_event_type import RiskEventType
        from .risk_level import RiskLevel
        from .risk_state import RiskState
        from .sign_in_location import SignInLocation
        from .sign_in_status import SignInStatus

        fields: dict[str, Callable[[Any], None]] = {
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appliedConditionalAccessPolicies": lambda n : setattr(self, 'applied_conditional_access_policies', n.get_collection_of_object_values(AppliedConditionalAccessPolicy)),
            "clientAppUsed": lambda n : setattr(self, 'client_app_used', n.get_str_value()),
            "conditionalAccessStatus": lambda n : setattr(self, 'conditional_access_status', n.get_enum_value(ConditionalAccessStatus)),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deviceDetail": lambda n : setattr(self, 'device_detail', n.get_object_value(DeviceDetail)),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "isInteractive": lambda n : setattr(self, 'is_interactive', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(SignInLocation)),
            "resourceDisplayName": lambda n : setattr(self, 'resource_display_name', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "riskDetail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(RiskDetail)),
            "riskEventTypes": lambda n : setattr(self, 'risk_event_types', n.get_collection_of_enum_values(RiskEventType)),
            "riskEventTypes_v2": lambda n : setattr(self, 'risk_event_types_v2', n.get_collection_of_primitive_values(str)),
            "riskLevelAggregated": lambda n : setattr(self, 'risk_level_aggregated', n.get_enum_value(RiskLevel)),
            "riskLevelDuringSignIn": lambda n : setattr(self, 'risk_level_during_sign_in', n.get_enum_value(RiskLevel)),
            "riskState": lambda n : setattr(self, 'risk_state', n.get_enum_value(RiskState)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(SignInStatus)),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_collection_of_object_values("appliedConditionalAccessPolicies", self.applied_conditional_access_policies)
        writer.write_str_value("clientAppUsed", self.client_app_used)
        writer.write_enum_value("conditionalAccessStatus", self.conditional_access_status)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("deviceDetail", self.device_detail)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_bool_value("isInteractive", self.is_interactive)
        writer.write_object_value("location", self.location)
        writer.write_str_value("resourceDisplayName", self.resource_display_name)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_collection_of_enum_values("riskEventTypes", self.risk_event_types)
        writer.write_collection_of_primitive_values("riskEventTypes_v2", self.risk_event_types_v2)
        writer.write_enum_value("riskLevelAggregated", self.risk_level_aggregated)
        writer.write_enum_value("riskLevelDuringSignIn", self.risk_level_during_sign_in)
        writer.write_enum_value("riskState", self.risk_state)
        writer.write_object_value("status", self.status)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

