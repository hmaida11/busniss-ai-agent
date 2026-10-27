import os
import sys
from openai import OpenAI
from agent_app.memory.sqlite_memory import SQLiteMemory
from agent_app.tools.fiber_tool import FiberOperationsTool
from agent_app.tools.finance_tool import FinanceTool
from agent_app.tools.hr_tool import HRManagementTool
from agent_app.tools.network_tool import NetworkIncidentTool
from agent_app.tools.crm_tool import CustomerCRMTool

class HybridEnterpriseAgent:
    def __init__(self):
        api_key = os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else None
        self.memory = SQLiteMemory()
        self.fiber_tool = FiberOperationsTool()
        self.finance_tool = FinanceTool()
        self.hr_tool = HRManagementTool()
        self.network_tool = NetworkIncidentTool()
        self.crm_tool = CustomerCRMTool()

    def run(self, user_input: str) -> str:
        self.memory.add_message("user", user_input)
        lower_input = user_input.lower()
        agent_response = None

        # 1. Tenter d'utiliser l'API OpenAI si configurée
        if self.client:
            try:
                history = self.memory.get_history()
                messages = [{"role": role, "content": content} for role, content in history[-6:]]
                system_prompt = {
                    "role": "system", 
                    "content": (
                        "You are an advanced enterprise AI assistant for a fiber optic company. "
                        "You manage inventory, network incidents, financial metrics, HR, and CRM."
                    )
                }
                messages.insert(0, system_prompt)
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages,
                    temperature=0.3
                )
                agent_response = response.choices[0].message.content
            except Exception:
                pass # Bascule silencieuse sur le mode local en cas d'erreur de crédit/API

        # 2. Mode de secours local (si l'API échoue ou n'a plus de crédits)
        if not agent_response or "429" in agent_response or "credits" in agent_response.lower():
            if "stock" in lower_input or "routeur" in lower_input or "ont" in lower_input:
                item = "router_wifi6" if "wifi 6" in lower_input or "routeur" in lower_input else "ont_device"
                res = self.fiber_tool.execute(action="check_stock", item_type=item)
                agent_response = f"[Mode Local] Vérification des stocks -> Article : {res.get('item')}, Stock disponible : {res.get('available_stock')}"
            elif "network" in lower_input or "reseau" in lower_input or "sousse" in lower_input:
                res = self.network_tool.execute(action="check_network")
                agent_response = f"[Mode Local] État du réseau -> Zones : {res.get('all_zones')}"
            elif "rentable" in lower_input or "seuil" in lower_input:
                res = self.finance_tool.execute(action="seuil_de_rentabilite", fixed_costs=6000.0, variable_cost_per_unit=25.0, price_per_unit=90.0)
                agent_response = f"[Mode Local] Calcul financier -> Unités : {res.get('breakeven_units')}, CA nécessaire : {res.get('breakeven_revenue')} TND"
            elif "tech" in lower_input or "hr" in lower_input or "technicien" in lower_input:
                res = self.hr_tool.execute(action="list_available")
                agent_response = f"[Mode Local] RH -> Techniciens disponibles : {res.get('available_technicians')}"
            elif "client" in lower_input or "crm" in lower_input:
                res = self.crm_tool.execute(action="get_client", client_name="Enterprise Corp")
                agent_response = f"[Mode Local] CRM -> Client : {res.get('client')} ({res.get('details')})"
            else:
                agent_response = "Alerte Crédits OpenAI (429). L'agent est en mode local. Essayez de demander : 'check stock router_wifi6', 'list available technicians', ou 'check network'."

        self.memory.add_message("assistant", agent_response)
        return agent_response

def main():
    agent = HybridEnterpriseAgent()
    print("=== Hybrid Fiber Optic Enterprise AI Agent (Active) ===")
    print("Type 'quit' or 'exit' to stop.\n")
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit"]:
                print("Goodbye!")
                break
            if not user_input.strip():
                continue
            print(f"Agent: {agent.run(user_input)}\n")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
