from fastapi import FastAPI,HTTPException
from model import Task

app = FastAPI()

#all functions to be used
from db import(
    fetch_all_todos,
    create_one,delete_all_todos,
    fetch_one_todo,update_one_todo,
    delete_one_todo
    )


#for all tasks
@app.get("/fetch_all")
async def fetch_all_tasks():
    res = await fetch_all_todos()
    if res:
        return res
    raise HTTPException(400, "No todo found")   

@app.delete("/detele_all")
async def delete_all_tasks():
    res = await delete_all_todos()
    if res:
        return {"Successfully deleted all todos":"200"}
    raise HTTPException(400,"Todos not deleted") 

#for particular tasks
@app.post("/insert_one/{task_number}",response_model=Task)
async def insert_one(task_number:int,task:Task):
    res = await create_one(task.dict(),task_number)
    if res:
        return res
    raise HTTPException(404,"two tasks cannot have same number")    

@app.get("/get_one/{task_number}",response_model=Task)
async def fetch_one(task_number:int):
    res = await fetch_one_todo(task_number)
    if res:
        return res
    raise HTTPException(404,f"no todo found with task number as {task_number}")

@app.put("/update_one/{task_number}",response_model=Task)
async def update_one(task_number:int,field:str,description:str):
    res = await update_one_todo(task_number,field,description)
    if res:
        return res
    raise HTTPException(400,f"todo with number {task_number} is not updated")

@app.delete("/delete_one/{task_number}")
async def delete_one(task_number:int):
    res = await delete_one_todo(task_number)
    if res:
        return {"Successfully deleted":"200"}
    raise HTTPException(400,f"todo with number {task_number} not deleted") 


