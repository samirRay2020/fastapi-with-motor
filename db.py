from fastapi.exceptions import RequestErrorModel
from model import Task
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
db = client.todoDB #database name
col = db.todo  #collection name

#operations for all todos
async def fetch_all_todos():
    todos = []
    cursor  = col.find({})
    async for doc in cursor:
        todos.append(Task(**doc))
    return todos  

async def delete_all_todos():
    cursor = col.find({})
    async for doc in cursor:
        docTask = Task(**doc)
        await col.delete_one({"details":docTask.details})
    return True   

#operations on for specific todos
async def create_one(todo,taskNum):
    cursor = await col.find_one({'tasknumber':taskNum})
    if cursor:
        return False
    else:    
        document = todo
        result = await col.insert_one(document)
        return document

async def fetch_one_todo(taskNum):
    cursor = await col.find_one({"tasknumber":taskNum})
    return cursor

async def update_one_todo(taskNum,field,description):
    await col.update_one({"tasknumber": taskNum}, {"$set": {field: description}})
    document = await col.find_one({"tasknumber": taskNum})
    return document

async def delete_one_todo(taskNum):
    cursor = await col.find_one({'tasknumber':taskNum})
    if(cursor):
        await col.delete_one({"tasknumber":taskNum})
        return True
    else:
        return False    