from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

selection_likelihood_info = lazy_import('msgraph.generated.models.selection_likelihood_info')

class ScoredEmailAddress(AdditionalDataHolder, Parsable):
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
    def address(self,) -> Optional[str]:
        """
        Gets the address property value. The email address.
        Returns: Optional[str]
        """
        return self._address
    
    @address.setter
    def address(self,value: Optional[str] = None) -> None:
        """
        Sets the address property value. The email address.
        Args:
            value: Value to set for the address property.
        """
        self._address = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new scoredEmailAddress and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The email address.
        self._address: Optional[str] = None
        # The itemId property
        self._item_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The relevance score of the email address. A relevance score is used as a sort key, in relation to the other returned results. A higher relevance score value corresponds to a more relevant result. Relevance is determined by the user’s communication and collaboration patterns and business relationships.
        self._relevance_score: Optional[float] = None
        # The selectionLikelihood property
        self._selection_likelihood: Optional[selection_likelihood_info.SelectionLikelihoodInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScoredEmailAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ScoredEmailAddress
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ScoredEmailAddress()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "item_id": lambda n : setattr(self, 'item_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "relevance_score": lambda n : setattr(self, 'relevance_score', n.get_float_value()),
            "selection_likelihood": lambda n : setattr(self, 'selection_likelihood', n.get_enum_value(selection_likelihood_info.SelectionLikelihoodInfo)),
        }
        return fields
    
    @property
    def item_id(self,) -> Optional[str]:
        """
        Gets the itemId property value. The itemId property
        Returns: Optional[str]
        """
        return self._item_id
    
    @item_id.setter
    def item_id(self,value: Optional[str] = None) -> None:
        """
        Sets the itemId property value. The itemId property
        Args:
            value: Value to set for the itemId property.
        """
        self._item_id = value
    
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
    def relevance_score(self,) -> Optional[float]:
        """
        Gets the relevanceScore property value. The relevance score of the email address. A relevance score is used as a sort key, in relation to the other returned results. A higher relevance score value corresponds to a more relevant result. Relevance is determined by the user’s communication and collaboration patterns and business relationships.
        Returns: Optional[float]
        """
        return self._relevance_score
    
    @relevance_score.setter
    def relevance_score(self,value: Optional[float] = None) -> None:
        """
        Sets the relevanceScore property value. The relevance score of the email address. A relevance score is used as a sort key, in relation to the other returned results. A higher relevance score value corresponds to a more relevant result. Relevance is determined by the user’s communication and collaboration patterns and business relationships.
        Args:
            value: Value to set for the relevanceScore property.
        """
        self._relevance_score = value
    
    @property
    def selection_likelihood(self,) -> Optional[selection_likelihood_info.SelectionLikelihoodInfo]:
        """
        Gets the selectionLikelihood property value. The selectionLikelihood property
        Returns: Optional[selection_likelihood_info.SelectionLikelihoodInfo]
        """
        return self._selection_likelihood
    
    @selection_likelihood.setter
    def selection_likelihood(self,value: Optional[selection_likelihood_info.SelectionLikelihoodInfo] = None) -> None:
        """
        Sets the selectionLikelihood property value. The selectionLikelihood property
        Args:
            value: Value to set for the selectionLikelihood property.
        """
        self._selection_likelihood = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("address", self.address)
        writer.write_str_value("itemId", self.item_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("relevanceScore", self.relevance_score)
        writer.write_enum_value("selectionLikelihood", self.selection_likelihood)
        writer.write_additional_data_value(self.additional_data)
    

