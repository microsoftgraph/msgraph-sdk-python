from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..identity_set import IdentitySet
    from .case import Case
    from .case_operation import CaseOperation
    from .ediscovery_case_settings import EdiscoveryCaseSettings
    from .ediscovery_custodian import EdiscoveryCustodian
    from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
    from .ediscovery_review_set import EdiscoveryReviewSet
    from .ediscovery_review_tag import EdiscoveryReviewTag
    from .ediscovery_search import EdiscoverySearch

from .case import Case

@dataclass
class EdiscoveryCase(Case, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.ediscoveryCase"
    # The user who closed the case.
    closed_by: Optional[IdentitySet] = None
    # The date and time when the case was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    closed_date_time: Optional[datetime.datetime] = None
    # Returns a list of case ediscoveryCustodian objects for this case.
    custodians: Optional[List[EdiscoveryCustodian]] = None
    # The external case number for customer reference.
    external_id: Optional[str] = None
    # Returns a list of case ediscoveryNoncustodialDataSource objects for this case.
    noncustodial_data_sources: Optional[List[EdiscoveryNoncustodialDataSource]] = None
    # Returns a list of case caseOperation objects for this case.
    operations: Optional[List[CaseOperation]] = None
    # Returns a list of eDiscoveryReviewSet objects in the case.
    review_sets: Optional[List[EdiscoveryReviewSet]] = None
    # Returns a list of eDiscoverySearch objects associated with this case.
    searches: Optional[List[EdiscoverySearch]] = None
    # Returns a list of eDIscoverySettings objects in the case.
    settings: Optional[EdiscoveryCaseSettings] = None
    # Returns a list of ediscoveryReviewTag objects associated to this case.
    tags: Optional[List[EdiscoveryReviewTag]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdiscoveryCase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryCase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryCase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..identity_set import IdentitySet
        from .case import Case
        from .case_operation import CaseOperation
        from .ediscovery_case_settings import EdiscoveryCaseSettings
        from .ediscovery_custodian import EdiscoveryCustodian
        from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
        from .ediscovery_review_set import EdiscoveryReviewSet
        from .ediscovery_review_tag import EdiscoveryReviewTag
        from .ediscovery_search import EdiscoverySearch

        from ..identity_set import IdentitySet
        from .case import Case
        from .case_operation import CaseOperation
        from .ediscovery_case_settings import EdiscoveryCaseSettings
        from .ediscovery_custodian import EdiscoveryCustodian
        from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
        from .ediscovery_review_set import EdiscoveryReviewSet
        from .ediscovery_review_tag import EdiscoveryReviewTag
        from .ediscovery_search import EdiscoverySearch

        fields: Dict[str, Callable[[Any], None]] = {
            "closedBy": lambda n : setattr(self, 'closed_by', n.get_object_value(IdentitySet)),
            "closedDateTime": lambda n : setattr(self, 'closed_date_time', n.get_datetime_value()),
            "custodians": lambda n : setattr(self, 'custodians', n.get_collection_of_object_values(EdiscoveryCustodian)),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "noncustodialDataSources": lambda n : setattr(self, 'noncustodial_data_sources', n.get_collection_of_object_values(EdiscoveryNoncustodialDataSource)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(CaseOperation)),
            "reviewSets": lambda n : setattr(self, 'review_sets', n.get_collection_of_object_values(EdiscoveryReviewSet)),
            "searches": lambda n : setattr(self, 'searches', n.get_collection_of_object_values(EdiscoverySearch)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(EdiscoveryCaseSettings)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(EdiscoveryReviewTag)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from ..identity_set import IdentitySet
        from .case import Case
        from .case_operation import CaseOperation
        from .ediscovery_case_settings import EdiscoveryCaseSettings
        from .ediscovery_custodian import EdiscoveryCustodian
        from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
        from .ediscovery_review_set import EdiscoveryReviewSet
        from .ediscovery_review_tag import EdiscoveryReviewTag
        from .ediscovery_search import EdiscoverySearch

        writer.write_object_value("closedBy", self.closed_by)
        writer.write_datetime_value("closedDateTime", self.closed_date_time)
        writer.write_collection_of_object_values("custodians", self.custodians)
        writer.write_str_value("externalId", self.external_id)
        writer.write_collection_of_object_values("noncustodialDataSources", self.noncustodial_data_sources)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("reviewSets", self.review_sets)
        writer.write_collection_of_object_values("searches", self.searches)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("tags", self.tags)
    

