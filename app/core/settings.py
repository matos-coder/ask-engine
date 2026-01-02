from dataclasses import dataclass

@dataclass
class ClientSettings:
    enable_agent_handoff: bool = False
    handoff_message: str = "Would you like to talk to our agent?"

# TEMP: fake in-memory settings
CLIENT_SETTINGS = {
    "demo": ClientSettings(enable_agent_handoff=False),
    "realestate": ClientSettings(enable_agent_handoff=True)
}

def get_client_settings(client_id: str) -> ClientSettings:
    return CLIENT_SETTINGS.get(client_id, ClientSettings())
