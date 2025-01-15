from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .add_large_gallery_view_operation import AddLargeGalleryViewOperation
    from .cancel_media_processing_operation import CancelMediaProcessingOperation
    from .entity import Entity
    from .invite_participants_operation import InviteParticipantsOperation
    from .mute_participant_operation import MuteParticipantOperation
    from .operation_status import OperationStatus
    from .play_prompt_operation import PlayPromptOperation
    from .record_operation import RecordOperation
    from .result_info import ResultInfo
    from .send_dtmf_tones_operation import SendDtmfTonesOperation
    from .start_hold_music_operation import StartHoldMusicOperation
    from .stop_hold_music_operation import StopHoldMusicOperation
    from .subscribe_to_tone_operation import SubscribeToToneOperation
    from .unmute_participant_operation import UnmuteParticipantOperation
    from .update_recording_status_operation import UpdateRecordingStatusOperation

from .entity import Entity

@dataclass
class CommsOperation(Entity, Parsable):
    # Unique Client Context string. Max limit is 256 chars.
    client_context: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The result information. Read-only.
    result_info: Optional[ResultInfo] = None
    # The status property
    status: Optional[OperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CommsOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CommsOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addLargeGalleryViewOperation".casefold():
            from .add_large_gallery_view_operation import AddLargeGalleryViewOperation

            return AddLargeGalleryViewOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cancelMediaProcessingOperation".casefold():
            from .cancel_media_processing_operation import CancelMediaProcessingOperation

            return CancelMediaProcessingOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inviteParticipantsOperation".casefold():
            from .invite_participants_operation import InviteParticipantsOperation

            return InviteParticipantsOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.muteParticipantOperation".casefold():
            from .mute_participant_operation import MuteParticipantOperation

            return MuteParticipantOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.playPromptOperation".casefold():
            from .play_prompt_operation import PlayPromptOperation

            return PlayPromptOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recordOperation".casefold():
            from .record_operation import RecordOperation

            return RecordOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sendDtmfTonesOperation".casefold():
            from .send_dtmf_tones_operation import SendDtmfTonesOperation

            return SendDtmfTonesOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.startHoldMusicOperation".casefold():
            from .start_hold_music_operation import StartHoldMusicOperation

            return StartHoldMusicOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.stopHoldMusicOperation".casefold():
            from .stop_hold_music_operation import StopHoldMusicOperation

            return StopHoldMusicOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subscribeToToneOperation".casefold():
            from .subscribe_to_tone_operation import SubscribeToToneOperation

            return SubscribeToToneOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unmuteParticipantOperation".casefold():
            from .unmute_participant_operation import UnmuteParticipantOperation

            return UnmuteParticipantOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.updateRecordingStatusOperation".casefold():
            from .update_recording_status_operation import UpdateRecordingStatusOperation

            return UpdateRecordingStatusOperation()
        return CommsOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .add_large_gallery_view_operation import AddLargeGalleryViewOperation
        from .cancel_media_processing_operation import CancelMediaProcessingOperation
        from .entity import Entity
        from .invite_participants_operation import InviteParticipantsOperation
        from .mute_participant_operation import MuteParticipantOperation
        from .operation_status import OperationStatus
        from .play_prompt_operation import PlayPromptOperation
        from .record_operation import RecordOperation
        from .result_info import ResultInfo
        from .send_dtmf_tones_operation import SendDtmfTonesOperation
        from .start_hold_music_operation import StartHoldMusicOperation
        from .stop_hold_music_operation import StopHoldMusicOperation
        from .subscribe_to_tone_operation import SubscribeToToneOperation
        from .unmute_participant_operation import UnmuteParticipantOperation
        from .update_recording_status_operation import UpdateRecordingStatusOperation

        from .add_large_gallery_view_operation import AddLargeGalleryViewOperation
        from .cancel_media_processing_operation import CancelMediaProcessingOperation
        from .entity import Entity
        from .invite_participants_operation import InviteParticipantsOperation
        from .mute_participant_operation import MuteParticipantOperation
        from .operation_status import OperationStatus
        from .play_prompt_operation import PlayPromptOperation
        from .record_operation import RecordOperation
        from .result_info import ResultInfo
        from .send_dtmf_tones_operation import SendDtmfTonesOperation
        from .start_hold_music_operation import StartHoldMusicOperation
        from .stop_hold_music_operation import StopHoldMusicOperation
        from .subscribe_to_tone_operation import SubscribeToToneOperation
        from .unmute_participant_operation import UnmuteParticipantOperation
        from .update_recording_status_operation import UpdateRecordingStatusOperation

        fields: dict[str, Callable[[Any], None]] = {
            "clientContext": lambda n : setattr(self, 'client_context', n.get_str_value()),
            "resultInfo": lambda n : setattr(self, 'result_info', n.get_object_value(ResultInfo)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(OperationStatus)),
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
        writer.write_str_value("clientContext", self.client_context)
        writer.write_object_value("resultInfo", self.result_info)
        writer.write_enum_value("status", self.status)
    

