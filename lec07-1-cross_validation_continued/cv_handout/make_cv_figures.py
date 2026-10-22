"""Generate the train / validation / test / holdout figures in this folder.

Run from anywhere:  python Lectures/lec07-1-cross_validation_continued/cv_handout/make_cv_figures.py

Color = the job a chunk of data does (the same in every figure):
  blue   = training (fit the model)
  orange = validation (choose between models / hyperparameters by comparing
           a performance metric, e.g. RMSE or accuracy)
  green  = test (estimate that metric on new data, looked at once)
  gray (hatched, y = ?) = new data where y is unknown
  dark gray = data with known y, before it has been split
  dashed outline = holdout (validation + test): a category, not a role, so it
                   never gets a color of its own
"""

import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

OUT = Path(__file__).resolve().parent
PAGE = (11, 6.7)  # inches, for every slide (2200 x 1340 px at dpi=200)

TRAIN = "#2a78d6"
VAL = "#eb6834"
TEST = "#1baf7a"
NEW = "#c9c8c2"
GIVEN = "#6b6a65"   # known-y data before it has been split
INK = "#0b0b0b"
INK2 = "#52514e"
GRID = "#e4e3df"
TEST_TEXT = "#127a55"  # darker green: test-colored text stays readable on white

# Canonical one-line description of each role's job. Every slide that explains
# training / validation / test uses these (wrapped to fit), so edit them here.
DESC = {
    "train": "Used to fit the model's parameters",
    "val": "Used to choose between models' hyperparameters by comparing the metric",
    "test": "Used to generate an honest estimate of the metric on new data. Use only ONCE",
}


# Canonical definition of holdout, used on every slide that shows it
HOLDOUT = "any data NOT used to fit the model"


def wrap(role, width):
    return textwrap.fill(DESC[role], width)


plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 14,
    "axes.edgecolor": INK2,
    "axes.labelcolor": INK,
    "xtick.color": INK2,
    "ytick.color": INK2,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "savefig.facecolor": "white",
    "figure.facecolor": "white",
})


def save(fig, name):
    # slide number in the bottom right, taken from the file name: cv04-... -> 4
    slide = int(name[2:4])
    fig.text(0.99, 0.01, str(slide), ha="right", va="bottom", fontsize=14,
             color=INK2)
    fig.savefig(OUT / name, dpi=200)
    plt.close(fig)
    print("wrote", OUT / name)


def block(ax, x, y, w, h, color, label=None, hatch=None, text_color="white",
          fontsize=13, weight="bold"):
    """A rounded bar representing a chunk of rows."""
    ax.add_patch(FancyBboxPatch(
        (x + 0.01, y), w - 0.02, h, boxstyle="round,pad=0,rounding_size=0.06",
        facecolor=color, edgecolor="white", linewidth=2, hatch=hatch))
    if label:
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                color=text_color, fontsize=fontsize, weight=weight)


