from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .teleconference_device_media_quality import TeleconferenceDeviceMediaQuality

@dataclass
class TeleconferenceDeviceQuality(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # A unique identifier for all  the participant calls in a conference or a unique identifier for two participant calls in P2P call. This needs to be copied over from Microsoft.Graph.Call.CallChainId.
    call_chain_id: Optional[UUID] = None
    # A geo-region where the service is deployed, such as ProdNoam.
    cloud_service_deployment_environment: Optional[str] = None
    # A unique deployment identifier assigned by Azure.
    cloud_service_deployment_id: Optional[str] = None
    # The Azure deployed cloud service instance name, such as FrontEndIN3.
    cloud_service_instance_name: Optional[str] = None
    # The Azure deployed cloud service name, such as contoso.cloudapp.net.
    cloud_service_name: Optional[str] = None
    # Any additional description, such as VTC Bldg 30/21.
    device_description: Optional[str] = None
    # The user media agent name, such as Cisco SX80.
    device_name: Optional[str] = None
    # A unique identifier for a specific media leg of a participant in a conference.  One participant can have multiple media leg identifiers if retargeting happens. CVI partner assigns this value.
    media_leg_id: Optional[UUID] = None
    # The list of media qualities in a media session (call), such as audio quality, video quality, and/or screen sharing quality.
    media_quality_list: Optional[List[TeleconferenceDeviceMediaQuality]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A unique identifier for a specific participant in a conference. The CVI partner needs to copy over Call.MyParticipantId to this property.
    participant_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeleconferenceDeviceQuality:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeleconferenceDeviceQuality
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeleconferenceDeviceQuality()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teleconference_device_media_quality import TeleconferenceDeviceMediaQuality

        from .teleconference_device_media_quality import TeleconferenceDeviceMediaQuality

        fields: Dict[str, Callable[[Any], None]] = {
            "callChainId": lambda n : setattr(self, 'call_chain_id', n.get_uuid_value()),
            "cloudServiceDeploymentEnvironment": lambda n : setattr(self, 'cloud_service_deployment_environment', n.get_str_value()),
            "cloudServiceDeploymentId": lambda n : setattr(self, 'cloud_service_deployment_id', n.get_str_value()),
            "cloudServiceInstanceName": lambda n : setattr(self, 'cloud_service_instance_name', n.get_str_value()),
            "cloudServiceName": lambda n : setattr(self, 'cloud_service_name', n.get_str_value()),
            "deviceDescription": lambda n : setattr(self, 'device_description', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "mediaLegId": lambda n : setattr(self, 'media_leg_id', n.get_uuid_value()),
            "mediaQualityList": lambda n : setattr(self, 'media_quality_list', n.get_collection_of_object_values(TeleconferenceDeviceMediaQuality)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "participantId": lambda n : setattr(self, 'participant_id', n.get_uuid_value()),
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
        writer.write_uuid_value("callChainId", self.call_chain_id)
        writer.write_str_value("cloudServiceDeploymentEnvironment", self.cloud_service_deployment_environment)
        writer.write_str_value("cloudServiceDeploymentId", self.cloud_service_deployment_id)
        writer.write_str_value("cloudServiceInstanceName", self.cloud_service_instance_name)
        writer.write_str_value("cloudServiceName", self.cloud_service_name)
        writer.write_str_value("deviceDescription", self.device_description)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_uuid_value("mediaLegId", self.media_leg_id)
        writer.write_collection_of_object_values("mediaQualityList", self.media_quality_list)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_uuid_value("participantId", self.participant_id)
        writer.write_additional_data_value(self.additional_data)
    

