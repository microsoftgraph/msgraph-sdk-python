from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .audit_log_query_status import AuditLogQueryStatus
    from .audit_log_record import AuditLogRecord
    from .audit_log_record_type import AuditLogRecordType

from ..entity import Entity

@dataclass
class AuditLogQuery(Entity, Parsable):
    """
    Represents a query against the unified audit log.
    """
    # The administrative units tagged to an audit log record.
    administrative_unit_id_filters: Optional[list[str]] = None
    # The display name of the saved audit log query.
    display_name: Optional[str] = None
    # The end date of the date range in the query.
    filter_end_date_time: Optional[datetime.datetime] = None
    # The start date of the date range in the query.
    filter_start_date_time: Optional[datetime.datetime] = None
    # The IP address of the device that was used when the activity was logged.
    ip_address_filters: Optional[list[str]] = None
    # Free text field to search non-indexed properties of the audit log.
    keyword_filter: Optional[str] = None
    # For SharePoint and OneDrive for Business activity, the full path name of the file or folder accessed by the user. For Exchange admin audit logging, the name of the object that was modified by the cmdlet.
    object_id_filters: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the user or admin activity. For a description of the most common operations/activities, see Search the audit log in the Office 365 Protection Center.
    operation_filters: Optional[list[str]] = None
    # The type of operation indicated by the record. For the list of member values, see auditLogRecordType.
    record_type_filters: Optional[list[AuditLogRecordType]] = None
    # An individual audit log record.
    records: Optional[list[AuditLogRecord]] = None
    # The serviceFilters property
    service_filters: Optional[list[str]] = None
    # Describes the current status of the query. The possible values are: notStarted, running, succeeded, failed, cancelled, unknownFutureValue.
    status: Optional[AuditLogQueryStatus] = None
    # The UPN (user principal name) of the user who performed the action (specified in the operation property) that resulted in the record being logged; for example, myname@mydomain_name.
    user_principal_name_filters: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditLogQuery:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditLogQuery
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuditLogQuery()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .audit_log_query_status import AuditLogQueryStatus
        from .audit_log_record import AuditLogRecord
        from .audit_log_record_type import AuditLogRecordType

        from ..entity import Entity
        from .audit_log_query_status import AuditLogQueryStatus
        from .audit_log_record import AuditLogRecord
        from .audit_log_record_type import AuditLogRecordType

        fields: dict[str, Callable[[Any], None]] = {
            "administrativeUnitIdFilters": lambda n : setattr(self, 'administrative_unit_id_filters', n.get_collection_of_primitive_values(str)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "filterEndDateTime": lambda n : setattr(self, 'filter_end_date_time', n.get_datetime_value()),
            "filterStartDateTime": lambda n : setattr(self, 'filter_start_date_time', n.get_datetime_value()),
            "ipAddressFilters": lambda n : setattr(self, 'ip_address_filters', n.get_collection_of_primitive_values(str)),
            "keywordFilter": lambda n : setattr(self, 'keyword_filter', n.get_str_value()),
            "objectIdFilters": lambda n : setattr(self, 'object_id_filters', n.get_collection_of_primitive_values(str)),
            "operationFilters": lambda n : setattr(self, 'operation_filters', n.get_collection_of_primitive_values(str)),
            "recordTypeFilters": lambda n : setattr(self, 'record_type_filters', n.get_collection_of_enum_values(AuditLogRecordType)),
            "records": lambda n : setattr(self, 'records', n.get_collection_of_object_values(AuditLogRecord)),
            "serviceFilters": lambda n : setattr(self, 'service_filters', n.get_collection_of_primitive_values(str)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AuditLogQueryStatus)),
            "userPrincipalNameFilters": lambda n : setattr(self, 'user_principal_name_filters', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("administrativeUnitIdFilters", self.administrative_unit_id_filters)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("filterEndDateTime", self.filter_end_date_time)
        writer.write_datetime_value("filterStartDateTime", self.filter_start_date_time)
        writer.write_collection_of_primitive_values("ipAddressFilters", self.ip_address_filters)
        writer.write_str_value("keywordFilter", self.keyword_filter)
        writer.write_collection_of_primitive_values("objectIdFilters", self.object_id_filters)
        writer.write_collection_of_primitive_values("operationFilters", self.operation_filters)
        writer.write_collection_of_enum_values("recordTypeFilters", self.record_type_filters)
        writer.write_collection_of_object_values("records", self.records)
        writer.write_collection_of_primitive_values("serviceFilters", self.service_filters)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_primitive_values("userPrincipalNameFilters", self.user_principal_name_filters)
    

