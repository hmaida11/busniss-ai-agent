from agent_app.tools.base import BaseTool
from typing import Any, Dict

class FiberOperationsTool(BaseTool):
    name = "fiber_operations"
    description = "Manages fiber optic inventory (routers, cables) and client installation tickets."

    def execute(self, action: str, item_type: str = "", quantity: int = 0, client_name: str = "") -> Dict[str, Any]:
        if action == "check_stock":
            stock = {"router_wifi6": 150, "ont_device": 85, "fiber_cable_meters": 5000, "sfp_module": 40}
            count = stock.get(item_type, 0)
            return {"status": "success", "item": item_type, "available_stock": count}
        elif action == "create_ticket":
            return {"status": "success", "message": f"Installation ticket created for client '{client_name}'."}
        return {"status": "error", "message": "Invalid fiber operation action."}
