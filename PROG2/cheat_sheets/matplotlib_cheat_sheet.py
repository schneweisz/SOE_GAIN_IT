"""
=============================================================================
                MATPLOTLIB ULTIMATE CHEAT SHEET (Python script)
=============================================================================
Fusd meg blokkonkent (pl. Spyder/VSCode "Run Cell" #%% jelolessel), vagy
futtasd vegig egyben: minden fuggveny egy kulon abrat (figure-t) nyit meg
es plt.show() -val jeleniti meg / plt.close()-zal zar be, hogy ne szemetelje
tele a memoriat sok futtatas utan.

Tartalom:
  1. Alapok: import, egyszeru vonaldiagram
  2. Figure es Axes objektumok (OOP stilus vs pyplot stilus)
  3. Tobbfele diagram tipus (line, scatter, bar, hist, pie, boxplot, stem)
  4. Stilusok: szinek, vonaltipusok, markerek
  5. Cimek, tengelyfeliratok, legenda, racs
  6. Tobb subplot egy figuran (subplot, subplots, GridSpec)
  7. Ketto y-tengely (twinx)
  8. Annotaciok, szoveg az abran
  9. Tengelyek testreszabasa (limit, scale, ticks)
 10. Szineskodolt/3D plot, colorbar
 11. Kepek megjelenitese (imshow)
 12. Abra mentese fajlba
 13. Stilus sablonok (style sheets) es rcParams
 14. Animacio (alap pelda)
 15. Hibaval rendelkezo adatok (errorbar)
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D  # 3D plotokhoz szukseges (regisztralja a '3d' projekciot)

# -----------------------------------------------------------------------
# 1) ALAPOK: egyszeru vonaldiagram (pyplot / MATLAB-szeru interfesz)
# -----------------------------------------------------------------------
def scenario_01_basic_line():
    x = np.linspace(0, 10, 100)       # 100 pont 0 es 10 kozott
    y = np.sin(x)                     # szinusz fuggveny ertekei

    plt.figure()                      # uj abra (figure) letrehozasa
    plt.plot(x, y)                    # vonaldiagram rajzolasa
    plt.title("1) Egyszeru vonaldiagram - sin(x)")
    plt.xlabel("x ertek")
    plt.ylabel("sin(x)")
    plt.show()                        # abra megjelenitese


# -----------------------------------------------------------------------
# 2) FIGURE + AXES (objektum orientalt stilus) - AJANLOTT komplexebb esetben
# -----------------------------------------------------------------------
def scenario_02_oop_style():
    x = np.linspace(0, 10, 100)
    y = np.cos(x)

    fig, ax = plt.subplots()          # fig = a teljes abra, ax = a rajzterulet
    ax.plot(x, y, label="cos(x)")     # rajzolas az ax objektumra
    ax.set_title("2) OOP stilus - fig, ax = plt.subplots()")
    ax.set_xlabel("x")
    ax.set_ylabel("cos(x)")
    ax.legend()                       # legenda a label alapjan
    plt.show()


# -----------------------------------------------------------------------
# 3) TOBBFELE DIAGRAM TIPUS
# -----------------------------------------------------------------------
def scenario_03_plot_types():
    rng = np.random.default_rng(42)   # determinisztikus veletlenszam-generator

    # --- Scatter plot (pontdiagram) ---
    x = rng.normal(size=50)
    y = rng.normal(size=50)
    plt.figure()
    plt.scatter(x, y, c="tab:blue", alpha=0.7, edgecolors="black")
    plt.title("3a) Scatter plot")
    plt.show()

    # --- Bar chart (oszlopdiagram) ---
    kategoriak = ["A", "B", "C", "D"]
    ertekek = [23, 17, 35, 29]
    plt.figure()
    plt.bar(kategoriak, ertekek, color="tab:orange")
    plt.title("3b) Bar chart")
    plt.show()

    # --- Horizontalis bar ---
    plt.figure()
    plt.barh(kategoriak, ertekek, color="tab:green")
    plt.title("3c) Horizontal bar chart")
    plt.show()

    # --- Histogram (hisztogram) ---
    adatok = rng.normal(loc=0, scale=1, size=1000)
    plt.figure()
    plt.hist(adatok, bins=30, color="tab:purple", edgecolor="white")
    plt.title("3d) Histogram")
    plt.show()

    # --- Pie chart (kordiagram) ---
    plt.figure()
    plt.pie(ertekek, labels=kategoriak, autopct="%1.1f%%", startangle=90)
    plt.title("3e) Pie chart")
    plt.axis("equal")                 # kor alaku maradjon, ne ellipszis
    plt.show()

    # --- Boxplot (doboz diagram, eloszlas / kiugro ertekek) ---
    adat_csoportok = [rng.normal(0, 1, 100), rng.normal(1, 2, 100), rng.normal(-1, 0.5, 100)]
    plt.figure()
    plt.boxplot(adat_csoportok, tick_labels=["Csop1", "Csop2", "Csop3"])
    plt.title("3f) Boxplot")
    plt.show()

    # --- Stem plot (diszkret jelek abrazolasara) ---
    x = np.arange(0, 10)
    y = rng.integers(1, 10, size=10)
    plt.figure()
    plt.stem(x, y)
    plt.title("3g) Stem plot")
    plt.show()


# -----------------------------------------------------------------------
# 4) STILUSOK: szinek, vonaltipusok, markerek
# -----------------------------------------------------------------------
def scenario_04_styles():
    x = np.linspace(0, 10, 50)

    plt.figure()
    # forma: plt.plot(x, y, szin_stilus_marker, kwargs...)
    plt.plot(x, np.sin(x), "r--", label="piros szaggatott")          # r=red, --=dashed
    plt.plot(x, np.sin(x) + 1, "g-.", label="zold pont-vonal")        # g=green, -.=dashdot
    plt.plot(x, np.sin(x) + 2, "bo", label="kek pontok (marker)")     # b=blue, o=korok
    plt.plot(x, np.sin(x) + 3, color="#ff8800", linewidth=3, linestyle=":", label="egyedi hexa szin")
    plt.plot(x, np.sin(x) + 4, marker="^", markersize=8, markerfacecolor="yellow",
             markeredgecolor="black", linestyle="none", label="csak markerek")
    plt.title("4) Vonaltipusok, szinek, markerek")
    plt.legend(loc="upper right")     # legenda pozicioja
    plt.show()


# -----------------------------------------------------------------------
# 5) CIMEK, TENGELYFELIRATOK, LEGENDA, RACS
# -----------------------------------------------------------------------
def scenario_05_labels_grid():
    x = np.linspace(0, 2 * np.pi, 200)

    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), label="sin")
    ax.plot(x, np.cos(x), label="cos")

    ax.set_title("5) Cimek, racs, legenda", fontsize=14, fontweight="bold")
    ax.set_xlabel("x [radian]")
    ax.set_ylabel("f(x)")
    ax.legend(loc="best", frameon=True, shadow=True)   # legenda automatikus legjobb helyre
    ax.grid(True, linestyle="--", alpha=0.6)           # racs bekapcsolasa
    plt.show()


# -----------------------------------------------------------------------
# 6) TOBB SUBPLOT EGY FIGURAN
# -----------------------------------------------------------------------
def scenario_06_subplots():
    x = np.linspace(0, 10, 100)

    # --- 2x2-es racs subplotokkal ---
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))     # axs egy 2x2-es tomb az Axes objektumokbol
    axs[0, 0].plot(x, np.sin(x), color="tab:blue")
    axs[0, 0].set_title("sin(x)")

    axs[0, 1].plot(x, np.cos(x), color="tab:orange")
    axs[0, 1].set_title("cos(x)")

    axs[1, 0].plot(x, np.tan(x), color="tab:green")
    axs[1, 0].set_ylim(-5, 5)                          # tan-nal erdemes korlatozni az y tartomanyt
    axs[1, 0].set_title("tan(x)")

    axs[1, 1].hist(np.random.randn(500), bins=20, color="tab:red")
    axs[1, 1].set_title("Veletlen eloszlas")

    fig.suptitle("6a) 2x2 subplot racs", fontsize=16)
    fig.tight_layout(rect=[0, 0, 1, 0.96])             # elkeruli, hogy a cimek/feliratok atfedjek egymast
    plt.show()

    # --- GridSpec: egyenlotlen meretu subplotok ---
    fig = plt.figure(figsize=(10, 6))
    gs = fig.add_gridspec(2, 3)                        # 2 sor, 3 oszlop "logikai" racs
    ax1 = fig.add_subplot(gs[0, :])                    # felso sor: teljes szelesseg
    ax2 = fig.add_subplot(gs[1, 0])                    # also sor, bal
    ax3 = fig.add_subplot(gs[1, 1])                    # also sor, kozep
    ax4 = fig.add_subplot(gs[1, 2])                    # also sor, jobb

    ax1.plot(x, np.sin(x)); ax1.set_title("Teljes szelesseg")
    ax2.bar(["a", "b"], [3, 5])
    ax3.scatter(np.random.rand(20), np.random.rand(20))
    ax4.pie([1, 2, 3])

    fig.suptitle("6b) GridSpec egyenlotlen elrendezes")
    plt.tight_layout()
    plt.show()


# -----------------------------------------------------------------------
# 7) KETTO Y-TENGELY (masodik y skala, pl. eltero mertekegysegekhez)
# -----------------------------------------------------------------------
def scenario_07_twin_axes():
    x = np.linspace(0, 10, 100)
    y1 = np.exp(x / 5)          # gyorsan novekvo adatsor
    y2 = np.sin(x)              # -1..1 kozott ingadozo adatsor

    fig, ax1 = plt.subplots()

    color1 = "tab:red"
    ax1.set_xlabel("x")
    ax1.set_ylabel("exp(x/5)", color=color1)
    ax1.plot(x, y1, color=color1)
    ax1.tick_params(axis="y", labelcolor=color1)

    ax2 = ax1.twinx()            # masodik tengely, ugyanazt az x tengelyt hasznalja
    color2 = "tab:blue"
    ax2.set_ylabel("sin(x)", color=color2)
    ax2.plot(x, y2, color=color2)
    ax2.tick_params(axis="y", labelcolor=color2)

    fig.suptitle("7) Ketto y-tengely (twinx)")
    fig.tight_layout()
    plt.show()


# -----------------------------------------------------------------------
# 8) ANNOTACIOK, SZOVEG AZ ABRAN
# -----------------------------------------------------------------------
def scenario_08_annotations():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Egyszeru szoveg elhelyezese adott koordinatan
    ax.text(5, 0.5, "Ez egy szoveg", fontsize=10, color="green")

    # Nyillal ellatott annotacio egy adott pontra mutatva
    max_idx = np.argmax(y)
    ax.annotate(
        "Maximum",
        xy=(x[max_idx], y[max_idx]),          # ide mutat a nyil
        xytext=(x[max_idx] + 1, y[max_idx] - 0.5),  # a szoveg helye
        arrowprops=dict(facecolor="black", arrowstyle="->"),
    )

    ax.set_title("8) Annotaciok es szoveg")
    plt.show()


# -----------------------------------------------------------------------
# 9) TENGELYEK TESTRESZABASA (limit, scale, ticks)
# -----------------------------------------------------------------------
def scenario_09_axis_customization():
    x = np.linspace(1, 100, 100)
    y = x ** 2

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.plot(x, y)
    ax1.set_xlim(0, 50)             # x tengely tartomanya
    ax1.set_ylim(0, 2500)           # y tengely tartomanya
    ax1.set_title("9a) Egyedi tengely-tartomany")

    ax2.plot(x, y)
    ax2.set_yscale("log")           # logaritmikus skala (nagysagrendi valtozasokhoz)
    ax2.set_xticks([1, 20, 40, 60, 80, 100])          # egyedi tick pozíciók
    ax2.set_xticklabels(["1", "20", "40", "60", "80", "100"], rotation=45)
    ax2.set_title("9b) Log skala + egyedi tick-ek")

    plt.tight_layout()
    plt.show()


# -----------------------------------------------------------------------
# 10) SZINESKODOLT / 3D PLOT, COLORBAR
# -----------------------------------------------------------------------
def scenario_10_colormaps_3d():
    rng = np.random.default_rng(0)

    # --- Scatter szin szerint kodolva + colorbar ---
    x = rng.random(100)
    y = rng.random(100)
    szinek = rng.random(100)        # minden pont sajat szinerteket kap

    fig, ax = plt.subplots()
    sc = ax.scatter(x, y, c=szinek, cmap="viridis", s=80)
    fig.colorbar(sc, ax=ax, label="ertek")           # oldalso szinskala
    ax.set_title("10a) Scatter colormap-pel + colorbar")
    plt.show()

    # --- Egyszeru 3D felulet (surface plot) ---
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")            # 3D tengely
    X = np.linspace(-5, 5, 50)
    Y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(X, Y)                          # racs a ket dimenzioban
    Z = np.sin(np.sqrt(X**2 + Y**2))                  # magassag fuggveny

    surf = ax.plot_surface(X, Y, Z, cmap="plasma")
    fig.colorbar(surf, ax=ax, shrink=0.5)
    ax.set_title("10b) 3D surface plot")
    plt.show()


# -----------------------------------------------------------------------
# 11) KEPEK MEGJELENITESE (imshow) - pl. matrixok, heatmap
# -----------------------------------------------------------------------
def scenario_11_imshow_heatmap():
    rng = np.random.default_rng(1)
    matrix = rng.random((10, 10))       # 10x10-es veletlen matrix

    fig, ax = plt.subplots()
    im = ax.imshow(matrix, cmap="coolwarm")           # matrix megjelenitese szinekkel
    fig.colorbar(im, ax=ax)
    ax.set_title("11) Heatmap (imshow)")

    # Ertekek ratetele minden cellara
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(j, i, f"{matrix[i, j]:.1f}", ha="center", va="center",
                     color="black", fontsize=6)
    plt.show()


# -----------------------------------------------------------------------
# 12) ABRA MENTESE FAJLBA
# -----------------------------------------------------------------------
def scenario_12_saving():
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x))
    ax.set_title("12) Ez az abra fajlba lesz mentve")

    # dpi = felbontas, bbox_inches="tight" = levagja a felesleges fehér szeleket
    fig.savefig("matplotlib_pelda_abra.png", dpi=150, bbox_inches="tight")
    # Tovabbi tamogatott formatumok: .pdf, .svg, .jpg, .eps
    plt.show()
    plt.close(fig)   # memoria felszabaditasa (sok abra eseten hasznos)


# -----------------------------------------------------------------------
# 13) STILUS SABLONOK (style sheets) ES rcParams
# -----------------------------------------------------------------------
def scenario_13_style_sheets():
    print("Elerheto stilusok:", plt.style.available[:5], "...")

    x = np.linspace(0, 10, 100)

    with plt.style.context("ggplot"):        # ideiglenes stilus csak ezen a blokkon belul
        plt.figure()
        plt.plot(x, np.sin(x))
        plt.title("13a) 'ggplot' stilus")
        plt.show()

    # Globalis beallitasok kezi modositasa (rcParams)
    mpl.rcParams["lines.linewidth"] = 2
    mpl.rcParams["font.size"] = 12
    mpl.rcParams["axes.grid"] = True

    plt.figure()
    plt.plot(x, np.cos(x))
    plt.title("13b) Egyedi rcParams beallitasokkal")
    plt.show()

    mpl.rcdefaults()   # visszaallitas alapertelmezettre, hogy ne zavarja a tobbi peldat


# -----------------------------------------------------------------------
# 14) ANIMACIO (alap pelda FuncAnimation-nel)
# -----------------------------------------------------------------------
def scenario_14_animation():
    from matplotlib.animation import FuncAnimation

    fig, ax = plt.subplots()
    x = np.linspace(0, 2 * np.pi, 100)
    line, = ax.plot(x, np.sin(x))           # kezdeti vonal, a "," fontos: line objektumot ad vissza
    ax.set_title("14) Animacio pelda (mozgo szinusz)")

    def update(frame):
        line.set_ydata(np.sin(x + frame / 10))   # a gorbe eltolasa minden frame-ben
        return line,

    ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
    plt.show()
    # Mentes animaciohoz (pelda, ffmpeg vagy pillow szukseges):
    # ani.save("animacio.gif", writer="pillow", fps=20)


# -----------------------------------------------------------------------
# 15) HIBAVAL RENDELKEZO ADATOK (errorbar) - pl. meresi bizonytalansag
# -----------------------------------------------------------------------
def scenario_15_errorbar():
    x = np.arange(0, 10, 1)
    y = x ** 0.5
    hiba = 0.2 + 0.1 * np.sqrt(x)          # peldaul meresi hiba merteke

    fig, ax = plt.subplots()
    ax.errorbar(x, y, yerr=hiba, fmt="o-", capsize=4, ecolor="red", label="meres +- hiba")
    ax.set_title("15) Errorbar - hibaval rendelkezo meresek")
    ax.legend()
    plt.show()


# =========================================================================
# FUTTATAS: kommentezd ki/be az egyes szcenariokat kedved szerint
# =========================================================================
if __name__ == "__main__":
    scenario_01_basic_line()
    scenario_02_oop_style()
    scenario_03_plot_types()
    scenario_04_styles()
    scenario_05_labels_grid()
    scenario_06_subplots()
    scenario_07_twin_axes()
    scenario_08_annotations()
    scenario_09_axis_customization()
    scenario_10_colormaps_3d()
    scenario_11_imshow_heatmap()
    scenario_12_saving()
    scenario_13_style_sheets()
    scenario_14_animation()
    scenario_15_errorbar()
