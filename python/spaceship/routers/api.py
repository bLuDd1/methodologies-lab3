from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World! My name is Dmytro'}

@router.get('/matrix')
def matrix() -> dict:
    matrix_a = np.random.rand(10, 10)
    matrix_b = np.random.rand(10, 10)

    result = np.dot(matrix_a, matrix_b)

    response = {
        "matrix_a": matrix_a.tolist(),
        "matrix_b": matrix_b.tolist(),
        "response": result.tolist()
    }

    return response