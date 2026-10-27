from agent_app.tools.base import BaseTool
from typing import Any, Dict

class NetworkIncidentTool(BaseTool):
    name = "network_incident"
    description = "Monitors fiber network link status and outages."

    def execute(self, action: str, zone: str = "") -> Dict[str, Any]:
        network_status = {
            "Monastir_Center": {"status": "Operational", "active_outages": 0},
            "Sousse_Zone": {"status": "Maintenance", "active_outages": 1}
        }
        if action == "check_network":
            return {"status": "success", "all_zones": network_status}
        return {"status": "error", "message": "Invalid network action."}
