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
            "description": "A description of the fc -dscp remarking table.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "description",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "A unique name of the fc- dscp remarking table.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "name",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
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
            "rest_name": "dscpremarkingpolicy",
            "update": false
        }
    ],
    "model": {
        "create": null,
        "delete": true,
        "description": "Provides the definition of a table that holds multiple Forwarding class to  DSCP  mappings. Used in Egress QoS policies.",
        "entity_name": "DSCPRemarkingPolicyTable",
        "extends": [
            "@audited"
        ],
        "get": true,
        "package": "policy/dscpmapping",
        "resource_name": "dscpremarkingpolicytables",
        "rest_name": "dscpremarkingpolicytable",
        "root": null,
        "update": true
    }
}