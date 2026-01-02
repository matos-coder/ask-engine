# app/settings/client.py

class ClientSettings:
    def __init__(
        self,
        enable_agent_handoff: bool = False,
        handoff_message: str = "A human agent will assist you shortly."
    ):
        self.enable_agent_handoff = enable_agent_handoff
        self.handoff_message = handoff_message


def get_client_settings(client_id: str) -> ClientSettings:
    """
    Later this comes from DB.
    For now: defaults.
    """
    return ClientSettings()
