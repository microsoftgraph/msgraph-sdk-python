from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ApplePushNotificationCertificate(entity.Entity):
    @property
    def apple_identifier(self,) -> Optional[str]:
        """
        Gets the appleIdentifier property value. Apple Id of the account used to create the MDM push certificate.
        Returns: Optional[str]
        """
        return self._apple_identifier
    
    @apple_identifier.setter
    def apple_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the appleIdentifier property value. Apple Id of the account used to create the MDM push certificate.
        Args:
            value: Value to set for the appleIdentifier property.
        """
        self._apple_identifier = value
    
    @property
    def certificate(self,) -> Optional[str]:
        """
        Gets the certificate property value. Not yet documented
        Returns: Optional[str]
        """
        return self._certificate
    
    @certificate.setter
    def certificate(self,value: Optional[str] = None) -> None:
        """
        Sets the certificate property value. Not yet documented
        Args:
            value: Value to set for the certificate property.
        """
        self._certificate = value
    
    @property
    def certificate_serial_number(self,) -> Optional[str]:
        """
        Gets the certificateSerialNumber property value. Certificate serial number. This property is read-only.
        Returns: Optional[str]
        """
        return self._certificate_serial_number
    
    @certificate_serial_number.setter
    def certificate_serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateSerialNumber property value. Certificate serial number. This property is read-only.
        Args:
            value: Value to set for the certificateSerialNumber property.
        """
        self._certificate_serial_number = value
    
    @property
    def certificate_upload_failure_reason(self,) -> Optional[str]:
        """
        Gets the certificateUploadFailureReason property value. The reason the certificate upload failed.
        Returns: Optional[str]
        """
        return self._certificate_upload_failure_reason
    
    @certificate_upload_failure_reason.setter
    def certificate_upload_failure_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateUploadFailureReason property value. The reason the certificate upload failed.
        Args:
            value: Value to set for the certificateUploadFailureReason property.
        """
        self._certificate_upload_failure_reason = value
    
    @property
    def certificate_upload_status(self,) -> Optional[str]:
        """
        Gets the certificateUploadStatus property value. The certificate upload status.
        Returns: Optional[str]
        """
        return self._certificate_upload_status
    
    @certificate_upload_status.setter
    def certificate_upload_status(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateUploadStatus property value. The certificate upload status.
        Args:
            value: Value to set for the certificateUploadStatus property.
        """
        self._certificate_upload_status = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new applePushNotificationCertificate and sets the default values.
        """
        super().__init__()
        # Apple Id of the account used to create the MDM push certificate.
        self._apple_identifier: Optional[str] = None
        # Not yet documented
        self._certificate: Optional[str] = None
        # Certificate serial number. This property is read-only.
        self._certificate_serial_number: Optional[str] = None
        # The reason the certificate upload failed.
        self._certificate_upload_failure_reason: Optional[str] = None
        # The certificate upload status.
        self._certificate_upload_status: Optional[str] = None
        # The expiration date and time for Apple push notification certificate.
        self._expiration_date_time: Optional[datetime] = None
        # Last modified date and time for Apple push notification certificate.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Topic Id.
        self._topic_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplePushNotificationCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApplePushNotificationCertificate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApplePushNotificationCertificate()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The expiration date and time for Apple push notification certificate.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The expiration date and time for Apple push notification certificate.
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
            "apple_identifier": lambda n : setattr(self, 'apple_identifier', n.get_str_value()),
            "certificate": lambda n : setattr(self, 'certificate', n.get_str_value()),
            "certificate_serial_number": lambda n : setattr(self, 'certificate_serial_number', n.get_str_value()),
            "certificate_upload_failure_reason": lambda n : setattr(self, 'certificate_upload_failure_reason', n.get_str_value()),
            "certificate_upload_status": lambda n : setattr(self, 'certificate_upload_status', n.get_str_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "topic_identifier": lambda n : setattr(self, 'topic_identifier', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Last modified date and time for Apple push notification certificate.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Last modified date and time for Apple push notification certificate.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appleIdentifier", self.apple_identifier)
        writer.write_str_value("certificate", self.certificate)
        writer.write_str_value("certificateUploadFailureReason", self.certificate_upload_failure_reason)
        writer.write_str_value("certificateUploadStatus", self.certificate_upload_status)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("topicIdentifier", self.topic_identifier)
    
    @property
    def topic_identifier(self,) -> Optional[str]:
        """
        Gets the topicIdentifier property value. Topic Id.
        Returns: Optional[str]
        """
        return self._topic_identifier
    
    @topic_identifier.setter
    def topic_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the topicIdentifier property value. Topic Id.
        Args:
            value: Value to set for the topicIdentifier property.
        """
        self._topic_identifier = value
    

