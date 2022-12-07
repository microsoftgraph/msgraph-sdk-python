from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

answer_input_type = lazy_import('msgraph.generated.models.answer_input_type')

class BookingQuestionAnswer(AdditionalDataHolder, Parsable):
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
    def answer(self,) -> Optional[str]:
        """
        Gets the answer property value. The answer given by the user in case the answerInputType is text.
        Returns: Optional[str]
        """
        return self._answer
    
    @answer.setter
    def answer(self,value: Optional[str] = None) -> None:
        """
        Sets the answer property value. The answer given by the user in case the answerInputType is text.
        Args:
            value: Value to set for the answer property.
        """
        self._answer = value
    
    @property
    def answer_input_type(self,) -> Optional[answer_input_type.AnswerInputType]:
        """
        Gets the answerInputType property value. The expected answer type. The possible values are: text, radioButton, unknownFutureValue.
        Returns: Optional[answer_input_type.AnswerInputType]
        """
        return self._answer_input_type
    
    @answer_input_type.setter
    def answer_input_type(self,value: Optional[answer_input_type.AnswerInputType] = None) -> None:
        """
        Sets the answerInputType property value. The expected answer type. The possible values are: text, radioButton, unknownFutureValue.
        Args:
            value: Value to set for the answerInputType property.
        """
        self._answer_input_type = value
    
    @property
    def answer_options(self,) -> Optional[List[str]]:
        """
        Gets the answerOptions property value. In case the answerInputType is radioButton, this will consists of a list of possible answer values.
        Returns: Optional[List[str]]
        """
        return self._answer_options
    
    @answer_options.setter
    def answer_options(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the answerOptions property value. In case the answerInputType is radioButton, this will consists of a list of possible answer values.
        Args:
            value: Value to set for the answerOptions property.
        """
        self._answer_options = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new bookingQuestionAnswer and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The answer given by the user in case the answerInputType is text.
        self._answer: Optional[str] = None
        # The expected answer type. The possible values are: text, radioButton, unknownFutureValue.
        self._answer_input_type: Optional[answer_input_type.AnswerInputType] = None
        # In case the answerInputType is radioButton, this will consists of a list of possible answer values.
        self._answer_options: Optional[List[str]] = None
        # Indicates whether it is mandatory to answer the custom question.
        self._is_required: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The question.
        self._question: Optional[str] = None
        # The ID of the custom question.
        self._question_id: Optional[str] = None
        # The answers selected by the user.
        self._selected_options: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingQuestionAnswer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingQuestionAnswer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingQuestionAnswer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "answer": lambda n : setattr(self, 'answer', n.get_str_value()),
            "answer_input_type": lambda n : setattr(self, 'answer_input_type', n.get_enum_value(answer_input_type.AnswerInputType)),
            "answer_options": lambda n : setattr(self, 'answer_options', n.get_collection_of_primitive_values(str)),
            "is_required": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "question": lambda n : setattr(self, 'question', n.get_str_value()),
            "question_id": lambda n : setattr(self, 'question_id', n.get_str_value()),
            "selected_options": lambda n : setattr(self, 'selected_options', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def is_required(self,) -> Optional[bool]:
        """
        Gets the isRequired property value. Indicates whether it is mandatory to answer the custom question.
        Returns: Optional[bool]
        """
        return self._is_required
    
    @is_required.setter
    def is_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRequired property value. Indicates whether it is mandatory to answer the custom question.
        Args:
            value: Value to set for the isRequired property.
        """
        self._is_required = value
    
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
    def question(self,) -> Optional[str]:
        """
        Gets the question property value. The question.
        Returns: Optional[str]
        """
        return self._question
    
    @question.setter
    def question(self,value: Optional[str] = None) -> None:
        """
        Sets the question property value. The question.
        Args:
            value: Value to set for the question property.
        """
        self._question = value
    
    @property
    def question_id(self,) -> Optional[str]:
        """
        Gets the questionId property value. The ID of the custom question.
        Returns: Optional[str]
        """
        return self._question_id
    
    @question_id.setter
    def question_id(self,value: Optional[str] = None) -> None:
        """
        Sets the questionId property value. The ID of the custom question.
        Args:
            value: Value to set for the questionId property.
        """
        self._question_id = value
    
    @property
    def selected_options(self,) -> Optional[List[str]]:
        """
        Gets the selectedOptions property value. The answers selected by the user.
        Returns: Optional[List[str]]
        """
        return self._selected_options
    
    @selected_options.setter
    def selected_options(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the selectedOptions property value. The answers selected by the user.
        Args:
            value: Value to set for the selectedOptions property.
        """
        self._selected_options = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("answer", self.answer)
        writer.write_enum_value("answerInputType", self.answer_input_type)
        writer.write_collection_of_primitive_values("answerOptions", self.answer_options)
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("question", self.question)
        writer.write_str_value("questionId", self.question_id)
        writer.write_collection_of_primitive_values("selectedOptions", self.selected_options)
        writer.write_additional_data_value(self.additional_data)
    

