import matplotlib.pyplot as plt

# -------------------------------
# GLOBAL STYLE (shared logic)
# -------------------------------
def _apply_style(title=None, xlabel=None, ylabel=None):
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.title(title, fontsize=14, fontweight="bold")
    plt.xlabel(xlabel, fontsize=11)
    plt.ylabel(ylabel, fontsize=11)
    plt.tight_layout()


# -------------------------------
# 1. Styled Line Plot
# -------------------------------
def styled_line(x, y, title="Line Plot", xlabel="X", ylabel="Y"):
    plt.figure()
    plt.plot(x, y, color="#1f77b4", linewidth=2)
    _apply_style(title, xlabel, ylabel)
    plt.show()


# -------------------------------
# 2. Styled Bar Plot
# -------------------------------
def styled_bar(x, y, title="Bar Plot", xlabel="Categories", ylabel="Values"):
    plt.figure()
    plt.bar(x, y, color="#ff7f0e")
    _apply_style(title, xlabel, ylabel)
    plt.show()


# -------------------------------
# 3. Styled Scatter Plot
# -------------------------------
def styled_scatter(x, y, title="Scatter Plot", xlabel="X", ylabel="Y"):
    plt.figure()
    plt.scatter(x, y, color="#2ca02c", s=80)
    _apply_style(title, xlabel, ylabel)
    plt.show()


# -------------------------------
# 4. Styled Histogram
# -------------------------------
def styled_hist(data, title="Histogram", xlabel="Value", ylabel="Frequency"):
    plt.figure()
    plt.hist(data, bins=10, color="#9467bd", edgecolor="black")
    _apply_style(title, xlabel, ylabel)
    plt.show()


# -------------------------------
# 5. Styled Box Plot
# -------------------------------
def styled_box(data, title="Box Plot", ylabel="Value"):
    plt.figure()
    plt.boxplot(data)
    _apply_style(title, None, ylabel)
    plt.show()
