# =====================================================================
# D3 Discussion #3 - Item #1
# Data Visualization in Python: U.S. Vice Presidents by Age
# Source: Wikipedia, "List of vice presidents of the United States by age"
# https://en.wikipedia.org/wiki/List_of_vice_presidents_of_the_United_States_by_age
#
# HOW TO USE IN GOOGLE COLAB:
# Paste each "CELL" section below into its own code cell (or paste the
# whole thing into one cell - it will still run top to bottom). No file
# upload is needed; the data is embedded as a CSV string in Cell 1.
# =====================================================================

# --------------------------- CELL 1 -----------------------------------
# Load the data and compute age at start of term
import io
import pandas as pd

vp_csv = """number,name,birth_date,death_date,term_start,term_end
1,John Adams,1735-10-30,1826-07-04,1789-04-21,1797-03-04
2,Thomas Jefferson,1743-04-13,1826-07-04,1797-03-04,1801-03-04
3,Aaron Burr,1756-02-06,1836-09-14,1801-03-04,1805-03-04
4,George Clinton,1739-07-26,1812-04-20,1805-03-04,1812-04-20
5,Elbridge Gerry,1744-07-17,1814-11-23,1813-03-04,1814-11-23
6,Daniel D. Tompkins,1774-06-21,1825-06-11,1817-03-04,1825-03-04
7,John C. Calhoun,1782-03-18,1850-03-31,1825-03-04,1832-12-28
8,Martin Van Buren,1782-12-05,1862-07-24,1833-03-04,1837-03-04
9,Richard M. Johnson,1780-10-17,1850-11-19,1837-03-04,1841-03-04
10,John Tyler,1790-03-29,1862-01-18,1841-03-04,1841-04-04
11,George M. Dallas,1792-07-10,1864-12-31,1845-03-04,1849-03-04
12,Millard Fillmore,1800-01-07,1874-03-08,1849-03-04,1850-07-09
13,William R. King,1786-04-07,1853-04-18,1853-03-04,1853-04-18
14,John C. Breckinridge,1821-01-16,1875-05-17,1857-03-04,1861-03-04
15,Hannibal Hamlin,1809-08-27,1891-07-04,1861-03-04,1865-03-04
16,Andrew Johnson,1808-12-29,1875-07-31,1865-03-04,1865-04-15
17,Schuyler Colfax,1823-03-23,1885-01-13,1869-03-04,1873-03-04
18,Henry Wilson,1812-02-16,1875-11-22,1873-03-04,1875-11-22
19,William A. Wheeler,1819-06-30,1887-06-04,1877-03-04,1881-03-04
20,Chester A. Arthur,1829-10-05,1886-11-18,1881-03-04,1881-09-19
21,Thomas A. Hendricks,1819-09-07,1885-11-25,1885-03-04,1885-11-25
22,Levi P. Morton,1824-05-16,1920-05-16,1889-03-04,1893-03-04
23,Adlai E. Stevenson,1835-10-23,1914-06-14,1893-03-04,1897-03-04
24,Garret A. Hobart,1844-06-03,1899-11-21,1897-03-04,1899-11-21
25,Theodore Roosevelt,1858-10-27,1919-01-06,1901-03-04,1901-09-14
26,Charles W. Fairbanks,1852-05-11,1918-06-04,1905-03-04,1909-03-04
27,James S. Sherman,1855-10-24,1912-10-30,1909-03-04,1912-10-30
28,Thomas R. Marshall,1854-03-14,1925-06-01,1913-03-04,1921-03-04
29,Calvin Coolidge,1872-07-04,1933-01-05,1921-03-04,1923-08-02
30,Charles G. Dawes,1865-08-27,1951-04-23,1925-03-04,1929-03-04
31,Charles Curtis,1860-01-25,1936-02-08,1929-03-04,1933-03-04
32,John Nance Garner,1868-11-22,1967-11-07,1933-03-04,1941-01-20
33,Henry A. Wallace,1888-10-07,1965-11-18,1941-01-20,1945-01-20
34,Harry S. Truman,1884-05-08,1972-12-26,1945-01-20,1945-04-12
35,Alben W. Barkley,1877-11-24,1956-04-30,1949-01-20,1953-01-20
36,Richard Nixon,1913-01-09,1994-04-22,1953-01-20,1961-01-20
37,Lyndon B. Johnson,1908-08-27,1973-01-22,1961-01-20,1963-11-22
38,Hubert H. Humphrey,1911-05-27,1978-01-13,1965-01-20,1969-01-20
39,Spiro T. Agnew,1918-11-09,1996-09-17,1969-01-20,1973-10-10
40,Gerald R. Ford,1913-07-14,2006-12-26,1973-12-06,1974-08-09
41,Nelson A. Rockefeller,1908-07-08,1979-01-26,1974-12-19,1977-01-20
42,Walter F. Mondale,1928-01-05,2021-04-19,1977-01-20,1981-01-20
43,George H. W. Bush,1924-06-12,2018-11-30,1981-01-20,1989-01-20
44,J. Danforth Quayle,1947-02-04,,1989-01-20,1993-01-20
45,Albert Gore Jr.,1948-03-31,,1993-01-20,2001-01-20
46,Richard B. Cheney,1941-01-30,,2001-01-20,2009-01-20
47,Joseph R. Biden Jr.,1942-11-20,,2009-01-20,2017-01-20
48,Michael R. Pence,1959-06-07,,2017-01-20,2021-01-20
49,Kamala D. Harris,1964-10-20,,2021-01-20,2025-01-20
50,J.D. Vance,1984-08-02,,2025-01-20,
"""

