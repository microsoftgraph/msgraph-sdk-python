from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .app_log_upload_state import AppLogUploadState
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceLogCollectionResponse(Entity, Parsable):
    """
    Windows Log Collection request entity.
    """
    # The User Principal Name (UPN) of the user that enrolled the device.
    enrolled_by_user: Optional[str] = None
    # The DateTime of the expiration of the logs.
    expiration_date_time_u_t_c: Optional[datetime.datetime] = None
    # The UPN for who initiated the request.
    initiated_by_user_principal_name: Optional[str] = None
    # Indicates Intune device unique identifier.
    managed_device_id: Optional[UUID] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The DateTime the request was received.
    received_date_time_u_t_c: Optional[datetime.datetime] = None
    # The DateTime of the request.
    requested_date_time_u_t_c: Optional[datetime.datetime] = None
    # The size of the logs in KB. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    size_in_k_b: Optional[float] = None
    # AppLogUploadStatus
    status: Optional[AppLogUploadState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceLogCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceLogCollectionResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceLogCollectionResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_log_upload_state import AppLogUploadState
        from .entity import Entity

        from .app_log_upload_state import AppLogUploadState
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "enrolledByUser": lambda n : setattr(self, 'enrolled_by_user', n.get_str_value()),
            "expirationDateTimeUTC": lambda n : setattr(self, 'expiration_date_time_u_t_c', n.get_datetime_value()),
            "initiatedByUserPrincipalName": lambda n : setattr(self, 'initiated_by_user_principal_name', n.get_str_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_uuid_value()),
            "receivedDateTimeUTC": lambda n : setattr(self, 'received_date_time_u_t_c', n.get_datetime_value()),
            "requestedDateTimeUTC": lambda n : setattr(self, 'requested_date_time_u_t_c', n.get_datetime_value()),
            "sizeInKB": lambda n : setattr(self, 'size_in_k_b', n.get_float_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AppLogUploadState)),
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
        writer.write_str_value("enrolledByUser", self.enrolled_by_user)
        writer.write_datetime_value("expirationDateTimeUTC", self.expiration_date_time_u_t_c)
        writer.write_str_value("initiatedByUserPrincipalName", self.initiated_by_user_principal_name)
        writer.write_uuid_value("managedDeviceId", self.managed_device_id)
        writer.write_datetime_value("receivedDateTimeUTC", self.received_date_time_u_t_c)
        writer.write_datetime_value("requestedDateTimeUTC", self.requested_date_time_u_t_c)
        writer.write_float_value("sizeInKB", self.size_in_k_b)
        writer.write_enum_value("status", self.status)
    

