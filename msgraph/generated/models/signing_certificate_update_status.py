from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class SigningCertificateUpdateStatus(AdditionalDataHolder, Parsable):
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
    def certificate_update_result(self,) -> Optional[str]:
        """
        Gets the certificateUpdateResult property value. Status of the last certificate update. Read-only. For a list of statuses, see certificateUpdateResult status.
        Returns: Optional[str]
        """
        return self._certificate_update_result
    
    @certificate_update_result.setter
    def certificate_update_result(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateUpdateResult property value. Status of the last certificate update. Read-only. For a list of statuses, see certificateUpdateResult status.
        Args:
            value: Value to set for the certificateUpdateResult property.
        """
        self._certificate_update_result = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new signingCertificateUpdateStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Status of the last certificate update. Read-only. For a list of statuses, see certificateUpdateResult status.
        self._certificate_update_result: Optional[str] = None
        # Date and time in ISO 8601 format and in UTC time when the certificate was last updated. Read-only.
        self._last_run_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SigningCertificateUpdateStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SigningCertificateUpdateStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SigningCertificateUpdateStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certificate_update_result": lambda n : setattr(self, 'certificate_update_result', n.get_str_value()),
            "last_run_date_time": lambda n : setattr(self, 'last_run_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def last_run_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastRunDateTime property value. Date and time in ISO 8601 format and in UTC time when the certificate was last updated. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_run_date_time
    
    @last_run_date_time.setter
    def last_run_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRunDateTime property value. Date and time in ISO 8601 format and in UTC time when the certificate was last updated. Read-only.
        Args:
            value: Value to set for the lastRunDateTime property.
        """
        self._last_run_date_time = value
    
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
        writer.write_str_value("certificateUpdateResult", self.certificate_update_result)
        writer.write_datetime_value("lastRunDateTime", self.last_run_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

