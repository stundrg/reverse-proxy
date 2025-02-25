from typing import Union

from fastapi import FastAPI

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
    N = 10**6  # 100만 개 요소

    # 랜덤한 1차원 배열 2개 생성

    # 실행 시간 측정 시작
    start_time = time.time()
    
    # 요소별 덧셈

    # 실행 시간 측정 종료
    end_time = time.time()
    
    # 수행 시간 리턴
    return {"execution_time": end_time - start_time}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}