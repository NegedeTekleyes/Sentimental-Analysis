import torch
from datasets import load_dataset
from transforms import(
    AutoTokenizer,
    AutoModelForSequenceClassfication,
    Trainer,
    TrainingArguments,
    pipeline
)
import numpy as np
from sklearn.metrics import accuracy_score, f1_score
import os

def load_and_prepare_data():
    """Load and prepare the IMDB dataset"""
    print("Loading IMDB dataset...")
    dataset = load_dataset("imbd")
    return dataset
def initialize_model():
    """Intialize model tokenizer"""
    print("Intializing DistilBert model...")
    model_name = "distilbert_base_uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassfication.from_pretrained(
        model_name,
        num_labels=2
    )
    return tokenizer, model

def tokenize_data(tokenizer, dataset):
    """Tokenize the dataset"""
    print("Tokenizing data...")

def tokenize_function(examples):
    return tokenizer(
        examples["text"],
        padding="max_length",
        truncation=True,
        max_length=256
    )   

tokenized_datasets = dataset.map(tokenize_function, batched= True)