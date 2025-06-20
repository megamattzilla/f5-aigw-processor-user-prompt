from f5_ai_gateway_sdk.parameters import Parameters
from f5_ai_gateway_sdk.processor import Processor
from f5_ai_gateway_sdk.processor_routes import ProcessorRoutes
from f5_ai_gateway_sdk.request_input import Message, MessageRole
from f5_ai_gateway_sdk.result import Result, Reject, RejectCode
from f5_ai_gateway_sdk.signature import BOTH_SIGNATURE, INPUT_ONLY_SIGNATURE
from f5_ai_gateway_sdk.tags import Tags
from f5_ai_gateway_sdk.type_hints import Metadata
from starlette.applications import Starlette

class UserPromptParameters(Parameters):
    enforce_user_prompt: str = "default"

class UserPromptProcessor(Processor):
    """
    A simple processor to append a message to the user prompt
    """

    def __init__(self):
        super().__init__(
            name="user-prompt",
            version="v1",
            namespace="demo",
            signature=BOTH_SIGNATURE,
            parameters_class=UserPromptParameters,
        )

    def process(self, prompt, response, metadata, parameters, request):

        # Append the contents of enforce_user_prompt to the content of messages where role is 'user'
        for message in prompt.messages:
            if message.role == 'user':
                message.content += f" {parameters.enforce_user_prompt}"

        return Result(
            tags=Tags({"enforced_user_prompt": ["True"]}),
            modified_prompt=prompt,
        )

app = Starlette(
    routes=ProcessorRoutes([UserPromptProcessor()]),
)