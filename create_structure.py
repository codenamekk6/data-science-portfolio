import os

folders = [
    "01-python-fundamentals/notebooks",
    "01-python-fundamentals/scripts",
    "02-business-statistics/descriptive-analysis",
    "02-business-statistics/hypothesis-testing",
    "03-supervised-learning/regression",
    "03-supervised-learning/classification",
    "04-unsupervised-learning/clustering",
    "04-unsupervised-learning/dimensionality-reduction",
    "05-ensemble-techniques/random-forest",
    "05-ensemble-techniques/boosting",
    "06-model-tuning/hyperparameter-tuning",
    "06-model-tuning/cross-validation",
    "07-projects/foodhub-demand-analysis",
    "07-projects/recell-price-prediction",
    "07-projects/ab-testing-landing-page"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    readme_path = os.path.join(folder.split('/')[0], 'README.md')
    if not os.path.exists(readme_path):
        with open(readme_path, 'w') as f:
            f.write(f"# {folder.split('/')[0].replace('-', ' ').title()}")
