import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

   
    matrix = np.array(numbers).reshape(3, 3)

   
    mean = [
        matrix.mean(axis=0).tolist(),
        matrix.mean(axis=1).tolist(),
        matrix.flatten().mean().tolist()
    ]
    
    variance = [
        matrix.var(axis=0).tolist(),
        matrix.var(axis=1).tolist(),
        matrix.flatten().var().tolist()
    ]
    
    standard_deviation = [
        matrix.std(axis=0).tolist(),
        matrix.std(axis=1).tolist(),
        matrix.flatten().std().tolist()
    ]
    
    max_values = [
        matrix.max(axis=0).tolist(),
        matrix.max(axis=1).tolist(),
        matrix.flatten().max().tolist()
    ]
    
    min_values = [
        matrix.min(axis=0).tolist(),
        matrix.min(axis=1).tolist(),
        matrix.flatten().min().tolist()
    ]
    
    sum_values = [
        matrix.sum(axis=0).tolist(),
        matrix.sum(axis=1).tolist(),
        matrix.flatten().sum().tolist()
    ]

    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': max_values,
        'min': min_values,
        'sum': sum_values
    }
