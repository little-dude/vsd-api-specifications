{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Describes the Forwarding Path List",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "description",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Description"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": true,
            "default_value": null,
            "deprecated": false,
            "description": "Name of the forwarding path list.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 64,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "name",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Name"
        }
    ],
    "children": [
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": true,
            "delete": false,
            "deprecated": null,
            "get": true,
            "relationship": "child",
            "rest_name": "forwardingpathlistentry",
            "update": false
        }
    ],
    "model": {
        "create": null,
        "delete": true,
        "description": "Forwarding path list is l4 based policy to PAT / IKE to underlay.",
        "entity_name": "ForwardingPathList",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy",
        "resource_name": "forwardingpathlists",
        "rest_name": "forwardingpathlist",
        "root": null,
        "update": true,
        "userlabel": "Forwarding Path Lists"
    }
}