import marimo

__generated_with = "0.1.86"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Design Patterns

        > https://refactoring.guru/design-patterns/python
        > https://python-patterns.guide

        - [ ] Creational Patterns
            - [ ] Factory
            - [ ] Builder
            - [ ] Prototype
            - [ ] Singleton
        - [ ] Structural Patterns
            - [ ] Adapter
            - [ ] Bridge
            - [ ] Decorator
            - [ ] Composite
            - [ ] Proxy
            - [ ] Facade
        - [ ] Behavioral Patterns
            - [ ] Iterator
            - [ ] Command
            - [ ] State
            - [ ] Observer
            - [ ] 
        """
    )
    return


@app.cell
def __():
    atoms = {"H": 1.008, "He": 4.003, "Li": 6.94}

    # Bad
    for symbol in atoms.keys():
        weight = atoms[symbol]

    # Good
    for symbol, weight in atoms.items():
        print(symbol, weight)
    return atoms, symbol, weight


@app.cell
def __(atoms):
    [symbol for symbol, weight in atoms.items() if weight > 5]
    {symbol for symbol, weight in atoms.items() if weight > 5}
    {symbol: weight for symbol, weight in atoms.items() if weight > 5}
    list(symbol for symbol, weight in atoms.items() if weight > 5)
    return


@app.cell
def __(atoms):
    it = iter(atoms)
    print(next(it))
    print(next(it))
    return it,


@app.cell
def __(it):
    while True:
        try:
            atom = next(it)
        except StopIteration:
            break
        else:
            print(atom)
    return atom,


@app.cell
def __():
    class OddNumbers(object):
        "An iterable object over odd numbers"

        def __init__(self, max: int):
            self.max = max

        def __iter__(self):
            return OddIterator(self)


    class OddIterator(object):
        def __init__(self, container: OddNumbers):
            self.container = container
            self.n = -1

        def __next__(self):
            self.n += 2
            if self.n > self.container.max:
                raise StopIteration
            return self.n

        def __iter__(self):
            return self
    return OddIterator, OddNumbers


@app.cell
def __(OddNumbers):
    odd_nums = OddNumbers(8)
    for n in odd_nums:
        print(n)
    return n, odd_nums


if __name__ == "__main__":
    app.run()
