import marimo

__generated_with = "0.1.86"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md("Hello world 👋")
    return


@app.cell
def __():
    import torch

    x = torch.rand(5, 3)
    print(x)
    return torch, x


@app.cell
def __():
    import numpy as np

    np.arange(10)
    return np,


if __name__ == "__main__":
    app.run()
