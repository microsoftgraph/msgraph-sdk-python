from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

provisioning_error_info = lazy_import('msgraph.generated.models.provisioning_error_info')
provisioning_result = lazy_import('msgraph.generated.models.provisioning_result')

class ProvisioningStatusInfo(AdditionalDataHolder, Parsable):
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
        Instantiates a new provisioningStatusInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The errorInformation property
        self._error_information: Optional[provisioning_error_info.ProvisioningErrorInfo] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Possible values are: success, warning, failure, skipped, unknownFutureValue.
        self._status: Optional[provisioning_result.ProvisioningResult] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProvisioningStatusInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningStatusInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProvisioningStatusInfo()
    
    @property
    def error_information(self,) -> Optional[provisioning_error_info.ProvisioningErrorInfo]:
        """
        Gets the errorInformation property value. The errorInformation property
        Returns: Optional[provisioning_error_info.ProvisioningErrorInfo]
        """
        return self._error_information
    
    @error_information.setter
    def error_information(self,value: Optional[provisioning_error_info.ProvisioningErrorInfo] = None) -> None:
        """
        Sets the errorInformation property value. The errorInformation property
        Args:
            value: Value to set for the errorInformation property.
        """
        self._error_information = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "error_information": lambda n : setattr(self, 'error_information', n.get_object_value(provisioning_error_info.ProvisioningErrorInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(provisioning_result.ProvisioningResult)),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("errorInformation", self.error_information)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[provisioning_result.ProvisioningResult]:
        """
        Gets the status property value. Possible values are: success, warning, failure, skipped, unknownFutureValue.
        Returns: Optional[provisioning_result.ProvisioningResult]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[provisioning_result.ProvisioningResult] = None) -> None:
        """
        Sets the status property value. Possible values are: success, warning, failure, skipped, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

