# Movie Rating Analysis
This project analyzes movie ratings data from 1,097 participants evaluating 400 movies. The analysis uses non-parametric statistical methods to examine how various factors influence viewer ratings, including movie popularity, release dates, viewer demographics, and franchise membership.

## Analysis Components

### Popularity and Rating Patterns

Movies were categorized into high and low popularity groups using a median split based on the number of ratings received. Analysis using a one-tailed Mann-Whitney U test revealed that more popular movies receive significantly higher ratings (U = 1,242,808,144.5, p < 0.000001). High popularity group (n = 90,214, mean = 2.9235) received significantly higher ratings than low popularity group (n = 22,000, mean = 2.4506).

### Temporal Trends

Release years were extracted from movie titles and movies were divided into newer and older groups using a median split (median year = 1999). A two-tailed Mann-Whitney U test showed statistically significant differences between newer and older movies (U = 1,553,577,699.0, p = 1.284922 × 10⁻⁶). Newer movies (n = 65,690, mean = 2.8438) and older movies (n = 46,524, mean = 2.8123) showed differences, though the effect size is relatively small.

### Gender-Based Rating Differences

Analysis of gender differences in movie ratings revealed that 12.5% of movies (50 out of 400) exhibit statistically significant gender-based rating differences (p ≤ 0.005). For individual movies like Shrek (2001), no significant gender difference was found at α = 0.005 (U = 96,830.5, p = 0.0505), with female viewers (n = 743, mean = 3.1555) and male viewers (n = 241, mean = 3.0830) showing similar ratings.

### Family Structure Effects

Analysis of only-child status effects showed that only 1.75% of movies (7 out of 400) exhibit statistically significant differences between only children and those with siblings. For The Lion King (1994), no significant difference was found (U = 52,929.0, p = 0.9784), with only children (n = 151, mean = 3.3477) and people with siblings (n = 776, mean = 3.4820) showing similar ratings.

### Viewing Context Effects

Analysis of social versus solo viewing preferences revealed that 1.5% of movies (6 out of 400) demonstrate statistically significant social watching effects. For The Wolf of Wall Street (2013), no significant difference was found (U = 49,303.5, p = 0.9437), with social viewers (n = 270, mean = 3.0333) and solo viewers (n = 393, mean = 3.1438) showing similar ratings.

### Distribution Comparisons

A two-sample Kolmogorov-Smirnov test comparing Home Alone (1990) and Finding Nemo (2003) revealed significantly different rating distributions (KS statistic = 0.153, p = 6.379397 × 10⁻¹⁰). Home Alone: n = 857, mean = 3.1301; Finding Nemo: n = 1,014, mean = 3.3881.

### Franchise Quality Consistency

Analysis of 8 major franchises (Star Wars, Harry Potter, The Matrix, Indiana Jones, Jurassic Park, Pirates of the Caribbean, Toy Story, Batman) using Kruskal-Wallis tests revealed that 87.5% of franchises (7 out of 8) exhibit inconsistent quality across their movies. Harry Potter (p = 0.3433) was the sole franchise showing rating consistency. All other franchises showed statistically significant rating differences across their movies (p ≤ 0.005).

### Decade-Based Analysis

Movies from the 1990s and 2000s were compared using a two-tailed Mann-Whitney U test. Results showed that movies from the 1990s (n = 33,055, mean = 2.8842) are rated significantly differently than those from the 2000s (n = 44,034, mean = 2.8205), with a mean difference of 0.0637 (U = 756,760,247.0, p = 6.073044 × 10⁻²²).
## Methodology

### Statistical Tests

- **Mann-Whitney U Test**: Non-parametric test for comparing two independent groups, used for one-tailed and two-tailed comparisons
- **Kolmogorov-Smirnov Test**: Non-parametric test for comparing complete distributions between two groups
- **Kruskal-Wallis Test**: Non-parametric alternative to one-way ANOVA for comparing multiple groups

### Significance Level

All tests used α = 0.005 as the significance threshold to control for multiple comparisons and reduce false positives.
### Data Processing

- Median splits were used to create comparison groups for popularity and release year analyses
- Non-responses (coded as −1) were excluded from relevant analyses
- Gender categories: female = 1, male = 2; self-described (3) excluded
- Only child status: only child = 1, has siblings = 0
- Viewing preference: social viewing = 0, solo viewing = 1
## Project Structure

```
.
├── movie_rating_analysis.py  # Main analysis script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .gitignore                # Git ignore rules
└── data/                     # Data directory
    └── movieReplicationSet.csv  # Movie ratings dataset
```
## Dataset Description

The dataset contains movie ratings from 1,097 research participants evaluating 400 movies. This dataset stems from a replication attempt of published research (Wallisch & Whritner, 2017).
### Movie Ratings
* Columns 1-400: Movie ratings (0 to 4 stars, with missing values)
* 400 movies total, including titles from major franchises
### Participant Demographics
* Column 475: Gender identity (1 = female, 2 = male, 3 = self-described)
* Column 476: Only child status (1 = yes, 0 = no, -1 = no response)
* Column 477: Viewing preference (1 = prefer watching alone, 0 = prefer social viewing, -1 = no response)
### Additional Data
* Columns 401-421: Sensation seeking behaviors (1-5 scale)
* Columns 422-464: Personality questions (1-5 scale)
* Columns 465-474: Movie experience ratings (1-5 scale)
