from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

provisioning_status_error_category = lazy_import('msgraph.generated.models.provisioning_status_error_category')

class ProvisioningErrorInfo(AdditionalDataHolder, Parsable):
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
    
    @property
    def additional_details(self,) -> Optional[str]:
        """
        Gets the additionalDetails property value. Additional details in case of error.
        Returns: Optional[str]
        """
        return self._additional_details
    
    @additional_details.setter
    def additional_details(self,value: Optional[str] = None) -> None:
        """
        Sets the additionalDetails property value. Additional details in case of error.
        Args:
            value: Value to set for the additionalDetails property.
        """
        self._additional_details = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new provisioningErrorInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Additional details in case of error.
        self._additional_details: Optional[str] = None
        # Categorizes the error code. Possible values are failure, nonServiceFailure, success, unknownFutureValue
        self._error_category: Optional[provisioning_status_error_category.ProvisioningStatusErrorCategory] = None
        # Unique error code if any occurred. Learn more
        self._error_code: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Summarizes the status and describes why the status happened.
        self._reason: Optional[str] = None
        # Provides the resolution for the corresponding error.
        self._recommended_action: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProvisioningErrorInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningErrorInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProvisioningErrorInfo()
    
    @property
    def error_category(self,) -> Optional[provisioning_status_error_category.ProvisioningStatusErrorCategory]:
        """
        Gets the errorCategory property value. Categorizes the error code. Possible values are failure, nonServiceFailure, success, unknownFutureValue
        Returns: Optional[provisioning_status_error_category.ProvisioningStatusErrorCategory]
        """
        return self._error_category
    
    @error_category.setter
    def error_category(self,value: Optional[provisioning_status_error_category.ProvisioningStatusErrorCategory] = None) -> None:
        """
        Sets the errorCategory property value. Categorizes the error code. Possible values are failure, nonServiceFailure, success, unknownFutureValue
        Args:
            value: Value to set for the errorCategory property.
        """
        self._error_category = value
    
    @property
    def error_code(self,) -> Optional[str]:
        """
        Gets the errorCode property value. Unique error code if any occurred. Learn more
        Returns: Optional[str]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[str] = None) -> None:
        """
        Sets the errorCode property value. Unique error code if any occurred. Learn more
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "additional_details": lambda n : setattr(self, 'additional_details', n.get_str_value()),
            "error_category": lambda n : setattr(self, 'error_category', n.get_enum_value(provisioning_status_error_category.ProvisioningStatusErrorCategory)),
            "error_code": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "recommended_action": lambda n : setattr(self, 'recommended_action', n.get_str_value()),
        }
        return fields
    
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
    
    @property
    def reason(self,) -> Optional[str]:
        """
        Gets the reason property value. Summarizes the status and describes why the status happened.
        Returns: Optional[str]
        """
        return self._reason
    
    @reason.setter
    def reason(self,value: Optional[str] = None) -> None:
        """
        Sets the reason property value. Summarizes the status and describes why the status happened.
        Args:
            value: Value to set for the reason property.
        """
        self._reason = value
    
    @property
    def recommended_action(self,) -> Optional[str]:
        """
        Gets the recommendedAction property value. Provides the resolution for the corresponding error.
        Returns: Optional[str]
        """
        return self._recommended_action
    
    @recommended_action.setter
    def recommended_action(self,value: Optional[str] = None) -> None:
        """
        Sets the recommendedAction property value. Provides the resolution for the corresponding error.
        Args:
            value: Value to set for the recommendedAction property.
        """
        self._recommended_action = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("additionalDetails", self.additional_details)
        writer.write_enum_value("errorCategory", self.error_category)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("recommendedAction", self.recommended_action)
        writer.write_additional_data_value(self.additional_data)
    

