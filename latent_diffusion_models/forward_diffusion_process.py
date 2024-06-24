"""
eps in N(0, I) and beta in (0, 1)

mu_sum = mu_1 + mu_2
var_sum = var_1 ** 2 + var_2 ** 2

mu(x_t) = mu(sqrt(1 - beta) * x_{t-1}) + mu(sqrt(beta) * eps)
= sqrt(1 - beta) * mu(x_{t-1}) + 0
= sqrt(1 - beta) * mu(x_{t_1})  # going to zero

var(x_t) = var(sqrt(1 - beta) * x_{t-1}) + var(sqrt(beta) * eps)
= (1 - beta) * var(x_{t-1}) + beta
= var(x_{t-1}) - beta * (var(x_{t-1}) - 1)  # going to one
"""

import cv2
import numpy as np

N = 10000
x_0 = cv2.imread("lenna.png")
beta = np.linspace(0.001, 0.02, num=N)

# forward diffusion process
x = x_0
for t in range(N):
    eps = np.random.normal(size=x.shape)
    x = np.sqrt(1 - beta[t]) * x + np.sqrt(beta[t]) * eps

    if t % 100 == 0:
        mean, std = x.mean(), x.std()
        print(f"step {t}\tmean {mean} and std {std}")
mean, std = x.mean(), x.std()
print(f"step {N}\tmean {mean} and std {std}")

# refined forward diffusion process
alpha = 1 - beta
alpha_ = np.cumprod(alpha)
x_t = np.sqrt(alpha_[t-1]) * x_0 + np.sqrt(1 - alpha_[t-1]) * eps
print(f"refined step {N}\tmean {x_t.mean()} and std {x_t.std()}")

"""
# N = 10000
...
step 8000       mean 0.0002637975335485851 and std 1.0002950200474168
step 8100       mean -0.00035737600438226404 and std 0.9994528901670551
step 8200       mean -0.0012679847031064357 and std 0.999763476894368
step 8300       mean -0.0024570908304876013 and std 0.9996399641456686
step 8400       mean -0.000698229805246329 and std 1.0004866051793722
step 8500       mean 0.0008774899446372116 and std 0.9987597014605069
step 8600       mean 3.0003066484134947e-05 and std 1.00115768880296
step 8700       mean 0.0009474937441675116 and std 1.000036669289246
step 8800       mean 0.0006836297334396028 and std 0.999451546276676
step 8900       mean 0.0013829474373023643 and std 1.0005261573439113
step 9000       mean 0.0012153259948235757 and std 0.9991613119558653
step 9100       mean 0.0011831843575671908 and std 1.0004257383688049
step 9200       mean 0.001535340327369819 and std 0.9989953677724945
step 9300       mean 0.001350682405427319 and std 0.9987519386984103
step 9400       mean -0.0007325928399936257 and std 1.0001411473303745
step 9500       mean -0.00041488909543047054 and std 0.9996451503945146
step 9600       mean 9.378755565377085e-05 and std 1.0000656925386051
step 9700       mean -1.2625541776070142e-05 and std 0.9993346378095607
step 9800       mean -0.0011585656150763061 and std 0.9995626464850328
step 9900       mean 0.0006413936111556502 and std 0.999258446676466
step 10000      mean 1.2480991860268043e-06 and std 0.9998746044566625
refined step 10000      mean -0.0010627958176740034 and std 1.000522106040768
"""
