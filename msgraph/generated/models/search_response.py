from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alteration_response = lazy_import('msgraph.generated.models.alteration_response')
result_template_dictionary = lazy_import('msgraph.generated.models.result_template_dictionary')
search_hits_container = lazy_import('msgraph.generated.models.search_hits_container')

class SearchResponse(AdditionalDataHolder, Parsable):
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
        Instantiates a new searchResponse and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A collection of search results.
        self._hits_containers: Optional[List[search_hits_container.SearchHitsContainer]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Provides information related to spelling corrections in the alteration response.
        self._query_alteration_response: Optional[alteration_response.AlterationResponse] = None
        # A dictionary of resultTemplateIds and associated values, which include the name and JSON schema of the result templates.
        self._result_templates: Optional[result_template_dictionary.ResultTemplateDictionary] = None
        # Contains the search terms sent in the initial search query.
        self._search_terms: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SearchResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SearchResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SearchResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "hits_containers": lambda n : setattr(self, 'hits_containers', n.get_collection_of_object_values(search_hits_container.SearchHitsContainer)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "query_alteration_response": lambda n : setattr(self, 'query_alteration_response', n.get_object_value(alteration_response.AlterationResponse)),
            "result_templates": lambda n : setattr(self, 'result_templates', n.get_object_value(result_template_dictionary.ResultTemplateDictionary)),
            "search_terms": lambda n : setattr(self, 'search_terms', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def hits_containers(self,) -> Optional[List[search_hits_container.SearchHitsContainer]]:
        """
        Gets the hitsContainers property value. A collection of search results.
        Returns: Optional[List[search_hits_container.SearchHitsContainer]]
        """
        return self._hits_containers
    
    @hits_containers.setter
    def hits_containers(self,value: Optional[List[search_hits_container.SearchHitsContainer]] = None) -> None:
        """
        Sets the hitsContainers property value. A collection of search results.
        Args:
            value: Value to set for the hitsContainers property.
        """
        self._hits_containers = value
    
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
    def query_alteration_response(self,) -> Optional[alteration_response.AlterationResponse]:
        """
        Gets the queryAlterationResponse property value. Provides information related to spelling corrections in the alteration response.
        Returns: Optional[alteration_response.AlterationResponse]
        """
        return self._query_alteration_response
    
    @query_alteration_response.setter
    def query_alteration_response(self,value: Optional[alteration_response.AlterationResponse] = None) -> None:
        """
        Sets the queryAlterationResponse property value. Provides information related to spelling corrections in the alteration response.
        Args:
            value: Value to set for the queryAlterationResponse property.
        """
        self._query_alteration_response = value
    
    @property
    def result_templates(self,) -> Optional[result_template_dictionary.ResultTemplateDictionary]:
        """
        Gets the resultTemplates property value. A dictionary of resultTemplateIds and associated values, which include the name and JSON schema of the result templates.
        Returns: Optional[result_template_dictionary.ResultTemplateDictionary]
        """
        return self._result_templates
    
    @result_templates.setter
    def result_templates(self,value: Optional[result_template_dictionary.ResultTemplateDictionary] = None) -> None:
        """
        Sets the resultTemplates property value. A dictionary of resultTemplateIds and associated values, which include the name and JSON schema of the result templates.
        Args:
            value: Value to set for the resultTemplates property.
        """
        self._result_templates = value
    
    @property
    def search_terms(self,) -> Optional[List[str]]:
        """
        Gets the searchTerms property value. Contains the search terms sent in the initial search query.
        Returns: Optional[List[str]]
        """
        return self._search_terms
    
    @search_terms.setter
    def search_terms(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the searchTerms property value. Contains the search terms sent in the initial search query.
        Args:
            value: Value to set for the searchTerms property.
        """
        self._search_terms = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("hitsContainers", self.hits_containers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("queryAlterationResponse", self.query_alteration_response)
        writer.write_object_value("resultTemplates", self.result_templates)
        writer.write_collection_of_primitive_values("searchTerms", self.search_terms)
        writer.write_additional_data_value(self.additional_data)
    

