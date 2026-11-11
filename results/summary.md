# Results: first pass only

## Mean rubric score by occupation

| occupation               |   gold_score |   opus55_score |   opus55_vs_expert |   haiku55_score |   haiku55_vs_expert |
|:-------------------------|-------------:|---------------:|-------------------:|----------------:|--------------------:|
| Accountants and Auditors |         0.68 |           0.83 |               1.25 |            0.76 |                1.13 |
| Compliance Officers      |         0.72 |           0.53 |               0.71 |            0.71 |                1.05 |
| Financial Managers       |         0.77 |           0.78 |               0.96 |            0.69 |                0.76 |
| Lawyers                  |         0.82 |           0.66 |               0.76 |            0.59 |                0.65 |

|                           |   gold_score |   opus55_score |   opus55_vs_expert |   haiku55_score |   haiku55_vs_expert |
|:--------------------------|-------------:|---------------:|-------------------:|----------------:|--------------------:|
| mean (tasks with a score) |         0.74 |            0.7 |               0.93 |            0.69 |                0.93 |

Expert scores cover tasks with expert files (17 of 20); `_vs_expert` is per-task model score / expert score.

## Cost

- opus55: model $54.38, judge $2.74, median 6.75 min/task, errors 2
- haiku55: model $1.68, judge $2.96, median 4.95 min/task, errors 0
- expert grading (judge only): $1.99
