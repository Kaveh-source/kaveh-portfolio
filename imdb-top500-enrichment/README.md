# IMDb Top 500 Movie Data Enrichment (Data Wrangling)

This folder contains my work from a graduate **data wrangling** project for a
movie streaming client. Starting from a movies dataset (2018–2020 releases),
I scraped additional information from **IMDb** and merged it to create an
enriched dataset for analysis.

The goal was to help the client better understand which movies perform well
(ratings, votes) and enrich their internal catalog for decision-making.

---

## My Role

- Used Python to **scrape IMDb** for the top 500 most-voted movies (2018–2020).
- Extracted: `movie_id`, rank, title, year, IMDb rating, number of votes.
- Cleaned and transformed the scraped data into a structured DataFrame and
  saved it as `IMDb_TopVoted.csv`.
- **Merged** the scraped IMDb data with the client dataset (`Movies.csv`) to
  create an enriched table including both internal and external attributes.
- Reordered and formatted fields to match the required final schema:
  `movie_id, rank, title, originalTitle, description, year, votes, rating,
  runtimeMinutes, ratingCategory, genres`.

---

## Data

- **Client dataset:** `Movies.csv` – internal catalog of movies (ID, title,
  originalTitle, description, ratingCategory, genres).
- **Scraped dataset:** IMDb movies (2018–2020) sorted by user votes, including:
  - Rank (by votes)
  - Title
  - Year
  - IMDb rating
  - Number of votes

> Note: The full raw data is not included here. You can substitute a smaller
> public or synthetic sample with the same column structure if you want to
> reproduce the workflow.

---

## Methods & Tools

- **Language:** Python  
- **Libraries:** `requests`, `BeautifulSoup`, `pandas`, `numpy`  
- **Approach:**
  - Web scraping of IMDb HTML page with the top-voted 2018–2020 movies.
  - Parsing HTML into structured tables (handling pagination, missing values,
    and inconsistent formats).
  - Data cleaning and type conversion for numeric fields (year, votes, rating).
  - Joining enriched IMDb data with the client's `Movies.csv` by `movie_id`
    and title.
  - Exporting the enriched dataset to
    `Project_3_Part_A_Group2.csv` (or equivalent filename).

---

## Key Outcomes

- Produced an **enriched movie dataset** combining client attributes
  (genre, description, ratingCategory) with IMDb popularity metrics
  (rating, votes, rank).
- Demonstrated **end-to-end data wrangling**:
  scraping → cleaning → transformation → joining → export.
- Enabled downstream analysis for **content selection, recommendation, and
  catalog strategy** for a streaming platform.

---

## Files in this folder

- `Project_3_Part_A_Group2.ipynb` – main notebook (scraping, cleaning,
  enrichment, and export).
- `IMDb_TopVoted_Group2.csv` – scraped IMDb data.  
- `Project_3_PartA_Group2.csv` – final enriched dataset combining client + IMDb data.
