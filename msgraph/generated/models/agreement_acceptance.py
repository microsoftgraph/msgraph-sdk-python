from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

agreement_acceptance_state = lazy_import('msgraph.generated.models.agreement_acceptance_state')
entity = lazy_import('msgraph.generated.models.entity')

class AgreementAcceptance(entity.Entity):
    """
    Provides operations to manage the collection of agreementAcceptance entities.
    """
    @property
    def agreement_file_id(self,) -> Optional[str]:
        """
        Gets the agreementFileId property value. The identifier of the agreement file accepted by the user.
        Returns: Optional[str]
        """
        return self._agreement_file_id
    
    @agreement_file_id.setter
    def agreement_file_id(self,value: Optional[str] = None) -> None:
        """
        Sets the agreementFileId property value. The identifier of the agreement file accepted by the user.
        Args:
            value: Value to set for the agreementFileId property.
        """
        self._agreement_file_id = value
    
    @property
    def agreement_id(self,) -> Optional[str]:
        """
        Gets the agreementId property value. The identifier of the agreement.
        Returns: Optional[str]
        """
        return self._agreement_id
    
    @agreement_id.setter
    def agreement_id(self,value: Optional[str] = None) -> None:
        """
        Sets the agreementId property value. The identifier of the agreement.
        Args:
            value: Value to set for the agreementId property.
        """
        self._agreement_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new agreementAcceptance and sets the default values.
        """
        super().__init__()
        # The identifier of the agreement file accepted by the user.
        self._agreement_file_id: Optional[str] = None
        # The identifier of the agreement.
        self._agreement_id: Optional[str] = None
        # The display name of the device used for accepting the agreement.
        self._device_display_name: Optional[str] = None
        # The unique identifier of the device used for accepting the agreement. Supports $filter (eq) and eq for null values.
        self._device_id: Optional[str] = None
        # The operating system used to accept the agreement.
        self._device_o_s_type: Optional[str] = None
        # The operating system version of the device used to accept the agreement.
        self._device_o_s_version: Optional[str] = None
        # The expiration date time of the acceptance. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ge, le) and eq for null values.
        self._expiration_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._recorded_date_time: Optional[datetime] = None
        # The state of the agreement acceptance. Possible values are: accepted, declined. Supports $filter (eq).
        self._state: Optional[agreement_acceptance_state.AgreementAcceptanceState] = None
        # Display name of the user when the acceptance was recorded.
        self._user_display_name: Optional[str] = None
        # Email of the user when the acceptance was recorded.
        self._user_email: Optional[str] = None
        # The identifier of the user who accepted the agreement. Supports $filter (eq).
        self._user_id: Optional[str] = None
        # UPN of the user when the acceptance was recorded.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AgreementAcceptance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AgreementAcceptance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AgreementAcceptance()
    
    @property
    def device_display_name(self,) -> Optional[str]:
        """
        Gets the deviceDisplayName property value. The display name of the device used for accepting the agreement.
        Returns: Optional[str]
        """
        return self._device_display_name
    
    @device_display_name.setter
    def device_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceDisplayName property value. The display name of the device used for accepting the agreement.
        Args:
            value: Value to set for the deviceDisplayName property.
        """
        self._device_display_name = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The unique identifier of the device used for accepting the agreement. Supports $filter (eq) and eq for null values.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The unique identifier of the device used for accepting the agreement. Supports $filter (eq) and eq for null values.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_o_s_type(self,) -> Optional[str]:
        """
        Gets the deviceOSType property value. The operating system used to accept the agreement.
        Returns: Optional[str]
        """
        return self._device_o_s_type
    
    @device_o_s_type.setter
    def device_o_s_type(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceOSType property value. The operating system used to accept the agreement.
        Args:
            value: Value to set for the deviceOSType property.
        """
        self._device_o_s_type = value
    
    @property
    def device_o_s_version(self,) -> Optional[str]:
        """
        Gets the deviceOSVersion property value. The operating system version of the device used to accept the agreement.
        Returns: Optional[str]
        """
        return self._device_o_s_version
    
    @device_o_s_version.setter
    def device_o_s_version(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceOSVersion property value. The operating system version of the device used to accept the agreement.
        Args:
            value: Value to set for the deviceOSVersion property.
        """
        self._device_o_s_version = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The expiration date time of the acceptance. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ge, le) and eq for null values.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The expiration date time of the acceptance. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ge, le) and eq for null values.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "agreement_file_id": lambda n : setattr(self, 'agreement_file_id', n.get_str_value()),
            "agreement_id": lambda n : setattr(self, 'agreement_id', n.get_str_value()),
            "device_display_name": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_o_s_type": lambda n : setattr(self, 'device_o_s_type', n.get_str_value()),
            "device_o_s_version": lambda n : setattr(self, 'device_o_s_version', n.get_str_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "recorded_date_time": lambda n : setattr(self, 'recorded_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(agreement_acceptance_state.AgreementAcceptanceState)),
            "user_display_name": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "user_email": lambda n : setattr(self, 'user_email', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def recorded_date_time(self,) -> Optional[datetime]:
        """
        Gets the recordedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._recorded_date_time
    
    @recorded_date_time.setter
    def recorded_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the recordedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the recordedDateTime property.
        """
        self._recorded_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("agreementFileId", self.agreement_file_id)
        writer.write_str_value("agreementId", self.agreement_id)
        writer.write_str_value("deviceDisplayName", self.device_display_name)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceOSType", self.device_o_s_type)
        writer.write_str_value("deviceOSVersion", self.device_o_s_version)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("recordedDateTime", self.recorded_date_time)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userEmail", self.user_email)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def state(self,) -> Optional[agreement_acceptance_state.AgreementAcceptanceState]:
        """
        Gets the state property value. The state of the agreement acceptance. Possible values are: accepted, declined. Supports $filter (eq).
        Returns: Optional[agreement_acceptance_state.AgreementAcceptanceState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[agreement_acceptance_state.AgreementAcceptanceState] = None) -> None:
        """
        Sets the state property value. The state of the agreement acceptance. Possible values are: accepted, declined. Supports $filter (eq).
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. Display name of the user when the acceptance was recorded.
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. Display name of the user when the acceptance was recorded.
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
    @property
    def user_email(self,) -> Optional[str]:
        """
        Gets the userEmail property value. Email of the user when the acceptance was recorded.
        Returns: Optional[str]
        """
        return self._user_email
    
    @user_email.setter
    def user_email(self,value: Optional[str] = None) -> None:
        """
        Sets the userEmail property value. Email of the user when the acceptance was recorded.
        Args:
            value: Value to set for the userEmail property.
        """
        self._user_email = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The identifier of the user who accepted the agreement. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The identifier of the user who accepted the agreement. Supports $filter (eq).
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. UPN of the user when the acceptance was recorded.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. UPN of the user when the acceptance was recorded.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