def holdout_box(ax, x0, y0, x1, y1, label=None, label_xy=None, ha="center",
                va="bottom", fontsize=13):
    """Dashed, unfilled outline grouping validation + test as "holdout".

    Holdout is a category, not a role, so it gets an outline rather than a
    colored block of its own. Used the same way on every slide."""
    ax.add_patch(FancyBboxPatch(
        (x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=0.1",
        facecolor="none", edgecolor=INK, linewidth=1.8, linestyle=(0, (5, 3)),
        clip_on=False, zorder=5))
    if label:
        ax.text(*label_xy, label, ha=ha, va=va, fontsize=fontsize,
                weight="bold", color=INK, linespacing=1.3, zorder=6)


def slide_title(fig, text):
    """Slide title: same place and size on every slide."""
    fig.text(0.018, 0.975, text, ha="left", va="top", fontsize=18,
             weight="bold", color=INK)


def blank_axes(xlim, ylim):
    """Every slide is the same page size, so the handouts print consistently."""
    fig, ax = plt.subplots(figsize=PAGE)
    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    return fig, ax


# ---------------------------------------------------------------------------
# 1, 3-4. The data, row by row, built up in three stages:
#   stage 1: what we're given (known y, unsplit) + new data (unknown y)
#   stage 2: lock the test set away
#   stage 3: split the rest into training and validation
# ---------------------------------------------------------------------------
DATA_STAGES = {
    1: dict(file="cv01-data_given.png", title="The Data We're Given",
            roles=[("Data we're\ngiven", GIVEN, 10)]),
    2: dict(file="cv03-data_test_split.png", title="Lock the Test Set Away",
            roles=[("Rest of\nthe data", GIVEN, 8), ("Test", TEST, 2)]),
    3: dict(file="cv04-data_roles.png",
            title="Split the Rest into Training & Validation",
            roles=[("Training", TRAIN, 6), ("Validation", VAL, 2), ("Test", TEST, 2)]),
}


def fig_data_roles(stage):
    rng = np.random.default_rng(293)
    roles = DATA_STAGES[stage]["roles"]
    n_new = 3
    cols = ["x1", "x2", "x3", "y"]
    cw, rh = 0.9, 0.42                 # cell width, row height
    gap_known_new = 0.9

    n_known = sum(n for _, _, n in roles)
    total_h = (n_known + n_new) * rh + gap_known_new
    fig, ax = blank_axes((-3.2, 4 * cw + 5.0), (-0.35, total_h + 1.8))
    slide_title(fig, DATA_STAGES[stage]["title"])

    # column headers
    for j, c in enumerate(cols):
        ax.text(j * cw + cw / 2, total_h + 0.2, c, ha="center", va="bottom",
                fontsize=15, weight="bold", color=INK)

    # draw values in a fixed order so the numbers don't change between runs
    known_vals = [[f"{rng.normal(0, 1):.1f}" if j < 3 else f"{rng.normal(5, 2):.1f}"
                   for j in range(4)] for _ in range(n_known)]
    new_vals = [[f"{rng.normal(0, 1):.1f}" for _ in range(3)] + ["?"]
                for _ in range(n_new)]

    # new data (y unknown) on top
    y = total_h
    new_top = y
    for row in new_vals:
        y -= rh
        for j, txt in enumerate(row):
            ax.add_patch(Rectangle((j * cw, y), cw, rh, facecolor=NEW,
                                   alpha=0.35 if j < 3 else 1.0,
                                   edgecolor="white", lw=1.5,
                                   hatch="//" if j == 3 else None))
            ax.text(j * cw + cw / 2, y + rh / 2, txt, ha="center",
                    va="center", fontsize=11 if j < 3 else 16,
                    color=INK, weight="bold" if j == 3 else "normal")
    new_bottom = y
    ax.text(-0.25, (new_bottom + new_top) / 2, "New data\n(the future)",
            ha="right", va="center", color=INK2, fontsize=15, weight="bold")

    # known-y data below
    y -= gap_known_new
    known_top = y
    role_spans = {}
    rows = iter(known_vals)
    for name, color, n in roles:
        top = y
        for _ in range(n):
            y -= rh
            for j, val in enumerate(next(rows)):
                ax.add_patch(Rectangle((j * cw, y), cw, rh, facecolor=color,
                                       alpha=0.18 if j < 3 else 0.9,
                                       edgecolor="white", lw=1.5))
                ax.text(j * cw + cw / 2, y + rh / 2, val, ha="center",
                        va="center", fontsize=11,
                        color=INK if j < 3 else "white",
                        weight="normal" if j < 3 else "bold")
        role_spans[name] = (y, top)
        ax.text(-0.25, (y + top) / 2, name, ha="right", va="center",
                color=color if name != "Test" else TEST_TEXT, fontsize=15,
                weight="bold")
    known_bottom = y

    # right-hand labels: test locked away / holdout outline, known/unknown y
    xr = 4 * cw + 0.25

    def vbracket(y0, y1, x, text, color, dx=0.15):
        ax.plot([x, x + dx, x + dx, x], [y1 - 0.03, y1 - 0.03, y0 + 0.03, y0 + 0.03],
                color=color, lw=1.8)
        ax.text(x + dx + 0.12, (y0 + y1) / 2, text, ha="left", va="center",
                color=color, fontsize=13, weight="bold")

    if stage == 2:
        vbracket(*role_spans["Test"], xr, "Locked away\nuntil the end", TEST_TEXT)
    if stage == 3:
        y0, y1 = role_spans["Test"][0], role_spans["Validation"][1]
        holdout_box(ax, -0.06, y0 - 0.06, 4 * cw + 0.06, y1 + 0.06,
                    "Holdout:\n" + textwrap.fill(HOLDOUT, 17), (xr, (y0 + y1) / 2),
                    ha="left", va="center")
    vbracket(known_bottom, known_top, xr + 2.9,
             "y known", INK2)
    vbracket(new_bottom, new_top, xr,
             "y unknown:\nwhat we actually\nwant to predict", INK2)

    save(fig, DATA_STAGES[stage]["file"])


# ---------------------------------------------------------------------------
# 2. Decision tree: which role does a chunk of data play?
# ---------------------------------------------------------------------------
def fig_decision_tree():
    fig, ax = blank_axes((-0.3, 10.3), (-0.4, 7.6))
    slide_title(fig, "Data Set Terminology & Purposes")
    ax.text(-0.2, 7.0, "Say you've chosen a metric/score to evaluate the performance "
            "of your model's predictions\n(e.g. RMSE, accuracy)",
            ha="left", va="top", fontsize=14, color=INK2, linespacing=1.4)

    def question(x, y, w, text):
        ax.add_patch(FancyBboxPatch(
            (x - w / 2, y - 0.45), w, 0.9,
            boxstyle="round,pad=0,rounding_size=0.12",
            facecolor="white", edgecolor=INK2, linewidth=1.8))
        ax.text(x, y, text, ha="center", va="center", fontsize=15,
                weight="bold", color=INK, linespacing=1.3)

    def leaf(x, y, color, text, job):
        block(ax, x - 1.0, y - 0.4, 2.0, 0.8, color, text, fontsize=15)
        ax.text(x, y - 0.6, job, ha="center", va="top", fontsize=12.5,
                color=INK2, linespacing=1.35)

    def edge(x0, y0, x1, y1, label):
        ax.annotate("", (x1, y1), (x0, y0),
                    arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1.8,
                                    shrinkA=0, shrinkB=0))
        ax.text((x0 + x1) / 2 + (-0.2 if x1 < x0 else 0.2),
                (y0 + y1) / 2, label, ha="right" if x1 < x0 else "left",
                va="center", fontsize=14, weight="bold", color=INK2)

    q1, q2 = (3.6, 5.6), (6.6, 3.5)
    l_train, l_val, l_test = (1.3, 3.5), (5.0, 1.6), (8.2, 1.6)
    question(*q1, 4.0, "Was data used to fit the model?")
    question(*q2, 4.4, "Did its result change\na modeling decision?")
    leaf(*l_train, TRAIN, "Training Data", wrap("train", 40))
    leaf(*l_val, VAL, "Validation Data", wrap("val", 24))
    leaf(*l_test, TEST, "Test Data", wrap("test", 28))
    edge(q1[0] - 0.8, q1[1] - 0.45, l_train[0], l_train[1] + 0.4, "Yes")
    edge(q1[0] + 0.8, q1[1] - 0.45, q2[0], q2[1] + 0.45, "No")
    edge(q2[0] - 0.8, q2[1] - 0.45, l_val[0], l_val[1] + 0.4, "Yes")
    edge(q2[0] + 0.8, q2[1] - 0.45, l_test[0], l_test[1] + 0.4, "No")
    # holdout = everything down the "No" branch
    holdout_box(ax, 3.0, -0.3, 9.95, 4.2, "Holdout Data", (3.0, 4.28),
                ha="left", va="bottom", fontsize=15)
    ax.text(9.95, 4.28, textwrap.fill(f"Holdout Data = {HOLDOUT}", 25),
            ha="right", va="bottom", fontsize=13, color=INK2, style="italic",
            linespacing=1.35)
    save(fig, "cv02-which_role.png")


