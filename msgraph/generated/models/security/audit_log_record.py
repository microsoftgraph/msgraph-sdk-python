from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .audit_data import AuditData
    from .audit_log_record_type import AuditLogRecordType
    from .audit_log_user_type import AuditLogUserType

from ..entity import Entity

@dataclass
class AuditLogRecord(Entity, Parsable):
    """
    Represents an individual audit log record.
    """
    # The collection of administrative units associated with the record.
    administrative_units: Optional[list[str]] = None
    # The audit data associated with the record.
    audit_data: Optional[AuditData] = None
    # The type of the audit log record.
    audit_log_record_type: Optional[AuditLogRecordType] = None
    # The IP address of the client that performed the activity.
    client_ip: Optional[str] = None
    # The date and time when the activity was performed.
    created_date_time: Optional[datetime.datetime] = None
    # The identifier of the object that was affected by the activity.
    object_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the activity that was performed.
    operation: Optional[str] = None
    # The GUID of the organization's Microsoft 365 tenant.
    organization_id: Optional[str] = None
    # The Microsoft 365 service where the activity occurred.
    service: Optional[str] = None
    # The identifier of the user, system account, service, or application that performed the activity.
    user_id: Optional[str] = None
    # The user principal name of the user who performed the activity.
    user_principal_name: Optional[str] = None
    # The type of user who performed the activity. Possible values are: regular, reserved, admin, dcAdmin, system, application, servicePrincipal, customPolicy, systemPolicy, partnerTechnician, guest, unknownFutureValue.
    user_type: Optional[AuditLogUserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditLogRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditLogRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuditLogRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .audit_data import AuditData
        from .audit_log_record_type import AuditLogRecordType
        from .audit_log_user_type import AuditLogUserType

        from ..entity import Entity
        from .audit_data import AuditData
        from .audit_log_record_type import AuditLogRecordType
        from .audit_log_user_type import AuditLogUserType

        fields: dict[str, Callable[[Any], None]] = {
            "administrativeUnits": lambda n : setattr(self, 'administrative_units', n.get_collection_of_primitive_values(str)),
            "auditData": lambda n : setattr(self, 'audit_data', n.get_object_value(AuditData)),
            "auditLogRecordType": lambda n : setattr(self, 'audit_log_record_type', n.get_enum_value(AuditLogRecordType)),
            "clientIp": lambda n : setattr(self, 'client_ip', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "objectId": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "operation": lambda n : setattr(self, 'operation', n.get_str_value()),
            "organizationId": lambda n : setattr(self, 'organization_id', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(AuditLogUserType)),
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
        writer.write_collection_of_primitive_values("administrativeUnits", self.administrative_units)
        writer.write_object_value("auditData", self.audit_data)
        writer.write_enum_value("auditLogRecordType", self.audit_log_record_type)
        writer.write_str_value("clientIp", self.client_ip)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("objectId", self.object_id)
        writer.write_str_value("operation", self.operation)
        writer.write_str_value("organizationId", self.organization_id)
        writer.write_str_value("service", self.service)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_enum_value("userType", self.user_type)
    

