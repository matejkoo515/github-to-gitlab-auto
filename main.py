#!/usr/bin/env python3
import requests

# CONFIGURAZIONE
GITLAB_URL = "https://gitlab.com/api/v4"
GITHUB_USERNAME = "your-username-github"  # Il tuo username GitHub
GITHUB_TOKEN = "your-github-token"  # Inserisci qui il tuo GitHub token con scope "repo"
GITLAB_TOKEN = "your-gitlab-token"   # Inserisci qui il tuo GitLab token con scope "api"
HEADERS_GITLAB = {"PRIVATE-TOKEN": GITLAB_TOKEN}

def get_gitlab_projects():
    """
    Recupera tutti i progetti GitLab di cui sei membro.
    """
    projects = []
    page = 1
    per_page = 100  # Numero massimo di progetti per pagina
    while True:
        params = {"membership": "true", "page": page, "per_page": per_page}
        response = requests.get(f"{GITLAB_URL}/projects", headers=HEADERS_GITLAB, params=params)
        if response.status_code != 200:
            print("Errore nel recupero dei progetti:", response.text)
            break
        data = response.json()
        if not data:
            break  # Termina se non ci sono più progetti
        projects.extend(data)
        page += 1
    return projects

def setup_mirroring(project_id, github_repo_url):
    """
    Configura il mirroring per un progetto GitLab specifico.
    """
    data = {
        "import_url": github_repo_url,
        "mirror": True,
        "mirror_trigger_builds": False,
        "username": GITHUB_USERNAME,
        "password": GITHUB_TOKEN
    }
    response = requests.put(
        f"{GITLAB_URL}/projects/{project_id}",
        headers=HEADERS_GITLAB,
        json=data
    )
    if response.status_code == 200:
        print(f"Mirroring configurato per il progetto {project_id}.")
    else:
        print(f"Errore nella configurazione del mirroring per il progetto {project_id}: {response.text}")

def main():
    projects = get_gitlab_projects()
    print(f"Trovati {len(projects)} progetti su GitLab.")
    for project in projects:
        project_id = project.get("id")
        project_name = project.get("path")
        # Costruiamo l'URL del repository GitHub basandoci sul naming (assicurati che il naming coincida)
        github_repo_url = f"https://github.com/{GITHUB_USERNAME}/{project_name}.git"
        print(f"Configurazione del mirroring per il progetto '{project_name}' (ID: {project_id}) da {github_repo_url}")
        setup_mirroring(project_id, github_repo_url)

if __name__ == "__main__":
    main()