# ---------------------------------------------------------------------------
# 5-6. Overlay + reveal pair, drawn on the same fixed canvas:
#   5: "holdout" is the category; validation and test are the two jobs
#   6: same top bar (validation set approach), 5-fold CV revealed beneath
# ---------------------------------------------------------------------------
def fig_holdout_and_cv(reveal):
    k = 5
    x_val, x_test = 5.2, 7.6           # where validation and test start
    fig, ax = blank_axes((-2.7, 10.2), (0.3, 9.95))

    # shared top: the validation set approach
    y_top = 7.7
    slide_title(fig, "Validation set approach: Split once → Get 1 score per model")
    block(ax, 0, y_top, x_val, 0.8, TRAIN, "Training")
    block(ax, x_val, y_top, x_test - x_val, 0.8, VAL, "Validation")
    block(ax, x_test, y_top, 10 - x_test, 0.8, TEST, "Test")
    holdout_box(ax, x_val - 0.06, y_top - 0.1, 10.06, y_top + 0.9,
                f"Holdout: {HOLDOUT}", (10.06, y_top + 1.0), ha="right")

    if not reveal:
        for xc, role, width in [(x_val / 2, "train", 40),
                                ((x_val + x_test) / 2, "val", 20),
                                ((x_test + 10) / 2, "test", 20)]:
            ax.text(xc, y_top - 0.3, wrap(role, width), ha="center",
                    va="top", fontsize=11.5, color=INK2, linespacing=1.3)
        save(fig, "cv05-holdout_umbrella.png")
        return

    # revealed beneath: k-fold CV on the non-test part
    ax.text(-2.6, 6.7, f"{k}-fold cross-validation: Rotate the validation fold "
            f"→ Get {k} scores per model, average them",
            ha="left", va="center", fontsize=15, weight="bold", color=INK)
    fw = x_test / k
    for r in range(k):
        y = 5.55 - r * 0.92
        for f in range(k):
            is_val = f == r
            block(ax, f * fw, y, fw, 0.68, VAL if is_val else TRAIN,
                  "Validation" if is_val else "Training", fontsize=11,
                  weight="bold" if is_val else "normal")
        block(ax, x_test, y, 10 - x_test, 0.68, TEST, "Test", fontsize=11)
        ax.text(-0.2, y + 0.34, f"Round {r + 1}  → score {r + 1}", ha="right",
                va="center", fontsize=12, color=INK2)
    save(fig, "cv06-validation_set_vs_kfold.png")


