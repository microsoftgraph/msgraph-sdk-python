from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import online_meeting_content_sharing_disabled_reason, online_meeting_video_disabled_reason

class OnlineMeetingRestricted(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new onlineMeetingRestricted and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies the reason shared content from this participant is disabled. Possible values are: watermarkProtection, unknownFutureValue.
        self._content_sharing_disabled: Optional[online_meeting_content_sharing_disabled_reason.OnlineMeetingContentSharingDisabledReason] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies the reason video from this participant is disabled. Possible values are: watermarkProtection, unknownFutureValue.
        self._video_disabled: Optional[online_meeting_video_disabled_reason.OnlineMeetingVideoDisabledReason] = None
    
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
    
    @property
    def content_sharing_disabled(self,) -> Optional[online_meeting_content_sharing_disabled_reason.OnlineMeetingContentSharingDisabledReason]:
        """
        Gets the contentSharingDisabled property value. Specifies the reason shared content from this participant is disabled. Possible values are: watermarkProtection, unknownFutureValue.
        Returns: Optional[online_meeting_content_sharing_disabled_reason.OnlineMeetingContentSharingDisabledReason]
        """
        return self._content_sharing_disabled
    
    @content_sharing_disabled.setter
    def content_sharing_disabled(self,value: Optional[online_meeting_content_sharing_disabled_reason.OnlineMeetingContentSharingDisabledReason] = None) -> None:
        """
        Sets the contentSharingDisabled property value. Specifies the reason shared content from this participant is disabled. Possible values are: watermarkProtection, unknownFutureValue.
        Args:
            value: Value to set for the content_sharing_disabled property.
        """
        self._content_sharing_disabled = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnlineMeetingRestricted:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeetingRestricted
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnlineMeetingRestricted()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import online_meeting_content_sharing_disabled_reason, online_meeting_video_disabled_reason

        fields: Dict[str, Callable[[Any], None]] = {
            "contentSharingDisabled": lambda n : setattr(self, 'content_sharing_disabled', n.get_enum_value(online_meeting_content_sharing_disabled_reason.OnlineMeetingContentSharingDisabledReason)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "videoDisabled": lambda n : setattr(self, 'video_disabled', n.get_enum_value(online_meeting_video_disabled_reason.OnlineMeetingVideoDisabledReason)),
        }
        return fields
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("contentSharingDisabled", self.content_sharing_disabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("videoDisabled", self.video_disabled)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def video_disabled(self,) -> Optional[online_meeting_video_disabled_reason.OnlineMeetingVideoDisabledReason]:
        """
        Gets the videoDisabled property value. Specifies the reason video from this participant is disabled. Possible values are: watermarkProtection, unknownFutureValue.
        Returns: Optional[online_meeting_video_disabled_reason.OnlineMeetingVideoDisabledReason]
        """
        return self._video_disabled
    
    @video_disabled.setter
    def video_disabled(self,value: Optional[online_meeting_video_disabled_reason.OnlineMeetingVideoDisabledReason] = None) -> None:
        """
        Sets the videoDisabled property value. Specifies the reason video from this participant is disabled. Possible values are: watermarkProtection, unknownFutureValue.
        Args:
            value: Value to set for the video_disabled property.
        """
        self._video_disabled = value
    

