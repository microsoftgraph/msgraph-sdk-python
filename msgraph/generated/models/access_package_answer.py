from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_question = lazy_import('msgraph.generated.models.access_package_question')

class AccessPackageAnswer(AdditionalDataHolder, Parsable):
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
    def answered_question(self,) -> Optional[access_package_question.AccessPackageQuestion]:
        """
        Gets the answeredQuestion property value. The answeredQuestion property
        Returns: Optional[access_package_question.AccessPackageQuestion]
        """
        return self._answered_question
    
    @answered_question.setter
    def answered_question(self,value: Optional[access_package_question.AccessPackageQuestion] = None) -> None:
        """
        Sets the answeredQuestion property value. The answeredQuestion property
        Args:
            value: Value to set for the answered_question property.
        """
        self._answered_question = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAnswer and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The answeredQuestion property
        self._answered_question: Optional[access_package_question.AccessPackageQuestion] = None
        # The localized display value shown to the requestor and approvers.
        self._display_value: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAnswer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAnswer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAnswer()
    
    @property
    def display_value(self,) -> Optional[str]:
        """
        Gets the displayValue property value. The localized display value shown to the requestor and approvers.
        Returns: Optional[str]
        """
        return self._display_value
    
    @display_value.setter
    def display_value(self,value: Optional[str] = None) -> None:
        """
        Sets the displayValue property value. The localized display value shown to the requestor and approvers.
        Args:
            value: Value to set for the display_value property.
        """
        self._display_value = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "answeredQuestion": lambda n : setattr(self, 'answered_question', n.get_object_value(access_package_question.AccessPackageQuestion)),
            "displayValue": lambda n : setattr(self, 'display_value', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("answeredQuestion", self.answered_question)
        writer.write_str_value("displayValue", self.display_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