# ---------------------------------------------------------------------------
# 7. Full workflow, ending with predictions on data where y is unknown
# ---------------------------------------------------------------------------
def fig_workflow():
    fig, ax = blank_axes((-6.6, 14.3), (-0.4, 11.4))
    slide_title(fig, "Overall Workflow")

    def step_label(y, num, title, sub):
        ax.text(-6.5, y + 0.55, f"{num}. {title}", ha="left", va="center",
                fontsize=13, weight="bold", color=INK)
        ax.text(-6.5, y + 0.32, sub, ha="left", va="top", fontsize=10.5,
                color=INK2, linespacing=1.3)

    # step 1: set test aside
    y = 8.6
    step_label(y, 1, "Lock the test set away", "before looking at anything")
    block(ax, 0, y, 8, 0.75, GIVEN, "Rest of the data (known y)", fontsize=12)
    block(ax, 8, y, 2, 0.75, TEST, "Test", fontsize=12)

    # step 2: CV to choose
    y = 6.4
    step_label(y, 2, "Cross-validate on the rest", "pick the hyperparameter value with\nthe best CV metric (e.g. RMSE)")
    # all 5 folds, stacked to the same total height as the test box
    k, h_total = 5, 0.75
    fw, rh = 8 / k, h_total / k
    for r in range(k):
        yy = y + h_total - (r + 1) * rh
        for f in range(k):
            ax.add_patch(Rectangle((f * fw + 0.01, yy + 0.01), fw - 0.02, rh - 0.02,
                                   facecolor=VAL if f == r else TRAIN,
                                   edgecolor="none"))
    block(ax, 8, y, 2, 0.75, TEST, "Test", text_color="white", fontsize=12)
    ax.add_patch(Rectangle((8.01, y), 1.98, 0.75, facecolor="white", alpha=0.6,
                           edgecolor="none"))
    ax.text(10.3, y + 0.6, "→ Best\n    hyperparameter\n    value", ha="left", va="center",
            fontsize=12, weight="bold", color=INK, linespacing=1.2)
    ax.text(10.3, y - 0.25, "fold models are\nthrown away", ha="left",
            va="top", fontsize=10.5, color=INK2)

    # step 3: refit
    y = 4.1
    step_label(y, 3, "Refit the chosen model", "on ALL non-test data")
    block(ax, 0, y, 8, 0.75, TRAIN,
          "Training (everything but test)\nwith best hyperparameter value", fontsize=11.5)
    block(ax, 8, y, 2, 0.75, TEST, "Test", fontsize=12)
    ax.add_patch(Rectangle((8.01, y), 1.98, 0.75, facecolor="white", alpha=0.6,
                           edgecolor="none"))
    ax.text(10.3, y + 0.38, "→ final model", ha="left", va="center",
            fontsize=12, weight="bold", color=INK)

    # step 4: test once
    y = 2.1
    step_label(y, 4, "Unlock the test set ONCE", "honest estimate of the metric on new data")
    block(ax, 0, y, 8, 0.75, "#e9e8e4", "", text_color=INK2, fontsize=12)
    block(ax, 8, y, 2, 0.75, TEST, "Test", fontsize=12)
    ax.text(10.3, y + 0.38, r"→ $\widehat{\mathbf{RMSE}}$ = 2.3", ha="left", va="center",
            fontsize=12, weight="bold", color=INK)
    ax.text(4, y + 0.38, "no more changes to the model after this",
            ha="center", va="center", fontsize=11, color=INK2, style="italic")

    # step 5: predict new data
    y = 0.1
    step_label(y, 5, "Deploy: predict new data", "where y is truly unknown")
    block(ax, 0, y, 10, 0.75, NEW, "New data:  x known,  y = ?",
          text_color=INK, hatch="//", fontsize=12)
    ax.text(10.3, y + 0.38, "→ ŷ, expect\n    $\\widehat{\\mathbf{RMSE}}$ ≈ 2.3", ha="left",
            va="center", fontsize=12, weight="bold", color=INK)
    save(fig, "cv07-workflow.png")


