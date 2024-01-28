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


@app.cell
def __():
    from datetime import datetime

    from pydantic import BaseModel, PositiveInt


    class Config(BaseModel):
        id: str
        model: str = "gpt-3.5-turbo"
        ts: datetime


    config = Config(id="test", model="gpt-4-beta", ts="2020-01-01T12:00")

    print(config.model)
    print(config.model_dump())
    return BaseModel, Config, PositiveInt, config, datetime


@app.cell
def __(mo):
    mo.md("You can then easily serialize the config, eg. to store in a file")
    return


@app.cell
def __(config):
    print(config.model_dump(exclude={"id"}, mode="json"))
    return


if __name__ == "__main__":
    app.run()
