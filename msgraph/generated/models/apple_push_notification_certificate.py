from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class ApplePushNotificationCertificate(Entity, Parsable):
    """
    Apple push notification certificate.
    """
    # Apple Id of the account used to create the MDM push certificate.
    apple_identifier: Optional[str] = None
    # The certificate property
    certificate: Optional[str] = None
    # Certificate serial number. This property is read-only.
    certificate_serial_number: Optional[str] = None
    # The reason the certificate upload failed.
    certificate_upload_failure_reason: Optional[str] = None
    # The certificate upload status.
    certificate_upload_status: Optional[str] = None
    # The expiration date and time for Apple push notification certificate.
    expiration_date_time: Optional[datetime.datetime] = None
    # Last modified date and time for Apple push notification certificate.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Topic Id.
    topic_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplePushNotificationCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplePushNotificationCertificate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplePushNotificationCertificate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "appleIdentifier": lambda n : setattr(self, 'apple_identifier', n.get_str_value()),
            "certificate": lambda n : setattr(self, 'certificate', n.get_str_value()),
            "certificateSerialNumber": lambda n : setattr(self, 'certificate_serial_number', n.get_str_value()),
            "certificateUploadFailureReason": lambda n : setattr(self, 'certificate_upload_failure_reason', n.get_str_value()),
            "certificateUploadStatus": lambda n : setattr(self, 'certificate_upload_status', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "topicIdentifier": lambda n : setattr(self, 'topic_identifier', n.get_str_value()),
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
        writer.write_str_value("appleIdentifier", self.apple_identifier)
        writer.write_str_value("certificate", self.certificate)
        writer.write_str_value("certificateUploadFailureReason", self.certificate_upload_failure_reason)
        writer.write_str_value("certificateUploadStatus", self.certificate_upload_status)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("topicIdentifier", self.topic_identifier)
    

