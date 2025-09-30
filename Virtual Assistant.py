import os
from dotenv import load_dotenv
import signal

load_dotenv() # loads all env variables 

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

# configuring ElevenLabs Conversation API

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.conversations.audio import DefaultAudioInterface
from elevenlabs.conversational_ai.conversations.types import ConversationConfig

conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

config = ConversationConfig(
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables={}
)

client = ElevenLabs(api_key=API_KEY)

conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
)