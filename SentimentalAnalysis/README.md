# SENTIMENTAL ANALYSIS

---

- Project Summary — How It Works, Dataset Used, Purpose, and Key Features

  This project is a custom sentiment analysis system built using HuggingFace Transformers and fine-tuned on the IMDB Movie Reviews Dataset.
  It automatically determines whether a given text expresses a Positive or Negative sentiment.

- Purpose of the Project

  This project aims to create a high-quality AI model that:

  Automatically analyzes opinions in text

  Removes the need for manual review

  Helps businesses understand customer feedback

  Supports researchers working with large text datasets

  Can be deployed into apps, APIs, dashboards, and automation tools

- It is especially useful for:

  Movie and product review analysis

  Social media monitoring

  Customer satisfaction systems

  Any text-based sentiment classification task

- Dataset Used — IMDB Movie Reviews

  The model is trained using the IMDB dataset, which is one of the most widely used datasets for sentiment analysis.

  Dataset Summary:

  50,000 movie reviews total

  25,000 reviews for training

  25,000 for testing

  Each review is labeled as:

  Positive (1)

  Negative (0)

- Examples:

  Positive: "This movie was absolutely fantastic!"

  Negative: "I hated this film, terrible acting."

  This dataset provides a balanced and clean foundation for training a high-performing sentiment model.

# How the System Work

---

- Step 1 — Data Preparation

  The IMDB dataset is loaded using datasets.load_dataset().

      Text is tokenized using DistilBERT tokenizer, converting sentences into numerical tokens.

      The data is batched and prepared for training.

- Step 2 — Model Training

  The base model is DistilBERT, a smaller and faster version of BERT.

  The model is fine-tuned for a binary classification task (Positive / Negative).

  Training is done using the HuggingFace Trainer API, which handles:

  batching

  optimization

  evaluation

  logging

  The model is trained for 3 epochs on GPU (Colab recommended).

- Step 3 — Evaluation

  The model is evaluated using:

  Accuracy

  Weighted F1-score

  Classification report

- Step 4 — Using the Model for Predictions

  After training, the model can analyze any text:

  from transformers import pipeline

  classifier = pipeline("sentiment-analysis", model="path/to/your/model")
  result = classifier("This movie was amazing!")

  print(result)
  Output: [{'label': 'POSITIVE', 'score': 0.98}]

- Key Features

  ✔️ Fine-tuned DistilBERT Transformer

  ✔️ Supervised learning on 50k IMDB reviews

  ✔️ High accuracy and F1-score

  ✔️ Clean and professional training pipeline

  ✔️ Ready to run on Google Colab

  ✔️ Easy deployment (API, script, or web app)

  ✔️ Includes model saving and loading scripts

- Installiation

  git clone https://github.com/NegedeTekleyes/Sentimental-Analysis.git
  cd Sentimental-Analysis
  pip install -r requirements.txt
