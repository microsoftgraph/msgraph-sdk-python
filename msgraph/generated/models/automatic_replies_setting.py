from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

automatic_replies_status = lazy_import('msgraph.generated.models.automatic_replies_status')
date_time_time_zone = lazy_import('msgraph.generated.models.date_time_time_zone')
external_audience_scope = lazy_import('msgraph.generated.models.external_audience_scope')

class AutomaticRepliesSetting(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new automaticRepliesSetting and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The set of audience external to the signed-in user's organization who will receive the ExternalReplyMessage, if Status is AlwaysEnabled or Scheduled. The possible values are: none, contactsOnly, all.
        self._external_audience: Optional[external_audience_scope.ExternalAudienceScope] = None
        # The automatic reply to send to the specified external audience, if Status is AlwaysEnabled or Scheduled.
        self._external_reply_message: Optional[str] = None
        # The automatic reply to send to the audience internal to the signed-in user's organization, if Status is AlwaysEnabled or Scheduled.
        self._internal_reply_message: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The date and time that automatic replies are set to end, if Status is set to Scheduled.
        self._scheduled_end_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The date and time that automatic replies are set to begin, if Status is set to Scheduled.
        self._scheduled_start_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # Configurations status for automatic replies. The possible values are: disabled, alwaysEnabled, scheduled.
        self._status: Optional[automatic_replies_status.AutomaticRepliesStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AutomaticRepliesSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AutomaticRepliesSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AutomaticRepliesSetting()
    
    @property
    def external_audience(self,) -> Optional[external_audience_scope.ExternalAudienceScope]:
        """
        Gets the externalAudience property value. The set of audience external to the signed-in user's organization who will receive the ExternalReplyMessage, if Status is AlwaysEnabled or Scheduled. The possible values are: none, contactsOnly, all.
        Returns: Optional[external_audience_scope.ExternalAudienceScope]
        """
        return self._external_audience
    
    @external_audience.setter
    def external_audience(self,value: Optional[external_audience_scope.ExternalAudienceScope] = None) -> None:
        """
        Sets the externalAudience property value. The set of audience external to the signed-in user's organization who will receive the ExternalReplyMessage, if Status is AlwaysEnabled or Scheduled. The possible values are: none, contactsOnly, all.
        Args:
            value: Value to set for the externalAudience property.
        """
        self._external_audience = value
    
    @property
    def external_reply_message(self,) -> Optional[str]:
        """
        Gets the externalReplyMessage property value. The automatic reply to send to the specified external audience, if Status is AlwaysEnabled or Scheduled.
        Returns: Optional[str]
        """
        return self._external_reply_message
    
    @external_reply_message.setter
    def external_reply_message(self,value: Optional[str] = None) -> None:
        """
        Sets the externalReplyMessage property value. The automatic reply to send to the specified external audience, if Status is AlwaysEnabled or Scheduled.
        Args:
            value: Value to set for the externalReplyMessage property.
        """
        self._external_reply_message = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "external_audience": lambda n : setattr(self, 'external_audience', n.get_enum_value(external_audience_scope.ExternalAudienceScope)),
            "external_reply_message": lambda n : setattr(self, 'external_reply_message', n.get_str_value()),
            "internal_reply_message": lambda n : setattr(self, 'internal_reply_message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scheduled_end_date_time": lambda n : setattr(self, 'scheduled_end_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "scheduled_start_date_time": lambda n : setattr(self, 'scheduled_start_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(automatic_replies_status.AutomaticRepliesStatus)),
        }
        return fields
    
    @property
    def internal_reply_message(self,) -> Optional[str]:
        """
        Gets the internalReplyMessage property value. The automatic reply to send to the audience internal to the signed-in user's organization, if Status is AlwaysEnabled or Scheduled.
        Returns: Optional[str]
        """
        return self._internal_reply_message
    
    @internal_reply_message.setter
    def internal_reply_message(self,value: Optional[str] = None) -> None:
        """
        Sets the internalReplyMessage property value. The automatic reply to send to the audience internal to the signed-in user's organization, if Status is AlwaysEnabled or Scheduled.
        Args:
            value: Value to set for the internalReplyMessage property.
        """
        self._internal_reply_message = value
    
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
    
    @property
    def scheduled_end_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the scheduledEndDateTime property value. The date and time that automatic replies are set to end, if Status is set to Scheduled.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._scheduled_end_date_time
    
    @scheduled_end_date_time.setter
    def scheduled_end_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the scheduledEndDateTime property value. The date and time that automatic replies are set to end, if Status is set to Scheduled.
        Args:
            value: Value to set for the scheduledEndDateTime property.
        """
        self._scheduled_end_date_time = value
    
    @property
    def scheduled_start_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the scheduledStartDateTime property value. The date and time that automatic replies are set to begin, if Status is set to Scheduled.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._scheduled_start_date_time
    
    @scheduled_start_date_time.setter
    def scheduled_start_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the scheduledStartDateTime property value. The date and time that automatic replies are set to begin, if Status is set to Scheduled.
        Args:
            value: Value to set for the scheduledStartDateTime property.
        """
        self._scheduled_start_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("externalAudience", self.external_audience)
        writer.write_str_value("externalReplyMessage", self.external_reply_message)
        writer.write_str_value("internalReplyMessage", self.internal_reply_message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("scheduledEndDateTime", self.scheduled_end_date_time)
        writer.write_object_value("scheduledStartDateTime", self.scheduled_start_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[automatic_replies_status.AutomaticRepliesStatus]:
        """
        Gets the status property value. Configurations status for automatic replies. The possible values are: disabled, alwaysEnabled, scheduled.
        Returns: Optional[automatic_replies_status.AutomaticRepliesStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[automatic_replies_status.AutomaticRepliesStatus] = None) -> None:
        """
        Sets the status property value. Configurations status for automatic replies. The possible values are: disabled, alwaysEnabled, scheduled.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

