from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_history_status, entity

from . import entity

@dataclass
class AccessReviewHistoryInstance(entity.Entity):
    # Uri which can be used to retrieve review history data. This URI will be active for 24 hours after being generated. Required.
    download_uri: Optional[str] = None
    # Timestamp when this instance and associated data expires and the history is deleted. Required.
    expiration_date_time: Optional[datetime] = None
    # Timestamp when all of the available data for this instance was collected. This will be set after this instance's status is set to done. Required.
    fulfilled_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Timestamp, reviews ending on or before this date will be included in the fetched history data.
    review_history_period_end_date_time: Optional[datetime] = None
    # Timestamp, reviews starting on or after this date will be included in the fetched history data.
    review_history_period_start_date_time: Optional[datetime] = None
    # Timestamp when the instance's history data is scheduled to be generated.
    run_date_time: Optional[datetime] = None
    # Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue. Once the status has been marked as done, a link can be generated to retrieve the instance's data by calling generateDownloadUri method.
    status: Optional[access_review_history_status.AccessReviewHistoryStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewHistoryInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewHistoryInstance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewHistoryInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_history_status, entity

        from . import access_review_history_status, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "downloadUri": lambda n : setattr(self, 'download_uri', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "fulfilledDateTime": lambda n : setattr(self, 'fulfilled_date_time', n.get_datetime_value()),
            "reviewHistoryPeriodEndDateTime": lambda n : setattr(self, 'review_history_period_end_date_time', n.get_datetime_value()),
            "reviewHistoryPeriodStartDateTime": lambda n : setattr(self, 'review_history_period_start_date_time', n.get_datetime_value()),
            "runDateTime": lambda n : setattr(self, 'run_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(access_review_history_status.AccessReviewHistoryStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("downloadUri", self.download_uri)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("fulfilledDateTime", self.fulfilled_date_time)
        writer.write_datetime_value("reviewHistoryPeriodEndDateTime", self.review_history_period_end_date_time)
        writer.write_datetime_value("reviewHistoryPeriodStartDateTime", self.review_history_period_start_date_time)
        writer.write_datetime_value("runDateTime", self.run_date_time)
        writer.write_enum_value("status", self.status)
    

