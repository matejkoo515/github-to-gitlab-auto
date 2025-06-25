# GitHub to GitLab Auto Update

**GitHub to GitLab Auto Update** è un progetto Python che automatizza la configurazione del mirroring tra i repository del tuo account GitHub e GitLab. Utilizzando le API di GitLab, lo script recupera tutti i progetti di cui sei membro su GitLab e configura, per ciascuno, il mirroring verso il repository corrispondente su GitHub. In questo modo, ogni aggiornamento fatto su GitHub verrà automaticamente sincronizzato su GitLab.

## Indice

- [Panoramica](#panoramica)
- [Caratteristiche](#caratteristiche)
- [Requisiti](#requisiti)
- [Installazione](#installazione)
- [Configurazione](#configurazione)
- [Utilizzo](#utilizzo)
- [Come Funziona](#come-funziona)
- [Contributi](#contributi)
- [Licenza](#licenza)

## Panoramica

Questo progetto si propone di risolvere il problema di dover aggiornare manualmente i repository importati da GitHub su GitLab.  
Con **GitHub to GitLab Auto Update**, puoi:

- Configurare automaticamente il mirroring dei repository in blocco.
- Mantenere sincronizzati i progetti, evitando operazioni ripetitive.
- Utilizzare uno script semplice, basato su Python e la libreria `requests`, per interagire con le API di GitLab.

## Caratteristiche

- **Automazione Completa:** Recupera tutti i progetti GitLab e configura il mirroring verso GitHub in automatico.
- **Facilità di Configurazione:** Basta impostare le variabili di configurazione con il tuo username e i token.
- **Supporto per Progetti Multipli:** Ideale per account con centinaia di repository.
- **Personalizzabile:** Puoi adattare lo script per gestire casi particolari, ad esempio se i nomi dei repository non coincidono perfettamente.

## Requisiti

- **Python 3.x**
- **Libreria Python `requests`:** Installabile con:
  ```bash
  pip install requests
  ```
- **Token di accesso:**
  - **GitHub Personal Access Token**: Con scope `repo` (richiesto per leggere i repository).
  - **GitLab Personal Access Token**: Con scope `api` (necessario per modificare le impostazioni dei progetti).

## Installazione

1. **Clona il repository:**
   ```bash
   git clone https://github.com/bocaletto-luca/github-to-gitlab-auto-update.git
   ```
2. **Entra nella directory del progetto:**
   ```bash
   cd github-to-gitlab-auto-update
   ```
3. **(Opzionale) Crea un ambiente virtuale e attivalo:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. **Installa la libreria richiesta:**
   ```bash
   pip install requests
   ```

## Configurazione

Modifica il file `github_to_gitlab_auto_update.py` per aggiornare le variabili di configurazione all'inizio del file:

```python
# Configurazione
GITLAB_URL = "https://gitlab.com/api/v4"
GITHUB_USERNAME = "bocaletto-luca"  # Il tuo username GitHub
GITHUB_TOKEN  = "your_github_token_here"  # Inserisci qui il tuo GitHub Personal Access Token
GITLAB_TOKEN  = "your_gitlab_token_here"   # Inserisci qui il tuo GitLab Personal Access Token
```

> **Nota:** Non lasciare mai i token in chiaro in repository pubblici. Per maggiore sicurezza, puoi far sì che lo script legga i token da variabili d'ambiente o da un file di configurazione escluso dal controllo versione.

## Utilizzo

Per eseguire lo script e configurare il mirroring per tutti i tuoi repository, utilizza il seguente comando da terminale:

```bash
python3 github_to_gitlab_auto_update.py
```

Lo script:
- Recupererà l'elenco dei progetti GitLab di cui sei membro.
- Per ciascun progetto, costruirà l'URL del repository su GitHub basandosi sul nome.
- Configurerà il mirroring su GitLab per sincronizzare automaticamente il repository da GitHub.

## Come Funziona

1. **Recupero dei Progetti:**  
   Utilizza l'API di GitLab per ottenere tutti i progetti in cui il tuo account è membro, gestendo la paginazione.

2. **Costruzione dell'URL GitHub:**  
   Per ogni progetto, lo script genera l'URL in base al nome del repository, così che corrisponda a `https://github.com/bocaletto-luca/<project_name>.git`.

3. **Configurazione del Mirroring:**  
   Con una chiamata PUT all'API di GitLab, lo script imposta il mirroring specificando:
   - `import_url`: URL del repository GitHub.
   - `mirror`: Abilitato (true).
   - `username` e `password`: Le credenziali GitHub per effettuare il pull dalle repository.

## Contributi

Contributi, suggerimenti e segnalazioni di bug sono benvenuti!  
Se desideri contribuire a **GitHub to GitLab Auto Update**, apri una issue o, meglio ancora, invia una pull request con le tue migliorie.

## Licenza

Distribuito con licenza MIT. Consulta il file [LICENSE](LICENSE) per maggiori dettagli.

---

Creato da **bocaletto-luca**.

---
