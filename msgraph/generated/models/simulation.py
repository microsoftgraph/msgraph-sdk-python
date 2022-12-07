from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

email_identity = lazy_import('msgraph.generated.models.email_identity')
entity = lazy_import('msgraph.generated.models.entity')
payload_delivery_platform = lazy_import('msgraph.generated.models.payload_delivery_platform')
simulation_attack_technique = lazy_import('msgraph.generated.models.simulation_attack_technique')
simulation_attack_type = lazy_import('msgraph.generated.models.simulation_attack_type')
simulation_report = lazy_import('msgraph.generated.models.simulation_report')
simulation_status = lazy_import('msgraph.generated.models.simulation_status')

class Simulation(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def attack_technique(self,) -> Optional[simulation_attack_technique.SimulationAttackTechnique]:
        """
        Gets the attackTechnique property value. The social engineering technique used in the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, credentialHarvesting, attachmentMalware, driveByUrl, linkInAttachment, linkToMalwareFile, unknownFutureValue. For more information on the types of social engineering attack techniques, see simulations.
        Returns: Optional[simulation_attack_technique.SimulationAttackTechnique]
        """
        return self._attack_technique
    
    @attack_technique.setter
    def attack_technique(self,value: Optional[simulation_attack_technique.SimulationAttackTechnique] = None) -> None:
        """
        Sets the attackTechnique property value. The social engineering technique used in the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, credentialHarvesting, attachmentMalware, driveByUrl, linkInAttachment, linkToMalwareFile, unknownFutureValue. For more information on the types of social engineering attack techniques, see simulations.
        Args:
            value: Value to set for the attackTechnique property.
        """
        self._attack_technique = value
    
    @property
    def attack_type(self,) -> Optional[simulation_attack_type.SimulationAttackType]:
        """
        Gets the attackType property value. Attack type of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, social, cloud, endpoint, unknownFutureValue.
        Returns: Optional[simulation_attack_type.SimulationAttackType]
        """
        return self._attack_type
    
    @attack_type.setter
    def attack_type(self,value: Optional[simulation_attack_type.SimulationAttackType] = None) -> None:
        """
        Sets the attackType property value. Attack type of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, social, cloud, endpoint, unknownFutureValue.
        Args:
            value: Value to set for the attackType property.
        """
        self._attack_type = value
    
    @property
    def automation_id(self,) -> Optional[str]:
        """
        Gets the automationId property value. Unique identifier for the attack simulation automation.
        Returns: Optional[str]
        """
        return self._automation_id
    
    @automation_id.setter
    def automation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the automationId property value. Unique identifier for the attack simulation automation.
        Args:
            value: Value to set for the automationId property.
        """
        self._automation_id = value
    
    @property
    def completion_date_time(self,) -> Optional[datetime]:
        """
        Gets the completionDateTime property value. Date and time of completion of the attack simulation and training campaign. Supports $filter and $orderby.
        Returns: Optional[datetime]
        """
        return self._completion_date_time
    
    @completion_date_time.setter
    def completion_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completionDateTime property value. Date and time of completion of the attack simulation and training campaign. Supports $filter and $orderby.
        Args:
            value: Value to set for the completionDateTime property.
        """
        self._completion_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new simulation and sets the default values.
        """
        super().__init__()
        # The social engineering technique used in the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, credentialHarvesting, attachmentMalware, driveByUrl, linkInAttachment, linkToMalwareFile, unknownFutureValue. For more information on the types of social engineering attack techniques, see simulations.
        self._attack_technique: Optional[simulation_attack_technique.SimulationAttackTechnique] = None
        # Attack type of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, social, cloud, endpoint, unknownFutureValue.
        self._attack_type: Optional[simulation_attack_type.SimulationAttackType] = None
        # Unique identifier for the attack simulation automation.
        self._automation_id: Optional[str] = None
        # Date and time of completion of the attack simulation and training campaign. Supports $filter and $orderby.
        self._completion_date_time: Optional[datetime] = None
        # Identity of the user who created the attack simulation and training campaign.
        self._created_by: Optional[email_identity.EmailIdentity] = None
        # Date and time of creation of the attack simulation and training campaign.
        self._created_date_time: Optional[datetime] = None
        # Description of the attack simulation and training campaign.
        self._description: Optional[str] = None
        # Display name of the attack simulation and training campaign. Supports $filter and $orderby.
        self._display_name: Optional[str] = None
        # Flag that represents if the attack simulation and training campaign was created from a simulation automation flow. Supports $filter and $orderby.
        self._is_automated: Optional[bool] = None
        # Identity of the user who most recently modified the attack simulation and training campaign.
        self._last_modified_by: Optional[email_identity.EmailIdentity] = None
        # Date and time of the most recent modification of the attack simulation and training campaign.
        self._last_modified_date_time: Optional[datetime] = None
        # Date and time of the launch/start of the attack simulation and training campaign. Supports $filter and $orderby.
        self._launch_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Method of delivery of the phishing payload used in the attack simulation and training campaign. Possible values are: unknown, sms, email, teams, unknownFutureValue.
        self._payload_delivery_platform: Optional[payload_delivery_platform.PayloadDeliveryPlatform] = None
        # Report of the attack simulation and training campaign.
        self._report: Optional[simulation_report.SimulationReport] = None
        # Status of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, draft, running, scheduled, succeeded, failed, cancelled, excluded, unknownFutureValue.
        self._status: Optional[simulation_status.SimulationStatus] = None
    
    @property
    def created_by(self,) -> Optional[email_identity.EmailIdentity]:
        """
        Gets the createdBy property value. Identity of the user who created the attack simulation and training campaign.
        Returns: Optional[email_identity.EmailIdentity]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[email_identity.EmailIdentity] = None) -> None:
        """
        Sets the createdBy property value. Identity of the user who created the attack simulation and training campaign.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time of creation of the attack simulation and training campaign.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time of creation of the attack simulation and training campaign.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Simulation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Simulation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Simulation()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the attack simulation and training campaign.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the attack simulation and training campaign.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the attack simulation and training campaign. Supports $filter and $orderby.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the attack simulation and training campaign. Supports $filter and $orderby.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attack_technique": lambda n : setattr(self, 'attack_technique', n.get_enum_value(simulation_attack_technique.SimulationAttackTechnique)),
            "attack_type": lambda n : setattr(self, 'attack_type', n.get_enum_value(simulation_attack_type.SimulationAttackType)),
            "automation_id": lambda n : setattr(self, 'automation_id', n.get_str_value()),
            "completion_date_time": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(email_identity.EmailIdentity)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_automated": lambda n : setattr(self, 'is_automated', n.get_bool_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(email_identity.EmailIdentity)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "launch_date_time": lambda n : setattr(self, 'launch_date_time', n.get_datetime_value()),
            "payload_delivery_platform": lambda n : setattr(self, 'payload_delivery_platform', n.get_enum_value(payload_delivery_platform.PayloadDeliveryPlatform)),
            "report": lambda n : setattr(self, 'report', n.get_object_value(simulation_report.SimulationReport)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(simulation_status.SimulationStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_automated(self,) -> Optional[bool]:
        """
        Gets the isAutomated property value. Flag that represents if the attack simulation and training campaign was created from a simulation automation flow. Supports $filter and $orderby.
        Returns: Optional[bool]
        """
        return self._is_automated
    
    @is_automated.setter
    def is_automated(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAutomated property value. Flag that represents if the attack simulation and training campaign was created from a simulation automation flow. Supports $filter and $orderby.
        Args:
            value: Value to set for the isAutomated property.
        """
        self._is_automated = value
    
    @property
    def last_modified_by(self,) -> Optional[email_identity.EmailIdentity]:
        """
        Gets the lastModifiedBy property value. Identity of the user who most recently modified the attack simulation and training campaign.
        Returns: Optional[email_identity.EmailIdentity]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[email_identity.EmailIdentity] = None) -> None:
        """
        Sets the lastModifiedBy property value. Identity of the user who most recently modified the attack simulation and training campaign.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Date and time of the most recent modification of the attack simulation and training campaign.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Date and time of the most recent modification of the attack simulation and training campaign.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def launch_date_time(self,) -> Optional[datetime]:
        """
        Gets the launchDateTime property value. Date and time of the launch/start of the attack simulation and training campaign. Supports $filter and $orderby.
        Returns: Optional[datetime]
        """
        return self._launch_date_time
    
    @launch_date_time.setter
    def launch_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the launchDateTime property value. Date and time of the launch/start of the attack simulation and training campaign. Supports $filter and $orderby.
        Args:
            value: Value to set for the launchDateTime property.
        """
        self._launch_date_time = value
    
    @property
    def payload_delivery_platform(self,) -> Optional[payload_delivery_platform.PayloadDeliveryPlatform]:
        """
        Gets the payloadDeliveryPlatform property value. Method of delivery of the phishing payload used in the attack simulation and training campaign. Possible values are: unknown, sms, email, teams, unknownFutureValue.
        Returns: Optional[payload_delivery_platform.PayloadDeliveryPlatform]
        """
        return self._payload_delivery_platform
    
    @payload_delivery_platform.setter
    def payload_delivery_platform(self,value: Optional[payload_delivery_platform.PayloadDeliveryPlatform] = None) -> None:
        """
        Sets the payloadDeliveryPlatform property value. Method of delivery of the phishing payload used in the attack simulation and training campaign. Possible values are: unknown, sms, email, teams, unknownFutureValue.
        Args:
            value: Value to set for the payloadDeliveryPlatform property.
        """
        self._payload_delivery_platform = value
    
    @property
    def report(self,) -> Optional[simulation_report.SimulationReport]:
        """
        Gets the report property value. Report of the attack simulation and training campaign.
        Returns: Optional[simulation_report.SimulationReport]
        """
        return self._report
    
    @report.setter
    def report(self,value: Optional[simulation_report.SimulationReport] = None) -> None:
        """
        Sets the report property value. Report of the attack simulation and training campaign.
        Args:
            value: Value to set for the report property.
        """
        self._report = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("attackTechnique", self.attack_technique)
        writer.write_enum_value("attackType", self.attack_type)
        writer.write_str_value("automationId", self.automation_id)
        writer.write_datetime_value("completionDateTime", self.completion_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isAutomated", self.is_automated)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("launchDateTime", self.launch_date_time)
        writer.write_enum_value("payloadDeliveryPlatform", self.payload_delivery_platform)
        writer.write_object_value("report", self.report)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[simulation_status.SimulationStatus]:
        """
        Gets the status property value. Status of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, draft, running, scheduled, succeeded, failed, cancelled, excluded, unknownFutureValue.
        Returns: Optional[simulation_status.SimulationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[simulation_status.SimulationStatus] = None) -> None:
        """
        Sets the status property value. Status of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, draft, running, scheduled, succeeded, failed, cancelled, excluded, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

