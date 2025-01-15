from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource
    from .entity import Entity
    from .governance_insight import GovernanceInsight
    from .identity import Identity
    from .user_identity import UserIdentity

from .entity import Entity

@dataclass
class AccessReviewInstanceDecisionItem(Entity, Parsable):
    # The identifier of the accessReviewInstance parent. Supports $select. Read-only.
    access_review_id: Optional[str] = None
    # The identifier of the user who applied the decision. Read-only.
    applied_by: Optional[UserIdentity] = None
    # The timestamp when the approval decision was applied.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't applied the decision or it was automatically applied. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Supports $select. Read-only.
    applied_date_time: Optional[datetime.datetime] = None
    # The result of applying the decision. Possible values: New, AppliedSuccessfully, AppliedWithUnknownFailure, AppliedSuccessfullyButObjectNotFound and ApplyNotSupported. Supports $select, $orderby, and $filter (eq only). Read-only.
    apply_result: Optional[str] = None
    # Result of the review. Possible values: Approve, Deny, NotReviewed, or DontKnow. Supports $select, $orderby, and $filter (eq only).
    decision: Optional[str] = None
    # Insights are recommendations to reviewers on whether to approve or deny a decision. There can be multiple insights associated with an accessReviewInstanceDecisionItem.
    insights: Optional[list[GovernanceInsight]] = None
    # Justification left by the reviewer when they made the decision.
    justification: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Every decision item in an access review represents a principal's access to a resource. This property represents details of the principal. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is 'Bob' and the resource is 'Sales'. Principals can be of two types - userIdentity and servicePrincipalIdentity. Supports $select. Read-only.
    principal: Optional[Identity] = None
    # A link to the principal object. For example, https://graph.microsoft.com/v1.0/users/a6c7aecb-cbfd-4763-87ef-e91b4bd509d9. Read-only.
    principal_link: Optional[str] = None
    # A system-generated recommendation for the approval decision based off last interactive sign-in to tenant. The value is Approve if the sign-in is fewer than 30 days after the start of review, Deny if the sign-in is greater than 30 days after, or NoInfoAvailable. Possible values: Approve, Deny, or NoInfoAvailable. Supports $select, $orderby, and $filter (eq only). Read-only.
    recommendation: Optional[str] = None
    # Every decision item in an access review represents a principal's access to a resource. This property represents details of the resource. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is Bob and the resource is 'Sales'. Resources can be of multiple types. See accessReviewInstanceDecisionItemResource. Read-only.
    resource: Optional[AccessReviewInstanceDecisionItemResource] = None
    # A link to the resource. For example, https://graph.microsoft.com/v1.0/servicePrincipals/c86300f3-8695-4320-9f6e-32a2555f5ff8. Supports $select. Read-only.
    resource_link: Optional[str] = None
    # The identifier of the reviewer.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Supports $select. Read-only.
    reviewed_by: Optional[UserIdentity] = None
    # The timestamp when the review decision occurred. Supports $select. Read-only.
    reviewed_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewInstanceDecisionItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewInstanceDecisionItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource
        from .entity import Entity
        from .governance_insight import GovernanceInsight
        from .identity import Identity
        from .user_identity import UserIdentity

        from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource
        from .entity import Entity
        from .governance_insight import GovernanceInsight
        from .identity import Identity
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "accessReviewId": lambda n : setattr(self, 'access_review_id', n.get_str_value()),
            "appliedBy": lambda n : setattr(self, 'applied_by', n.get_object_value(UserIdentity)),
            "appliedDateTime": lambda n : setattr(self, 'applied_date_time', n.get_datetime_value()),
            "applyResult": lambda n : setattr(self, 'apply_result', n.get_str_value()),
            "decision": lambda n : setattr(self, 'decision', n.get_str_value()),
            "insights": lambda n : setattr(self, 'insights', n.get_collection_of_object_values(GovernanceInsight)),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(Identity)),
            "principalLink": lambda n : setattr(self, 'principal_link', n.get_str_value()),
            "recommendation": lambda n : setattr(self, 'recommendation', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(AccessReviewInstanceDecisionItemResource)),
            "resourceLink": lambda n : setattr(self, 'resource_link', n.get_str_value()),
            "reviewedBy": lambda n : setattr(self, 'reviewed_by', n.get_object_value(UserIdentity)),
            "reviewedDateTime": lambda n : setattr(self, 'reviewed_date_time', n.get_datetime_value()),
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
        writer.write_str_value("accessReviewId", self.access_review_id)
        writer.write_object_value("appliedBy", self.applied_by)
        writer.write_datetime_value("appliedDateTime", self.applied_date_time)
        writer.write_str_value("applyResult", self.apply_result)
        writer.write_str_value("decision", self.decision)
        writer.write_collection_of_object_values("insights", self.insights)
        writer.write_str_value("justification", self.justification)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalLink", self.principal_link)
        writer.write_str_value("recommendation", self.recommendation)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("resourceLink", self.resource_link)
        writer.write_object_value("reviewedBy", self.reviewed_by)
        writer.write_datetime_value("reviewedDateTime", self.reviewed_date_time)
    

