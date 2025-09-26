import pymc as pm
import arviz as az

# Define a simple Bayesian model: coin toss (Bernoulli with unknown bias)
with pm.Model() as model:
    p = pm.Beta("p", alpha=1, beta=1)        # prior
    y_obs = pm.Bernoulli("y_obs", p=p, observed=[1, 0, 1, 1, 0])  # data
    trace = pm.sample(1000, tune=1000, target_accept=0.9)

# Summarize results
print(az.summary(trace, var_names=["p"]))

az.plot_posterior(trace, var_names=["p"])

# save the plot
import matplotlib.pyplot as plt
plt.savefig("posterior_plot.png")
plt.show()
# Save the trace for further analysis
az.to_netcdf(trace, "trace.nc")