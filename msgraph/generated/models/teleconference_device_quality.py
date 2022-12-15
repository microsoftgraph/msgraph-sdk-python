from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teleconference_device_media_quality = lazy_import('msgraph.generated.models.teleconference_device_media_quality')

class TeleconferenceDeviceQuality(AdditionalDataHolder, Parsable):
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
    def call_chain_id(self,) -> Optional[Guid]:
        """
        Gets the callChainId property value. A unique identifier for all  the participant calls in a conference or a unique identifier for two participant calls in P2P call. This needs to be copied over from Microsoft.Graph.Call.CallChainId.
        Returns: Optional[Guid]
        """
        return self._call_chain_id
    
    @call_chain_id.setter
    def call_chain_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the callChainId property value. A unique identifier for all  the participant calls in a conference or a unique identifier for two participant calls in P2P call. This needs to be copied over from Microsoft.Graph.Call.CallChainId.
        Args:
            value: Value to set for the callChainId property.
        """
        self._call_chain_id = value
    
    @property
    def cloud_service_deployment_environment(self,) -> Optional[str]:
        """
        Gets the cloudServiceDeploymentEnvironment property value. A geo-region where the service is deployed, such as ProdNoam.
        Returns: Optional[str]
        """
        return self._cloud_service_deployment_environment
    
    @cloud_service_deployment_environment.setter
    def cloud_service_deployment_environment(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudServiceDeploymentEnvironment property value. A geo-region where the service is deployed, such as ProdNoam.
        Args:
            value: Value to set for the cloudServiceDeploymentEnvironment property.
        """
        self._cloud_service_deployment_environment = value
    
    @property
    def cloud_service_deployment_id(self,) -> Optional[str]:
        """
        Gets the cloudServiceDeploymentId property value. A unique deployment identifier assigned by Azure.
        Returns: Optional[str]
        """
        return self._cloud_service_deployment_id
    
    @cloud_service_deployment_id.setter
    def cloud_service_deployment_id(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudServiceDeploymentId property value. A unique deployment identifier assigned by Azure.
        Args:
            value: Value to set for the cloudServiceDeploymentId property.
        """
        self._cloud_service_deployment_id = value
    
    @property
    def cloud_service_instance_name(self,) -> Optional[str]:
        """
        Gets the cloudServiceInstanceName property value. The Azure deployed cloud service instance name, such as FrontEnd_IN_3.
        Returns: Optional[str]
        """
        return self._cloud_service_instance_name
    
    @cloud_service_instance_name.setter
    def cloud_service_instance_name(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudServiceInstanceName property value. The Azure deployed cloud service instance name, such as FrontEnd_IN_3.
        Args:
            value: Value to set for the cloudServiceInstanceName property.
        """
        self._cloud_service_instance_name = value
    
    @property
    def cloud_service_name(self,) -> Optional[str]:
        """
        Gets the cloudServiceName property value. The Azure deployed cloud service name, such as contoso.cloudapp.net.
        Returns: Optional[str]
        """
        return self._cloud_service_name
    
    @cloud_service_name.setter
    def cloud_service_name(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudServiceName property value. The Azure deployed cloud service name, such as contoso.cloudapp.net.
        Args:
            value: Value to set for the cloudServiceName property.
        """
        self._cloud_service_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teleconferenceDeviceQuality and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A unique identifier for all  the participant calls in a conference or a unique identifier for two participant calls in P2P call. This needs to be copied over from Microsoft.Graph.Call.CallChainId.
        self._call_chain_id: Optional[Guid] = None
        # A geo-region where the service is deployed, such as ProdNoam.
        self._cloud_service_deployment_environment: Optional[str] = None
        # A unique deployment identifier assigned by Azure.
        self._cloud_service_deployment_id: Optional[str] = None
        # The Azure deployed cloud service instance name, such as FrontEnd_IN_3.
        self._cloud_service_instance_name: Optional[str] = None
        # The Azure deployed cloud service name, such as contoso.cloudapp.net.
        self._cloud_service_name: Optional[str] = None
        # Any additional description, such as VTC Bldg 30/21.
        self._device_description: Optional[str] = None
        # The user media agent name, such as Cisco SX80.
        self._device_name: Optional[str] = None
        # A unique identifier for a specific media leg of a participant in a conference.  One participant can have multiple media leg identifiers if retargeting happens. CVI partner assigns this value.
        self._media_leg_id: Optional[Guid] = None
        # The list of media qualities in a media session (call), such as audio quality, video quality, and/or screen sharing quality.
        self._media_quality_list: Optional[List[teleconference_device_media_quality.TeleconferenceDeviceMediaQuality]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A unique identifier for a specific participant in a conference. The CVI partner needs to copy over Call.MyParticipantId to this property.
        self._participant_id: Optional[Guid] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeleconferenceDeviceQuality:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeleconferenceDeviceQuality
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeleconferenceDeviceQuality()
    
    @property
    def device_description(self,) -> Optional[str]:
        """
        Gets the deviceDescription property value. Any additional description, such as VTC Bldg 30/21.
        Returns: Optional[str]
        """
        return self._device_description
    
    @device_description.setter
    def device_description(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceDescription property value. Any additional description, such as VTC Bldg 30/21.
        Args:
            value: Value to set for the deviceDescription property.
        """
        self._device_description = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The user media agent name, such as Cisco SX80.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The user media agent name, such as Cisco SX80.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "call_chain_id": lambda n : setattr(self, 'call_chain_id', n.get_object_value(Guid)),
            "cloud_service_deployment_environment": lambda n : setattr(self, 'cloud_service_deployment_environment', n.get_str_value()),
            "cloud_service_deployment_id": lambda n : setattr(self, 'cloud_service_deployment_id', n.get_str_value()),
            "cloud_service_instance_name": lambda n : setattr(self, 'cloud_service_instance_name', n.get_str_value()),
            "cloud_service_name": lambda n : setattr(self, 'cloud_service_name', n.get_str_value()),
            "device_description": lambda n : setattr(self, 'device_description', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "media_leg_id": lambda n : setattr(self, 'media_leg_id', n.get_object_value(Guid)),
            "media_quality_list": lambda n : setattr(self, 'media_quality_list', n.get_collection_of_object_values(teleconference_device_media_quality.TeleconferenceDeviceMediaQuality)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "participant_id": lambda n : setattr(self, 'participant_id', n.get_object_value(Guid)),
        }
        return fields
    
    @property
    def media_leg_id(self,) -> Optional[Guid]:
        """
        Gets the mediaLegId property value. A unique identifier for a specific media leg of a participant in a conference.  One participant can have multiple media leg identifiers if retargeting happens. CVI partner assigns this value.
        Returns: Optional[Guid]
        """
        return self._media_leg_id
    
    @media_leg_id.setter
    def media_leg_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the mediaLegId property value. A unique identifier for a specific media leg of a participant in a conference.  One participant can have multiple media leg identifiers if retargeting happens. CVI partner assigns this value.
        Args:
            value: Value to set for the mediaLegId property.
        """
        self._media_leg_id = value
    
    @property
    def media_quality_list(self,) -> Optional[List[teleconference_device_media_quality.TeleconferenceDeviceMediaQuality]]:
        """
        Gets the mediaQualityList property value. The list of media qualities in a media session (call), such as audio quality, video quality, and/or screen sharing quality.
        Returns: Optional[List[teleconference_device_media_quality.TeleconferenceDeviceMediaQuality]]
        """
        return self._media_quality_list
    
    @media_quality_list.setter
    def media_quality_list(self,value: Optional[List[teleconference_device_media_quality.TeleconferenceDeviceMediaQuality]] = None) -> None:
        """
        Sets the mediaQualityList property value. The list of media qualities in a media session (call), such as audio quality, video quality, and/or screen sharing quality.
        Args:
            value: Value to set for the mediaQualityList property.
        """
        self._media_quality_list = value
    
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
    def participant_id(self,) -> Optional[Guid]:
        """
        Gets the participantId property value. A unique identifier for a specific participant in a conference. The CVI partner needs to copy over Call.MyParticipantId to this property.
        Returns: Optional[Guid]
        """
        return self._participant_id
    
    @participant_id.setter
    def participant_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the participantId property value. A unique identifier for a specific participant in a conference. The CVI partner needs to copy over Call.MyParticipantId to this property.
        Args:
            value: Value to set for the participantId property.
        """
        self._participant_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("callChainId", self.call_chain_id)
        writer.write_str_value("cloudServiceDeploymentEnvironment", self.cloud_service_deployment_environment)
        writer.write_str_value("cloudServiceDeploymentId", self.cloud_service_deployment_id)
        writer.write_str_value("cloudServiceInstanceName", self.cloud_service_instance_name)
        writer.write_str_value("cloudServiceName", self.cloud_service_name)
        writer.write_str_value("deviceDescription", self.device_description)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_object_value("mediaLegId", self.media_leg_id)
        writer.write_collection_of_object_values("mediaQualityList", self.media_quality_list)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("participantId", self.participant_id)
        writer.write_additional_data_value(self.additional_data)
    

