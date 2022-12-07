from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_history_status = lazy_import('msgraph.generated.models.access_review_history_status')
entity = lazy_import('msgraph.generated.models.entity')

class AccessReviewHistoryInstance(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new accessReviewHistoryInstance and sets the default values.
        """
        super().__init__()
        # Uri which can be used to retrieve review history data. This URI will be active for 24 hours after being generated. Required.
        self._download_uri: Optional[str] = None
        # Timestamp when this instance and associated data expires and the history is deleted. Required.
        self._expiration_date_time: Optional[datetime] = None
        # Timestamp when all of the available data for this instance was collected. This will be set after this instance's status is set to done. Required.
        self._fulfilled_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Timestamp, reviews ending on or before this date will be included in the fetched history data.
        self._review_history_period_end_date_time: Optional[datetime] = None
        # Timestamp, reviews starting on or after this date will be included in the fetched history data.
        self._review_history_period_start_date_time: Optional[datetime] = None
        # Timestamp when the instance's history data is scheduled to be generated.
        self._run_date_time: Optional[datetime] = None
        # Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue. Once the status has been marked as done, a link can be generated to retrieve the instance's data by calling generateDownloadUri method.
        self._status: Optional[access_review_history_status.AccessReviewHistoryStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewHistoryInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewHistoryInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewHistoryInstance()
    
    @property
    def download_uri(self,) -> Optional[str]:
        """
        Gets the downloadUri property value. Uri which can be used to retrieve review history data. This URI will be active for 24 hours after being generated. Required.
        Returns: Optional[str]
        """
        return self._download_uri
    
    @download_uri.setter
    def download_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the downloadUri property value. Uri which can be used to retrieve review history data. This URI will be active for 24 hours after being generated. Required.
        Args:
            value: Value to set for the downloadUri property.
        """
        self._download_uri = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. Timestamp when this instance and associated data expires and the history is deleted. Required.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. Timestamp when this instance and associated data expires and the history is deleted. Required.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    @property
    def fulfilled_date_time(self,) -> Optional[datetime]:
        """
        Gets the fulfilledDateTime property value. Timestamp when all of the available data for this instance was collected. This will be set after this instance's status is set to done. Required.
        Returns: Optional[datetime]
        """
        return self._fulfilled_date_time
    
    @fulfilled_date_time.setter
    def fulfilled_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the fulfilledDateTime property value. Timestamp when all of the available data for this instance was collected. This will be set after this instance's status is set to done. Required.
        Args:
            value: Value to set for the fulfilledDateTime property.
        """
        self._fulfilled_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "download_uri": lambda n : setattr(self, 'download_uri', n.get_str_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "fulfilled_date_time": lambda n : setattr(self, 'fulfilled_date_time', n.get_datetime_value()),
            "review_history_period_end_date_time": lambda n : setattr(self, 'review_history_period_end_date_time', n.get_datetime_value()),
            "review_history_period_start_date_time": lambda n : setattr(self, 'review_history_period_start_date_time', n.get_datetime_value()),
            "run_date_time": lambda n : setattr(self, 'run_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(access_review_history_status.AccessReviewHistoryStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def review_history_period_end_date_time(self,) -> Optional[datetime]:
        """
        Gets the reviewHistoryPeriodEndDateTime property value. Timestamp, reviews ending on or before this date will be included in the fetched history data.
        Returns: Optional[datetime]
        """
        return self._review_history_period_end_date_time
    
    @review_history_period_end_date_time.setter
    def review_history_period_end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the reviewHistoryPeriodEndDateTime property value. Timestamp, reviews ending on or before this date will be included in the fetched history data.
        Args:
            value: Value to set for the reviewHistoryPeriodEndDateTime property.
        """
        self._review_history_period_end_date_time = value
    
    @property
    def review_history_period_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the reviewHistoryPeriodStartDateTime property value. Timestamp, reviews starting on or after this date will be included in the fetched history data.
        Returns: Optional[datetime]
        """
        return self._review_history_period_start_date_time
    
    @review_history_period_start_date_time.setter
    def review_history_period_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the reviewHistoryPeriodStartDateTime property value. Timestamp, reviews starting on or after this date will be included in the fetched history data.
        Args:
            value: Value to set for the reviewHistoryPeriodStartDateTime property.
        """
        self._review_history_period_start_date_time = value
    
    @property
    def run_date_time(self,) -> Optional[datetime]:
        """
        Gets the runDateTime property value. Timestamp when the instance's history data is scheduled to be generated.
        Returns: Optional[datetime]
        """
        return self._run_date_time
    
    @run_date_time.setter
    def run_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the runDateTime property value. Timestamp when the instance's history data is scheduled to be generated.
        Args:
            value: Value to set for the runDateTime property.
        """
        self._run_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("downloadUri", self.download_uri)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("fulfilledDateTime", self.fulfilled_date_time)
        writer.write_datetime_value("reviewHistoryPeriodEndDateTime", self.review_history_period_end_date_time)
        writer.write_datetime_value("reviewHistoryPeriodStartDateTime", self.review_history_period_start_date_time)
        writer.write_datetime_value("runDateTime", self.run_date_time)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[access_review_history_status.AccessReviewHistoryStatus]:
        """
        Gets the status property value. Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue. Once the status has been marked as done, a link can be generated to retrieve the instance's data by calling generateDownloadUri method.
        Returns: Optional[access_review_history_status.AccessReviewHistoryStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[access_review_history_status.AccessReviewHistoryStatus] = None) -> None:
        """
        Sets the status property value. Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue. Once the status has been marked as done, a link can be generated to retrieve the instance's data by calling generateDownloadUri method.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

