
> 🚨 This is an experimental processor for demonstration purposes only. It is not intended for production use. 🚨

Similar functionality to F5 [system-prompt](https://aigateway.clouddocs.f5.com/processors/system-prompt.html) processor, but the enforcement message is appended to role "user" class only.

Pre-build image provided at [megamattzilla/ai-gateway-sdk-demo:user-prompt-v1.0](https://hub.docker.com/r/megamattzilla/ai-gateway-sdk-demo/tags?page=1&ordering=last_updated) on Docker Hub.


## Overview: User-Prompt custom AI Gateway Processor

The `system-prompt` processor is an F5 provided AI Gateway processor that appends the configured text to the users prompt with role "system". Example:

```json
{
    [
        {"role": "system", "content": "Enforcement text here"},
        {"role": "user", "content": "What does an example openAI API request look like ?"}
    ]
  }
```

Some LLMs will follow instructions better if the enforcement text is instead appended to the end of the users prompt. Example:
```json
{
    [
        {"role": "user", "content": "What does an example openAI API request look like ? Enforcement text here"}
    ]
  }
```

The custom processor user-prompt will take the enforcement text and append it to the end of the users prompt instead of the system prompt.

When you add the user-prompt processor to your AI Gateway configuration and remove the system-prompt processor, you will achieve the desired behavior of only appending enforcement messages to user prompts, not system prompts.


### Run in AI Gateway: Configure Custom user-prompt Processor
> This steps assumes you are running the user-prompt processor in a container runtime environment, such as Docker or Kubernetes.
```yaml
processors:
  - name: user-prompt
    type: external
    config:
      endpoint: http://your-container-name:8000
      namespace: demo
      version: 1
    params:
      modify: true
      enforce_user_prompt: Your enforcement message (on a single line for best results).

```

## Build and Run from source for development
Overview of all steps on clouddocs.f5.com [AI Gateway Python SDK](https://aigateway.clouddocs.f5.com/sdk/python/tutorial.html).

> You can test the SDK in a build environment here or you can skip to building the Docker image below.

Run custom user-prompt processor in build:
```bash
python -m uvicorn user-prompt:app --host 127.0.0.1 --port 9999 --reload
```

run test curl to test processor in development:
```bash
$ ./cURL-test.sh

HTTP/1.1 200 OK
date: Fri, 20 Jun 2025 21:09:32 GMT
server: uvicorn
content-type: multipart/form-data;charset=utf-8;boundary="SZmL7tpUeUKNpNBbecUi0pa1SQYVLvnBYRpB43qHk0Uzj0pu8C2u8YwO4QmhXLVy"
Transfer-Encoding: chunked

--SZmL7tpUeUKNpNBbecUi0pa1SQYVLvnBYRpB43qHk0Uzj0pu8C2u8YwO4QmhXLVy
Content-Disposition: form-data; name="input.messages"
Content-Type: application/json

{"messages":[{"content":"Do you like dogs? Remember to only mention cats in your response","role":"user"}]}
--SZmL7tpUeUKNpNBbecUi0pa1SQYVLvnBYRpB43qHk0Uzj0pu8C2u8YwO4QmhXLVy
Content-Disposition: form-data; name="metadata"
Content-Type: application/json

{"processor_id": "demo:user-prompt", "processor_version": "v1", "tags": {"enforced_user_prompt": ["true"]}}
--SZmL7tpUeUKNpNBbecUi0pa1SQYVLvnBYRpB43qHk0Uzj0pu8C2u8YwO4QmhXLVy--
```

## Build your own docker image using provided Dockerfile
> The Dockerfile is provided in the repository.

- Review the Dockerfile.
- Review the requirements.txt file to see the python pip dependencies.
```bash
## Substitute with your desired repository name and version
$ docker build -t megamattzilla/ai-gateway-sdk-demo:user-prompt-v1.0 .

## Push the Docker image to your container registry
$ docker push megamattzilla/ai-gateway-sdk-demo:user-prompt-v1.0
```