df = pd.read_csv(io.StringIO(vp_csv),
                  parse_dates=["birth_date", "death_date", "term_start", "term_end"])

def age_in_years(start, end):
    return (end - start).days / 365.25

df["age_at_start"] = df.apply(lambda r: age_in_years(r["birth_date"], r["term_start"]), axis=1)
df["term_start_year"] = df["term_start"].dt.year

print(df[["number", "name", "term_start_year", "age_at_start"]].round(1).to_string(index=False))
print()
print(df["age_at_start"].describe().round(1))


# --------------------------- CELL 2 -----------------------------------
# Visualization 1: bar chart of age at start of term, chronological order
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")

BLUE = "#2E6F95"
GOLD = "#D9822B"

colors_ = [BLUE] * len(df)
idx_min = df["age_at_start"].idxmin()
idx_max = df["age_at_start"].idxmax()
colors_[idx_min] = GOLD
colors_[idx_max] = GOLD

fig, ax = plt.subplots(figsize=(13, 6))
ax.bar(df["number"], df["age_at_start"], color=colors_, width=0.75)

mean_age = df["age_at_start"].mean()
ax.axhline(mean_age, color="#555555", linewidth=1.2, linestyle="--", zorder=0)
ax.text(48.7, mean_age + 2.2, f"Mean = {mean_age:.1f} yrs", va="bottom", ha="right",
        fontsize=10, color="#555555",
        bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1))

bbox_kw = dict(facecolor="white", edgecolor="#7a4a00", alpha=0.92, boxstyle="round,pad=0.3")

ax.annotate(f"Youngest: {df.loc[idx_min,'name']}\n({df.loc[idx_min,'age_at_start']:.1f} yrs, {df.loc[idx_min,'term_start_year']})",
            xy=(df.loc[idx_min, "number"], df.loc[idx_min, "age_at_start"]),
            xytext=(df.loc[idx_min, "number"] + 2, df.loc[idx_min, "age_at_start"] + 14),
            fontsize=9, ha="left", va="bottom", color="#7a4a00", bbox=bbox_kw,
            arrowprops=dict(arrowstyle="->", color="#7a4a00", lw=1))

ax.annotate(f"Oldest: {df.loc[idx_max,'name']}\n({df.loc[idx_max,'age_at_start']:.1f} yrs, {df.loc[idx_max,'term_start_year']})",
            xy=(df.loc[idx_max, "number"], df.loc[idx_max, "age_at_start"]),
            xytext=(df.loc[idx_max, "number"] + 3, df.loc[idx_max, "age_at_start"] + 1),
            fontsize=9, ha="left", va="bottom", color="#7a4a00", bbox=bbox_kw,
            arrowprops=dict(arrowstyle="->", color="#7a4a00", lw=1))

ax.set_xlabel("Vice president (No. 1 = John Adams  ->  No. 50 = J.D. Vance, chronological)")
ax.set_ylabel("Age at start of term (years)")
ax.set_title("Age at Start of Vice Presidency, by Chronological Order (1789-2025)", fontsize=13, weight="bold")
ax.set_ylim(0, 85)
ax.set_xlim(-1, 55)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
plt.show()


# --------------------------- CELL 3 -----------------------------------
# Visualization 2: scatter + trend line - has age at inauguration drifted
# over time?
fig, ax = plt.subplots(figsize=(10, 6))
sns.regplot(
    data=df, x="term_start_year", y="age_at_start", ax=ax,
    scatter_kws=dict(color=BLUE, s=55, alpha=0.85, edgecolor="white"),
    line_kws=dict(color=GOLD, linewidth=2.5), ci=95,
)
ax.set_xlabel("Year vice presidency began")
ax.set_ylabel("Age at start of term (years)")
ax.set_title("Age at Inauguration Has Drifted Upward Over U.S. History", fontsize=13, weight="bold")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
plt.show()

print(f"Correlation (year vs. age): r = {df['term_start_year'].corr(df['age_at_start']):.3f}")
