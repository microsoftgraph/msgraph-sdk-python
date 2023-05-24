from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import synchronization_job_subject

class SynchronizationLinkedObjects(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationLinkedObjects and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The manager property
        self._manager: Optional[synchronization_job_subject.SynchronizationJobSubject] = None
        # The members property
        self._members: Optional[List[synchronization_job_subject.SynchronizationJobSubject]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The owners property
        self._owners: Optional[List[synchronization_job_subject.SynchronizationJobSubject]] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationLinkedObjects:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationLinkedObjects
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationLinkedObjects()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import synchronization_job_subject

        fields: Dict[str, Callable[[Any], None]] = {
            "manager": lambda n : setattr(self, 'manager', n.get_object_value(synchronization_job_subject.SynchronizationJobSubject)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(synchronization_job_subject.SynchronizationJobSubject)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(synchronization_job_subject.SynchronizationJobSubject)),
        }
        return fields
    
    @property
    def manager(self,) -> Optional[synchronization_job_subject.SynchronizationJobSubject]:
        """
        Gets the manager property value. The manager property
        Returns: Optional[synchronization_job_subject.SynchronizationJobSubject]
        """
        return self._manager
    
    @manager.setter
    def manager(self,value: Optional[synchronization_job_subject.SynchronizationJobSubject] = None) -> None:
        """
        Sets the manager property value. The manager property
        Args:
            value: Value to set for the manager property.
        """
        self._manager = value
    
    @property
    def members(self,) -> Optional[List[synchronization_job_subject.SynchronizationJobSubject]]:
        """
        Gets the members property value. The members property
        Returns: Optional[List[synchronization_job_subject.SynchronizationJobSubject]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[synchronization_job_subject.SynchronizationJobSubject]] = None) -> None:
        """
        Sets the members property value. The members property
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
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
    
    @property
    def owners(self,) -> Optional[List[synchronization_job_subject.SynchronizationJobSubject]]:
        """
        Gets the owners property value. The owners property
        Returns: Optional[List[synchronization_job_subject.SynchronizationJobSubject]]
        """
        return self._owners
    
    @owners.setter
    def owners(self,value: Optional[List[synchronization_job_subject.SynchronizationJobSubject]] = None) -> None:
        """
        Sets the owners property value. The owners property
        Args:
            value: Value to set for the owners property.
        """
        self._owners = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("manager", self.manager)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("owners", self.owners)
        writer.write_additional_data_value(self.additional_data)
    

