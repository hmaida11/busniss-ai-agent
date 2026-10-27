from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseTool(ABC):
    name: str
    description: str

    @abstractmethod
    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        pass

class FileHandlerTool(BaseTool):
    name = "file_handler"
    description = "Lit ou écrit des fichiers texte en toute sécurité."

    def execute(self, action: str, filepath: str, content: str = "") -> Dict[str, Any]:
        if action == "read":
            with open(filepath, "r", encoding="utf-8") as f:
                return {"status": "success", "content": f.read()}
        elif action == "write":
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            return {"status": "success", "message": f"Fichier {filepath} écrit avec succès."}
        return {"status": "error", "message": "Action invalide."}