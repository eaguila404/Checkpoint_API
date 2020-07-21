# Checkpoint_API


ENDPOINTS:



"/register",method = post, Register a new Checkpoint to the Network.
"/checkpoints", method = get, List all Checkpoints in the Network.
"/checkpoint/<guid>", method = get, Return a specific Checkpoint.
"/checkpoint/update/<guid>", method = put, Update the attributes of a specific Checkpoint.
"/checkpoint/delete/<guid>", method = delete, Delete a specific Checkpoint form the Network.
 
 "/report", method = post, Report a Checkpoint as Exposed.
 "/exposedcheckpoints", method = get, List all Exposed Checkpoints.
 "/exposedcheckpoint/<guid>", method = get, List a specific Exposed Checkpoint.
"/exposedcheckpoint/delete/<id>", method = delete, Delete a specific Exposed Checkpoint.
 
 
 
Database:
TABLE 1: CHECKPOINTS
guid, longitude, latitude

TABLE 2: EXPOSED_CHECKPOINTS
id, guid, epoch
 
