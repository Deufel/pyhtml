import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        """
    # Working Title `pyhtml`

    This is mainly an educational project to see how a dev package looks in a marimo notebook. 

    > This work is *heavily* inspired by [mohtml](https://koaning.github.io/mohtml/) which is heavily inspired by [FastHTML](https://fastht.ml/).

    ## Installation

    ## Demo

    ```python
    # You can import any HTML element this way
    from mohtml import a, p, div, script, h1

    div(
        script(src="https://cdn.tailwindcss.com"),
        h1("welcome to my blog", klass="font-bold text-xl"),
        p("my name is vincent", klass="text-gray-500 text-sm"),
        a("please check my site", href="https://calmcode.io", klass="underline")
    )
    ```

    This code will generate the following HTML:
    """
    )
    return


@app.cell
def _(a, div, h1, p, script):
    myhtml = div(
        script(src="https://cdn.tailwindcss.com"),
        h1("welcome to my blog", klass="font-bold text-xl"),
        p("my name is vincent", klass="text-gray-500 text-sm"),
        a("please check my site", href="https://calmcode.io", klass="underline")
    )

    myhtml
    return (myhtml,)


@app.cell
def _(mo):
    mo.md(
        """
    Notice the syntax here. 

    1. Each function call represents an HTML element. 
    2. Each function call can define `**kwargs` which are passed unto the HTML element as you might expect. 
    3. You can add children to the elements via `*args`. Errors will be raised when you try to add children to elements that do not support that like `<br/>`.

    You can also render the HTML from Marimo directly, this is what it would look like:
    """
    )
    return


@app.cell
def _(mo, myhtml):
    mo.Html(f"{myhtml}")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Next Steps

     - Datastar specific add ons
     - Add ```<selectedContent>``` tag I Think that this is in cromium only so far..
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    from mohtml import a, div, p, h1, script, link
    return a, div, h1, mo, p, script


if __name__ == "__main__":
    app.run()
