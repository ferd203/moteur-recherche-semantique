# Moteur de Recherche Sémantique avec RAG

Ce projet est un moteur de recherche sémantique développé en Python.

Il permet de charger des documents texte, de les découper en chunks, de générer des embeddings, de les indexer avec FAISS, puis de répondre à une question en utilisant un modèle LLM local via Ollama.

L'objectif principal du projet est de comprendre le fonctionnement interne d'un système RAG sans utiliser directement un framework comme LangChain ou LlamaIndex.

---

## Objectifs du projet

Ce projet permet de comprendre et pratiquer :

* le chargement de documents texte ;
* le découpage de documents en chunks ;
* la génération d'embeddings ;
* la recherche vectorielle avec FAISS ;
* la construction d'un pipeline RAG ;
* l'utilisation d'un LLM local avec Ollama ;
* l'affichage des sources utilisées ;
* la programmation orientée objet en Python ;
* l'utilisation de `@dataclass` ;
* la séparation des responsabilités dans une architecture logicielle ;
* la sauvegarde et le chargement d'un index FAISS.

---

## Architecture générale

```text
documents/
    ↓
DocumentLoader
    ↓
list[Chunk]
    ↓
SemanticSearchEngine
    ↓
VectorStore
    ↓
list[SearchResult]
    ↓
RAG
    ↓
PromptBuilder
    ↓
OllamaLLM
    ↓
Réponse + sources
```

---

## Technologies utilisées

* Python
* Sentence Transformers
* FAISS
* NumPy
* Ollama
* Llama 3.2 ou autre modèle local
* Dataclasses
* Programmation orientée objet

---

## Structure du projet

```text
moteur-recherche-semantique/
│
├── app.py
├── chunk.py
├── search_result.py
├── document_loader.py
├── sentence_chunker.py
├── search_engine.py
├── vector_store.py
├── prompt_builder.py
├── rag.py
├── ollama_llm.py
│
├── documents/
│   ├── airflow.txt
│   ├── docker.txt
│   ├── python.txt
│   └── rag.txt
│
├── storage/
│   ├── index.faiss
│   └── chunks.json
│
├── requirements.txt
├── .gitignore
└── README.md
```

Le dossier `storage/` est généré automatiquement.
Il peut être ignoré par Git si on souhaite reconstruire l'index localement.

---

## Concepts importants

### Chunk

Un `Chunk` représente un morceau de document.

```python
from dataclasses import dataclass


@dataclass
class Chunk:
    document: str
    source: str
    chunk_id: int
```

Chaque chunk contient :

* le texte du chunk ;
* le nom du fichier source ;
* l'identifiant du chunk dans le fichier.

---

### SearchResult

Un `SearchResult` représente le résultat d'une recherche vectorielle.

```python
from dataclasses import dataclass

from chunk import Chunk


@dataclass
class SearchResult:
    chunk: Chunk
    distance: float
```

Chaque résultat contient :

* le chunk retrouvé ;
* la distance retournée par FAISS.

---

## Fonctionnement du pipeline

### 1. Chargement des documents

Le `DocumentLoader` lit les fichiers `.txt` présents dans le dossier `documents/`.

### 2. Découpage en chunks

Le `SentenceChunker` découpe chaque document en morceaux de texte plus petits.

### 3. Création des embeddings

Le `SemanticSearchEngine` utilise Sentence Transformers pour convertir les chunks en vecteurs numériques.

### 4. Indexation avec FAISS

Le `VectorStore` stocke les embeddings dans un index FAISS.

### 5. Recherche sémantique

Lorsqu'une question est posée, elle est transformée en embedding, puis FAISS recherche les chunks les plus proches.

### 6. Construction du prompt

Le `PromptBuilder` construit un prompt à partir des chunks retrouvés.

### 7. Génération de réponse

Le `OllamaLLM` envoie le prompt à un modèle local via Ollama.

### 8. Affichage des sources

Le RAG retourne la réponse ainsi que les sources utilisées.

---

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/ton-compte/moteur-recherche-semantique.git
cd moteur-recherche-semantique
```

Remplacer `ton-compte` par ton nom d'utilisateur GitHub.

---

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
```

---

### 3. Activer l'environnement virtuel

Sur Windows :

```bash
.venv\Scripts\activate
```

Sur Linux ou macOS :

```bash
source .venv/bin/activate
```

---

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Fichier requirements.txt

Le fichier `requirements.txt` contient les dépendances principales du projet :

```txt
sentence-transformers
faiss-cpu
numpy
ollama
```

---

## Installation d'Ollama

Installer Ollama depuis le site officiel.

Ensuite, télécharger un modèle local :

```bash
ollama pull llama3.2
```

Vérifier les modèles installés :

```bash
ollama list
```

Si `llama3.2` n'est pas installé, il faut soit l'installer, soit modifier le nom du modèle dans `app.py` avec un modèle disponible localement.

Exemple :

```python
llm = OllamaLLM(
    model_name="llama3.2",
)
```

---

## Lancer le projet

```bash
python app.py
```

Exemple de question dans `app.py` :

```python
response = rag.ask(
    question="C'est quoi Airflow ?",
    top_k=3,
)
```

---

## Exemple de sortie

```text
Réponse :
Airflow est un outil permettant d'orchestrer des workflows de données.

Sources :
- airflow.txt (chunk 0) distance=0.3421
- rag.txt (chunk 2) distance=0.5148
```

---

## Sauvegarde du VectorStore

Le projet peut sauvegarder l'index FAISS et les chunks dans le dossier `storage/`.

```text
storage/
├── index.faiss
└── chunks.json
```

Cela permet d'éviter de recalculer les embeddings à chaque lancement.

---

## Exemple de logique de chargement

Le projet peut fonctionner ainsi :

```text
Si le dossier storage existe :
    charger l'index FAISS et les chunks
Sinon :
    charger les documents
    créer les chunks
    générer les embeddings
    construire l'index FAISS
    sauvegarder le VectorStore
```

Cette logique permet de rendre le démarrage plus rapide après la première exécution.

---

## État actuel du projet

Le projet permet actuellement de :

* charger des fichiers `.txt` ;
* découper les documents en chunks ;
* générer des embeddings ;
* construire un index FAISS ;
* effectuer une recherche sémantique ;
* générer une réponse avec Ollama ;
* afficher les sources utilisées ;
* sauvegarder les chunks et l'index FAISS ;
* recharger un VectorStore sauvegardé.

---

## Prochaines améliorations

Les prochaines étapes prévues sont :

* historique conversationnel ;
* streaming des réponses ;
* recherche hybride BM25 + FAISS ;
* re-ranking des résultats ;
* évaluation du RAG ;
* API avec FastAPI ;
* interface web ;
* déploiement avec Docker.

---

## Objectif pédagogique

Ce projet a été construit étape par étape pour comprendre ce qui se passe derrière un système RAG.

L'objectif n'est pas seulement d'utiliser une bibliothèque existante, mais de comprendre les briques fondamentales :

* documents ;
* chunks ;
* embeddings ;
* index vectoriel ;
* recherche sémantique ;
* prompt ;
* LLM ;
* sources ;
* architecture orientée objet.

---

## Auteur

HOUNGBEME Mitondji Ferdinand