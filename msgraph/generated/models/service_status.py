from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .backup_service_consumer import BackupServiceConsumer
    from .backup_service_status import BackupServiceStatus
    from .disable_reason import DisableReason
    from .identity_set import IdentitySet

@dataclass
class ServiceStatus(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The type of consumer. The possible values are: unknown, firstparty, thirdparty, unknownFutureValue.
    backup_service_consumer: Optional[BackupServiceConsumer] = None
    # The reason the service is disabled. The possible values are: none, controllerServiceAppDeleted, invalidBillingProfile, userRequested, unknownFutureValue.
    disable_reason: Optional[DisableReason] = None
    # The expiration time of the grace period.
    grace_period_date_time: Optional[datetime.datetime] = None
    # Identity of the person who last modified the entity.
    last_modified_by: Optional[IdentitySet] = None
    # Timestamp of the last modification of the entity.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The expiration time of the restoration allowed period.
    restore_allowed_till_date_time: Optional[datetime.datetime] = None
    # Status of the service. This value indicates what capabilities can be used. The possible values are: disabled, enabled, protectionChangeLocked, restoreLocked, unknownFutureValue.
    status: Optional[BackupServiceStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .backup_service_consumer import BackupServiceConsumer
        from .backup_service_status import BackupServiceStatus
        from .disable_reason import DisableReason
        from .identity_set import IdentitySet

        from .backup_service_consumer import BackupServiceConsumer
        from .backup_service_status import BackupServiceStatus
        from .disable_reason import DisableReason
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "backupServiceConsumer": lambda n : setattr(self, 'backup_service_consumer', n.get_enum_value(BackupServiceConsumer)),
            "disableReason": lambda n : setattr(self, 'disable_reason', n.get_enum_value(DisableReason)),
            "gracePeriodDateTime": lambda n : setattr(self, 'grace_period_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restoreAllowedTillDateTime": lambda n : setattr(self, 'restore_allowed_till_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(BackupServiceStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("backupServiceConsumer", self.backup_service_consumer)
        writer.write_enum_value("disableReason", self.disable_reason)
        writer.write_datetime_value("gracePeriodDateTime", self.grace_period_date_time)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("restoreAllowedTillDateTime", self.restore_allowed_till_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

