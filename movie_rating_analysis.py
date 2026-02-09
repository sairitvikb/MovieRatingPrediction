#  add project header and imports for analysis script

"""
Movie Rating Analysis
Statistical analysis of movie ratings data.
"""

import pandas as pd
import numpy as np
from scipy import stats
# load dataset from data/movieReplicationSet.csv


df = pd.read_csv('data/movieReplicationSet.csv')
#implement popularity vs rating statistical test

print("=" * 60)
print("Q1: Do movies with higher popularity receive higher ratings?")
print("=" * 60)

ratings_long = df.melt(id_vars=['Movie'], var_name='User', value_name='Rating')
ratings_long = ratings_long.dropna(subset=['Rating'])
movie_stats = ratings_long.groupby('Movie').agg(
    num_ratings=('Rating', 'count'),
    mean_rating=('Rating', 'mean')
).reset_index()

median_ratings = movie_stats['num_ratings'].median()
movie_stats['popularity'] = np.where(movie_stats['num_ratings'] >= median_ratings, 'high', 'low')

high_pop = movie_stats[movie_stats['popularity'] == 'high']['Movie']
low_pop = movie_stats[movie_stats['popularity'] == 'low']['Movie']

high_pop_ratings = ratings_long[ratings_long['Movie'].isin(high_pop)]['Rating']
low_pop_ratings = ratings_long[ratings_long['Movie'].isin(low_pop)]['Rating']

u_stat, p_value = stats.mannwhitneyu(high_pop_ratings, low_pop_ratings, alternative='greater')

print(f"Mann-Whitney U test (one-tailed)")
print(f"U-statistic: {u_stat:,.1f}, p-value: {p_value:.2e}")
print(f"High popularity: n={len(high_pop_ratings):,}, mean={high_pop_ratings.mean():.4f}")
print(f"Low popularity: n={len(low_pop_ratings):,}, mean={low_pop_ratings.mean():.4f}")
print(f"Conclusion: {'Reject H0' if p_value < 0.005 else 'Fail to reject H0'} (alpha=0.005)")
#compare newer and older movie ratings

print("\n" + "=" * 60)
print("Q2: Are newer movies rated differently than older movies?")
print("=" * 60)

movie_years = movie_stats[['Movie']].copy()
movie_years['year'] = movie_years['Movie'].str.extract(r'\((\d{4})\)').astype(float)
median_year = movie_years['year'].median()
movie_years['era'] = np.where(movie_years['year'] >= median_year, 'new', 'old')

new_movies = movie_years[movie_years['era'] == 'new']['Movie']
old_movies = movie_years[movie_years['era'] == 'old']['Movie']

new_ratings = ratings_long[ratings_long['Movie'].isin(new_movies)]['Rating']
old_ratings = ratings_long[ratings_long['Movie'].isin(old_movies)]['Rating']

u_stat, p_value = stats.mannwhitneyu(new_ratings, old_ratings, alternative='two-sided')

print(f"Mann-Whitney U test (two-tailed)")
print(f"U-statistic: {u_stat:,.1f}, p-value: {p_value:.2e}")
print(f"New movies (>={median_year:.0f}): n={len(new_ratings):,}, mean={new_ratings.mean():.4f}")
print(f"Old movies (<{median_year:.0f}): n={len(old_ratings):,}, mean={old_ratings.mean():.4f}")
print(f"Conclusion: {'Reject H0' if p_value < 0.005 else 'Fail to reject H0'} (alpha=0.005)")
# compare Shrek ratings with similar movies

print("\n" + "=" * 60)
print("Q3: Is Shrek rated higher than other animated movies?")
print("=" * 60)

shrek_ratings = df['Shrek (2001)'].dropna()
comparison_movies = ['Finding Nemo (2003)', 'The Incredibles (2004)', "Pirates of the Caribbean: The Curse of the Black Pearl (2003)"]
available_movies = [m for m in comparison_movies if m in df.columns]
other_ratings = df[available_movies].values.flatten()
other_ratings = other_ratings[~np.isnan(other_ratings)]

u_stat, p_value = stats.mannwhitneyu(shrek_ratings, other_ratings, alternative='greater')

print(f"Mann-Whitney U test (one-tailed)")
print(f"U-statistic: {u_stat:,.1f}, p-value: {p_value:.2e}")
print(f"Shrek: n={len(shrek_ratings)}, mean={shrek_ratings.mean():.4f}")
print(f"Comparison movies: n={len(other_ratings)}, mean={other_ratings.mean():.4f}")
print(f"Conclusion: {'Reject H0' if p_value < 0.005 else 'Fail to reject H0'} (alpha=0.005)")
# analyze gender-based rating differences

print("\n" + "=" * 60)
print("Q4: Do male and female viewers rate movies differently?")
print("=" * 60)

gender_cols = [c for c in df.columns if 'gender' in c.lower()]
movie_cols = [c for c in df.columns if '(' in c and ')' in c]

