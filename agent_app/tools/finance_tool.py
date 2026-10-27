from agent_app.tools.base import BaseTool
from typing import Any, Dict

class FinanceTool(BaseTool):
    name = "finance_calculator"
    description = "Calculates project profit margins and break-even point (seuil de rentabilité)."

    def execute(self, action: str, fixed_costs: float = 0.0, variable_cost_per_unit: float = 0.0, price_per_unit: float = 0.0) -> Dict[str, Any]:
        if action == "seuil_de_rentabilite":
            if price_per_unit <= variable_cost_per_unit:
                return {"status": "error", "message": "Price must be greater than variable cost."}
            breakeven_units = fixed_costs / (price_per_unit - variable_cost_per_unit)
            breakeven_revenue = breakeven_units * price_per_unit
            return {"status": "success", "breakeven_units": round(breakeven_units, 2), "breakeven_revenue": round(breakeven_revenue, 2)}
        return {"status": "error", "message": "Invalid finance action."}
