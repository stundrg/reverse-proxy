from typing import Union
from fastapi import FastAPI
import random
import time

app = FastAPI()


@app.get("/")
def read_root():
    a = [1 ,2 ,3 ,4]
    b = [5 ,6 ,7 ,8]
    
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    
    return {"Hello": result}
@app.get("/two-dimensional-array")
def two_dimensional_array():
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[i])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    # TODO

    return {"result": result}

@app.get("/add-large-arrays")
def add_large_arrays():
    N = 10**6  

    # 랜덤한 1차원 리스트 2개 생성
    a = [random.random() for _ in range(N)]
    b = [random.random() for _ in range(N)]

    start_time = time.time()
    
    # for 루프를 이용한 요소별 덧셈
    result = []
    for i in range(N):
        result.append(a[i] + b[i])

    end_time = time.time()
    
    return {"execution_time": end_time - start_time}

@app.get("/add-large-arrays_choice")
def add_large_arrays_choice():
    N = 10**6  
    start_creation_time = time.time()
    # 랜덤한 1차원 리스트 2개 생성
    a = [random.choice(range(0, 100)) for _ in range(N)]
    b = [random.choice(range(0, 100)) for _ in range(N)]

    add_start_time = time.time()
    
    # for 루프를 이용한 요소별 덧셈
    result = []
    for i in range(N):
        result.append(a[i] + b[i])

    add_end_time = time.time()
    end_creation_time = time.time()
    return {
        "execution_time": add_end_time - add_start_time,
        "array_creation_time": end_creation_time - start_creation_time}
    
    
    

# TODO = add_large_arrays 와 add_large_arrays_choice를 고차 함수를 이용해서 중복코드 제거
# step 1 
# def add_arrays(N, generate_random_array): 만듬
# return (array_creation_time,addtion_time) 리턴값임
# def generate_random_array_with_randint(N):
#     return list
# def generate_random_array_with_choice(N):
#     return list 두개를 만듬 조합함

def add_arrays(N = 10**8, generate_random_array):
    
    start_creation_time = time.time()
    a = [random.choice(range(0, 100)) for _ in range(N)]
    b = [random.choice(range(0, 100)) for _ in range(N)]

    add_start_time = time.time()
    
    a = generate_random_array(N)
    b = generate_random_array(N)
    
    result = []
    for i in range(N):
        result.append(a[i] + b[i])

    add_end_time = time.time()
    end_creation_time = time.time()
    new_var = add_end_time - add_start_time
    return {
        "execution_time": new_var,
        "array_creation_time": end_creation_time - start_creation_time}

def generate_random_array_with_randint(N):
    return list

def generate_random_array_with_choice(N):
    return list
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}