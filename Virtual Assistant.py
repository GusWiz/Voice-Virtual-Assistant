import os
from dotenv import load_dotenv
import signal

load_dotenv() # loads all env variables 

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

# configuring ElevenLabs Conversation API

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
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

def print_agent_resonse(response):
    print(f"Agent: {response}")

def print_interrupted_response(original, correct):
    print(f"Agent interrupted, truncated response: {corrected}")

def print_user_transcript(transcript):
    print(f"User transcript: {transcript}")

    