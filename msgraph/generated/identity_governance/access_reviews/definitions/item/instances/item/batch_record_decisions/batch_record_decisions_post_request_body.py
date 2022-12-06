from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class BatchRecordDecisionsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the batchRecordDecisions method.
    """
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
        Instantiates a new batchRecordDecisionsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The decision property
        self._decision: Optional[str] = None
        # The justification property
        self._justification: Optional[str] = None
        # The principalId property
        self._principal_id: Optional[str] = None
        # The resourceId property
        self._resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BatchRecordDecisionsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BatchRecordDecisionsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BatchRecordDecisionsPostRequestBody()
    
    @property
    def decision(self,) -> Optional[str]:
        """
        Gets the decision property value. The decision property
        Returns: Optional[str]
        """
        return self._decision
    
    @decision.setter
    def decision(self,value: Optional[str] = None) -> None:
        """
        Sets the decision property value. The decision property
        Args:
            value: Value to set for the decision property.
        """
        self._decision = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "decision": lambda n : setattr(self, 'decision', n.get_str_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "principal_id": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
        }
        return fields
    
    @property
    def justification(self,) -> Optional[str]:
        """
        Gets the justification property value. The justification property
        Returns: Optional[str]
        """
        return self._justification
    
    @justification.setter
    def justification(self,value: Optional[str] = None) -> None:
        """
        Sets the justification property value. The justification property
        Args:
            value: Value to set for the justification property.
        """
        self._justification = value
    
    @property
    def principal_id(self,) -> Optional[str]:
        """
        Gets the principalId property value. The principalId property
        Returns: Optional[str]
        """
        return self._principal_id
    
    @principal_id.setter
    def principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the principalId property value. The principalId property
        Args:
            value: Value to set for the principalId property.
        """
        self._principal_id = value
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. The resourceId property
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. The resourceId property
        Args:
            value: Value to set for the resourceId property.
        """
        self._resource_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("decision", self.decision)
        writer.write_str_value("justification", self.justification)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_additional_data_value(self.additional_data)
    

