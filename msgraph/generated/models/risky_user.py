from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
risk_detail = lazy_import('msgraph.generated.models.risk_detail')
risk_level = lazy_import('msgraph.generated.models.risk_level')
risk_state = lazy_import('msgraph.generated.models.risk_state')
risky_user_history_item = lazy_import('msgraph.generated.models.risky_user_history_item')

class RiskyUser(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new RiskyUser and sets the default values.
        """
        super().__init__()
        # The activity related to user risk level change
        self._history: Optional[List[risky_user_history_item.RiskyUserHistoryItem]] = None
        # Indicates whether the user is deleted. Possible values are: true, false.
        self._is_deleted: Optional[bool] = None
        # Indicates whether a user's risky state is being processed by the backend.
        self._is_processing: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Details of the detected risk. Possible values are: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, hidden, adminConfirmedUserCompromised, unknownFutureValue.
        self._risk_detail: Optional[risk_detail.RiskDetail] = None
        # The date and time that the risky user was last updated.  The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._risk_last_updated_date_time: Optional[datetime] = None
        # Level of the detected risky user. Possible values are: low, medium, high, hidden, none, unknownFutureValue.
        self._risk_level: Optional[risk_level.RiskLevel] = None
        # State of the user's risk. Possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
        self._risk_state: Optional[risk_state.RiskState] = None
        # Risky user display name.
        self._user_display_name: Optional[str] = None
        # Risky user principal name.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RiskyUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RiskyUser
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RiskyUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(risky_user_history_item.RiskyUserHistoryItem)),
            "is_deleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "is_processing": lambda n : setattr(self, 'is_processing', n.get_bool_value()),
            "risk_detail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(risk_detail.RiskDetail)),
            "risk_last_updated_date_time": lambda n : setattr(self, 'risk_last_updated_date_time', n.get_datetime_value()),
            "risk_level": lambda n : setattr(self, 'risk_level', n.get_enum_value(risk_level.RiskLevel)),
            "risk_state": lambda n : setattr(self, 'risk_state', n.get_enum_value(risk_state.RiskState)),
            "user_display_name": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def history(self,) -> Optional[List[risky_user_history_item.RiskyUserHistoryItem]]:
        """
        Gets the history property value. The activity related to user risk level change
        Returns: Optional[List[risky_user_history_item.RiskyUserHistoryItem]]
        """
        return self._history
    
    @history.setter
    def history(self,value: Optional[List[risky_user_history_item.RiskyUserHistoryItem]] = None) -> None:
        """
        Sets the history property value. The activity related to user risk level change
        Args:
            value: Value to set for the history property.
        """
        self._history = value
    
    @property
    def is_deleted(self,) -> Optional[bool]:
        """
        Gets the isDeleted property value. Indicates whether the user is deleted. Possible values are: true, false.
        Returns: Optional[bool]
        """
        return self._is_deleted
    
    @is_deleted.setter
    def is_deleted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDeleted property value. Indicates whether the user is deleted. Possible values are: true, false.
        Args:
            value: Value to set for the isDeleted property.
        """
        self._is_deleted = value
    
    @property
    def is_processing(self,) -> Optional[bool]:
        """
        Gets the isProcessing property value. Indicates whether a user's risky state is being processed by the backend.
        Returns: Optional[bool]
        """
        return self._is_processing
    
    @is_processing.setter
    def is_processing(self,value: Optional[bool] = None) -> None:
        """
        Sets the isProcessing property value. Indicates whether a user's risky state is being processed by the backend.
        Args:
            value: Value to set for the isProcessing property.
        """
        self._is_processing = value
    
    @property
    def risk_detail(self,) -> Optional[risk_detail.RiskDetail]:
        """
        Gets the riskDetail property value. Details of the detected risk. Possible values are: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, hidden, adminConfirmedUserCompromised, unknownFutureValue.
        Returns: Optional[risk_detail.RiskDetail]
        """
        return self._risk_detail
    
    @risk_detail.setter
    def risk_detail(self,value: Optional[risk_detail.RiskDetail] = None) -> None:
        """
        Sets the riskDetail property value. Details of the detected risk. Possible values are: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, hidden, adminConfirmedUserCompromised, unknownFutureValue.
        Args:
            value: Value to set for the riskDetail property.
        """
        self._risk_detail = value
    
    @property
    def risk_last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the riskLastUpdatedDateTime property value. The date and time that the risky user was last updated.  The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._risk_last_updated_date_time
    
    @risk_last_updated_date_time.setter
    def risk_last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the riskLastUpdatedDateTime property value. The date and time that the risky user was last updated.  The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the riskLastUpdatedDateTime property.
        """
        self._risk_last_updated_date_time = value
    
    @property
    def risk_level(self,) -> Optional[risk_level.RiskLevel]:
        """
        Gets the riskLevel property value. Level of the detected risky user. Possible values are: low, medium, high, hidden, none, unknownFutureValue.
        Returns: Optional[risk_level.RiskLevel]
        """
        return self._risk_level
    
    @risk_level.setter
    def risk_level(self,value: Optional[risk_level.RiskLevel] = None) -> None:
        """
        Sets the riskLevel property value. Level of the detected risky user. Possible values are: low, medium, high, hidden, none, unknownFutureValue.
        Args:
            value: Value to set for the riskLevel property.
        """
        self._risk_level = value
    
    @property
    def risk_state(self,) -> Optional[risk_state.RiskState]:
        """
        Gets the riskState property value. State of the user's risk. Possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
        Returns: Optional[risk_state.RiskState]
        """
        return self._risk_state
    
    @risk_state.setter
    def risk_state(self,value: Optional[risk_state.RiskState] = None) -> None:
        """
        Sets the riskState property value. State of the user's risk. Possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
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
        writer.write_collection_of_object_values("history", self.history)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_bool_value("isProcessing", self.is_processing)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_datetime_value("riskLastUpdatedDateTime", self.risk_last_updated_date_time)
        writer.write_enum_value("riskLevel", self.risk_level)
        writer.write_enum_value("riskState", self.risk_state)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. Risky user display name.
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. Risky user display name.
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. Risky user principal name.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. Risky user principal name.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

