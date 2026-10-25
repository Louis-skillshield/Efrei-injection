# Efrei · Journée 4 · Injection SQL sur la base Vélib'

Une petite appli Streamlit qui recherche un abonné par son nom.
La version **vulnérable** est fournie : vous allez l'attaquer, puis écrire la version **sécurisée**.

## Installation

```bash
git clone https://github.com/Louis-skillshield/Efrei-injection.git
cd Efrei-injection
cp .env.example .env      # puis renseigner vos identifiants PostgreSQL
uv sync
```

La base `velib_db` de la journée 3 doit être chargée.

## Contenu

| Fichier | Rôle |
|---|---|
| `main.py` | L'appli Streamlit. La fonction `get_abonne_list_securise` est à écrire (`# TODO S2`) |
| `role_app_recherche.sql` | S6 (bonus) : un rôle qui ne peut lire que la table `abonne` |
| `src/database.py` | Connexion PostgreSQL à partir du `.env` |

## Lancer

```bash
uv run streamlit run main.py
```

Les énoncés (S1 à S6) sont dans les mini-pratiques de la journée 4.

Les attaques par injection ne se testent **que sur vos propres applications**.
