from agent_app.tools.base import BaseTool
from typing import Any, Dict

class HRManagementTool(BaseTool):
    name = "hr_management"
    description = "Manages technician schedules and certifications."

    def execute(self, action: str, technician_name: str = "") -> Dict[str, Any]:
        team = {
            "Ahmed": {"status": "Available", "certifications": ["Fiber Splicing"]},
            "Karim": {"status": "On Field", "certifications": ["ONT Config"]}
        }
        if action == "list_available":
            available = [name for name, info in team.items() if info["status"] == "Available"]
            return {"status": "success", "available_technicians": available}
        return {"status": "error", "message": "Invalid HR action."}
