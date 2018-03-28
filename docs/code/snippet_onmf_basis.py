import numpy as np

import nimfa

V = np.random.rand(40, 100)
onmf = nimfa.Onmf(V, seed="nndsvd", rank=10, max_iter=12, update='onmf_basis',
                objective='fro')
onmf_fit = onmf()
