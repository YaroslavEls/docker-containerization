from fastapi import APIRouter
import numpy as nump

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/matrix')
def get_matrix():
    matrix_a = nump.random.rand(10,10)
    matrix_b = nump.random.rand(10,10)
    product = nump.matmul(matrix_a, matrix_b)

    return {
        'matrix_a': matrix_a.tolist(),
        'matrix_b': matrix_b.tolist(),
        'product': product.tolist()
    }