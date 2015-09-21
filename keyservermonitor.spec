{
  "apis": {
    "children": {
      "/keyservermonitors/id/metadatas": {
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
      "/keyservermonitors/{id}/keyservermonitorencryptedseeds": {
        "RESTName": "keyservermonitorencryptedseed",
        "entityName": "KeyServerMonitorEncryptedSeed",
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
        "resourceName": "keyservermonitorencryptedseeds"
      },
      "/keyservermonitors/{id}/keyservermonitorencryptedseks": {
        "RESTName": "keyservermonitorencryptedsek",
        "entityName": "KeyServerMonitorEncryptedSEK",
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
        "resourceName": "keyservermonitorencryptedseks"
      },
      "/keyservermonitors/{id}/keyservermonitorseeds": {
        "RESTName": "keyservermonitorseed",
        "entityName": "KeyServerMonitorSeed",
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
        "resourceName": "keyservermonitorseeds"
      },
      "/keyservermonitors/{id}/keyservermonitorseks": {
        "RESTName": "keyservermonitorsek",
        "entityName": "KeyServerMonitorSEK",
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
        "resourceName": "keyservermonitorseks"
      }
    },
    "parents": {
      "/enterprises/{id}/keyservermonitors": {
        "RESTName": "enterprise",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "enterprises"
      }
    },
    "self": {
      "/keyservermonitors/{id}": {
        "RESTName": "keyservermonitor",
        "operations": [
          {
            "availability": null,
            "method": "PUT"
          },
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "keyservermonitors"
      }
    }
  },
  "model": {
    "RESTName": "keyservermonitor",
    "attributes": {
      "enterpriseSecuredDataRecordCount": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Total number of Enterprise Secured Data records",
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
        "type": "long",
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
      "gatewaySecuredDataRecordCount": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Total number of Gateway Secured Data records",
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
        "type": "long",
        "unique": false
      },
      "keyserverMonitorEncryptedSEKCount": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Total number of Keyserver Monitor Encrypted SEK records",
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
        "type": "long",
        "unique": false
      },
      "keyserverMonitorEncryptedSeedCount": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Total number of Keyserver Monitor Encrypted Seed records",
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
        "type": "long",
        "unique": false
      },
      "keyserverMonitorSEKCount": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Total number of Keyserver Monitor SEK records",
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
        "type": "long",
        "unique": false
      },
      "keyserverMonitorSeedCount": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Total number of Keyserver Monitor Seed records",
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
        "type": "long",
        "unique": false
      },
      "lastUpdateTime": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "The time the latest SEK or Seed was created/removed (milliseconds since epoch)",
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
        "type": "long",
        "unique": false
      }
    },
    "description": "Represents a Keyserver Monitor Snapshot",
    "entityName": "KeyServerMonitor",
    "package": "/keyserver",
    "resourceName": "keyservermonitors"
  }
}