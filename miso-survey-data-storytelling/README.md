# Insights from the Analysis of MISO Survey Results

This folder contains my work from a graduate **data storytelling** project analyzing
MISO survey results (2018, 2021, 2024) on information technology and library services
at a university.

The goal was to turn raw survey data into a clear, actionable story for the
**Chief Information Officer (CIO)** about how faculty, staff, and students perceive
IT services over time and where to invest for improvement.

---

## My Role

- Cleaned and merged the **faculty MISO survey datasets (2018 & 2024)**.
- Removed empty / low-value columns, fixed data types, and created derived variables
  (e.g., average satisfaction by IT service and faculty group).
- Identified **lowest-rated** and **most-improved** IT services across years.
- Helped shape the **central insight** and storyline for the final presentation.
- Designed several key **visualizations** and contributed to the **executive summary**
  for the final “Insights from the Analysis of MISO Survey Results” report.

---

## Data

- 2018, 2021, 2024 MISO survey results (students, faculty, staff).
- Likert-scale questions on:
  - Satisfaction with IT & library services
  - Frequency of use and importance
  - Contribution to academic goals
  - Awareness of services
- Demographic questions to compare results across faculty groups.

> Note: The original survey data is institutional and not public, so it is **not**
> included in this repository. You can substitute anonymized or synthetic samples
> that follow a similar structure if needed.

---

## Methods & Tools

- **Language / tools:** Python (pandas, matplotlib / seaborn), Excel, PowerPoint.
- **Approach:**
  - Data preparation: cleaning, merging, and restructuring 2018 & 2024 faculty data.
  - Exploratory Data Analysis: summary tables and charts to surface trends & pain points.
  - Comparative analysis of **2018 vs. 2024** satisfaction for key IT service categories.
  - Visual design guided by Brent Dykes’ *Effective Data Storytelling* principles
    (clarity, focus, preattentive attributes, decluttering, etc.).
  - Narrative development using the **Data Storytelling Arc** (setup → conflict →
    resolution) tailored to a CIO audience.

---

## Key Insights (from the project)

- Overall satisfaction with several **core IT services improved** between 2018 and 2024,
  especially in classroom and network services.
- A small group of services remained **consistently low-rated**, indicating persistent
  gaps in support and communication.
- Differences across faculty groups highlighted where **targeted investment and
  outreach** could have the biggest impact.

---

## Files in this folder

- `miso_2024_faculty_cleaning_and_insights.ipynb` – main analysis & visualization notebook.
-  `Group_1_ Report.pdf` – final report for the CIO.
