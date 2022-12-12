migrate((db) => {
  const collection = new Collection({
    "id": "2mhl7x6lcxzwbfr",
    "created": "2022-12-12 02:11:04.227Z",
    "updated": "2022-12-12 02:11:04.227Z",
    "name": "example",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "cwvyvojp",
        "name": "title",
        "type": "text",
        "required": true,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "n4zia8qy",
        "name": "content",
        "type": "text",
        "required": true,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      }
    ],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("2mhl7x6lcxzwbfr");

  return dao.deleteCollection(collection);
})
