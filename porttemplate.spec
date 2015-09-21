{
  "apis": {
    "children": {
      "/porttemplates/id/metadatas": {
        "RESTName": "metadata",
        "entityName": "Metadata",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          },
          {
            "availability": null,
            "method": "POST"
          }
        ],
        "resourceName": "metadatas"
      },
      "/porttemplates/{id}/vlantemplates": {
        "RESTName": "vlantemplate",
        "entityName": "VLANTemplate",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          },
          {
            "availability": null,
            "method": "POST"
          }
        ],
        "resourceName": "vlantemplates"
      }
    },
    "parents": {
      "/gatewaytemplates/{id}/porttemplates": {
        "RESTName": "gatewaytemplate",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          },
          {
            "availability": null,
            "method": "POST"
          }
        ],
        "resourceName": "gatewaytemplates"
      }
    },
    "self": {
      "/porttemplates/{id}": {
        "RESTName": "porttemplate",
        "operations": [
          {
            "availability": null,
            "method": "PUT"
          },
          {
            "availability": null,
            "method": "DELETE"
          },
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "porttemplates"
      }
    }
  },
  "model": {
    "RESTName": "porttemplate",
    "attributes": {
      "VLANRange": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.",
        "exposed": true,
        "filterable": false,
        "format": null,
        "maxLength": null,
        "maxValue": null,
        "minLength": null,
        "minValue": null,
        "orderable": false,
        "readOnly": false,
        "required": false,
        "transient": false,
        "type": "string",
        "unique": false
      },
      "associatedEgressQOSPolicyID": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "ID of the Egress QOS Policy associated with this Vlan.",
        "exposed": true,
        "filterable": false,
        "format": null,
        "maxLength": null,
        "maxValue": null,
        "minLength": null,
        "minValue": null,
        "orderable": false,
        "readOnly": false,
        "required": false,
        "transient": false,
        "type": "string",
        "unique": false
      },
      "description": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "A description of the Port",
        "exposed": true,
        "filterable": false,
        "format": null,
        "maxLength": null,
        "maxValue": null,
        "minLength": null,
        "minValue": null,
        "orderable": false,
        "readOnly": false,
        "required": false,
        "transient": false,
        "type": "string",
        "unique": false
      },
      "entityScope": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Specify if scope of entity is Data center or Enterprise level",
        "exposed": true,
        "filterable": false,
        "format": null,
        "maxLength": null,
        "maxValue": null,
        "minLength": null,
        "minValue": null,
        "orderable": false,
        "readOnly": false,
        "required": false,
        "transient": false,
        "type": "EntityScope",
        "unique": false
      },
      "name": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Name of the Port",
        "exposed": true,
        "filterable": false,
        "format": null,
        "maxLength": null,
        "maxValue": null,
        "minLength": null,
        "minValue": null,
        "orderable": false,
        "readOnly": false,
        "required": true,
        "transient": false,
        "type": "string",
        "unique": false
      },
      "physicalName": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Identifier of the Port",
        "exposed": true,
        "filterable": false,
        "format": null,
        "maxLength": null,
        "maxValue": null,
        "minLength": null,
        "minValue": null,
        "orderable": false,
        "readOnly": false,
        "required": true,
        "transient": false,
        "type": "string",
        "unique": false
      },
      "portType": {
        "allowedChars": null,
        "allowedChoices": [
          "ACCESS",
          "NETWORK"
        ],
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Type of the Port - NETWORK, ACCESS Possible values are ACCESS, NETWORK, .",
        "exposed": true,
        "filterable": false,
        "format": null,
        "maxLength": null,
        "maxValue": null,
        "minLength": null,
        "minValue": null,
        "orderable": false,
        "readOnly": false,
        "required": true,
        "transient": false,
        "type": "enum",
        "unique": false
      }
    },
    "description": "Represents Port Template object under a given gateway template object",
    "entityName": "PortTemplate",
    "package": "/gateway",
    "resourceName": "porttemplates"
  }
}