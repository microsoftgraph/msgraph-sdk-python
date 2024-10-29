from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .synchronization_job_subject import SynchronizationJobSubject

@dataclass
class SynchronizationJobApplicationParameters(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier of the synchronizationRule to be applied. This rule ID is defined in the schema for a given synchronization job or template.
    rule_id: Optional[str] = None
    # The identifiers of one or more objects to which a synchronizationJob is to be applied.
    subjects: Optional[List[SynchronizationJobSubject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SynchronizationJobApplicationParameters:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationJobApplicationParameters
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationJobApplicationParameters()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .synchronization_job_subject import SynchronizationJobSubject

        from .synchronization_job_subject import SynchronizationJobSubject

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ruleId": lambda n : setattr(self, 'rule_id', n.get_str_value()),
            "subjects": lambda n : setattr(self, 'subjects', n.get_collection_of_object_values(SynchronizationJobSubject)),
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
        from .synchronization_job_subject import SynchronizationJobSubject

        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("ruleId", self.rule_id)
        writer.write_collection_of_object_values("subjects", self.subjects)
        writer.write_additional_data_value(self.additional_data)
    

