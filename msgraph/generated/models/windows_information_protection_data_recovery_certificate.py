from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class WindowsInformationProtectionDataRecoveryCertificate(AdditionalDataHolder, Parsable):
    """
    Windows Information Protection DataRecoveryCertificate
    """
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
    def certificate(self,) -> Optional[bytes]:
        """
        Gets the certificate property value. Data recovery Certificate
        Returns: Optional[bytes]
        """
        return self._certificate
    
    @certificate.setter
    def certificate(self,value: Optional[bytes] = None) -> None:
        """
        Sets the certificate property value. Data recovery Certificate
        Args:
            value: Value to set for the certificate property.
        """
        self._certificate = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsInformationProtectionDataRecoveryCertificate and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Data recovery Certificate
        self._certificate: Optional[bytes] = None
        # Data recovery Certificate description
        self._description: Optional[str] = None
        # Data recovery Certificate expiration datetime
        self._expiration_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Data recovery Certificate subject name
        self._subject_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtectionDataRecoveryCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionDataRecoveryCertificate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsInformationProtectionDataRecoveryCertificate()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Data recovery Certificate description
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Data recovery Certificate description
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. Data recovery Certificate expiration datetime
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. Data recovery Certificate expiration datetime
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
            "certificate": lambda n : setattr(self, 'certificate', n.get_bytes_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "subject_name": lambda n : setattr(self, 'subject_name', n.get_str_value()),
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
        writer.write_object_value("certificate", self.certificate)
        writer.write_str_value("description", self.description)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("subjectName", self.subject_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def subject_name(self,) -> Optional[str]:
        """
        Gets the subjectName property value. Data recovery Certificate subject name
        Returns: Optional[str]
        """
        return self._subject_name
    
    @subject_name.setter
    def subject_name(self,value: Optional[str] = None) -> None:
        """
        Sets the subjectName property value. Data recovery Certificate subject name
        Args:
            value: Value to set for the subjectName property.
        """
        self._subject_name = value
    

