from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
risk_detail = lazy_import('msgraph.generated.models.risk_detail')
risk_level = lazy_import('msgraph.generated.models.risk_level')
risk_state = lazy_import('msgraph.generated.models.risk_state')
risky_service_principal_history_item = lazy_import('msgraph.generated.models.risky_service_principal_history_item')

class RiskyServicePrincipal(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The globally unique identifier for the associated application (its appId property), if any.
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The globally unique identifier for the associated application (its appId property), if any.
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new riskyServicePrincipal and sets the default values.
        """
        super().__init__()
        # The globally unique identifier for the associated application (its appId property), if any.
        self._app_id: Optional[str] = None
        # The display name for the service principal.
        self._display_name: Optional[str] = None
        # Represents the risk history of Azure AD service principals.
        self._history: Optional[List[risky_service_principal_history_item.RiskyServicePrincipalHistoryItem]] = None
        # true if the service principal account is enabled; otherwise, false.
        self._is_enabled: Optional[bool] = None
        # Indicates whether Azure AD is currently processing the service principal's risky state.
        self._is_processing: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: none, hidden,  unknownFutureValue, adminConfirmedServicePrincipalCompromised, adminDismissedAllRiskForServicePrincipal. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: adminConfirmedServicePrincipalCompromised , adminDismissedAllRiskForServicePrincipal.
        self._risk_detail: Optional[risk_detail.RiskDetail] = None
        # The date and time that the risk state was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2021 is 2021-01-01T00:00:00Z. Supports $filter (eq).
        self._risk_last_updated_date_time: Optional[datetime] = None
        # Level of the detected risky workload identity. The possible values are: low, medium, high, hidden, none, unknownFutureValue. Supports $filter (eq).
        self._risk_level: Optional[risk_level.RiskLevel] = None
        # State of the service principal's risk. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
        self._risk_state: Optional[risk_state.RiskState] = None
        # Identifies whether the service principal represents an Application, a ManagedIdentity, or a legacy application (socialIdp). This is set by Azure AD internally and is inherited from servicePrincipal.
        self._service_principal_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RiskyServicePrincipal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RiskyServicePrincipal
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RiskyServicePrincipal()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the service principal.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the service principal.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(risky_service_principal_history_item.RiskyServicePrincipalHistoryItem)),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "is_processing": lambda n : setattr(self, 'is_processing', n.get_bool_value()),
            "risk_detail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(risk_detail.RiskDetail)),
            "risk_last_updated_date_time": lambda n : setattr(self, 'risk_last_updated_date_time', n.get_datetime_value()),
            "risk_level": lambda n : setattr(self, 'risk_level', n.get_enum_value(risk_level.RiskLevel)),
            "risk_state": lambda n : setattr(self, 'risk_state', n.get_enum_value(risk_state.RiskState)),
            "service_principal_type": lambda n : setattr(self, 'service_principal_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def history(self,) -> Optional[List[risky_service_principal_history_item.RiskyServicePrincipalHistoryItem]]:
        """
        Gets the history property value. Represents the risk history of Azure AD service principals.
        Returns: Optional[List[risky_service_principal_history_item.RiskyServicePrincipalHistoryItem]]
        """
        return self._history
    
    @history.setter
    def history(self,value: Optional[List[risky_service_principal_history_item.RiskyServicePrincipalHistoryItem]] = None) -> None:
        """
        Sets the history property value. Represents the risk history of Azure AD service principals.
        Args:
            value: Value to set for the history property.
        """
        self._history = value
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. true if the service principal account is enabled; otherwise, false.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. true if the service principal account is enabled; otherwise, false.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    @property
    def is_processing(self,) -> Optional[bool]:
        """
        Gets the isProcessing property value. Indicates whether Azure AD is currently processing the service principal's risky state.
        Returns: Optional[bool]
        """
        return self._is_processing
    
    @is_processing.setter
    def is_processing(self,value: Optional[bool] = None) -> None:
        """
        Sets the isProcessing property value. Indicates whether Azure AD is currently processing the service principal's risky state.
        Args:
            value: Value to set for the isProcessing property.
        """
        self._is_processing = value
    
    @property
    def risk_detail(self,) -> Optional[risk_detail.RiskDetail]:
        """
        Gets the riskDetail property value. Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: none, hidden,  unknownFutureValue, adminConfirmedServicePrincipalCompromised, adminDismissedAllRiskForServicePrincipal. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: adminConfirmedServicePrincipalCompromised , adminDismissedAllRiskForServicePrincipal.
        Returns: Optional[risk_detail.RiskDetail]
        """
        return self._risk_detail
    
    @risk_detail.setter
    def risk_detail(self,value: Optional[risk_detail.RiskDetail] = None) -> None:
        """
        Sets the riskDetail property value. Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: none, hidden,  unknownFutureValue, adminConfirmedServicePrincipalCompromised, adminDismissedAllRiskForServicePrincipal. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: adminConfirmedServicePrincipalCompromised , adminDismissedAllRiskForServicePrincipal.
        Args:
            value: Value to set for the riskDetail property.
        """
        self._risk_detail = value
    
    @property
    def risk_last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the riskLastUpdatedDateTime property value. The date and time that the risk state was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2021 is 2021-01-01T00:00:00Z. Supports $filter (eq).
        Returns: Optional[datetime]
        """
        return self._risk_last_updated_date_time
    
    @risk_last_updated_date_time.setter
    def risk_last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the riskLastUpdatedDateTime property value. The date and time that the risk state was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2021 is 2021-01-01T00:00:00Z. Supports $filter (eq).
        Args:
            value: Value to set for the riskLastUpdatedDateTime property.
        """
        self._risk_last_updated_date_time = value
    
    @property
    def risk_level(self,) -> Optional[risk_level.RiskLevel]:
        """
        Gets the riskLevel property value. Level of the detected risky workload identity. The possible values are: low, medium, high, hidden, none, unknownFutureValue. Supports $filter (eq).
        Returns: Optional[risk_level.RiskLevel]
        """
        return self._risk_level
    
    @risk_level.setter
    def risk_level(self,value: Optional[risk_level.RiskLevel] = None) -> None:
        """
        Sets the riskLevel property value. Level of the detected risky workload identity. The possible values are: low, medium, high, hidden, none, unknownFutureValue. Supports $filter (eq).
        Args:
            value: Value to set for the riskLevel property.
        """
        self._risk_level = value
    
    @property
    def risk_state(self,) -> Optional[risk_state.RiskState]:
        """
        Gets the riskState property value. State of the service principal's risk. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
        Returns: Optional[risk_state.RiskState]
        """
        return self._risk_state
    
    @risk_state.setter
    def risk_state(self,value: Optional[risk_state.RiskState] = None) -> None:
        """
        Sets the riskState property value. State of the service principal's risk. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
        Args:
            value: Value to set for the riskState property.
        """
        self._risk_state = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("history", self.history)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("isProcessing", self.is_processing)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_datetime_value("riskLastUpdatedDateTime", self.risk_last_updated_date_time)
        writer.write_enum_value("riskLevel", self.risk_level)
        writer.write_enum_value("riskState", self.risk_state)
        writer.write_str_value("servicePrincipalType", self.service_principal_type)
    
    @property
    def service_principal_type(self,) -> Optional[str]:
        """
        Gets the servicePrincipalType property value. Identifies whether the service principal represents an Application, a ManagedIdentity, or a legacy application (socialIdp). This is set by Azure AD internally and is inherited from servicePrincipal.
        Returns: Optional[str]
        """
        return self._service_principal_type
    
    @service_principal_type.setter
    def service_principal_type(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePrincipalType property value. Identifies whether the service principal represents an Application, a ManagedIdentity, or a legacy application (socialIdp). This is set by Azure AD internally and is inherited from servicePrincipal.
        Args:
            value: Value to set for the servicePrincipalType property.
        """
        self._service_principal_type = value
    