# ---------------------------------------------------------------------------
# 8. Summary table: training vs validation vs test, with holdout spanning
# ---------------------------------------------------------------------------
ROLES_TABLE = [
    ("Used to fit the model?", ["Yes", "No", "No"]),
    ("Used to make modeling\ndecisions?\n(e.g. set hyperparameters)",
     ["No", "Yes", "No"]),
    ("When do we look\nat it?", ["Throughout\nfitting", "Repeatedly,\nwhile tuning",
                                 "Only ONCE,\nonly AFTER all\ndecisions are made"]),
    ("Purpose", [wrap("train", 24), wrap("val", 24), wrap("test", 23)]),
    ("Analogy", ["Homework\nproblems", "Practice\nexams", "The real\nfinal exam"]),
]


def fig_roles_table():
    x0, lw, cw = 0, 3.4, 2.7             # label column start/width, column width
    heights = [0.75, 1.25, 1.25, 1.6, 0.9]
    total = sum(heights)
    fig, ax = blank_axes((-0.1, lw + 3 * cw + 0.1), (-0.45, total + 2.5))
    slide_title(fig, "Summary: Training vs. Validation vs. Test")

    # header: colored role cells, with the holdout outline over validation + test
    y_head = total + 0.15
    for j, (name, color) in enumerate([("Training", TRAIN), ("Validation", VAL),
                                       ("Test", TEST)]):
        block(ax, lw + j * cw, y_head, cw, 0.75, color, name, fontsize=15)
    # holdout outline runs down the whole validation + test columns
    holdout_box(ax, lw + cw + 0.03, 0.02, lw + 3 * cw - 0.03, y_head + 0.85,
                f"Holdout: {HOLDOUT}",
                (lw + 2 * cw, y_head + 0.95), fontsize=14)

    # body rows
    y = total
    for i, ((label, cells), h) in enumerate(zip(ROLES_TABLE, heights)):
        y -= h
        if i % 2 == 0:
            ax.add_patch(Rectangle((x0, y), lw + 3 * cw, h, facecolor="#f3f2ef",
                                   edgecolor="none"))
        ax.text(x0 + 0.15, y + h / 2, label, ha="left", va="center",
                fontsize=13, weight="bold", color=INK, linespacing=1.3)
        for j, txt in enumerate(cells):
            big = txt in ("Yes", "No")
            ax.text(lw + j * cw + cw / 2, y + h / 2, txt, ha="center",
                    va="center", fontsize=16 if big else 13, linespacing=1.3,
                    weight="bold" if big else "normal",
                    color=INK if (big and txt == "Yes") or not big else INK2)
    # thin column separators
    for j in range(4):
        ax.plot([lw + j * cw] * 2, [0, total], color=GRID, lw=1.2)
    save(fig, "cv08-roles_table.png")


if __name__ == "__main__":
    for stage in DATA_STAGES:
        fig_data_roles(stage)
    fig_decision_tree()
    fig_holdout_and_cv(reveal=False)
    fig_holdout_and_cv(reveal=True)
    fig_workflow()
    fig_roles_table()
