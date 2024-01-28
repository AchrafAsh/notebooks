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


if __name__ == "__main__":
    app.run()