if gender_cols:
    gender_col = gender_cols[0]
    male_ratings = df[df[gender_col] == 1][movie_cols].values.flatten()
    male_ratings = male_ratings[~np.isnan(male_ratings)]
    female_ratings = df[df[gender_col] == 2][movie_cols].values.flatten()
    female_ratings = female_ratings[~np.isnan(female_ratings)]
    
    u_stat, p_value = stats.mannwhitneyu(male_ratings, female_ratings, alternative='two-sided')
    
    print(f"Mann-Whitney U test (two-tailed)")
    print(f"U-statistic: {u_stat:,.1f}, p-value: {p_value:.2e}")
    print(f"Male viewers: n={len(male_ratings):,}, mean={male_ratings.mean():.4f}")
    print(f"Female viewers: n={len(female_ratings):,}, mean={female_ratings.mean():.4f}")
    print(f"Conclusion: {'Reject H0' if p_value < 0.005 else 'Fail to reject H0'} (alpha=0.005)")
#analyze only-child vs siblings rating differences

print("\n" + "=" * 60)
print("Q5: Do only children rate movies differently?")
print("=" * 60)

sibling_cols = [c for c in df.columns if 'sibling' in c.lower() or 'only' in c.lower()]
if sibling_cols:
    sibling_col = sibling_cols[0]
    only_child_ratings = df[df[sibling_col] == 1][movie_cols].values.flatten()
    only_child_ratings = only_child_ratings[~np.isnan(only_child_ratings)]
    has_sibling_ratings = df[df[sibling_col] == 0][movie_cols].values.flatten()
    has_sibling_ratings = has_sibling_ratings[~np.isnan(has_sibling_ratings)]
    
    u_stat, p_value = stats.mannwhitneyu(only_child_ratings, has_sibling_ratings, alternative='two-sided')
    
    print(f"Mann-Whitney U test (two-tailed)")
    print(f"U-statistic: {u_stat:,.1f}, p-value: {p_value:.2e}")
    print(f"Only children: n={len(only_child_ratings):,}, mean={only_child_ratings.mean():.4f}")
    print(f"Has siblings: n={len(has_sibling_ratings):,}, mean={has_sibling_ratings.mean():.4f}")
    print(f"Conclusion: {'Reject H0' if p_value < 0.005 else 'Fail to reject H0'} (alpha=0.005)")
#analyze social vs solo movie watching behavior

print("\n" + "=" * 60)
print("Q6: Do social viewers rate differently than solo viewers?")
print("=" * 60)

social_cols = [c for c in df.columns if 'movies with people' in c.lower() or 'social' in c.lower()]
if social_cols:
    social_col = social_cols[0]
    social_ratings = df[df[social_col] == 1][movie_cols].values.flatten()
    social_ratings = social_ratings[~np.isnan(social_ratings)]
    solo_ratings = df[df[social_col] == 0][movie_cols].values.flatten()
    solo_ratings = solo_ratings[~np.isnan(solo_ratings)]
    
    u_stat, p_value = stats.mannwhitneyu(social_ratings, solo_ratings, alternative='two-sided')
    
    print(f"Mann-Whitney U test (two-tailed)")
    print(f"U-statistic: {u_stat:,.1f}, p-value: {p_value:.2e}")
    print(f"Social viewers: n={len(social_ratings):,}, mean={social_ratings.mean():.4f}")
    print(f"Solo viewers: n={len(solo_ratings):,}, mean={solo_ratings.mean():.4f}")
    print(f"Conclusion: {'Reject H0' if p_value < 0.005 else 'Fail to reject H0'} (alpha=0.005)")
#analyze franchise sequel vs original ratings

print("\n" + "=" * 60)
print("Q7-Q11: Franchise Rating Comparisons")
print("=" * 60)

franchises = {
    'Star Wars': ['Star Wars: Episode IV - A New Hope (1977)', 'Star Wars: Episode V - The Empire Strikes Back (1980)', 'Star Wars: Episode VI - Return of the Jedi (1983)'],
    'Harry Potter': ['Harry Potter and the Sorcerer\'s Stone (2001)', 'Harry Potter and the Chamber of Secrets (2002)'],
    'Matrix': ['The Matrix (1999)', 'The Matrix Reloaded (2003)'],
    'Indiana Jones': ['Raiders of the Lost Ark (1981)', 'Indiana Jones and the Last Crusade (1989)'],
    'Jurassic Park': ['Jurassic Park (1993)', 'The Lost World: Jurassic Park (1997)']
}

for franchise, movies in franchises.items():
    available = [m for m in movies if m in df.columns]
    if len(available) >= 2:
        first_movie = df[available[0]].dropna()
        sequel_ratings = df[available[1:]].values.flatten()
        sequel_ratings = sequel_ratings[~np.isnan(sequel_ratings)]
        
        u_stat, p_value = stats.mannwhitneyu(first_movie, sequel_ratings, alternative='greater')
        
        print(f"\n{franchise}:")
        print(f"  First vs sequels: U={u_stat:,.0f}, p={p_value:.4f}")
        print(f"  First: mean={first_movie.mean():.3f}, Sequels: mean={sequel_ratings.mean():.3f}")
        print(f"  Result: {'First rated higher' if p_value < 0.005 else 'No significant difference'}")
# finalize analysis script and outputs

print("\n" + "=" * 60)
print("Analysis Complete")
print("=" * 60)
