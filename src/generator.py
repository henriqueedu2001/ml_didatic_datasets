import numpy as np

class Generator:
    def generate_uniform_dist(dataset_size: int, min_value: float, max_value: float) -> np.array:
        """Gera uma distribuição uniforme no intervalo (a,b)

        Args:
            dataset_size (int): quantidade de pontos do dataset
            min_value (float): valor mínimo da distribuição
            max_value (float): valor máximo da distribuição

        Returns:
            _type_: _description_
        """
        # geranção de n=dataset_size valores no intervalo [0,1)
        dataset = np.random.random(dataset_size)
        
        # transformação linear de [0,1) até [a, b)
        dataset = min_value + (max_value - min_value)*dataset
        
        return dataset