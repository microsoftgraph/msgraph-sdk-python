from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BackupCountStatistics(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The date and time when this metric was calculated. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_computed_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The count of artifacts in offboardRequested state. This metric captures artifacts in protection‑unit–level offboarding and artifacts offboarded due to an unhealthy billing profile.
    offboard_requested: Optional[int] = None
    # The count of artifacts in protected state.
    protected_completed: Optional[int] = None
    # The count of artifacts whose protection was attempted but failed. These artifacts typically have unprotected as their status.
    protected_failed: Optional[int] = None
    # The count of artifacts whose protection attempt is currently in progress. This metric applies to artifacts for which the process to start or resume taking backups is still required.
    protected_in_progress: Optional[int] = None
    # The count of artifacts not associated with any policy. This property is always null for a policy-level report. Nullable.
    removed: Optional[int] = None
    # The count of artifacts in the specified entity. The currently supported entity is a backup policy.
    total: Optional[int] = None
    # The count of artifacts that are no longer actively protected. These artifacts have historical restore points, but no new backups are taken.
    unprotected_completed: Optional[int] = None
    # The count of artifacts for which unprotection was attempted but didn't complete. These artifacts are typically in the protected state.
    unprotected_failed: Optional[int] = None
    # The count of artifacts for which unprotection is currently in progress.
    unprotected_in_progress: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BackupCountStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BackupCountStatistics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BackupCountStatistics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "lastComputedDateTime": lambda n : setattr(self, 'last_computed_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offboardRequested": lambda n : setattr(self, 'offboard_requested', n.get_int_value()),
            "protectedCompleted": lambda n : setattr(self, 'protected_completed', n.get_int_value()),
            "protectedFailed": lambda n : setattr(self, 'protected_failed', n.get_int_value()),
            "protectedInProgress": lambda n : setattr(self, 'protected_in_progress', n.get_int_value()),
            "removed": lambda n : setattr(self, 'removed', n.get_int_value()),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
            "unprotectedCompleted": lambda n : setattr(self, 'unprotected_completed', n.get_int_value()),
            "unprotectedFailed": lambda n : setattr(self, 'unprotected_failed', n.get_int_value()),
            "unprotectedInProgress": lambda n : setattr(self, 'unprotected_in_progress', n.get_int_value()),
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
        writer.write_datetime_value("lastComputedDateTime", self.last_computed_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("offboardRequested", self.offboard_requested)
        writer.write_int_value("protectedCompleted", self.protected_completed)
        writer.write_int_value("protectedFailed", self.protected_failed)
        writer.write_int_value("protectedInProgress", self.protected_in_progress)
        writer.write_int_value("removed", self.removed)
        writer.write_int_value("total", self.total)
        writer.write_int_value("unprotectedCompleted", self.unprotected_completed)
        writer.write_int_value("unprotectedFailed", self.unprotected_failed)
        writer.write_int_value("unprotectedInProgress", self.unprotected_in_progress)
        writer.write_additional_data_value(self.additional_data)
    

