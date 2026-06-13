# Relational Create / Host Object

Use this reference when creating an object that must be hosted by or related to another object.

Examples: door in wall, attachment on record, child task in project, line item under invoice, resource in a layer, comment on document.

## Procedure

1. Resolve the parent/host ID from the app, not from display text alone.
2. Verify the parent type is valid for this child.
3. Verify the requested offset, range, or relationship is allowed.
4. Verify context such as layer, story, project, document, workspace, or account.
5. Dry-run with parent ID and relationship fields.
6. Apply only after approval when write is in scope.
7. Read back the created object and its relation to the parent.
8. Roll back only the created child object if needed.

## Required Readback

- child ID;
- child type;
- parent/host ID;
- relation type;
- relevant offset/range/position;
- context/layer/story/workspace;
- native/proxy class.

## Failure Rule

Creating an unhosted object when the user requested a hosted object is an intent failure, even if the app returns success.
