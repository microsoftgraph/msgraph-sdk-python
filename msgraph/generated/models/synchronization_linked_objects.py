from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .synchronization_job_subject import SynchronizationJobSubject

@dataclass
class SynchronizationLinkedObjects(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The manager property
    manager: Optional[SynchronizationJobSubject] = None
    # All group members that you would like to provision.
    members: Optional[List[SynchronizationJobSubject]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The owners property
    owners: Optional[List[SynchronizationJobSubject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SynchronizationLinkedObjects:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationLinkedObjects
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationLinkedObjects()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .synchronization_job_subject import SynchronizationJobSubject

        from .synchronization_job_subject import SynchronizationJobSubject

        fields: Dict[str, Callable[[Any], None]] = {
            "manager": lambda n : setattr(self, 'manager', n.get_object_value(SynchronizationJobSubject)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(SynchronizationJobSubject)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(SynchronizationJobSubject)),
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
        writer.write_object_value("manager", self.manager)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("owners", self.owners)
        writer.write_additional_data_value(self.additional_data)
    

