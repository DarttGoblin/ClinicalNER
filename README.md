# 🧬 ClinicalNER: Named Entity Recognition in Biomedical Literature

Welcome to the official repository for **ClinicalNER**, a clinical Named Entity Recognition system that extracts biomedical entities — diseases, symptoms, genes, and proteins — from real PubMed abstracts using distant supervision and deep learning models.

---

## 📌 Project Overview

ClinicalNER was developed as part of an NLP research project to build a scalable biomedical NER system using:

- 📚 **Real abstracts** collected from PubMed
- 🧠 **Distant supervision** for automatic annotation
- 🤖 Deep learning models (BiLSTM and BiLSTM+CRF)
- 📊 Sequence labeling evaluation (Precision, Recall, F1)

---

## 🗂️ Project Structure

ClinicalNER_Project/
│
├── ClinicalNER.ipynb # Main training and evaluation notebook
│
├── other_files/ # Extra/temporary JSONL files from scraping or annotation
│ ├── pubmed_abstracts.jsonl
│ ├── BioPortal_annotation_dataset.jsonl
│ └── ... (cleaned/preprocessed versions)
│
├── data/ # Final cleaned data used for training
│ ├── pubmed_abstracts.txt # Raw PubMed abstracts (6000)
│ ├── pubmed_abstracts_labled.txt # BIO-labeled file for BiLSTM(+CRF)
│ └── biobert_ner_data.tsv # TSV-formatted version for BioBERT
│
├── models/ # Trained model files
│ ├── BiLSTM.pt
│ ├── BiLSTM-CRF.pt
│ └── BiLSTM-CRF_full.pth


---

## 🚀 How It Works

### 1. 📥 Data Collection
We extracted 6000 abstracts from PubMed using 30 queries per entity type (disease, gene, symptom, protein), 50 abstracts each.

### 2. 🧹 Preprocessing
- Sentence segmentation and tokenization (`spaCy`)
- Text normalization
- Removal of headers and metadata

### 3. 🏷️ Distant Supervision
Using hand-crafted dictionaries, we applied weak labeling using BIO tags:
- `B-DISEASE`, `I-GENE`, `O`, etc.
- Ambiguous terms (e.g., `"MAP"`, `"SET"`) filtered out for gene/protein

### 4. 🧠 Models
Two models were implemented:
- `BiLSTM` (baseline)
- `BiLSTM + CRF` (improved with sequence-level decoding)

### 5. 📊 Evaluation
We used `seqeval` to compute:
- Precision, Recall, F1-score
- Entity-wise + micro/macro averages

---

## ⚙️ How to Use This Repo

> Run everything from `ClinicalNER.ipynb` (Colab/Locally)

### 🔧 Requirements

Install required packages:
```bash
pip install torch transformers seqeval spacy biopython
python -m spacy download en_core_web_sm

▶️ To Train Models
Load and preprocess data

Run BiLSTM training block

Run BiLSTM + CRF training block

Evaluate using seqeval

📈 Model Performance
Model       	Prs 	Rcl	    F1-s
BiLSTM	        0.00	0.00	0.00
BiLSTM + CRF	1.00	1.00	1.00

🟢 CRF improved tagging performance drastically by modeling label sequences.

⚠️ Known Limitations
❌ BioBERT was not successfully trained due to sequence length errors (abstracts > 512 tokens).

🟡 The dataset is weakly labeled, so results are optimistic — real-world performance needs validation on manually annotated corpora.

🧠 Authors
👩 Zahra Abouhane

🧑 Project Partner(s) (if any)

🏫 University: UCA, NLP M2

📚 Citation
If you use this work, please cite or credit the project in your research/report.

📬 Contact
For any question or feedback, open an issue or contact abouhanezahra@uca.ac.ma

🌱 Future Work
✅ Finish BioBERT training with sequence truncation

🧪 Add real manually labeled test set

📖 Explore transfer learning with PubMedBERT

🧬 ClinicalNER – because biomedical NLP deserves better.