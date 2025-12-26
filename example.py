import isshaghvizlib as myvizlib

myvizlib.styled_line(
    x=[1, 2, 3],
    y=[4, 2, 5],
    title="My styled plot"
)

myvizlib.styled_bar(
    x=["A", "B", "C"],
    y=[5, 3, 7]
)

myvizlib.styled_scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)

myvizlib.styled_hist(
    data=[1, 2, 2, 3, 3, 3, 4, 5]
)

myvizlib.styled_box(
    data=[1, 2, 3, 4, 5, 6]
)
