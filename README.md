# PyMC with uv Environment

This repository demonstrates how to set up a fresh Python environment using [`uv`](https://github.com/astral-sh/uv) and run a simple [PyMC](https://www.pymc.io) example.

---

## 1. Create and Activate Environment

```bash
# Create a new virtual environment
uv venv .venv

# Activate the environment (macOS/Linux)
source .venv/bin/activate

# Activate on Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

---

## 2 Install Dependencies

`uv pip install pymc arviz`

---

## 3. Run model

```python
import pymc as pm
import arviz as az

# Define a simple Bayesian model: coin toss (Bernoulli with unknown bias)
with pm.Model() as model:
    p = pm.Beta("p", alpha=1, beta=1)        # prior
    y_obs = pm.Bernoulli("y_obs", p=p, observed=[1, 0, 1, 1, 0])  # data
    trace = pm.sample(1000, tune=1000, target_accept=0.9)

# Summarize results
print(az.summary(trace, var_names=["p"]))
```

---

## 4. Run the script

```bash
python simple_pymc_example.py
```
