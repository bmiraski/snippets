"""Solve Byte 117."""

import pandas as pd

movies = pd.read_excel('data/movies.xlsx', header=7, usecols='C:D')

genres = movies.genres.str.split('|', expand=True)
genres.columns = ['genre1', 'genre2', 'genre3', 'genre4', 'genre5', 'genre6']

movies_expand = pd.concat([movies.movie, genres], axis=1)
movies_expand = movies_expand.set_index('movie').stack()
movies_expand = movies_expand.reset_index()
movies_expand = movies_expand.drop('level_1', axis=1)
movies_expand.columns = ['movie', 'genre']

has_genre = movies_expand['genre'] != '(no genres listed)'
movies_tidy = movies_expand[has_genre].copy()

genre_gb = movies_tidy.groupby('genre')['movie'].size().sort_values(
    ascending=False)
print(genre_gb)
