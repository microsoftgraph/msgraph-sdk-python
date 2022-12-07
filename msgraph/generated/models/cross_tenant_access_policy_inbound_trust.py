from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class CrossTenantAccessPolicyInboundTrust(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new crossTenantAccessPolicyInboundTrust and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies whether compliant devices from external Azure AD organizations are trusted.
        self._is_compliant_device_accepted: Optional[bool] = None
        # Specifies whether hybrid Azure AD joined devices from external Azure AD organizations are trusted.
        self._is_hybrid_azure_a_d_joined_device_accepted: Optional[bool] = None
        # Specifies whether MFA from external Azure AD organizations is trusted.
        self._is_mfa_accepted: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicyInboundTrust:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyInboundTrust
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CrossTenantAccessPolicyInboundTrust()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_compliant_device_accepted": lambda n : setattr(self, 'is_compliant_device_accepted', n.get_bool_value()),
            "is_hybrid_azure_a_d_joined_device_accepted": lambda n : setattr(self, 'is_hybrid_azure_a_d_joined_device_accepted', n.get_bool_value()),
            "is_mfa_accepted": lambda n : setattr(self, 'is_mfa_accepted', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_compliant_device_accepted(self,) -> Optional[bool]:
        """
        Gets the isCompliantDeviceAccepted property value. Specifies whether compliant devices from external Azure AD organizations are trusted.
        Returns: Optional[bool]
        """
        return self._is_compliant_device_accepted
    
    @is_compliant_device_accepted.setter
    def is_compliant_device_accepted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCompliantDeviceAccepted property value. Specifies whether compliant devices from external Azure AD organizations are trusted.
        Args:
            value: Value to set for the isCompliantDeviceAccepted property.
        """
        self._is_compliant_device_accepted = value
    
    @property
    def is_hybrid_azure_a_d_joined_device_accepted(self,) -> Optional[bool]:
        """
        Gets the isHybridAzureADJoinedDeviceAccepted property value. Specifies whether hybrid Azure AD joined devices from external Azure AD organizations are trusted.
        Returns: Optional[bool]
        """
        return self._is_hybrid_azure_a_d_joined_device_accepted
    
    @is_hybrid_azure_a_d_joined_device_accepted.setter
    def is_hybrid_azure_a_d_joined_device_accepted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isHybridAzureADJoinedDeviceAccepted property value. Specifies whether hybrid Azure AD joined devices from external Azure AD organizations are trusted.
        Args:
            value: Value to set for the isHybridAzureADJoinedDeviceAccepted property.
        """
        self._is_hybrid_azure_a_d_joined_device_accepted = value
    
    @property
    def is_mfa_accepted(self,) -> Optional[bool]:
        """
        Gets the isMfaAccepted property value. Specifies whether MFA from external Azure AD organizations is trusted.
        Returns: Optional[bool]
        """
        return self._is_mfa_accepted
    
    @is_mfa_accepted.setter
    def is_mfa_accepted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMfaAccepted property value. Specifies whether MFA from external Azure AD organizations is trusted.
        Args:
            value: Value to set for the isMfaAccepted property.
        """
        self._is_mfa_accepted = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("isCompliantDeviceAccepted", self.is_compliant_device_accepted)
        writer.write_bool_value("isHybridAzureADJoinedDeviceAccepted", self.is_hybrid_azure_a_d_joined_device_accepted)
        writer.write_bool_value("isMfaAccepted", self.is_mfa_accepted)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

